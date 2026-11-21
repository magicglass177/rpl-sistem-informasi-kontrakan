# Temuan Keamanan — Tinjauan Jobsheet 11 dan Tindak Lanjut Jobsheet 12

Tinjauan terhadap diff autentikasi, otorisasi, dan antarmuka (Lampiran C.2).
Rujukan: OWASP Top 10:2025 dan praktik Flask.

## Temuan dan tindakan

| No | Temuan | Bukti / dampak | Tindakan | Status |
|---:|---|---|---|---|
| 1 | Kode AI menggunakan decorator `@hanya_pemilih` yang tidak pernah didefinisikan | Nama fungsi seharusnya `hanya_pemilik`; seluruh rute yang memakainya akan menimbulkan `NameError`, sehingga penegakan peran tidak berjalan sama sekali | Diganti menjadi `@hanya_pemilik` untuk kelola kamar/penyewa dan laporan, serta `@semua_peran` untuk modul operasional; ditambahkan uji 403 untuk GET dan POST | Sudah diperbaiki |
| 2 | Pemeriksaan `next` memiliki escape backslash yang salah (`"\"`), sehingga modul tidak dapat diimpor dan potensi open redirect tidak tertutup | `python -c "import routes"` gagal; `next=https://situs-jahat.example` berisiko dialihkan keluar situs | Diperbaiki menjadi `"\\" not in tujuan` pada `_tujuan_aman`; uji menegaskan alihkan selalu ke alamat internal | Sudah diperbaiki |
| 3 | Skrip pembuatan akun lama menerima kata sandi dari variabel lingkungan dan memanggil `create_akun` dengan dua argumen | Kata sandi dapat terekam di riwayat perintah/CI; fungsi baru memerlukan peran | Skrip diganti dengan `scripts/buat_pengguna.py` yang memakai `getpass` dan memanggil `services.buat_pengguna(username, password, peran)` | Sudah diperbaiki |
| 4 | Pesan galat login berbeda antara "kata sandi salah" dan "nama pengguna tidak ada" | Membocorkan keberadaan akun (user enumeration) | Satu pesan "Username atau password salah." untuk keduanya; `check_password_hash` tetap dijalankan pada hash palsu `_HASH_PALSU` agar waktu respons serupa | Sudah diperbaiki |
| 5 | Sesi tidak dibersihkan saat login dan cookie belum dibatasi | Risiko session fixation dan pembacaan cookie oleh skrip | `session.clear()` sebelum mengisi `pengguna_id`; `SESSION_COOKIE_HTTPONLY=True` dan `SESSION_COOKIE_SAMESITE="Lax"`; logout POST memanggil `session.clear()` | Sudah diperbaiki |
| 6 | Tidak ada pembatasan jumlah percobaan login | Penyerang dapat melakukan brute force tanpa batas | Modul `percobaan.py`: 5 kegagalan/5 menit per IP+username; percobaan ke-6 ditolak 429; uji batas dan kedaluwarsa lulus | Sudah diperbaiki |
| 7 | Tidak ada token CSRF pada form POST | Permintaan lintas situs dapat memicu hapus/ubah data bila pengguna sedang login | Token acak per sesi, input tersembunyi pada 9 form, `secrets.compare_digest`; POST tanpa token ditolak 400 dan dicatat | Sudah diperbaiki |
| 8 | Atribut `Secure` pada cookie sesi belum aktif | Cookie dapat dikirim melalui HTTP bila deployment salah konfigurasi | `SESSION_COOKIE_SECURE=PRODUKSI` melalui `APP_ENV=production`; produksi tanpa kunci gagal start; uji subprocess lulus | Sudah diperbaiki |
| 9 | Kejadian keamanan belum dicatat | Login gagal, 403, dan CSRF gagal tidak terdeteksi | `app.logger` mencatat kejadian tanpa kata sandi; username memakai `%r`; uji `assertLogs` lulus | Sudah diperbaiki |
| 10 | Header keamanan dasar belum ada | Risiko clickjacking dan MIME sniffing | `after_request` menambahkan `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`; uji lulus | Sudah diperbaiki |
| 11 | Penyimpanan batas login di memori | Hanya berlaku per proses; rilis multi-proses perlu penyimpanan bersama | Rencana Sprint 3: pindahkan ke basis data/cache bersama, logika tetap | Ditunda (Sprint 3) |
| 12 | CSP ketat belum memungkinkan karena `onsubmit` sebaris | Risiko kecil; konfirmasi hapus masih memakai JS inline | Pindahkan ke berkas JS lokal bersama HTTPS pada Pertemuan 14 | Ditunda (Pertemuan 14) |
| 13 | `pip-audit` tidak terpasang di lingkungan | Tidak dapat memindai kerentanan dependensi otomatis | `requirements.txt` sudah berversi; semua paket adalah dependensi Flask yang dikenal; audit otomatis ditunda bila lingkungan mengizinkan | Ditunda |

## Daftar periksa C.2

| No | Pemeriksaan | Hasil |
|---:|---|---|
| 1 | Kata sandi tersimpan sebagai hash berasam (bukan MD5/SHA polos) | Ya |
| 2 | Tidak ada kata sandi, akun contoh, atau secret key tertulis di kode/repositori | Ya |
| 3 | Pesan galat login sama untuk dua kasus | Ya |
| 4 | `session.clear()` saat login dan logout; logout hanya POST | Ya |
| 5 | Semua rute dalam matriks memakai decorator, termasuk POST | Ya |
| 6 | Peran dibaca dari basis data di server, bukan dari form/URL | Ya |
| 7 | Parameter `next` hanya menerima alamat dalam situs | Ya |
| 8 | Temuan yang belum diperbaiki tercatat untuk Pertemuan 12 | Ya |
| 9 | Semua formulir POST memiliki token CSRF yang diperiksa server | Ya |
| 10 | Batas percobaan login dan pesan galat sama | Ya |
| 11 | Login gagal, akses ditolak, dan CSRF gagal dicatat tanpa rahasia | Ya |
| 12 | Mode produksi mewajibkan kunci; cookie Secure dan header dasar aktif | Ya |
| 13 | Dependensi dikenal, diperlukan, dan versi dikunci | Ya |
| 14 | Audit otomatis dependensi (pip-audit) tersedia di lingkungan | Ditunda |

Catatan tambahan Jobsheet 12: `percobaan.py` menyimpan kegagalan di memori (per proses);
untuk rilis multi-proses diperlukan penyimpanan bersama. CSP ketat belum memungkinkan
karena konfirmasi hapus memakai `onsubmit` sebaris. Keduanya tercatat sebagai temuan tertunda.

Catatan: akun awal dibuat secara lokal lewat skrip; `instance/`, `*.db`, `.env`, dan
`.venv/` tidak ikut di-commit. Uji keamanan hanya dilakukan pada aplikasi kelompok sendiri.
