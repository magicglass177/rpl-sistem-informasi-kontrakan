import sqlite3
from pathlib import Path
from decimal import Decimal


BASE_DIR = Path(__file__).resolve().parent
INSTANCE_DIR = BASE_DIR / "instance"
DB_PATH = INSTANCE_DIR / "kontrakan.db"
SCHEMA_PATH = BASE_DIR / "docs" / "desain" / "schema.sql"


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

def get_all_sewa(kata_kunci=""):
    """
    Mengambil seluruh periode sewa dengan JOIN ke penyewa dan kamar.
    Pencarian mencakup nama penyewa dan nomor kamar.
    """
    connection = get_db_connection()

    try:
        pola = f"%{kata_kunci.strip()}%"

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
            WHERE p.nama LIKE ? OR k.nomor_kamar LIKE ?
            ORDER BY s.tanggal_mulai DESC, s.id_sewa DESC
            """,
            (pola, pola)
        ).fetchall()

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
