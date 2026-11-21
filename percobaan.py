"""Pembatasan percobaan login.

Penyimpanan memori ini hanya berlaku untuk satu proses. Untuk rilis dengan beberapa
proses, ganti penyimpanan dengan basis data atau cache bersama; logika di bawah
tetap menjadi acuan.
"""
import time

BATAS = 5       # jumlah kegagalan yang diizinkan
JENDELA = 300   # detik; kegagalan lebih lama dari ini dilupakan

_gagal = {}


def _bersihkan(kunci, sekarang):
    """Buang catatan yang sudah kedaluwarsa untuk kunci ini."""
    _gagal[kunci] = [
        t for t in _gagal.get(kunci, [])
        if sekarang - t < JENDELA
    ]


def terkunci(kunci, sekarang=None):
    """True bila kunci sudah mencapai batas kegagalan dalam jendela waktu."""
    sekarang = time.monotonic() if sekarang is None else sekarang
    _bersihkan(kunci, sekarang)
    return len(_gagal[kunci]) >= BATAS


def catat_gagal(kunci, sekarang=None):
    """Catat satu kegagalan pada kunci, lalu bersihkan catatan lama."""
    sekarang = time.monotonic() if sekarang is None else sekarang
    _bersihkan(kunci, sekarang)
    _gagal[kunci].append(sekarang)


def reset(kunci):
    """Hapus semua catatan kegagalan setelah login berhasil."""
    _gagal.pop(kunci, None)
