import sqlite3
from pathlib import Path


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
