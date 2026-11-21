"""Uji alur inti kontrakan dari sisi pengguna (melalui HTTP)."""
from datetime import date, timedelta

import models


def tambah_kamar(kirim, klien, nomor="A-01", harga="850000"):
    return kirim(klien, "/kamar/tambah", nomor_kamar=nomor, harga_sewa=harga)


def buat_sewa_aktif():
    """Siapkan kamar, penyewa, dan sewa yang sedang berlangsung."""
    models.create_kamar("A-01", "850000")
    models.create_penyewa("Andi", "081234567890", "Jalan Melati No. 10")
    hari_ini = date.today()
    mulai = (hari_ini - timedelta(days=1)).isoformat()
    selesai = (hari_ini + timedelta(days=30)).isoformat()
    berhasil, _ = models.create_sewa(1, 1, mulai, selesai, "", "850000")
    assert berhasil


def test_tambah_kamar_lalu_tampil_di_daftar(pemilik, kirim):
    respons = tambah_kamar(kirim, pemilik)

    assert "Data kamar berhasil ditambahkan." in respons.text
    assert "A-01" in respons.text
    assert [k["nomor_kamar"] for k in models.get_all_kamar()] == ["A-01"]


def test_nomor_kamar_ganda_ditolak(pemilik, kirim):
    tambah_kamar(kirim, pemilik, "A-01")
    respons = tambah_kamar(kirim, pemilik, "A-01")

    assert "sudah ada" in respons.text
    assert len(models.get_all_kamar()) == 1


def test_status_kamar_tersedia_lalu_terisi(pemilik, kirim):
    tambah_kamar(kirim, pemilik)
    assert models.get_all_kamar()[0]["status_ketersediaan"] == "Tersedia"

    buat_sewa_aktif()
    assert models.get_all_kamar()[0]["status_ketersediaan"] == "Terisi"


def test_sewa_tumpang_tindih_ditolak(pemilik, kirim):
    buat_sewa_aktif()
    respons = kirim(
        pemilik,
        "/sewa/tambah",
        id_kamar="1",
        id_penyewa="1",
        tanggal_mulai=date.today().isoformat(),
        tanggal_selesai=(date.today() + timedelta(days=10)).isoformat(),
        tanggal_jatuh_tempo="",
        harga_sewa_disepakati="850000",
    )

    assert "tumpang tindih" in respons.text
    assert len(models.get_all_sewa()) == 1


def test_pencarian_kamar_tidak_memakai_wildcard(pemilik, kirim):
    """TC-37: '%' harus dibaca sebagai huruf biasa, bukan wildcard LIKE."""
    tambah_kamar(kirim, pemilik, "A-01")
    tambah_kamar(kirim, pemilik, "B-01")

    respons = pemilik.get("/kamar", query_string={"q": "%"})

    assert "A-01" not in respons.text
    assert "B-01" not in respons.text


def test_hapus_kamar_yang_dipakai_sewa_ditolak(pemilik, kirim):
    buat_sewa_aktif()

    respons = kirim(pemilik, "/kamar/1/hapus")

    assert "tidak dapat dihapus" in respons.text
    assert len(models.get_all_kamar()) == 1
