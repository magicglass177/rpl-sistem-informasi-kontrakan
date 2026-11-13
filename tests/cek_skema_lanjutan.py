import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "docs" / "desain" / "schema.sql"

db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")

with SCHEMA.open("r", encoding="utf-8-sig") as file:
    db.executescript(file.read())

cur = db.cursor()
passed = 0
failed = 0


def cek_diterima(nama, sql, params=()):
    global passed, failed
    try:
        cur.execute(sql, params)
        db.commit()
        print(f"OK diterima: {nama}")
        passed += 1
    except sqlite3.IntegrityError as error:
        db.rollback()
        print(f"GAGAL: {nama} -- {error}")
        failed += 1


def cek_ditolak(nama, sql, params=()):
    global passed, failed
    try:
        cur.execute(sql, params)
        db.commit()
        print(f"GAGAL: {nama} -- seharusnya ditolak")
        failed += 1
    except sqlite3.IntegrityError as error:
        db.rollback()
        print(f"OK ditolak: {nama} ({error})")
        passed += 1


# Data dasar
cur.execute(
    "INSERT INTO kamar (nomor_kamar, harga_sewa) VALUES ('A01', 1000000)"
)
cur.execute(
    "INSERT INTO kamar (nomor_kamar, harga_sewa) VALUES ('A02', 1200000)"
)
cur.execute(
    "INSERT INTO penyewa (nama, no_telepon, alamat) VALUES ('Budi', '081234567890', 'Jl. Melati')"
)
cur.execute(
    "INSERT INTO penyewa (nama, no_telepon, alamat) VALUES ('Andi', '081234567891', 'Jl. Mawar')"
)

cur.execute("""
    INSERT INTO sewa (
        id_kamar, id_penyewa, tanggal_mulai,
        tanggal_selesai, harga_sewa_disepakati
    )
    VALUES (1, 1, '2026-01-01', '2026-01-31', 1000000)
""")
db.commit()

# 1. Periode setelah periode sebelumnya boleh diterima
cek_diterima(
    "Periode berurutan pada kamar yang sama",
    """
    INSERT INTO sewa (
        id_kamar, id_penyewa, tanggal_mulai,
        tanggal_selesai, harga_sewa_disepakati
    )
    VALUES (1, 2, '2026-02-01', '2026-02-28', 1000000)
    """
)

# 2. Periode yang sama pada kamar berbeda boleh diterima
cek_diterima(
    "Periode sama pada kamar berbeda",
    """
    INSERT INTO sewa (
        id_kamar, id_penyewa, tanggal_mulai,
        tanggal_selesai, harga_sewa_disepakati
    )
    VALUES (2, 1, '2026-01-01', '2026-01-31', 1200000)
    """
)

# 3. UPDATE yang menyebabkan tumpang tindih harus ditolak
cek_ditolak(
    "UPDATE periode sewa menjadi bertumpang tindih",
    """
    UPDATE sewa
    SET tanggal_mulai = '2026-01-15'
    WHERE id_sewa = 2
    """
)

# 4. Pembayaran valid
cek_diterima(
    "Pembayaran pertama",
    """
    INSERT INTO pembayaran (id_sewa, tanggal_pembayaran, jumlah_bayar)
    VALUES (1, '2026-01-05', 500000)
    """
)

# 5. Pembayaran kedua untuk sewa yang sama
cek_diterima(
    "Pembayaran cicilan kedua",
    """
    INSERT INTO pembayaran (id_sewa, tanggal_pembayaran, jumlah_bayar)
    VALUES (1, '2026-01-15', 500000)
    """
)

# 6. Kamar yang masih memiliki riwayat sewa tidak boleh dihapus
cek_ditolak(
    "Menghapus kamar yang masih memiliki riwayat sewa",
    "DELETE FROM kamar WHERE id_kamar = 1"
)

# 7. Penyewa yang masih memiliki riwayat sewa tidak boleh dihapus
cek_ditolak(
    "Menghapus penyewa yang masih memiliki riwayat sewa",
    "DELETE FROM penyewa WHERE id_penyewa = 1"
)

# 8. Sewa yang masih memiliki pembayaran tidak boleh dihapus
cek_ditolak(
    "Menghapus sewa yang masih memiliki pembayaran",
    "DELETE FROM sewa WHERE id_sewa = 1"
)

print("\n=== RINGKASAN PENGUJIAN LANJUTAN ===")
print(f"Pengujian berhasil : {passed}")
print(f"Pengujian gagal    : {failed}")

db.close()

if failed:
    raise SystemExit(1)

print("HASIL: Seluruh pengujian lanjutan berhasil.")
