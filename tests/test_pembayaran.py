"""Uji status pembayaran, riwayat, dan laporan pendapatan."""
from datetime import date, timedelta

import models


def siap_sewa(harga="850000", jatuh_tempo=""):
    """Buat satu sewa untuk diuji pembayarannya."""
    models.create_kamar("A-01", harga)
    models.create_penyewa("Andi", "081234567890", "Jalan Melati No. 10")
    berhasil, _ = models.create_sewa(
        1, 1, "2026-03-01", "2026-03-31", jatuh_tempo, harga
    )
    assert berhasil
    return 1


def bayar(kirim, klien, id_sewa, tanggal, jumlah):
    return kirim(
        klien,
        "/pembayaran/tambah",
        id_sewa=str(id_sewa),
        tanggal_pembayaran=tanggal,
        jumlah_bayar=jumlah,
    )


def test_lunas_setelah_bayar_penuh(pemilik, kirim):
    id_sewa = siap_sewa()
    bayar(kirim, pemilik, id_sewa, "2026-03-10", "850000")

    assert models.get_all_pembayaran()[0]["status_pembayaran"] == "Lunas"


def test_belum_lunas_sebelum_jatuh_tempo(pemilik, kirim):
    tempo = (date.today() + timedelta(days=10)).isoformat()
    id_sewa = siap_sewa(jatuh_tempo=tempo)
    bayar(kirim, pemilik, id_sewa, date.today().isoformat(), "500000")

    assert models.get_all_pembayaran()[0]["status_pembayaran"] == "Belum Lunas"


def test_terlambat_setelah_jatuh_tempo(pemilik, kirim):
    tempo = (date.today() - timedelta(days=1)).isoformat()
    id_sewa = siap_sewa(jatuh_tempo=tempo)
    bayar(kirim, pemilik, id_sewa, date.today().isoformat(), "500000")

    assert models.get_all_pembayaran()[0]["status_pembayaran"] == "Terlambat"


def test_pembayaran_bertahap_terakumulasi(pemilik, kirim):
    id_sewa = siap_sewa()
    bayar(kirim, pemilik, id_sewa, "2026-03-10", "400000")
    bayar(kirim, pemilik, id_sewa, "2026-03-20", "450000")

    assert len(models.get_all_pembayaran()) == 2
    assert models.get_all_pembayaran()[0]["total_bayar"] == 850000
    assert models.get_all_pembayaran()[0]["status_pembayaran"] == "Lunas"


def test_laporan_menampilkan_pembayaran_pada_periode(pemilik, kirim):
    id_sewa = siap_sewa()
    bayar(kirim, pemilik, id_sewa, "2026-03-10", "850000")

    respons = pemilik.get(
        "/laporan",
        query_string={
            "tanggal_mulai": "2026-03-01",
            "tanggal_selesai": "2026-03-31",
        },
    )

    assert "Andi" in respons.text
    assert "A-01" in respons.text


def test_laporan_di_luar_periode_kosong(pemilik, kirim):
    id_sewa = siap_sewa()
    bayar(kirim, pemilik, id_sewa, "2026-03-10", "850000")

    respons = pemilik.get(
        "/laporan",
        query_string={
            "tanggal_mulai": "2026-04-01",
            "tanggal_selesai": "2026-04-30",
        },
    )

    assert "Andi" not in respons.text
