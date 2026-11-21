import sqlite3
from pathlib import Path
from decimal import Decimal


BASE_DIR = Path(__file__).resolve().parent
INSTANCE_DIR = BASE_DIR / "instance"
DB_PATH = INSTANCE_DIR / "kontrakan.db"
SCHEMA_PATH = BASE_DIR / "docs" / "desain" / "schema.sql"


def _migrasi_akun_pengguna():
    """
    Menambahkan kolom peran pada basis data yang sudah ada.
    Skema baru sudah menyertakan kolom tersebut; migrasi ini untuk basis data lama.
    """
    connection = get_db_connection()

    try:
        kolom = [
            row[1]
            for row in connection.execute("PRAGMA table_info(akun_pengguna)")
        ]

        if "peran" not in kolom:
            connection.execute(
                """
                ALTER TABLE akun_pengguna
                ADD COLUMN peran TEXT NOT NULL
                DEFAULT 'pemilik'
                CHECK (peran IN ('pemilik', 'kasir'))
                """
            )

        connection.commit()
    finally:
        connection.close()


def get_db_connection():
    """
    Membuat koneksi SQLite dan mengaktifkan foreign key.
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")

    return connection



def init_db():
    """
    Membuat database dan tabel berdasarkan schema.sql
    hanya jika file database belum tersedia.
    """
    INSTANCE_DIR.mkdir(parents=True, exist_ok=True)

    if DB_PATH.exists():
        _migrasi_akun_pengguna()
        return

    if not SCHEMA_PATH.exists():
        raise FileNotFoundError(
            f"File skema tidak ditemukan: {SCHEMA_PATH}"
        )

    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8-sig")

    connection = get_db_connection()

    try:
        connection.executescript(schema_sql)
        connection.commit()
    finally:
        connection.close()


def get_all_kamar(kata_kunci=""):
    """
    Mengambil seluruh data kamar dan menghitung status ketersediaan
    berdasarkan periode sewa yang sedang berlangsung.
    """
    connection = get_db_connection()

    try:
        query = """
            SELECT
                k.id_kamar,
                k.nomor_kamar,
                k.harga_sewa,
                CASE
                    WHEN EXISTS (
                        SELECT 1
                        FROM sewa AS s
                        WHERE s.id_kamar = k.id_kamar
                          AND date('now', 'localtime')
                              BETWEEN date(s.tanggal_mulai)
                              AND date(s.tanggal_selesai)
                    )
                    THEN 'Terisi'
                    ELSE 'Tersedia'
                END AS status_ketersediaan
            FROM kamar AS k
            WHERE k.nomor_kamar LIKE ?
            ORDER BY k.nomor_kamar ASC
        """

        return connection.execute(
            query,
            (f"%{kata_kunci.strip()}%",)
        ).fetchall()

    finally:
        connection.close()


def create_kamar(nomor_kamar, harga_sewa):
    """
    Menyimpan data kamar baru.

    Hasil:
    - (True, None) jika berhasil.
    - (False, 'duplicate') jika nomor kamar sudah digunakan.
    - (False, 'database') jika terjadi kesalahan database lainnya.
    """
    connection = get_db_connection()

    try:
        connection.execute(
            """
            INSERT INTO kamar (nomor_kamar, harga_sewa)
            VALUES (?, ?)
            """,
            (nomor_kamar, str(Decimal(harga_sewa)))
        )

        connection.commit()
        return True, None

    except sqlite3.IntegrityError as error:
        connection.rollback()

        if "UNIQUE constraint failed: kamar.nomor_kamar" in str(error):
            return False, "duplicate"

        return False, "database"

    except sqlite3.Error:
        connection.rollback()
        return False, "database"

    finally:
        connection.close()

def get_kamar_by_id(id_kamar):
    """Mengambil satu data kamar berdasarkan ID."""
    connection = get_db_connection()

    try:
        return connection.execute(
            """
            SELECT id_kamar, nomor_kamar, harga_sewa
            FROM kamar
            WHERE id_kamar = ?
            """,
            (id_kamar,)
        ).fetchone()

    finally:
        connection.close()


def update_kamar(id_kamar, nomor_kamar, harga_sewa):
    """
    Memperbarui data kamar.

    Hasil:
    - (True, None) jika berhasil.
    - (False, 'duplicate') jika nomor kamar sudah digunakan.
    - (False, 'database') jika terjadi kesalahan database.
    """
    connection = get_db_connection()

    try:
        connection.execute(
            """
            UPDATE kamar
            SET nomor_kamar = ?, harga_sewa = ?
            WHERE id_kamar = ?
            """,
            (
                nomor_kamar,
                str(Decimal(harga_sewa)),
                id_kamar,
            )
        )

        connection.commit()
        return True, None

    except sqlite3.IntegrityError as error:
        connection.rollback()

        if "UNIQUE constraint failed: kamar.nomor_kamar" in str(error):
            return False, "duplicate"

        return False, "database"

    except sqlite3.Error:
        connection.rollback()
        return False, "database"

    finally:
        connection.close()


def get_all_penyewa(kata_kunci=""):
    """
    Mengambil seluruh data penyewa, diurutkan berdasarkan nama.
    Pencarian mencakup nama, nomor telepon, dan alamat.
    """
    connection = get_db_connection()

    try:
        pola = f"%{kata_kunci.strip()}%"

        return connection.execute(
            """
            SELECT id_penyewa, nama, no_telepon, alamat
            FROM penyewa
            WHERE nama LIKE ?
               OR no_telepon LIKE ?
               OR alamat LIKE ?
            ORDER BY nama COLLATE NOCASE ASC
            """,
            (pola, pola, pola)
        ).fetchall()

    finally:
        connection.close()


def get_penyewa_by_id(id_penyewa):
    """Mengambil satu data penyewa berdasarkan ID."""
    connection = get_db_connection()

    try:
        return connection.execute(
            """
            SELECT id_penyewa, nama, no_telepon, alamat
            FROM penyewa
            WHERE id_penyewa = ?
            """,
            (id_penyewa,)
        ).fetchone()

    finally:
        connection.close()


def create_penyewa(nama, no_telepon, alamat):
    """
    Menyimpan data penyewa baru.

    Hasil:
    - (True, None) jika berhasil.
    - (False, 'database') jika terjadi kesalahan database.
    """
    connection = get_db_connection()

    try:
        connection.execute(
            """
            INSERT INTO penyewa (nama, no_telepon, alamat)
            VALUES (?, ?, ?)
            """,
            (nama, no_telepon, alamat)
        )

        connection.commit()
        return True, None

    except sqlite3.Error:
        connection.rollback()
        return False, "database"

    finally:
        connection.close()


def update_penyewa(id_penyewa, nama, no_telepon, alamat):
    """
    Memperbarui data penyewa.

    Hasil:
    - (True, None) jika berhasil.
    - (False, 'not_found') jika penyewa tidak ditemukan.
    - (False, 'database') jika terjadi kesalahan database.
    """
    connection = get_db_connection()

    try:
        cursor = connection.execute(
            """
            UPDATE penyewa
            SET nama = ?, no_telepon = ?, alamat = ?
            WHERE id_penyewa = ?
            """,
            (nama, no_telepon, alamat, id_penyewa)
        )

        connection.commit()

        if cursor.rowcount == 0:
            return False, "not_found"

        return True, None

    except sqlite3.Error:
        connection.rollback()
        return False, "database"

    finally:
        connection.close()


def delete_penyewa(id_penyewa):
    """
    Menghapus data penyewa berdasarkan ID.

    Hasil:
    - (True, None) jika berhasil.
    - (False, 'not_found') jika penyewa tidak ditemukan.
    - (False, 'in_use') jika penyewa masih dirujuk oleh data sewa.
    - (False, 'database') jika terjadi kesalahan database lainnya.
    """
    connection = get_db_connection()

    try:
        cursor = connection.execute(
            """
            DELETE FROM penyewa
            WHERE id_penyewa = ?
            """,
            (id_penyewa,)
        )

        connection.commit()

        if cursor.rowcount == 0:
            return False, "not_found"

        return True, None

    except sqlite3.IntegrityError:
        # Penyewa masih dirujuk oleh tabel sewa (ON DELETE RESTRICT).
        connection.rollback()
        return False, "in_use"

    except sqlite3.Error:
        connection.rollback()
        return False, "database"

    finally:
        connection.close()


def delete_kamar(id_kamar):
    """
    Menghapus data kamar berdasarkan ID.

    Hasil:
    - (True, None) jika berhasil.
    - (False, 'not_found') jika kamar tidak ditemukan.
    - (False, 'in_use') jika kamar masih dirujuk oleh data sewa.
    - (False, 'database') jika terjadi kesalahan database lainnya.
    """
    connection = get_db_connection()

    try:
        cursor = connection.execute(
            """
            DELETE FROM kamar
            WHERE id_kamar = ?
            """,
            (id_kamar,)
        )

        connection.commit()

        if cursor.rowcount == 0:
            return False, "not_found"

        return True, None

    except sqlite3.IntegrityError:
        # Kamar masih dirujuk oleh tabel sewa (ON DELETE RESTRICT).
        connection.rollback()
        return False, "in_use"

    except sqlite3.Error:
        connection.rollback()
        return False, "database"

    finally:
        connection.close()

def _escape_like(teks):
    """Netralkan % dan _ agar dicari sebagai huruf biasa pada LIKE."""
    return teks.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")


def get_all_sewa(kata_kunci="", status=""):
    """
    Mengambil seluruh periode sewa dengan JOIN ke penyewa dan kamar.
    Pencarian mencakup nama penyewa dan nomor kamar.
    """
    connection = get_db_connection()

    try:
        kata = kata_kunci.strip()
        pola = f"%{_escape_like(kata)}%"

        sql = """
            SELECT
                s.id_sewa,
                s.id_kamar,
                s.id_penyewa,
                s.tanggal_mulai,
                s.tanggal_selesai,
                s.tanggal_jatuh_tempo,
                s.harga_sewa_disepakati,
                p.nama AS nama_penyewa,
                k.nomor_kamar AS nomor_kamar
            FROM sewa AS s
            JOIN penyewa AS p ON p.id_penyewa = s.id_penyewa
            JOIN kamar AS k ON k.id_kamar = s.id_kamar
            WHERE (p.nama LIKE ? ESCAPE '\\' OR k.nomor_kamar LIKE ? ESCAPE '\\')
        """
        param = [pola, pola]

        if status == "aktif":
            sql += " AND date(s.tanggal_selesai) >= date('now', 'localtime')"
        elif status == "berakhir":
            sql += " AND date(s.tanggal_selesai) < date('now', 'localtime')"

        sql += " ORDER BY s.tanggal_mulai DESC, s.id_sewa DESC"

        return connection.execute(sql, param).fetchall()

    finally:
        connection.close()


def get_sewa_by_id(id_sewa):
    """Mengambil satu periode sewa berdasarkan ID, lengkap dengan nama induk."""
    connection = get_db_connection()

    try:
        return connection.execute(
            """
            SELECT
                s.id_sewa,
                s.id_kamar,
                s.id_penyewa,
                s.tanggal_mulai,
                s.tanggal_selesai,
                s.tanggal_jatuh_tempo,
                s.harga_sewa_disepakati,
                p.nama AS nama_penyewa,
                k.nomor_kamar AS nomor_kamar
            FROM sewa AS s
            JOIN penyewa AS p ON p.id_penyewa = s.id_penyewa
            JOIN kamar AS k ON k.id_kamar = s.id_kamar
            WHERE s.id_sewa = ?
            """,
            (id_sewa,)
        ).fetchone()

    finally:
        connection.close()

def create_sewa(id_kamar, id_penyewa, tanggal_mulai, tanggal_selesai, tanggal_jatuh_tempo, harga_sewa_disepakati):
    """
    Menyimpan satu periode sewa dalam satu transaksi.

    Hasil:
    - (True, None) jika berhasil.
    - (False, 'kamar_not_found') jika kamar tidak ditemukan.
    - (False, 'penyewa_not_found') jika penyewa tidak ditemukan.
    - (False, 'overlap') jika periode sewa bertumpang tindih.
    - (False, 'database') jika terjadi kesalahan database lainnya.
    """
    connection = get_db_connection()

    try:
        kamar = connection.execute(
            "SELECT 1 FROM kamar WHERE id_kamar = ?",
            (id_kamar,)
        ).fetchone()

        if kamar is None:
            return False, "kamar_not_found"

        penyewa = connection.execute(
            "SELECT 1 FROM penyewa WHERE id_penyewa = ?",
            (id_penyewa,)
        ).fetchone()

        if penyewa is None:
            return False, "penyewa_not_found"

        # Satu transaksi: INSERT sewa lalu commit sekali di akhir.
        connection.execute(
            """
            INSERT INTO sewa (
                id_kamar, id_penyewa, tanggal_mulai,
                tanggal_selesai, tanggal_jatuh_tempo,
                harga_sewa_disepakati
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                id_kamar,
                id_penyewa,
                tanggal_mulai,
                tanggal_selesai,
                tanggal_jatuh_tempo or None,
                str(Decimal(harga_sewa_disepakati)),
            )
        )

        connection.commit()
        return True, None

    except sqlite3.IntegrityError as error:
        connection.rollback()
        pesan = str(error)

        if "Periode sewa kamar bertumpang tindih" in pesan:
            return False, "overlap"

        if "FOREIGN KEY constraint failed" in pesan:
            return False, "not_found"

        return False, "database"

    except sqlite3.Error:
        connection.rollback()
        return False, "database"

    finally:
        connection.close()


from werkzeug.security import check_password_hash, generate_password_hash


def tambah_pengguna(username, password_hash, peran):
    """Menyimpan akun pengguna baru."""
    connection = get_db_connection()

    try:
        connection.execute(
            """
            INSERT INTO akun_pengguna (username, password_hash, peran)
            VALUES (?, ?, ?)
            """,
            (username.strip(), password_hash, peran),
        )
        connection.commit()
        return True, None

    except sqlite3.IntegrityError:
        connection.rollback()
        return False, "duplicate"

    except sqlite3.Error:
        connection.rollback()
        return False, "database"

    finally:
        connection.close()


def cari_pengguna(username):
    """Mencari akun pengguna berdasarkan username."""
    connection = get_db_connection()

    try:
        return connection.execute(
            """
            SELECT id_akun, username, peran, password_hash
            FROM akun_pengguna
            WHERE username = ?
            """,
            (username.strip(),),
        ).fetchone()

    finally:
        connection.close()


def ambil_pengguna(id_akun):
    """Mengambil akun pengguna berdasarkan ID."""
    connection = get_db_connection()

    try:
        return connection.execute(
            """
            SELECT id_akun, username, peran, password_hash
            FROM akun_pengguna
            WHERE id_akun = ?
            """,
            (id_akun,),
        ).fetchone()

    finally:
        connection.close()


def get_akun_by_username(username):
    """Mengambil akun pengguna berdasarkan username."""
    return cari_pengguna(username)


def create_akun(username, password, peran):
    """Membuat akun pengguna baru."""
    return tambah_pengguna(username, generate_password_hash(password), peran)


def verify_password(stored_hash, password):
    """Memeriksa password terhadap hash yang tersimpan."""
    try:
        return check_password_hash(stored_hash, password)
    except (TypeError, ValueError):
        return False


def _status_pembayaran(total_bayar, tagihan, tanggal_jatuh_tempo):
    """Menghitung status pembayaran berdasarkan total bayar dan jatuh tempo."""
    if total_bayar >= tagihan:
        return "Lunas"

    if tanggal_jatuh_tempo and str(tanggal_jatuh_tempo) < _tanggal_hari_ini():
        return "Terlambat"

    return "Belum Lunas"


def _tanggal_hari_ini():
    from datetime import date

    return date.today().isoformat()


def get_all_pembayaran(kata_kunci="", status=""):
    """Mengambil seluruh pembayaran dengan JOIN ke sewa, penyewa, dan kamar."""
    connection = get_db_connection()

    try:
        kata = kata_kunci.strip()
        pola = f"%{_escape_like(kata)}%"

        rows = connection.execute(
            """
            SELECT
                p.id_pembayaran,
                p.id_sewa,
                p.tanggal_pembayaran,
                p.jumlah_bayar,
                s.id_kamar,
                s.id_penyewa,
                s.tanggal_mulai,
                s.tanggal_selesai,
                s.tanggal_jatuh_tempo,
                s.harga_sewa_disepakati,
                pe.nama AS nama_penyewa,
                k.nomor_kamar AS nomor_kamar
            FROM pembayaran AS p
            JOIN sewa AS s ON s.id_sewa = p.id_sewa
            JOIN penyewa AS pe ON pe.id_penyewa = s.id_penyewa
            JOIN kamar AS k ON k.id_kamar = s.id_kamar
            WHERE pe.nama LIKE ? ESCAPE '\\'
               OR k.nomor_kamar LIKE ? ESCAPE '\\'
            ORDER BY p.tanggal_pembayaran DESC, p.id_pembayaran DESC
            """,
            (pola, pola),
        ).fetchall()

        hasil = []

        for row in rows:
            total_bayar = connection.execute(
                """
                SELECT COALESCE(SUM(jumlah_bayar), 0) AS total
                FROM pembayaran
                WHERE id_sewa = ?
                """,
                (row["id_sewa"],),
            ).fetchone()["total"]

            item = dict(row)
            item["total_bayar"] = total_bayar
            item["tagihan"] = row["harga_sewa_disepakati"]
            item["status_pembayaran"] = _status_pembayaran(
                total_bayar,
                row["harga_sewa_disepakati"],
                row["tanggal_jatuh_tempo"],
            )
            hasil.append(item)

        if status in {"Lunas", "Belum Lunas", "Terlambat"}:
            hasil = [
                item for item in hasil
                if item["status_pembayaran"] == status
            ]

        return hasil

    finally:
        connection.close()


def get_pembayaran_by_id(id_pembayaran):
    """Mengambil satu pembayaran berdasarkan ID, lengkap dengan data sewa."""
    connection = get_db_connection()

    try:
        row = connection.execute(
            """
            SELECT
                p.id_pembayaran,
                p.id_sewa,
                p.tanggal_pembayaran,
                p.jumlah_bayar,
                s.id_kamar,
                s.id_penyewa,
                s.tanggal_mulai,
                s.tanggal_selesai,
                s.tanggal_jatuh_tempo,
                s.harga_sewa_disepakati,
                pe.nama AS nama_penyewa,
                k.nomor_kamar AS nomor_kamar
            FROM pembayaran AS p
            JOIN sewa AS s ON s.id_sewa = p.id_sewa
            JOIN penyewa AS pe ON pe.id_penyewa = s.id_penyewa
            JOIN kamar AS k ON k.id_kamar = s.id_kamar
            WHERE p.id_pembayaran = ?
            """,
            (id_pembayaran,),
        ).fetchone()

        if row is None:
            return None

        total_bayar = connection.execute(
            """
            SELECT COALESCE(SUM(jumlah_bayar), 0) AS total
            FROM pembayaran
            WHERE id_sewa = ?
            """,
            (row["id_sewa"],),
        ).fetchone()["total"]

        item = dict(row)
        item["total_bayar"] = total_bayar
        item["tagihan"] = row["harga_sewa_disepakati"]
        item["status_pembayaran"] = _status_pembayaran(
            total_bayar,
            row["harga_sewa_disepakati"],
            row["tanggal_jatuh_tempo"],
        )
        return item

    finally:
        connection.close()


def create_pembayaran(id_sewa, tanggal_pembayaran, jumlah_bayar):
    """Menyimpan satu pembayaran."""
    connection = get_db_connection()

    try:
        sewa = connection.execute(
            "SELECT 1 FROM sewa WHERE id_sewa = ?",
            (id_sewa,),
        ).fetchone()

        if sewa is None:
            return False, "sewa_not_found"

        connection.execute(
            """
            INSERT INTO pembayaran (id_sewa, tanggal_pembayaran, jumlah_bayar)
            VALUES (?, ?, ?)
            """,
            (id_sewa, tanggal_pembayaran, str(jumlah_bayar)),
        )
        connection.commit()
        return True, None

    except sqlite3.IntegrityError:
        connection.rollback()
        return False, "database"

    except sqlite3.Error:
        connection.rollback()
        return False, "database"

    finally:
        connection.close()


def delete_pembayaran(id_pembayaran):
    """Menghapus satu pembayaran."""
    connection = get_db_connection()

    try:
        row = connection.execute(
            "SELECT 1 FROM pembayaran WHERE id_pembayaran = ?",
            (id_pembayaran,),
        ).fetchone()

        if row is None:
            return False, "not_found"

        connection.execute(
            "DELETE FROM pembayaran WHERE id_pembayaran = ?",
            (id_pembayaran,),
        )
        connection.commit()
        return True, None

    except sqlite3.Error:
        connection.rollback()
        return False, "database"

    finally:
        connection.close()


def get_laporan_pembayaran(tanggal_mulai="", tanggal_selesai="", kata_kunci=""):
    """Mengambil daftar pembayaran untuk laporan berdasarkan periode."""
    connection = get_db_connection()

    try:
        kata = kata_kunci.strip()
        pola = f"%{_escape_like(kata)}%"

        sql = """
            SELECT
                p.id_pembayaran,
                p.id_sewa,
                p.tanggal_pembayaran,
                p.jumlah_bayar,
                s.id_kamar,
                s.id_penyewa,
                s.tanggal_mulai,
                s.tanggal_selesai,
                s.tanggal_jatuh_tempo,
                s.harga_sewa_disepakati,
                pe.nama AS nama_penyewa,
                k.nomor_kamar AS nomor_kamar
            FROM pembayaran AS p
            JOIN sewa AS s ON s.id_sewa = p.id_sewa
            JOIN penyewa AS pe ON pe.id_penyewa = s.id_penyewa
            JOIN kamar AS k ON k.id_kamar = s.id_kamar
            WHERE (pe.nama LIKE ? ESCAPE '\\' OR k.nomor_kamar LIKE ? ESCAPE '\\')
        """
        params = [pola, pola]

        if tanggal_mulai.strip():
            sql += " AND p.tanggal_pembayaran >= ?"
            params.append(tanggal_mulai.strip())

        if tanggal_selesai.strip():
            sql += " AND p.tanggal_pembayaran <= ?"
            params.append(tanggal_selesai.strip())

        sql += " ORDER BY p.tanggal_pembayaran DESC, p.id_pembayaran DESC"

        return connection.execute(sql, params).fetchall()

    finally:
        connection.close()
