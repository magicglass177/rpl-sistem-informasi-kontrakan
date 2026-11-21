"""Uji autentikasi: login, pesan galat, batas percobaan, dan logout."""
from models import cari_pengguna


def test_login_berhasil_memuat_akun_ke_sesi(pemilik):
    akun = cari_pengguna("bu_pemilik")

    with pemilik.session_transaction() as sesi:
        assert sesi["pengguna_id"] == akun["id_akun"]


def test_pesan_galat_login_sama_untuk_semua_kasus(kirim, tamu):
    ada = kirim(
        tamu,
        "/login",
        username="bu_pemilik",
        password="sandi-salah",
        ikuti=False,
    )
    tidak_ada = kirim(
        tamu,
        "/login",
        username="pengguna_tidak_ada",
        password="sandi-salah",
        ikuti=False,
    )

    assert ada.status_code == 401
    assert tidak_ada.status_code == 401
    # Membandingkan seluruh HTML terlalu kuat: field username sengaja diisi
    # ulang, sehingga markup berbeda walau pesan galatnya identik.
    pesan = "Username atau password salah."
    assert pesan in ada.text
    assert pesan in tidak_ada.text
    assert "tidak ditemukan" not in ada.text.lower()
    assert "tidak terdaftar" not in ada.text.lower()


def test_batas_percobaan_login(kirim, tamu):
    for _ in range(5):
        respons = kirim(
            tamu,
            "/login",
            username="bu_pemilik",
            password="sandi-salah",
            ikuti=False,
        )
        assert respons.status_code == 401

    respons = kirim(
        tamu,
        "/login",
        username="bu_pemilik",
        password="rahasia-uji-1",
        ikuti=False,
    )
    assert respons.status_code == 429
    assert "Terlalu banyak percobaan" in respons.text


def test_logout_menghapus_sesi(kirim, pemilik):
    respons = kirim(pemilik, "/logout", ikuti=False)

    assert respons.status_code == 302
    with pemilik.session_transaction() as sesi:
        assert "pengguna_id" not in sesi
