"""Uji pertama: memastikan pytest dan fixture berjalan.

Batas bawah harga sewa (0) harus diterima sesuai kamus data.
"""
import services


def test_harga_nol_diterima():
    data, galat = services.validate_kamar(
        {"nomor_kamar": "A-01", "harga_sewa": "0"}
    )

    assert galat == {}
    assert data["harga_sewa"] == "0"
