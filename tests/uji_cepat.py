import os
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

TEMP_DIR = tempfile.TemporaryDirectory()
TEMP_PATH = Path(TEMP_DIR.name)

import models

models.INSTANCE_DIR = TEMP_PATH
models.DB_PATH = TEMP_PATH / "kontrakan_uji_cepat.db"

os.environ.setdefault("FLASK_SECRET_KEY", "test-only-secret-key")

from app import create_app


def cek(kondisi, pesan):
    if not kondisi:
        raise AssertionError(pesan)


def main():
    app = create_app()
    app.config.update(TESTING=True)
    client = app.test_client()

    # Pastikan database uji kosong.
    connection = models.get_db_connection()
    try:
        connection.execute("DELETE FROM pembayaran")
        connection.execute("DELETE FROM sewa")
        connection.execute("DELETE FROM penyewa")
        connection.execute("DELETE FROM kamar")
        connection.execute("DELETE FROM akun_pengguna")
        connection.commit()
    finally:
        connection.close()

    # 1. Daftar kamar (keadaan kosong).
    response = client.get("/kamar")
    cek(response.status_code == 200, "Daftar kamar tidak dapat dibuka.")
    cek("Belum ada data" in response.get_data(as_text=True), "Pesan kosong tidak tampil.")

    # 2. Tambah kamar valid.
    response = client.post(
        "/kamar/tambah",
        data={"nomor_kamar": "A-01", "harga_sewa": "850000"},
        follow_redirects=True,
    )
    cek(response.status_code == 200, "Tambah kamar valid gagal.")
    cek("Data kamar berhasil ditambahkan." in response.get_data(as_text=True), "Pesan sukses tambah tidak tampil.")
    cek(len(models.get_all_kamar()) == 1, "Data kamar valid tidak tersimpan.")

    # 3. Tambah kamar tidak valid (nomor kosong).
    response = client.post(
        "/kamar/tambah",
        data={"nomor_kamar": "", "harga_sewa": "850000"},
    )
    cek(response.status_code == 400, "Tambah kamar tidak valid tidak ditolak.")
    cek(len(models.get_all_kamar()) == 1, "Data tidak valid tersimpan.")

    id_kamar = models.get_all_kamar()[0]["id_kamar"]

    # 4. Ubah kamar valid.
    response = client.post(
        f"/kamar/{id_kamar}/ubah",
        data={"nomor_kamar": "A-01-UBAH", "harga_sewa": "900000"},
        follow_redirects=True,
    )
    cek(response.status_code == 200, "Ubah kamar valid gagal.")
    cek(models.get_kamar_by_id(id_kamar)["nomor_kamar"] == "A-01-UBAH", "Perubahan kamar tidak tersimpan.")

    # 5. Hapus kamar yang tidak dipakai.
    response = client.post(
        f"/kamar/{id_kamar}/hapus",
        follow_redirects=True,
    )
    cek(response.status_code == 200, "Hapus kamar gagal.")
    cek(models.get_kamar_by_id(id_kamar) is None, "Kamar tidak terhapus.")

    # 6. Pencarian.
    models.create_kamar("B-01", "750000")
    models.create_kamar("C-01", "800000")
    response = client.get("/kamar?q=B-01")
    halaman = response.get_data(as_text=True)
    cek("B-01" in halaman, "Pencarian tidak menampilkan data yang cocok.")
    cek("C-01" not in halaman, "Pencarian menampilkan data yang tidak cocok.")

    # 7. Transaksi: induk tidak ada tidak meninggalkan baris sebagian.
    models.create_penyewa("Penyewa Uji", "081234567890", "Jalan Uji No. 1")
    id_penyewa = models.get_all_penyewa()[0]["id_penyewa"]
    jumlah_sebelum = len(models.get_all_sewa())
    berhasil, status = models.create_sewa(
        999999,
        id_penyewa,
        "2026-01-01",
        "2026-01-31",
        "",
        "850000",
    )
    cek(not berhasil, "Transaksi dengan induk tidak ada seharusnya gagal.")
    cek(len(models.get_all_sewa()) == jumlah_sebelum, "Transaksi gagal meninggalkan baris sebagian.")

    # 8. Transaksi valid tersimpan.
    id_kamar = next(
        kamar["id_kamar"] for kamar in models.get_all_kamar()
        if kamar["nomor_kamar"] == "B-01"
    )
    berhasil, status = models.create_sewa(
        id_kamar,
        id_penyewa,
        "2026-02-01",
        "2026-02-28",
        "2026-02-15",
        "750000",
    )
    cek(berhasil, f"Transaksi valid gagal: {status}")
    cek(len(models.get_all_sewa()) == jumlah_sebelum + 1, "Transaksi valid tidak tersimpan.")

    print("=" * 50)
    print("SEMUA UJI LULUS")
    print("=" * 50)


if __name__ == "__main__":
    try:
        main()
    finally:
        TEMP_DIR.cleanup()
