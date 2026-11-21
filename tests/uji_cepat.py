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

    models.create_akun("admin", "rahasia", "pemilik")
    client.post(
        "/login",
        data={"username": "admin", "password": "rahasia"},
    )

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

    # 9. Pembayaran bertahap dan status lunas.
    id_kamar_bayar = next(
        kamar["id_kamar"] for kamar in models.get_all_kamar()
        if kamar["nomor_kamar"] == "B-01"
    )
    berhasil, status = models.create_sewa(
        id_kamar_bayar,
        id_penyewa,
        "2026-03-01",
        "2026-03-31",
        "2026-03-15",
        "750000",
    )
    cek(berhasil, f"Transaksi sewa untuk pembayaran gagal: {status}")

    id_sewa_bayar = models.get_all_sewa()[0]["id_sewa"]
    berhasil, status = models.create_pembayaran(
        id_sewa_bayar,
        "2026-03-10",
        "750000",
    )
    cek(berhasil, f"Pembayaran valid gagal: {status}")
    cek(len(models.get_all_pembayaran()) == 1, "Pembayaran valid tidak tersimpan.")

    pembayaran = models.get_all_pembayaran()[0]
    cek(
        pembayaran["status_pembayaran"] == "Lunas",
        "Status pembayaran tidak menjadi Lunas.",
    )

    # 10. Pembayaran dengan induk tidak ada ditolak.
    berhasil, status = models.create_pembayaran(
        999999,
        "2026-03-10",
        "100000",
    )
    cek(not berhasil, "Pembayaran dengan sewa tidak ada seharusnya gagal.")
    cek(
        len(models.get_all_pembayaran()) == 1,
        "Pembayaran tidak valid meninggalkan data.",
    )

    # 11. Laporan pendapatan berdasarkan periode.
    rows = models.get_laporan_pembayaran("2026-03-01", "2026-03-31")
    cek(len(rows) == 1, "Laporan tidak menampilkan pembayaran pada periode.")
    cek(
        abs(sum(float(item["jumlah_bayar"]) for item in rows) - 750000) < 0.01,
        "Total pendapatan laporan tidak sesuai.",
    )

    rows_kosong = models.get_laporan_pembayaran("2026-04-01", "2026-04-30")
    cek(len(rows_kosong) == 0, "Laporan menampilkan data di luar periode.")

    # 12. Tamu dialihkan ke login dengan parameter next.
    client_tamu = app.test_client()
    response = client_tamu.get("/kamar")
    cek(response.status_code == 302, "Tamu harus dialihkan ke login.")
    cek(
        "/login" in response.headers["Location"]
        and "next=" in response.headers["Location"],
        "Redirect tamu harus membawa parameter next.",
    )

    # 13. Satu pesan galat yang sama untuk kata sandi dan username salah.
    client_login = app.test_client()
    response = client_login.post(
        "/login",
        data={"username": "admin", "password": "sandi-salah"},
        follow_redirects=True,
    )
    cek(
        "Username atau password salah." in response.get_data(as_text=True),
        "Pesan galat kata sandi salah tidak tampil.",
    )

    response = client_login.post(
        "/login",
        data={"username": "pengguna_tidak_ada", "password": "sandi-salah"},
        follow_redirects=True,
    )
    cek(
        "Username atau password salah." in response.get_data(as_text=True),
        "Pesan galat username salah tidak sama.",
    )

    # 14. Kata sandi tersimpan sebagai hash berasam, bukan teks.
    akun_admin = models.get_akun_by_username("admin")
    cek(akun_admin is not None, "Akun admin tidak ditemukan.")
    cek(
        str(akun_admin["password_hash"]).startswith(("scrypt:", "pbkdf2:")),
        "Kata sandi tidak tersimpan sebagai hash berasam.",
    )
    cek(
        akun_admin["password_hash"] != "rahasia",
        "Kata sandi tersimpan sebagai teks biasa.",
    )

    # 15. Parameter next luar situs diabaikan (cegah open redirect).
    client_next = app.test_client()
    response = client_next.post(
        "/login?next=https://situs-jahat.example",
        data={"username": "admin", "password": "rahasia"},
    )
    cek(response.status_code == 302, "Login sukses harus dialihkan.")
    lokasi = response.headers["Location"]
    cek("situs-jahat.example" not in lokasi, "Open redirect tidak dicegah.")
    cek(lokasi.startswith("/"), "Alihkan harus menuju alamat internal.")

    # 16. Otorisasi: kasir ditolak, pemilik diizinkan.
    berhasil, status = models.create_akun("kasiruji", "sandi-kasir-uji", "kasir")
    cek(berhasil, f"Akun kasir uji gagal dibuat: {status}")

    client_kasir = app.test_client()
    response = client_kasir.post(
        "/login",
        data={"username": "kasiruji", "password": "sandi-kasir-uji"},
    )
    cek(response.status_code == 302, "Login peran kasir gagal.")

    response = client_kasir.get("/kamar/tambah")
    cek(response.status_code == 403, "Kasir harus mendapat 403 pada halaman tambah.")
    cek(
        "Akses Ditolak" in response.get_data(as_text=True),
        "Halaman 403 tidak tampil.",
    )

    jumlah_sebelum = len(models.get_all_kamar())
    response = client_kasir.post(
        "/kamar/tambah",
        data={"nomor_kamar": "X-99", "harga_sewa": "100000"},
    )
    cek(response.status_code == 403, "Kasir harus dilarang POST tambah kamar.")
    cek(
        len(models.get_all_kamar()) == jumlah_sebelum,
        "Data berubah akibat POST dari peran kasir.",
    )

    response = client_kasir.get("/kamar")
    cek(response.status_code == 200, "Kasir harus bisa membuka daftar kamar.")

    response = client.get("/kamar/tambah")
    cek(response.status_code == 200, "Peran pemilik harus bisa membuka tambah kamar.")

    # 17. Logout lewat POST mengosongkan sesi.
    response = client_kasir.post("/logout", follow_redirects=True)
    cek(response.status_code == 200, "Logout gagal.")
    response = client_kasir.get("/kamar")
    cek(response.status_code == 302, "Sesi belum kosong setelah logout.")

    print("=" * 50)
    print("SEMUA UJI LULUS")
    print("=" * 50)


if __name__ == "__main__":
    try:
        main()
    finally:
        TEMP_DIR.cleanup()
