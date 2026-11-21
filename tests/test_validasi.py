"""DRAF AI — uji partisi ekuivalen dan nilai batas (services.py).

Nilai harapan diambil dari kolom "Hasil diharapkan" pada
docs/pengujian/test-case.md, bukan dihitung dari kode.
"""
import pytest

import services


def kamar(**ubah):
    form = {"nomor_kamar": "A-01", "harga_sewa": "850000"}
    form.update(ubah)
    return form


def penyewa(**ubah):
    form = {
        "nama": "Andi Pratama",
        "no_telepon": "081234567890",
        "alamat": "Jalan Melati No. 10",
    }
    form.update(ubah)
    return form


def sewa(**ubah):
    form = {
        "id_kamar": "1",
        "id_penyewa": "1",
        "tanggal_mulai": "2026-03-01",
        "tanggal_selesai": "2026-03-31",
        "tanggal_jatuh_tempo": "",
        "harga_sewa_disepakati": "850000",
    }
    form.update(ubah)
    return form


# TC-01..TC-11: harga sewa (kamus data: >= 0, DECIMAL(12,2))
@pytest.mark.parametrize("harga, valid", [
    ("0", True),                 # TC-01 batas bawah
    ("1", True),                 # TC-02
    ("850000", True),            # TC-03 nilai tipikal
    (" 850000 ", True),          # TC-04 spasi pinggir
    ("9999999999.99", True),     # TC-05 batas atas DECIMAL(12,2)
    ("10000000000.00", False),   # TC-06 tepat di atas batas
    ("-1", False),               # TC-07 negatif
    ("abc", False),              # TC-08 bukan angka
    ("", False),                 # TC-09 kosong
    ("²", False),                # TC-10 angka Unicode
    ("Infinity", False),         # TC-11 tak hingga
])
def test_harga_sewa(harga, valid):
    data, galat = services.validate_kamar(kamar(harga_sewa=harga))
    assert (galat == {}) is valid
    if valid:
        assert data["harga_sewa"] == harga.strip()
    else:
        # Diperbaiki: periksa kunci galat yang tepat, bukan sekadar "ada galat".
        assert "harga_sewa" in galat


# TC-12..TC-15: nomor kamar (kamus data: 1-20 karakter, wajib, unik)
@pytest.mark.parametrize("nomor, valid", [
    ("A", True),                 # TC-12 batas bawah
    ("A" * 20, True),            # TC-13 batas atas
    ("A" * 21, False),           # TC-14 tepat di atas batas
    ("", False),                 # TC-15 kosong
])
def test_nomor_kamar(nomor, valid):
    data, galat = services.validate_kamar(kamar(nomor_kamar=nomor))
    assert (galat == {}) is valid
    if valid:
        assert data["nomor_kamar"] == nomor


# TC-19..TC-24: nomor telepon (08+8..11 digit atau +628+8..11 digit)
@pytest.mark.parametrize("telepon, valid", [
    ("081234567890", True),      # TC-19 tipikal
    ("0812345678", True),        # TC-20 batas bawah 10 digit
    ("08123456789", True),       # TC-21 11 digit
    ("0812345678901", True),     # TC-22 batas atas 13 digit
    ("08123456789012", False),   # TC-23 14 digit
    ("+621234567890", False),    # TC-24 awalan salah
])
def test_no_telepon(telepon, valid):
    _, galat = services.validate_penyewa(penyewa(no_telepon=telepon))
    assert (galat == {}) is valid


# TC-25 dan satu jalur normal: nama penyewa
@pytest.mark.parametrize("nama, valid", [
    ("Andi Pratama", True),
    ("", False),                 # TC-25
])
def test_nama_penyewa(nama, valid):
    data, galat = services.validate_penyewa(penyewa(nama=nama))
    # Diperbaiki: asersi dangkal diganti pemeriksaan kunci yang spesifik.
    assert ("nama" in galat) is (not valid)
    if valid:
        assert data["nama"] == nama


# TC-26..TC-28: tanggal mulai sewa
@pytest.mark.parametrize("tanggal, valid, kunci", [
    ("2026-03-01", True, None),     # TC-26
    ("20261108", False, "tanggal_mulai"),  # TC-27 format kompak ditolak
    ("2026-02-30", False, "tanggal_mulai"),  # TC-28 tidak ada di kalender
])
def test_tanggal_sewa(tanggal, valid, kunci):
    _, galat = services.validate_sewa(sewa(tanggal_mulai=tanggal))
    assert (galat == {}) is valid
    # Diperbaiki: periksa bahwa galat memang berasal dari isian tanggal mulai.
    # Pada draf AI, TC-27 salah lulus karena galatnya berasal dari tanggal
    # selesai yang lebih awal, bukan dari format tanggal kompak.
    if kunci:
        assert kunci in galat


# TC-29: urutan tanggal
def test_urutan_tanggal():
    _, galat = services.validate_sewa(
        sewa(tanggal_mulai="2026-03-01", tanggal_selesai="2026-02-28")
    )
    # Diperbaiki: sebut kunci galatnya, jangan hanya "ada galat".
    assert "tanggal_selesai" in galat


# TC-30..TC-32: jumlah bayar (kamus data: > 0)
@pytest.mark.parametrize("jumlah, valid", [
    ("0", False),                # TC-30 batas bawah
    ("1", True),                 # TC-31
    ("-1", False),               # TC-32
])
def test_jumlah_bayar(jumlah, valid):
    _, galat = services.validate_pembayaran(
        {
            "id_sewa": "1",
            "tanggal_pembayaran": "2026-03-10",
            "jumlah_bayar": jumlah,
        }
    )
    assert (galat == {}) is valid
