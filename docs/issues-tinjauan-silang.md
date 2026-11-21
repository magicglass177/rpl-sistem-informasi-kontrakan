# Draf Issue Tinjauan Silang — Jobsheet 12

Lima draf berikut disiapkan memakai templat Lampiran D.2. Belum dikirim karena pasangan
kelompok peninjau belum ditetapkan. **Jangan menyerang aplikasi kelompok lain**; tinjauan
dilakukan hanya dengan membaca kode pada commit yang ditunjuk dosen. Setiap Issue ditujukan
ke repositori kelompok yang ditinjau, dengan permalink ke baris kode (klik nomor baris di
GitHub → *Copy permalink*). Ganti `<commit>` dan `<.baris>` setelah pasangan ditetapkan.

---

## I-01 [Keamanan] Form POST belum memakai token CSRF

- **Lokasi:** `templates/base.html` (form logout) dan seluruh form tambah/ubah/hapus — `https://github.com/<kelompok>/<repo>/blob/<commit>/templates/base.html#L23`
- **Kategori:** A01 Broken Access Control | **Risiko:** Tinggi
- **Mengapa ini masalah:** Perubahan data hanya dilindungi decorator peran. Situs pihak ketiga dapat mengirim POST memakai cookie sesi korban, sehingga hapus/ubah terjadi tanpa persetujuan pengguna.
- **Cara memeriksa (tanpa menyerang):** Baca kode; tidak ada input `csrf_token` dan tidak ada pemeriksaan token pada `before_request`.
- **Usulan:** Token acak per sesi (`secrets.token_hex`), input tersembunyi di semua form POST, `secrets.compare_digest`, tolak 400 saat gagal.
- **Wajib diperbaiki atau saran:** Wajib diperbaiki.

## I-02 [Keamanan] Belum ada batas percobaan login

- **Lokasi:** `routes.py` fungsi `login()` — `https://github.com/<kelompok>/<repo>/blob/<commit>/routes.py#L103`
- **Kategori:** A07 Authentication Failures | **Risiko:** Sedang
- **Mengapa ini masalah:** Kredensial dapat dicoba berulang kali tanpa pembatasan, memungkinkan brute force.
- **Cara memeriksa:** Baca rute; tidak ada penghitung kegagalan, tidak ada respons 429.
- **Usulan:** Maksimal 5 kegagalan per 5 menit per IP+username; kembalikan 429; catat kejadian tanpa kata sandi; sertakan uji kedaluwarsa.
- **Wajib diperbaiki atau saran:** Wajib diperbaiki.

## I-03 [Keamanan] Kejadian login gagal dan akses ditolak tidak dicatat

- **Lokasi:** `app.py` dan `routes.py` — `https://github.com/<kelompok>/<repo>/blob/<commit>/routes.py#L144`
- **Kategori:** A09 Security Logging & Alerting Failures | **Risiko:** Sedang
- **Mengapa ini masalah:** Tanpa catatan, upaya login gagal dan akses ditolak tidak terdeteksi dan sulit diselidiki.
- **Cara memeriksa:** Cari `logger`/`logging`; tidak ada konfigurasi pencatatan kejadian keamanan.
- **Usulan:** Catat login gagal/berhasil, akun terkunci, 403, dan CSRF gagal; gunakan `%r` untuk username; jangan pernah mencatat kata sandi.
- **Wajib diperbaiki atau saran:** Wajib diperbaiki.

## I-04 [Keamanan] Cookie Secure dan header keamanan belum ada

- **Lokasi:** `app.py` konfigurasi aplikasi — `https://github.com/<kelompok>/<repo>/blob/<commit>/app.py#L19`
- **Kategori:** A02 Security Misconfiguration | **Risiko:** Sedang
- **Mengapa ini masalah:** Cookie dapat dikirim lewat HTTP bila deployment salah; tidak ada header terhadap clickjacking dan MIME sniffing.
- **Cara memeriksa:** Baca konfigurasi; tidak ada `SESSION_COOKIE_SECURE`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`.
- **Usulan:** `APP_ENV=production` mewajibkan kunci; `SESSION_COOKIE_SECURE=PRODUKSI`; header ditambahkan via `after_request`.
- **Wajib diperbaiki atau saran:** Wajib diperbaiki.

## I-05 [Kualitas] Konfirmasi hapus memakai JavaScript sebaris

- **Lokasi:** `templates/kamar_list.html` baris ±64 — `https://github.com/<kelompok>/<repo>/blob/<commit>/templates/kamar_list.html#L64`
- **Kategori:** A02 / Kualitas kode | **Risiko:** Rendah
- **Mengapa ini masalah:** Atribut `onsubmit="return confirm(...)"` menghalangi penerapan Content-Security-Policy ketat.
- **Cara memeriksa:** Baca template; konfirmasi ditulis sebaris di dalam tag form.
- **Usulan:** Pindahkan ke berkas JS lokal atau dialog yang diizinkan CSP; jangan mengubah perilaku server.
- **Wajib diperbaiki atau saran:** Saran (bisa ditunda ke pertemuan berikutnya).

## Dua catatan positif

1. Pemisahan lapisan rapi: SQL hanya di `models.py`, aturan validasi di `services.py`, rute tipis — memudahkan tinjauan dan uji.
2. Seluruh rute dalam matriks akses sudah memakai decorator peran, termasuk rute POST.

## Status pengiriman

Belum dikirim. Setelah dosen menetapkan pasangan: ganti placeholder URL/commit/baris, buat satu Issue per temuan, lampirkan permalink, dan tunggu tanggapan dari kelompok pemilik kode.
