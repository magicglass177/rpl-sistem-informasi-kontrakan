"""Matriks akses: rute x peran (tamu, kasir, pemilik)."""
import pytest

# (metode, alamat, tamu, kasir, pemilik) -> status yang diharapkan.
MATRIKS = [
    ("GET", "/kamar", 302, 200, 200),
    ("GET", "/kamar/tambah", 302, 403, 200),
    # Daftar penyewa adalah halaman baca bersama (@semua_peran), bukan 403.
    ("GET", "/penyewa", 302, 200, 200),
    ("GET", "/sewa", 302, 200, 200),
    ("GET", "/sewa/tambah", 302, 200, 200),
    ("GET", "/pembayaran", 302, 200, 200),
    ("GET", "/pembayaran/tambah", 302, 200, 200),
    ("GET", "/laporan", 302, 403, 200),
]


@pytest.mark.parametrize(
    "metode, alamat, utk_tamu, utk_kasir, utk_pemilik", MATRIKS
)
def test_matriks_akses(
    tamu, kasir, pemilik, metode, alamat, utk_tamu, utk_kasir, utk_pemilik
):
    assert tamu.open(alamat, method=metode).status_code == utk_tamu
    assert kasir.open(alamat, method=metode).status_code == utk_kasir
    assert pemilik.open(alamat, method=metode).status_code == utk_pemilik


def test_kasir_tidak_dapat_tambah_kamar_lewat_post(kasir, kirim):
    respons = kirim(
        kasir,
        "/kamar/tambah",
        nomor_kamar="X-1",
        harga_sewa="1",
        ikuti=False,
    )
    assert respons.status_code == 403


def test_kasir_tidak_dapat_melihat_laporan(kasir):
    respons = kasir.get("/laporan")
    assert respons.status_code == 403
    assert "Akses Ditolak" in respons.text


def test_post_tanpa_token_csrf_ditolak(pemilik):
    respons = pemilik.post(
        "/kamar/tambah",
        data={"nomor_kamar": "X-1", "harga_sewa": "1"},
    )
    assert respons.status_code == 400
