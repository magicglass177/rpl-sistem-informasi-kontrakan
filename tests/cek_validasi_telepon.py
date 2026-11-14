import sqlite3
from pathlib import Path

schema_path = (
    Path(__file__).resolve().parents[1]
    / "docs" / "desain" / "schema.sql"
)
schema = schema_path.read_text(encoding="utf-8")

connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON;")
connection.executescript(schema)

nomor_valid = [
    "081234567890",
    "0812345678",
    "0812345678901",
    "+6281234567890",
    "+62812345678",
    "+62812345678901",
]

nomor_tidak_valid = [
    "0812-3456-7890",
    "0812 3456 7890",
    "+62 81234567890",
    "6281234567890",
    "071234567890",
    "08123",
    "+628123",
    "08abcdefgh",
    "+628abcdefgh",
    "0812345678901234",
]


def uji_nomor(nomor, harus_diterima):
    try:
        connection.execute(
            """
            INSERT INTO penyewa (nama, no_telepon, alamat)
            VALUES (?, ?, ?)
            """,
            ("Penyewa Uji", nomor, "Alamat Uji"),
        )
        connection.commit()

        if not harus_diterima:
            raise AssertionError(
                f"Nomor tidak valid justru diterima: {nomor}"
            )

        print(f"OK diterima: {nomor}")

    except sqlite3.IntegrityError:
        if harus_diterima:
            raise AssertionError(
                f"Nomor valid justru ditolak: {nomor}"
            )

        print(f"OK ditolak: {nomor}")


print("=== PENGUJIAN NOMOR TELEPON VALID ===")
for nomor in nomor_valid:
    uji_nomor(nomor, True)

print("\\n=== PENGUJIAN NOMOR TELEPON TIDAK VALID ===")
for nomor in nomor_tidak_valid:
    uji_nomor(nomor, False)

connection.close()

print("\\n=== RINGKASAN ===")
print(f"Nomor valid diuji       : {len(nomor_valid)}")
print(f"Nomor tidak valid diuji : {len(nomor_tidak_valid)}")
print("HASIL: Seluruh pengujian validasi nomor telepon berhasil.")
