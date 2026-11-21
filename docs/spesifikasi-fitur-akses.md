# Matriks Akses dan Spesifikasi Fitur — Jobsheet 11

## Matriks akses

Peran yang dipakai: **pemilik** (akses penuh) dan **kasir** (akses terbatas).
Tanda ✓ = diizinkan, ✗ = ditolak (403), "login" = harus masuk terlebih dahulu.

| Halaman / aksi | Tamu | Pemilik | Kasir |
|---|---|---|---|
| Halaman login | ✓ | ✓ | ✓ |
| Beranda (`/`) | login | ✓ | ✓ |
| Daftar kamar | login | ✓ | ✓ |
| Tambah / ubah / hapus kamar | login | ✓ | ✗ |
| Daftar penyewa | login | ✓ | ✓ |
| Tambah / ubah / hapus penyewa | login | ✓ | ✗ |
| Daftar periode sewa | login | ✓ | ✓ |
| Tambah periode sewa | login | ✓ | ✓ |
| Daftar pembayaran | login | ✓ | ✓ |
| Tambah / hapus pembayaran | login | ✓ | ✓ |
| Laporan pendapatan | login | ✓ | ✗ |
| Logout (POST) | login | ✓ | ✓ |

Penegakan dilakukan di server oleh decorator `peran_diperlukan(...)` pada setiap rute,
termasuk rute POST. Tautan dan tombol yang disembunyikan hanya pelengkap tampilan.

## Kriteria penerimaan fitur kecil

| No | Fitur kecil | Kriteria penerimaan | Pelaksana |
|---|---|---|---|
| H1 | Akun awal dan hash | Kata sandi tersimpan sebagai hash `scrypt:`/`pbkdf2:`; kata sandi tidak ada di kode; akun dibuat lewat `scripts/buat_pengguna.py` dengan `getpass` | Pengembang |
| H2 | Login dan logout | Kredensial salah memakai satu pesan yang sama; sukses membuat sesi hanya berisi `pengguna_id`; logout hanya lewat POST | Pengembang |
| H3 | Pembatasan peran | Tamu dialihkan ke login membawa `next`; peran salah mendapat 403; berlaku pula untuk POST | Pengembang |
| H4 | Antarmuka sesuai wireframe | Menu menurut peran; satu templat induk dan satu CSS; pesan sukses dan galat terbaca | Pengembang |
| H5 | Validasi dua lapis | Atribut HTML5 dan validasi server keduanya aktif; isian dipertahankan saat galat | Pengembang |
