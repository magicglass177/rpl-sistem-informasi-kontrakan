import atexit
import os
import sys
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path

# Pastikan direktori utama proyek dapat diakses.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

# Gunakan database sementara, bukan database utama.
TEMP_DIR = tempfile.TemporaryDirectory()
TEMP_PATH = Path(TEMP_DIR.name)
atexit.register(TEMP_DIR.cleanup)

import models

models.INSTANCE_DIR = TEMP_PATH
models.DB_PATH = TEMP_PATH / "kontrakan_test_kamar.db"

# Secret key khusus pengujian.
os.environ.setdefault("FLASK_SECRET_KEY", "test-only-secret-key")

from app import create_app


class TestCrudKamar(unittest.TestCase):
    """Pengujian CRUD kamar melalui rute Flask dan database sementara."""

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app.config.update(TESTING=True)
        cls.client = cls.app.test_client()

    def setUp(self):
        self._kosongkan_database()

        models.create_kamar("A-01", "850000")
        models.create_kamar("B-01", "750000")

        daftar = models.get_all_kamar()
        self.id_a01 = next(
            kamar["id_kamar"] for kamar in daftar
            if kamar["nomor_kamar"] == "A-01"
        )
        self.id_b01 = next(
            kamar["id_kamar"] for kamar in daftar
            if kamar["nomor_kamar"] == "B-01"
        )

    def _kosongkan_database(self):
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

    def _tambah_penyewa(self, nama="Penyewa Uji"):
        berhasil, status = models.create_penyewa(
            nama,
            "081234567890",
            "Jalan Melati No. 10",
        )
        self.assertTrue(berhasil, status)
        return models.get_all_penyewa()[0]["id_penyewa"]

    def _tambah_sewa(self, id_kamar, id_penyewa):
        hari_ini = date.today()
        connection = models.get_db_connection()

        try:
            connection.execute(
                """
                INSERT INTO sewa (
                    id_kamar, id_penyewa, tanggal_mulai,
                    tanggal_selesai, harga_sewa_disepakati
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    id_kamar,
                    id_penyewa,
                    (hari_ini - timedelta(days=1)).isoformat(),
                    (hari_ini + timedelta(days=1)).isoformat(),
                    850000,
                )
            )
            connection.commit()
        finally:
            connection.close()

    # ---------- Read ----------

    def test_01_daftar_kamar_menampilkan_data(self):
        response = self.client.get("/kamar")
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("A-01", halaman)
        self.assertIn("B-01", halaman)
        self.assertIn("Rp850.000", halaman)

    def test_02_daftar_kamar_kosong_menampilkan_pesan(self):
        self._kosongkan_database()

        response = self.client.get("/kamar")
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Belum ada data", halaman)

    def test_03_pencarian_kamar(self):
        response = self.client.get("/kamar?q=A-01")
        halaman = response.get_data(as_text=True)

        self.assertIn("A-01", halaman)
        self.assertNotIn("B-01", halaman)

    def test_04_status_kamar_terisi_saat_ada_sewa_aktif(self):
        id_penyewa = self._tambah_penyewa()
        self._tambah_sewa(self.id_a01, id_penyewa)

        response = self.client.get("/kamar")
        halaman = response.get_data(as_text=True)

        self.assertIn("Terisi", halaman)
        self.assertIn("Tersedia", halaman)

    # ---------- Create ----------

    def test_05_tambah_kamar_valid(self):
        response = self.client.post(
            "/kamar/tambah",
            data={"nomor_kamar": "C-01", "harga_sewa": "900000"},
            follow_redirects=True,
        )
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Data kamar berhasil ditambahkan.", halaman)
        self.assertIn("C-01", halaman)

        kamar = next(
            kamar for kamar in models.get_all_kamar()
            if kamar["nomor_kamar"] == "C-01"
        )
        self.assertEqual(float(kamar["harga_sewa"]), 900000.0)

    def test_06_tambah_kamar_nomor_kosong_ditolak(self):
        response = self.client.post(
            "/kamar/tambah",
            data={"nomor_kamar": "", "harga_sewa": "850000"},
        )
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 400)
        self.assertIn("Nomor kamar wajib diisi.", halaman)
        # Isian lain yang sudah diketik tidak boleh hilang.
        self.assertIn('value="850000"', halaman)
        self.assertEqual(len(models.get_all_kamar()), 2)

    def test_07_tambah_kamar_harga_negatif_ditolak(self):
        response = self.client.post(
            "/kamar/tambah",
            data={"nomor_kamar": "C-02", "harga_sewa": "-5"},
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Harga sewa tidak boleh negatif.",
            response.get_data(as_text=True),
        )
        self.assertEqual(len(models.get_all_kamar()), 2)

    def test_08_tambah_kamar_harga_teks_ditolak(self):
        response = self.client.post(
            "/kamar/tambah",
            data={"nomor_kamar": "C-03", "harga_sewa": "abc"},
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Harga sewa harus berupa angka.",
            response.get_data(as_text=True),
        )

    def test_09_tambah_kamar_duplikat_ditolak(self):
        response = self.client.post(
            "/kamar/tambah",
            data={"nomor_kamar": "A-01", "harga_sewa": "900000"},
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "sudah ada",
            response.get_data(as_text=True),
        )
        self.assertEqual(len(models.get_all_kamar()), 2)

    def test_10_tambah_kamar_nomor_terlalu_panjang_ditolak(self):
        response = self.client.post(
            "/kamar/tambah",
            data={"nomor_kamar": "X" * 21, "harga_sewa": "900000"},
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "maksimal 20 karakter",
            response.get_data(as_text=True),
        )

    # ---------- Update ----------

    def test_11_form_ubah_menampilkan_data_lama(self):
        response = self.client.get(f"/kamar/{self.id_a01}/ubah")
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("A-01", halaman)
        self.assertIn('value="850000"', halaman)

    def test_12_ubah_kamar_valid(self):
        response = self.client.post(
            f"/kamar/{self.id_a01}/ubah",
            data={"nomor_kamar": "A-01-UPDATED", "harga_sewa": "950000"},
            follow_redirects=True,
        )
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Data kamar berhasil diperbarui.", halaman)

        kamar = models.get_kamar_by_id(self.id_a01)
        self.assertEqual(kamar["nomor_kamar"], "A-01-UPDATED")
        self.assertEqual(float(kamar["harga_sewa"]), 950000.0)

    def test_13_ubah_kamar_menjadi_duplikat_ditolak(self):
        response = self.client.post(
            f"/kamar/{self.id_a01}/ubah",
            data={"nomor_kamar": "B-01", "harga_sewa": "850000"},
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "sudah ada",
            response.get_data(as_text=True),
        )
        self.assertEqual(
            models.get_kamar_by_id(self.id_a01)["nomor_kamar"],
            "A-01",
        )

    def test_14_ubah_kamar_tidak_ditemukan_404(self):
        response = self.client.get("/kamar/999999/ubah")
        self.assertEqual(response.status_code, 404)

    # ---------- Delete ----------

    def test_15_hapus_kamar_lewat_post(self):
        response = self.client.post(
            f"/kamar/{self.id_a01}/hapus",
            follow_redirects=True,
        )
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Data kamar berhasil dihapus.", halaman)
        self.assertIsNone(models.get_kamar_by_id(self.id_a01))

    def test_16_hapus_kamar_lewat_get_tidak_diizinkan(self):
        response = self.client.get(f"/kamar/{self.id_a01}/hapus")

        self.assertEqual(response.status_code, 405)
        self.assertIsNotNone(models.get_kamar_by_id(self.id_a01))

    def test_17_hapus_kamar_yang_dipakai_sewa_ditolak(self):
        id_penyewa = self._tambah_penyewa()
        self._tambah_sewa(self.id_a01, id_penyewa)

        response = self.client.post(
            f"/kamar/{self.id_a01}/hapus",
            follow_redirects=True,
        )
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("tidak dapat dihapus", halaman)
        self.assertIsNotNone(models.get_kamar_by_id(self.id_a01))

    def test_18_hapus_kamar_tidak_ditemukan_404(self):
        response = self.client.post("/kamar/999999/hapus")
        self.assertEqual(response.status_code, 404)

    # ---------- Keamanan ----------

    def test_19_sql_injection_disimpan_sebagai_teks(self):
        payload = "';DROP TABLE kamar"
        self.assertLessEqual(len(payload), 20)

        response = self.client.post(
            "/kamar/tambah",
            data={"nomor_kamar": payload, "harga_sewa": "800000"},
        )

        self.assertEqual(response.status_code, 302)

        connection = models.get_db_connection()

        try:
            jumlah_tabel = connection.execute(
                """
                SELECT COUNT(*) FROM sqlite_master
                WHERE type = 'table' AND name = 'kamar'
                """
            ).fetchone()[0]
            tersimpan = connection.execute(
                "SELECT nomor_kamar FROM kamar WHERE nomor_kamar = ?",
                (payload,)
            ).fetchone()
        finally:
            connection.close()

        self.assertEqual(jumlah_tabel, 1)
        self.assertIsNotNone(tersimpan)
        self.assertEqual(tersimpan["nomor_kamar"], payload)

    def test_20_teks_html_di_escape_oleh_jinja(self):
        response = self.client.post(
            "/kamar/tambah",
            data={"nomor_kamar": "<b>tes</b>", "harga_sewa": "800000"},
            follow_redirects=True,
        )
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("&lt;b&gt;tes&lt;/b&gt;", halaman)
        self.assertNotIn("<b>tes</b>", halaman)


class TestValidasiKamar(unittest.TestCase):
    """Pengujian unit untuk aturan validasi kamar."""

    def test_harga_nol_diterima(self):
        from services import validate_kamar

        data, errors = validate_kamar(
            {"nomor_kamar": "A-01", "harga_sewa": "0"}
        )

        self.assertEqual(errors, {})
        self.assertEqual(data["harga_sewa"], "0")

    def test_harga_desimal_diterima(self):
        from services import validate_kamar

        data, errors = validate_kamar(
            {"nomor_kamar": "A-01", "harga_sewa": "850000.50"}
        )

        self.assertEqual(errors, {})
        self.assertEqual(data["harga_sewa"], "850000.50")

    def test_harga_nan_ditolak(self):
        from services import validate_kamar

        _, errors = validate_kamar(
            {"nomor_kamar": "A-01", "harga_sewa": "NaN"}
        )

        self.assertIn("harga_sewa", errors)

    def test_harga_infinity_ditolak(self):
        from services import validate_kamar

        _, errors = validate_kamar(
            {"nomor_kamar": "A-01", "harga_sewa": "Infinity"}
        )

        self.assertIn("harga_sewa", errors)

    def test_nomor_kamar_hanya_spasi_ditolak(self):
        from services import validate_kamar

        _, errors = validate_kamar(
            {"nomor_kamar": "   ", "harga_sewa": "850000"}
        )

        self.assertIn("nomor_kamar", errors)


if __name__ == "__main__":
    print("=" * 60)
    print("PENGUJIAN OTOMATIS CRUD DAN KEAMANAN MODUL KAMAR")
    print("=" * 60)
    print(f"Database pengujian: {models.DB_PATH}")
    print("Database utama tidak digunakan.")
    print()

    unittest.main(verbosity=2)
