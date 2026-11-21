"""Fixture bersama untuk semua uji pytest.

Memakai basis data sementara, sehingga instance/kontrakan.db (data nyata)
tidak pernah tersentuh. Sesuai Lampiran D.1 Jobshet 13, disesuaikan dengan
proyek Sistem Informasi Pengelolaan Kontrakan.
"""
import os
import sys
import tempfile
from pathlib import Path

import pytest
from werkzeug.security import generate_password_hash

# Uji unittest lama (Jobssheet 12) mengganti models.DB_PATH saat diimpor dan
# dijalankan terpisah lewat `python -m unittest discover -s tests` serta
# `python tests/uji_cepat.py`. Keduanya tetap dipertahankan; hanya tidak
# dikumpulkan oleh pytest agar tidak bertabrakan dengan fixture di bawah.
collect_ignore = ["test_keamanan.py"]

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# app.py membuat objek app saat diimpor dan memerlukan kunci dari lingkungan.
os.environ.setdefault("FLASK_SECRET_KEY", "kunci-uji-js13")

import models

# Arahkan model ke berkas sementara SEBELUM mengimpor app (app memanggil init_db).
_folder_uji = Path(tempfile.mkdtemp(prefix="kontrakan-uji-"))
models.INSTANCE_DIR = _folder_uji
models.DB_PATH = _folder_uji / "uji.db"

import app as aplikasi
import percobaan

SANDI_PEMILIK = "rahasia-uji-1"
SANDI_KASIR = "rahasia-uji-2"

# Hash cepat khusus uji agar ratusan uji berjalan singkat.
# Kode produksi tetap memakai nilai bawaan Werkzeug.
_hash_cepat = lambda s: generate_password_hash(s, method="pbkdf2:sha256:1000")


@pytest.fixture(autouse=True)
def basis_bersih():
    """Setiap uji mulai dari basis data kosong berisi dua akun uji."""
    models.DB_PATH.unlink(missing_ok=True)
    models.init_db()
    percobaan._gagal.clear()
    models.tambah_pengguna(
        "bu_pemilik", _hash_cepat(SANDI_PEMILIK), "pemilik"
    )
    models.tambah_pengguna("kasir1", _hash_cepat(SANDI_KASIR), "kasir")


@pytest.fixture
def kirim():
    """Fungsi POST yang otomatis membawa token CSRF yang sah."""

    def _kirim(klien, alamat, ikuti=True, **data):
        with klien.session_transaction() as sesi:
            sesi.setdefault("csrf_token", "token-uji")
            token = sesi["csrf_token"]
        data.setdefault("csrf_token", token)
        return klien.post(alamat, data=data, follow_redirects=ikuti)

    return _kirim


@pytest.fixture
def tamu():
    return aplikasi.app.test_client()


@pytest.fixture
def pemilik(kirim):
    klien = aplikasi.app.test_client()
    kirim(
        klien,
        "/login",
        username="bu_pemilik",
        password=SANDI_PEMILIK,
    )
    return klien


@pytest.fixture
def kasir(kirim):
    klien = aplikasi.app.test_client()
    kirim(
        klien,
        "/login",
        username="kasir1",
        password=SANDI_KASIR,
    )
    return klien
