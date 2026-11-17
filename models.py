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