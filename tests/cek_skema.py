import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "docs" / "desain" / "schema.sql"

connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")

with SCHEMA.open("r", encoding="utf-8-sig") as file:
    connection.executescript(file.read())

cursor = connection.cursor()

# Data dasar yang valid
cursor.execute(
    "INSERT INTO akun_pengguna (username, password_hash) VALUES (?, ?)",
    ("admin", "hash_password_admin")
)

cursor.execute(
    "INSERT INTO kamar (nomor_kamar, harga_sewa) VALUES (?, ?)",
    ("A01", 1000000)
)

cursor.execute(
    "INSERT INTO kamar (nomor_kamar, harga_sewa) VALUES (?, ?)",
    ("A02", 1200000)
)

cursor.execute(
    """
    INSERT INTO penyewa (nama, no_telepon, alamat)
    VALUES (?, ?, ?)
    """,
    ("Budi", "081234567890", "Jl. Melati")
)

cursor.execute(
    """
    INSERT INTO penyewa (nama, no_telepon, alamat)
    VALUES (?, ?, ?)
    """,
    ("Andi", "081234567891", "Jl. Mawar")
)

cursor.execute(
    """
    INSERT INTO sewa (
        id_kamar, id_penyewa, tanggal_mulai,
        tanggal_selesai, tanggal_jatuh_tempo,
        harga_sewa_disepakati
    )
    VALUES (1, 1, '2026-01-01', '2026-01-31', NULL, 1000000)
    """
)

connection.commit()
print("OK diterima: data dasar valid")

passed = 0
failed = 0


def harus_ditolak(nama, perintah, parameter=()):
    global passed, failed

    try:
        cursor.execute(perintah, parameter)
        connection.commit()
        print(f"GAGAL: {nama} -- data tidak ditolak")
        failed += 1
    except sqlite3.IntegrityError as error:
        connection.rollback()
        print(f"OK ditolak: {nama} ({error})")
        passed += 1


# 1. Username harus unik
harus_ditolak(
    "Username duplikat",
    """
    INSERT INTO akun_pengguna (username, password_hash)
    VALUES (?, ?)
    """,
    ("admin", "hash_lain")
)

# 2. Nomor kamar harus unik
harus_ditolak(
    "Nomor kamar duplikat",
    """
    INSERT INTO kamar (nomor_kamar, harga_sewa)
    VALUES (?, ?)
    """,
    ("A01", 900000)
)

# 3. Harga kamar tidak boleh negatif
harus_ditolak(
    "Harga sewa kamar negatif",
    """
    INSERT INTO kamar (nomor_kamar, harga_sewa)
    VALUES (?, ?)
    """,
    ("A03", -500000)
)

# 4. FK kamar harus mengarah ke kamar yang tersedia
harus_ditolak(
    "ID kamar tidak ditemukan",
    """
    INSERT INTO sewa (
        id_kamar, id_penyewa, tanggal_mulai,
        tanggal_selesai, harga_sewa_disepakati
    )
    VALUES (999, 1, '2026-02-01', '2026-02-28', 1000000)
    """
)

# 5. FK penyewa harus mengarah ke penyewa yang tersedia
harus_ditolak(
    "ID penyewa tidak ditemukan",
    """
    INSERT INTO sewa (
        id_kamar, id_penyewa, tanggal_mulai,
        tanggal_selesai, harga_sewa_disepakati
    )
    VALUES (2, 999, '2026-02-01', '2026-02-28', 1000000)
    """
)

# 6. Tanggal selesai tidak boleh sebelum tanggal mulai
harus_ditolak(
    "Tanggal selesai sebelum tanggal mulai",
    """
    INSERT INTO sewa (
        id_kamar, id_penyewa, tanggal_mulai,
        tanggal_selesai, harga_sewa_disepakati
    )
    VALUES (2, 1, '2026-02-28', '2026-02-01', 1000000)
    """
)

# 7. Tanggal kalender harus valid
harus_ditolak(
    "Tanggal kalender tidak valid",
    """
    INSERT INTO sewa (
        id_kamar, id_penyewa, tanggal_mulai,
        tanggal_selesai, harga_sewa_disepakati
    )
    VALUES (2, 1, '2026-02-30', '2026-03-31', 1000000)
    """
)

# 8. Kamar yang sama tidak boleh memiliki periode tumpang tindih
harus_ditolak(
    "Periode sewa bertumpang tindih",
    """
    INSERT INTO sewa (
        id_kamar, id_penyewa, tanggal_mulai,
        tanggal_selesai, harga_sewa_disepakati
    )
    VALUES (1, 2, '2026-01-15', '2026-02-15', 1000000)
    """
)

# 9. Jumlah pembayaran harus lebih besar dari nol
harus_ditolak(
    "Jumlah pembayaran nol",
    """
    INSERT INTO pembayaran (
        id_sewa, tanggal_pembayaran, jumlah_bayar
    )
    VALUES (1, '2026-01-05', 0)
    """
)

# 10. FK pembayaran harus mengarah ke sewa yang tersedia
harus_ditolak(
    "ID sewa pembayaran tidak ditemukan",
    """
    INSERT INTO pembayaran (
        id_sewa, tanggal_pembayaran, jumlah_bayar
    )
    VALUES (999, '2026-01-05', 500000)
    """
)

# 11. Tanggal pembayaran harus valid
harus_ditolak(
    "Tanggal pembayaran tidak valid",
    """
    INSERT INTO pembayaran (
        id_sewa, tanggal_pembayaran, jumlah_bayar
    )
    VALUES (1, '2026-02-30', 500000)
    """
)

print("\n=== RINGKASAN PENGUJIAN ===")
print(f"Pengujian penolakan berhasil : {passed}")
print(f"Pengujian gagal              : {failed}")

connection.close()

if failed:
    raise SystemExit(1)

print("HASIL: Seluruh pengujian penolakan berhasil.")
