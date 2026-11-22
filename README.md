# Sistem Informasi Pengelolaan Kontrakan

Aplikasi web sederhana untuk mengelola kamar kontrakan, data penyewa,
periode sewa, pembayaran, dan laporan pendapatan. Dibuat sebagai proyek
mata kuliah Rekayasa Perangkat Lunak, Prodi D3 TI Politeknik Sampit.

Versi saat ini: **1.0.0** (lihat [CHANGELOG.md](CHANGELOG.md)).

## Fitur

- Login dengan dua peran: **pemilik** (semua fitur) dan **kasir** (melihat
  daftar kamar, periode sewa, pembayaran; tanpa kelola penyewa dan laporan).
- Kelola kamar: tambah, ubah, hapus, cari, dan status ketersediaan
  (Tersedia/Terisi).
- Kelola penyewa: tambah, ubah, hapus, cari.
- Periode sewa: tambah, cek tumpang tindih, status aktif/berakhir.
- Catat pembayaran; status Lunas/Belum Lunas/Terlambat; riwayat.
- Laporan pendapatan berdasarkan periode pembayaran.
- Pencadangan basis data (`python cadangkan.py`).

## Kebutuhan

- Python 3.10 atau lebih baru
- Git (untuk mengambil kode)

## Instalasi

```text
git clone https://github.com/[akun]/[repositori].git
cd [repositori]
python -m venv .venv
.venv\Scripts\activate          (Windows)
source .venv/bin/activate       (Linux/macOS)
python -m pip install -r requirements.txt
```

Untuk menjalankan pengujian, pasang juga dependensi pengembangan:

```text
python -m pip install -r requirements-dev.txt
```

## Konfigurasi (variabel lingkungan)

| Variabel | Fungsi | Bawaan |
|---|---|---|
| `APP_ENV` | `production` untuk mode produksi | (kosong = pengembangan) |
| `SECRET_KEY` (atau `FLASK_SECRET_KEY`) | Kunci sesi. **Wajib** pada produksi | — |
| `KONTRAKAN_DB` | Lokasi berkas basis data | `instance/kontrakan.db` |
| `COOKIE_SECURE` | `1` = cookie hanya lewat HTTPS; `0` bila memakai HTTP biasa di jaringan tertutup | `1` pada produksi |

Membuat kunci acak:

```text
python -c "import secrets; print(secrets.token_hex(32))"
```

**Jangan menyimpan kunci di dalam kode atau di Git.**

## Membuat akun pertama

```text
python scripts/buat_pengguna.py
```

Isi nama pengguna, peran (`pemilik` atau `kasir`), dan kata sandi
(minimal 8 karakter). Kata sandi dibaca dengan `getpass` dan tidak tersimpan
di berkas apa pun.

## Menjalankan

Pengembangan (di komputer sendiri):

```text
python app.py
```

Buka http://127.0.0.1:5000. Jika `FLASK_SECRET_KEY` belum disetel, aplikasi
membuat kunci acak untuk pengembangan (sesi tidak bertahan antar restart);
untuk penggunaan nyata setel `FLASK_SECRET_KEY`/`SECRET_KEY`.

Produksi (server WSGI, contoh Waitress):

```text
python -m pip install waitress
set APP_ENV=production            (Windows)   |   export APP_ENV=production   (Linux)
set SECRET_KEY=<kunci acak>       (Windows)   |   export SECRET_KEY=<kunci acak>
set KONTRAKAN_DB=<lokasi db>      (Windows)   |   export KONTRAKAN_DB=<lokasi db>
set COOKIE_SECURE=0               (hanya jaringan tertutup tanpa HTTPS)
waitress-serve --listen=127.0.0.1:8000 app:app
```

Untuk diakses dari komputer lain di jaringan toko (hanya jaringan tertutup):

```text
waitress-serve --listen=0.0.0.0:8000 app:app
```

Izinkan port 8000 pada firewall, lalu akses dari komputer kedua dengan
`http://[alamat IP]:8000`.

## Pengujian

```text
python -m pytest -q tests
python tests/uji_cepat.py
python -m unittest discover -s tests
```

Hasil yang diharapkan: 117 uji pytest + 23 subtes lulus, `SEMUA UJI LULUS`,
dan 59 unittest OK. Basis data uji memakai berkas sementara; `kontrakan.db`
nyata tidak tersentuh.

## Cadangan dan pemulihan

Membuat cadangan:

```text
python cadangkan.py
```

Hasil: `cadangan/kontrakan-YYYYMMDD-HHMMSS.db`. Folder `cadangan/` tidak
ikut Git.

Pemulihan: hentikan aplikasi, salin berkas cadangan menimpa berkas basis data,
jalankan lagi. Uji pemulihan secara berkala.

Prosedur untuk klien: cadangan rutin (mis. harian/mingguan), simpan di tempat
terpisah dari komputer toko, dan uji pemulihan minimal sekali per bulan.

## Struktur

```text
app.py            factory aplikasi, konfigurasi, CSRF, header keamanan
routes.py         rute HTTP tipis
services.py       validasi dan aturan bisnis
models.py         SQL dan akses basis data
percobaan.py      pembatasan percobaan login
versi.py          nomor versi
cadangkan.py      pencadangan basis data
templates/        templat Jinja2
static/           gaya CSS
tests/            uji otomatis (pytest + unittest)
docs/             dokumentasi, spesifikasi, pengujian, UAT
scripts/          skrip bantu (buat_pengguna.py)
```

## Keamanan

- Kunci rahasia dari variabel lingkungan; produksi tanpa kunci menolak start.
- Token CSRF pada semua form POST.
- Batas percobaan login dan pencatatan kejadian tanpa kata sandi.
- Cookie sesi HttpOnly, SameSite=Lax, Secure pada produksi.
- Header keamanan dasar pada setiap respons.

## Lisensi

Proyek akademik — Prodi D3 TI Politeknik Sampit.
