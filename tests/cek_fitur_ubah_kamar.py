
import os
import sys
import tempfile
import unittest
from pathlib import Path

# Pastikan direktori utama proyek dapat diakses.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

# Import model sebelum aplikasi.
import models

# Gunakan database sementara, bukan database utama.
TEMP_DIR = tempfile.TemporaryDirectory()
TEMP_PATH = Path(TEMP_DIR.name)

models.INSTANCE_DIR = TEMP_PATH
models.DB_PATH = TEMP_PATH / "kontrakan_test.db"

# Secret key khusus pengujian.
os.environ["FLASK_SECRET_KEY"] = "test-only-secret-key"

# Import aplikasi setelah lokasi database diganti.
from app import app as flask_app

def _token(klien):
    """Ambil atau buat token CSRF pada sesi klien uji."""
    with klien.session_transaction() as sesi:
        if "csrf_token" not in sesi:
            sesi["csrf_token"] = "token-uji"
        return sesi["csrf_token"]


def post(klien, url, **kwargs):
    """Kirim POST dengan token CSRF yang sah."""
    data = dict(kwargs.pop("data", None) or {})
    data.setdefault("csrf_token", _token(klien))
    return klien.post(url, data=data, **kwargs)


class TestFiturUbahKamar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        flask_app.config.update(
            TESTING=True
        )

        cls.client = flask_app.test_client()

        # Siapkan dua kamar untuk pengujian.
        models.create_kamar("A-01", "850000")
        models.create_kamar("B-02", "750000")

        daftar = models.get_all_kamar()

        cls.kamar_pertama = next(
            kamar for kamar in daftar
            if kamar["nomor_kamar"] == "A-01"
        )

        cls.kamar_kedua = next(
            kamar for kamar in daftar
            if kamar["nomor_kamar"] == "B-02"
        )

        cls.id_pertama = cls.kamar_pertama["id_kamar"]
        cls.id_kedua = cls.kamar_kedua["id_kamar"]

    def test_01_halaman_edit_berhasil_dibuka(self):
        response = self.client.get(
            f"/kamar/{self.id_pertama}/ubah"
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"A-01", response.data)
        self.assertIn(b'value="850000"', response.data)

    def test_02_perubahan_kamar_berhasil_disimpan(self):
        response = post(self.client, 
            f"/kamar/{self.id_pertama}/ubah",
            data={
                "nomor_kamar": "A-01-UPDATED",
                "harga_sewa": "950000",
            },
        )

        self.assertEqual(response.status_code, 302)

        kamar = models.get_kamar_by_id(self.id_pertama)

        self.assertEqual(
            kamar["nomor_kamar"],
            "A-01-UPDATED"
        )

        self.assertEqual(
            float(kamar["harga_sewa"]),
            950000.0
        )

    def test_03_nomor_kamar_duplikat_ditolak(self):
        response = post(self.client, 
            f"/kamar/{self.id_pertama}/ubah",
            data={
                "nomor_kamar": "B-02",
                "harga_sewa": "900000",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(b"sudah ada", response.data)

        kamar = models.get_kamar_by_id(self.id_pertama)

        self.assertEqual(
            kamar["nomor_kamar"],
            "A-01-UPDATED"
        )

    def test_04_harga_negatif_ditolak(self):
        response = post(self.client, 
            f"/kamar/{self.id_pertama}/ubah",
            data={
                "nomor_kamar": "A-01-UPDATED",
                "harga_sewa": "-1000",
            },
        )

        self.assertEqual(response.status_code, 400)

        self.assertIn(
            b"Harga sewa tidak boleh negatif.",
            response.data
        )

    def test_05_nomor_kamar_kosong_ditolak(self):
        response = post(self.client, 
            f"/kamar/{self.id_pertama}/ubah",
            data={
                "nomor_kamar": "",
                "harga_sewa": "900000",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Nomor kamar wajib diisi.", response.data)

    def test_06_id_kamar_tidak_ditemukan(self):
        response = self.client.get("/kamar/999999/ubah")

        self.assertEqual(response.status_code, 404)

    def test_07_post_id_kamar_tidak_ditemukan(self):
        response = post(self.client, 
            "/kamar/999999/ubah",
            data={
                "nomor_kamar": "C-03",
                "harga_sewa": "800000",
            },
        )

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    print("=" * 55)
    print("PENGUJIAN FITUR UBAH KAMAR")
    print("=" * 55)
    print(f"Database pengujian: {models.DB_PATH}")
    print("Database utama tidak digunakan.")
    print()

    unittest.main(verbosity=2)

    TEMP_DIR.cleanup()
