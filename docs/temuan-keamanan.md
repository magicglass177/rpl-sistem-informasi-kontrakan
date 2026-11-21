# Temuan Keamanan — Tinjauan Jobsheet 11

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
| 6 | Tidak ada pembatasan jumlah percobaan login | Penyerang dapat melakukan brute force tanpa batas | Belum diterapkan pada Jobsheet 11; direncanakan pada Pertemuan 12 dengan batas percobaan + jeda waktu dan uji pencegah | Ditunda (Pertemuan 12) |
| 7 | Tidak ada token CSRF pada form POST | Permintaan lintas situs dapat memicu hapus/ubah data bila pengguna sedang login | Belum diterapkan; direncanakan token CSRF pada semua form POST dan penolakan permintaan tanpa token | Ditunda (Pertemuan 12) |
| 8 | Atribut `Secure` pada cookie sesi belum aktif | Cookie dapat dikirim melalui HTTP bila deployment salah konfigurasi | Akan diaktifkan bersama HTTPS pada deployment (Pertemuan 14); saat ini hanya HttpOnly dan SameSite | Ditunda (Pertemuan 14) |

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

Catatan: akun awal dibuat secara lokal lewat skrip; `instance/`, `*.db`, `.env`, dan
`.venv/` tidak ikut di-commit. Uji keamanan hanya dilakukan pada aplikasi kelompok sendiri.
