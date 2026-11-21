import atexit
import os
import sys
import tempfile
import unittest
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
models.DB_PATH = TEMP_PATH / "kontrakan_test_penyewa.db"

# Secret key khusus pengujian.
os.environ.setdefault("FLASK_SECRET_KEY", "test-only-secret-key")

from app import create_app


class TestCrudPenyewa(unittest.TestCase):
    """Pengujian CRUD penyewa melalui rute Flask dan database sementara."""

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app.config.update(TESTING=True)
        cls.client = cls.app.test_client()

    def setUp(self):
        self._kosongkan_database()

        berhasil, status = models.create_penyewa(
            "Andi Pratama",
            "081234567890",
            "Jalan Melati No. 10",
        )
        self.assertTrue(berhasil, status)

        self.id_andi = models.get_all_penyewa()[0]["id_penyewa"]

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

    def _tambah_kamar(self, nomor="A-01"):
        berhasil, status = models.create_kamar(nomor, "850000")
        self.assertTrue(berhasil, status)

        return next(
            kamar["id_kamar"] for kamar in models.get_all_kamar()
            if kamar["nomor_kamar"] == nomor
        )

    def _tambah_sewa(self, id_kamar, id_penyewa):
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
                    "2026-01-01",
                    "2026-01-31",
                    850000,
                )
            )
            connection.commit()
        finally:
            connection.close()

    # ---------- Read ----------

    def test_01_daftar_penyewa_menampilkan_data(self):
        response = self.client.get("/penyewa")
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Andi Pratama", halaman)
        self.assertIn("081234567890", halaman)
        self.assertIn("Jalan Melati No. 10", halaman)

    def test_02_daftar_penyewa_kosong_menampilkan_pesan(self):
        self._kosongkan_database()

        response = self.client.get("/penyewa")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Belum ada data", response.get_data(as_text=True))

    def test_03_pencarian_penyewa_berdasarkan_nama(self):
        models.create_penyewa(
            "Budi Santoso", "081298765432", "Jalan Mawar No. 2"
        )

        response = self.client.get("/penyewa?q=Budi")
        halaman = response.get_data(as_text=True)

        self.assertIn("Budi Santoso", halaman)
        self.assertNotIn("Andi Pratama", halaman)

    def test_04_pencarian_penyewa_berdasarkan_telepon(self):
        response = self.client.get("/penyewa?q=081234567890")
        halaman = response.get_data(as_text=True)

        self.assertIn("Andi Pratama", halaman)

    def test_05_pencarian_penyewa_berdasarkan_alamat(self):
        response = self.client.get("/penyewa?q=Melati")
        halaman = response.get_data(as_text=True)

        self.assertIn("Andi Pratama", halaman)

    # ---------- Create ----------

    def test_06_tambah_penyewa_valid(self):
        response = self.client.post(
            "/penyewa/tambah",
            data={
                "nama": "Siti Aminah",
                "no_telepon": "081298765432",
                "alamat": "Jalan Mawar No. 2",
            },
            follow_redirects=True,
        )
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Data penyewa berhasil ditambahkan.", halaman)
        self.assertIn("Siti Aminah", halaman)

    def test_07_tambah_penyewa_nama_kosong_ditolak(self):
        response = self.client.post(
            "/penyewa/tambah",
            data={
                "nama": "",
                "no_telepon": "081298765432",
                "alamat": "Jalan Mawar No. 2",
            },
        )
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 400)
        self.assertIn("Nama penyewa wajib diisi.", halaman)
        # Isian lain yang sudah diketik tidak boleh hilang.
        self.assertIn('value="081298765432"', halaman)
        self.assertEqual(len(models.get_all_penyewa()), 1)

    def test_08_tambah_penyewa_alamat_kosong_ditolak(self):
        response = self.client.post(
            "/penyewa/tambah",
            data={
                "nama": "Siti Aminah",
                "no_telepon": "081298765432",
                "alamat": "",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Alamat wajib diisi.",
            response.get_data(as_text=True),
        )

    def test_09_batas_nomor_telepon_valid_diterima(self):
        daftar_nomor = [
            "0812345678",       # 08 + 8 digit (10 karakter)
            "0812345678901",    # 08 + 11 digit (13 karakter)
            "+62812345678",     # +628 + 8 digit (12 karakter)
            "+62812345678901",  # +628 + 11 digit (15 karakter)
        ]

        for indeks, nomor in enumerate(daftar_nomor, start=1):
            with self.subTest(nomor=nomor):
                response = self.client.post(
                    "/penyewa/tambah",
                    data={
                        "nama": f"Penyewa Batas {indeks}",
                        "no_telepon": nomor,
                        "alamat": "Jalan Uji No. 1",
                    },
                )
                self.assertEqual(response.status_code, 302)

        self.assertEqual(len(models.get_all_penyewa()), 5)

    def test_10_nomor_telepon_tidak_valid_ditolak(self):
        daftar_nomor = [
            "081234567",         # 9 digit
            "08123456789012",    # 14 digit
            "071234567890",      # awalan tidak valid
            "6281234567890",     # tanpa tanda +
            "+62 81234567890",   # mengandung spasi
            "0812-3456-7890",    # mengandung tanda hubung
            "08abcdefgh",        # mengandung huruf
            "+628123",           # terlalu pendek
        ]

        for nomor in daftar_nomor:
            with self.subTest(nomor=nomor):
                response = self.client.post(
                    "/penyewa/tambah",
                    data={
                        "nama": "Penyewa Tidak Valid",
                        "no_telepon": nomor,
                        "alamat": "Jalan Uji No. 1",
                    },
                )

                self.assertEqual(response.status_code, 400)
                self.assertIn(
                    "Nomor telepon harus diawali",
                    response.get_data(as_text=True),
                )

        self.assertEqual(len(models.get_all_penyewa()), 1)

    def test_11_isian_di_trim_sebelum_disimpan(self):
        response = self.client.post(
            "/penyewa/tambah",
            data={
                "nama": "  Siti Aminah  ",
                "no_telepon": "  081298765432  ",
                "alamat": "  Jalan Mawar No. 2  ",
            },
        )

        self.assertEqual(response.status_code, 302)

        penyewa = next(
            penyewa for penyewa in models.get_all_penyewa()
            if penyewa["nama"] == "Siti Aminah"
        )
        self.assertEqual(penyewa["no_telepon"], "081298765432")
        self.assertEqual(penyewa["alamat"], "Jalan Mawar No. 2")

    def test_12_nomor_telepon_sama_boleh_digunakan_dua_penyewa(self):
        # Kamus data menetapkan nomor telepon belum UNIQUE.
        response = self.client.post(
            "/penyewa/tambah",
            data={
                "nama": "Budi Santoso",
                "no_telepon": "081234567890",
                "alamat": "Jalan Mawar No. 2",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(models.get_all_penyewa()), 2)

    # ---------- Update ----------

    def test_13_form_ubah_menampilkan_data_lama(self):
        response = self.client.get(f"/penyewa/{self.id_andi}/ubah")
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Andi Pratama", halaman)
        self.assertIn("081234567890", halaman)
        self.assertIn("Jalan Melati No. 10", halaman)

    def test_14_ubah_penyewa_valid(self):
        response = self.client.post(
            f"/penyewa/{self.id_andi}/ubah",
            data={
                "nama": "Andi Pratama Putra",
                "no_telepon": "+6281234567890",
                "alamat": "Jalan Melati No. 12",
            },
            follow_redirects=True,
        )
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Data penyewa berhasil diperbarui.", halaman)

        penyewa = models.get_penyewa_by_id(self.id_andi)
        self.assertEqual(penyewa["nama"], "Andi Pratama Putra")
        self.assertEqual(penyewa["no_telepon"], "+6281234567890")
        self.assertEqual(penyewa["alamat"], "Jalan Melati No. 12")

    def test_15_ubah_penyewa_tidak_ditemukan_404(self):
        response = self.client.get("/penyewa/999999/ubah")
        self.assertEqual(response.status_code, 404)

    def test_16_ubah_penyewa_dengan_telepon_tidak_valid_ditolak(self):
        response = self.client.post(
            f"/penyewa/{self.id_andi}/ubah",
            data={
                "nama": "Andi Pratama",
                "no_telepon": "0812",
                "alamat": "Jalan Melati No. 10",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn(
            "Nomor telepon harus diawali",
            response.get_data(as_text=True),
        )

    # ---------- Delete ----------

    def test_17_hapus_penyewa_lewat_post(self):
        response = self.client.post(
            f"/penyewa/{self.id_andi}/hapus",
            follow_redirects=True,
        )
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Data penyewa berhasil dihapus.", halaman)
        self.assertIsNone(models.get_penyewa_by_id(self.id_andi))

    def test_18_hapus_penyewa_lewat_get_tidak_diizinkan(self):
        response = self.client.get(f"/penyewa/{self.id_andi}/hapus")

        self.assertEqual(response.status_code, 405)
        self.assertIsNotNone(models.get_penyewa_by_id(self.id_andi))

    def test_19_hapus_penyewa_yang_dipakai_sewa_ditolak(self):
        id_kamar = self._tambah_kamar()
        self._tambah_sewa(id_kamar, self.id_andi)

        response = self.client.post(
            f"/penyewa/{self.id_andi}/hapus",
            follow_redirects=True,
        )
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("tidak dapat dihapus", halaman)
        self.assertIsNotNone(models.get_penyewa_by_id(self.id_andi))

    def test_20_hapus_penyewa_tidak_ditemukan_404(self):
        response = self.client.post("/penyewa/999999/hapus")
        self.assertEqual(response.status_code, 404)

    # ---------- Keamanan ----------

    def test_21_sql_injection_pada_alamat_disimpan_sebagai_teks(self):
        payload = "Robert'); DROP TABLE penyewa;--"

        response = self.client.post(
            "/penyewa/tambah",
            data={
                "nama": "Robert",
                "no_telepon": "081234567891",
                "alamat": payload,
            },
        )

        self.assertEqual(response.status_code, 302)

        connection = models.get_db_connection()

        try:
            jumlah_tabel = connection.execute(
                """
                SELECT COUNT(*) FROM sqlite_master
                WHERE type = 'table' AND name = 'penyewa'
                """
            ).fetchone()[0]
            tersimpan = connection.execute(
                "SELECT alamat FROM penyewa WHERE alamat = ?",
                (payload,)
            ).fetchone()
        finally:
            connection.close()

        self.assertEqual(jumlah_tabel, 1)
        self.assertIsNotNone(tersimpan)
        self.assertEqual(tersimpan["alamat"], payload)

    def test_22_teks_html_di_escape_oleh_jinja(self):
        response = self.client.post(
            "/penyewa/tambah",
            data={
                "nama": "<b>tes</b>",
                "no_telepon": "081234567891",
                "alamat": "Jalan Uji No. 1",
            },
            follow_redirects=True,
        )
        halaman = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("&lt;b&gt;tes&lt;/b&gt;", halaman)
        self.assertNotIn("<b>tes</b>", halaman)


class TestValidasiPenyewa(unittest.TestCase):
    """Pengujian unit untuk aturan validasi penyewa."""

    def _validasi(self, nama="Andi", telepon="081234567890", alamat="Jl. Uji"):
        from services import validate_penyewa

        return validate_penyewa(
            {"nama": nama, "no_telepon": telepon, "alamat": alamat}
        )

    def test_nama_lebih_dari_100_karakter_ditolak(self):
        _, errors = self._validasi(nama="A" * 101)

        self.assertIn("nama", errors)

    def test_nama_100_karakter_diterima(self):
        _, errors = self._validasi(nama="A" * 100)

        self.assertEqual(errors, {})

    def test_batas_telepon_lokal_diterima(self):
        for nomor in ("0812345678", "0812345678901"):
            with self.subTest(nomor=nomor):
                _, errors = self._validasi(telepon=nomor)
                self.assertEqual(errors, {})

    def test_batas_telepon_internasional_diterima(self):
        for nomor in ("+62812345678", "+62812345678901"):
            with self.subTest(nomor=nomor):
                _, errors = self._validasi(telepon=nomor)
                self.assertEqual(errors, {})

    def test_telepon_di_luar_batas_ditolak(self):
        for nomor in ("081234567", "08123456789012", "+6281234567", "+628123456789012"):
            with self.subTest(nomor=nomor):
                _, errors = self._validasi(telepon=nomor)
                self.assertIn("no_telepon", errors)

    def test_telepon_dengan_karakter_bukan_angka_ditolak(self):
        for nomor in ("0812-3456-7890", "0812 3456 7890", "08abcdefgh"):
            with self.subTest(nomor=nomor):
                _, errors = self._validasi(telepon=nomor)
                self.assertIn("no_telepon", errors)


if __name__ == "__main__":
    print("=" * 60)
    print("PENGUJIAN OTOMATIS CRUD DAN KEAMANAN MODUL PENYEWA")
    print("=" * 60)
    print(f"Database pengujian: {models.DB_PATH}")
    print("Database utama tidak digunakan.")
    print()

    unittest.main(verbosity=2)
