import atexit
import os
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

TEMP_DIR = tempfile.TemporaryDirectory()
atexit.register(TEMP_DIR.cleanup)

import models

models.INSTANCE_DIR = Path(TEMP_DIR.name)
models.DB_PATH = Path(TEMP_DIR.name) / "kontrakan_test_keamanan.db"

os.environ.setdefault("FLASK_SECRET_KEY", "test-only-secret-key")

from app import create_app


class TestKeamanan(unittest.TestCase):
    """Pengujian pencatatan kejadian keamanan dan konfigurasi."""

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app.config.update(TESTING=True)
        cls.client = cls.app.test_client()
        models.create_akun("adminuji", "sandi-adminuji", "pemilik")
        models.create_akun("kasiruji", "sandi-kasiruji", "kasir")

    @staticmethod
    def _token(klien):
        with klien.session_transaction() as sesi:
            if "csrf_token" not in sesi:
                sesi["csrf_token"] = "token-uji"
            return sesi["csrf_token"]

    def post(self, klien, url, **kwargs):
        data = dict(kwargs.pop("data", None) or {})
        data.setdefault("csrf_token", self._token(klien))
        return klien.post(url, data=data, **kwargs)

    def test_log_login_gagal_tanpa_kata_sandi(self):
        kata_sandi_rahasia = "jangan-tampil-di-log-999"

        with self.assertLogs("app", level="WARNING") as tangkap:
            self.post(
                self.client,
                "/login",
                data={"username": "adminuji", "password": kata_sandi_rahasia},
            )

        teks = "\n".join(tangkap.output)
        self.assertIn("Login gagal", teks)
        self.assertIn("adminuji", teks)
        self.assertNotIn(kata_sandi_rahasia, teks)

    def test_log_akses_ditolak(self):
        klien = self.app.test_client()
        self.post(
            klien,
            "/login",
            data={"username": "kasiruji", "password": "sandi-kasiruji"},
        )

        with self.assertLogs("app", level="WARNING") as tangkap:
            respons = klien.get("/kamar/tambah")

        self.assertEqual(respons.status_code, 403)
        self.assertIn("Akses ditolak", "\n".join(tangkap.output))

    def test_log_csrf_gagal(self):
        klien = self.app.test_client()

        with self.assertLogs("app", level="WARNING") as tangkap:
            respons = klien.post("/login", data={"username": "x", "password": "y"})

        self.assertEqual(respons.status_code, 400)
        self.assertIn("CSRF gagal", "\n".join(tangkap.output))


if __name__ == "__main__":
    unittest.main(verbosity=2)
