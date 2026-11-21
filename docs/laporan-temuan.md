# Laporan Temuan — Jobsheet 12

## Identitas

- Proyek: Sistem Informasi Pengelolaan Kontrakan
- Kelompok: (diisi sesuai identitas kelompok)
- Pertemuan: Jobsheet 12 — Minggu 12
- Commit yang ditinjau: `main` pada `cafb5a3`

## Prediksi tiga kategori OWASP paling mungkin (Langkah 2)

| Prioritas | Kategori | Alasan prediksi |
|---:|---|---|
| 1 | A01 Broken Access Control | Form POST belum memakai token CSRF; rute sudah memakai decorator peran, tetapi perlindungan lintas situs belum ada |
| 2 | A07 Authentication Failures | Belum ada batas percobaan login; pesan galat dan sesi sudah benar dari Jobsheet 11 |
| 3 | A02 Security Misconfiguration | `SESSION_COOKIE_SECURE` belum diatur untuk produksi dan header keamanan dasar belum ditambahkan |

Kategori lain yang juga dicek: A09 (pencatatan kejadian login/akses ditolak belum ada),
A03 (nama dan versi paket), A10 (rincian galat ke pengguna), dan A04/A05 (sudah baik dari Jobsheet 11).

---

## Tinjauan kasus latihan (Langkah 3)

Kasus: `kasus_rentan.py` (Lampiran B.1), dibaca baris demi baris tanpa menjalankan aplikasi.
Kategori memakai ID A01-A10 sesuai OWASP Top 10:2025.

| No | Masalah | Kategori OWASP | Dampak | Risiko |
|---|---|---|---|---|
| (1) | Mengimpor `flask_auth_helperz`, paket yang tidak dikenal/fiktif | A03 Software Supply Chain Failures | Nama paket tiruan dapat dipakai pihak ketiga untuk menyisipkan kode berbahaya saat instalasi | Sedang |
| (2) | `app.secret_key = "rahasia123"` tertulis di kode | A04 Cryptographic Failures | Siapa pun yang membaca kode dapat memalsukan cookie sesi dan masuk sebagai pengguna lain | Tinggi |
| (3) | `hashlib.md5(p.encode())` untuk kata sandi, tanpa garam | A04 Cryptographic Failures | Hash cepat dipecah; kata sandi sama menghasilkan hash sama | Tinggi |
| (4) | SQL disusun dengan f-string dari `username` | A05 Injection | Penyerang mengubah perintah SQL dan masuk tanpa kata sandi | Tinggi |
| (5) | Pesan "Kata sandi salah untuk pengguna " + `u` | A07 Authentication Failures | Membocorkan nama pengguna yang terdaftar (user enumeration) | Rendah |
| (6) | `redirect(request.args["next"])` tanpa validasi | A01 Broken Access Control | Open redirect: korban dibawa ke situs jahat setelah login | Sedang |
| (7) | `/barang/<id>/hapus` memakai GET, tanpa login dan CSRF | A01 Broken Access Control | Siapa pun dapat menghapus data, termasuk lewat tautan/ gambar di situs lain | Tinggi |
| (8) | `/catatan/<id>` hanya cek login, bukan kepemilikan | A01 Broken Access Control | Pengguna dapat membaca catatan milik pengguna lain (IDOR) | Tinggi |
| (9) | `return f"Galat: {e!r}"` menampilkan rincian exception | A10 Mishandling of Exceptional Conditions | Struktur basis data dan galat internal terbongkar | Rendah-Sedang |
| (10) | `app.run(host="0.0.0.0", debug=True)` | A02 Security Misconfiguration | Konsol debug interaktif dan akses dari jaringan terbuka | Tinggi |

Temuan tambahan di luar nomor: koneksi SQLite global dengan `check_same_thread=False`
berisiko pada banyak thread, dan tidak ada pencatatan kejadian login/akses ditolak (A09).

---

## Tiga bukti kasus (Langkah 4)

Lingkungan latihan dibuat di folder terpisah di luar repositori berisi `kasus_rentan.py`,
`flask_auth_helperz.py` (modul kosong lokal), dan `siapkan_kasus.py`. Basis data diisi dengan
data karangan, lalu pembuktian dilakukan dengan Flask test client.

### Bukti 1 — Login tanpa kata sandi (SQL injection)

- Masukan: `username = pemilik' -- `, `password = kata-sandi-apa-saja`, `next=/`
- Hasil: `302 Location: /`, sesi berisi `{'id': 1, 'peran': 'pemilik'}`
- Kesimpulan: komentar SQL `--` menonaktifkan pemeriksaan hash, sehingga kata sandi tidak diperiksa.

### Bukti 2 — Hapus data lewat GET tanpa login

- Masukan: `GET /barang/1/hapus` dengan klien tanpa sesi
- Hasil: status `302`; jumlah barang turun dari `2` menjadi `1`
- Kesimpulan: perubahan data terjadi tanpa autentikasi, tanpa POST, dan tanpa token CSRF.

### Bukti 3 — Open redirect dan kebocoran rincian galat

- Masukan A: `POST /login?next=https://situs-jahat.example` dengan kredensial benar
- Hasil A: `302 Location: https://situs-jahat.example`
- Masukan B: `GET /laporan`
- Hasil B: `Galat: OperationalError('no such table: penjualan')`
- Kesimpulan: `next` tidak divalidasi dan rincian internal ditampilkan ke pengguna.

---

## Lima temuan kasus latihan (Langkah 5)

Diurutkan dari risiko tertinggi.

### T-01 — Login tanpa kata sandi melalui SQL injection

- **Lokasi:** `kasus_rentan.py` nomor (4), query f-string pada `login()`
- **Kategori:** A05 Injection
- **Deskripsi:** Nilai `username` disambung langsung ke perintah SQL, sehingga tanda kutip dan
  komentar SQL mengubah arti query.
- **Bukti:** Bukti 1 — `pemilik' -- ` menghasilkan sesi pemilik tanpa kata sandi yang benar.
- **Dampak:** Penguasaan akun siapa pun, termasuk peran pemilik.
- **Risiko:** Tinggi
- **Perbaikan:** SQL berparameter (`WHERE username = ? AND password_hash = ?`).
- **Status:** Terbuka (kasus latihan; perbaikan dicatat pada bagian catatan AI)

### T-02 — Hapus data lewat GET tanpa pemeriksaan akses

- **Lokasi:** `kasus_rentan.py` nomor (7), rute `/barang/<int:id>/hapus`
- **Kategori:** A01 Broken Access Control
- **Deskripsi:** Rute penghapusan memakai GET dan tidak memeriksa sesi maupun peran.
- **Bukti:** Bukti 2 — barang terhapus dari klien tanpa login.
- **Dampak:** Siapa pun dapat merusak data; tautan lintas situs dapat memicu penghapusan.
- **Risiko:** Tinggi
- **Perbaikan:** POST + decorator peran + token CSRF.
- **Status:** Terbuka

### T-03 — Kata sandi disimpan sebagai MD5 tanpa garam

- **Lokasi:** `kasus_rentan.py` nomor (3)
- **Kategori:** A04 Cryptographic Failures
- **Deskripsi:** MD5 cepat dihitung dan tidak memakai garam; hash sama untuk kata sandi sama.
- **Bukti:** `md5('sandi-karangan-1')` selalu menghasilkan nilai yang sama untuk semua pengguna.
- **Dampak:** Bila basis data bocor, sebagian besar kata sandi dapat dipulihkan.
- **Risiko:** Tinggi
- **Perbaikan:** `generate_password_hash` / `check_password_hash` dari Werkzeug.
- **Status:** Terbuka

### T-04 — Catatan pengguna lain dapat dibaca (IDOR)

- **Lokasi:** `kasus_rentan.py` nomor (8), rute `/catatan/<int:id>`
- **Kategori:** A01 Broken Access Control
- **Deskripsi:** Hanya status login yang dicek; `id` catatan tidak dibandingkan dengan pemiliknya.
- **Bukti:** Analisis kode — query `SELECT isi FROM catatan WHERE id = ?` tidak memuat
  `pengguna_id` dari sesi.
- **Dampak:** Kebocoran data pribadi antarpengguna.
- **Risiko:** Tinggi
- **Perbaikan:** `WHERE id = ? AND pengguna_id = ?` dengan nilai dari sesi.
- **Status:** Terbuka

### T-05 — Open redirect pada parameter `next`

- **Lokasi:** `kasus_rentan.py` nomor (6)
- **Kategori:** A01 Broken Access Control
- **Deskripsi:** Nilai `next` dipakai apa adanya tanpa pemeriksaan alamat internal.
- **Bukti:** Bukti 3A — alihkan ke `https://situs-jahat.example`.
- **Dampak:** Korban diarahkan ke situs phishing setelah login yang sah.
- **Risiko:** Sedang
- **Perbaikan:** Terima hanya alamat yang diawali `/`, bukan `//`, tanpa backslash.
- **Status:** Terbuka

### Temuan kasus lain yang tercatat

- T-06 `secret_key` tertanam di kode (A04, Tinggi).
- T-07 `debug=True` dan `host="0.0.0.0"` (A02, Tinggi).
- T-08 rincian exception ke pengguna (A10, Rendah-Sedang; Bukti 3B).
- T-09 paket `flask_auth_helperz` tidak dikenal (A03, Sedang).
- T-10 pesan galat login membedakan username (A07, Rendah).

---

## Catatan kualitas perbaikan AI (Langkah 6)

Perbaikan diminta **satu temuan per prompt**, lalu hasilnya dibaca lagi dengan
Lampiran C. Versi perbaikan ada pada `kasus_perbaikan.py` di folder latihan.

| Temuan | Hasil AI | Peninjauan saya |
|---|---|---|
| T-01 SQL injection | Benar: query diganti SQL berparameter | Diterima; bukti: `pemilik' -- ` kini ditolak 401 |
| T-03 MD5 | Benar: `generate_password_hash`/`check_password_hash` | Diterima |
| T-02 hapus via GET | Benar: diubah ke POST dan 403 untuk tamu | Diterima, tetapi token CSRF belum ditambahkan pada kasus latihan (sengaja tidak dipakai di luar proyek) |
| T-05 open redirect | AI hanya mengecek `next.startswith('/')` | **Dikoreksi**: `//` masih dianggap alamat luar dan backslash perlu ditolak; saya tambahkan dua syarat |
| T-04 IDOR | AI tidak menyertakan pemeriksaan kepemilikan pada draf pertama | **Dikoreksi**: query diubah menjadi `WHERE id = ? AND pengguna_id = ?` |
| T-09/T-10 galat & pesan | Benar: pesan umum ke pengguna, rincian ke log dengan `logger.exception` | Diterima; log menampilkan traceback, pengguna melihat "Laporan belum dapat ditampilkan." |

**Kesimpulan:** AI memperbaiki penyebab pada sebagian besar temuan (bukan sekadar gejala),
tetapi melewatkan dua pemeriksaan kontrol akses. Itu menegaskan bahwa tinjauan AI saja tidak
cukup; kasus pinggir dan kepemilikan data harus dicek manual.

Bukti setelah perbaikan: SQL injection → 401; `next` luar → 302 ke `/`; catatan pemilik
diakses kasir → 404; hapus via GET → 405; laporan gagal → 500 dengan pesan umum.

---

## Tinjauan mandiri proyek sendiri (Langkah 7)

Daftar periksa Lampiran C diterapkan pada `app.py`, `routes.py`, `services.py`, `models.py`,
templat, dan `requirements.txt`, lalu digabung dengan `docs/temuan-keamanan.md`.

### P-01 — Form POST belum memiliki token CSRF

- **Lokasi:** seluruh formulir POST (login, logout, tambah/ubah/hapus kamar, penyewa, sewa, pembayaran)
- **Kategori:** A01 Broken Access Control
- **Deskripsi:** Penegakan peran sudah benar, tetapi permintaan POST dari situs lain masih dapat
  dikirim menggunakan cookie sesi korban.
- **Bukti:** `POST /kamar/tambah` tanpa kolom `csrf_token` masih diproses rute.
- **Dampak:** Perubahan atau penghapusan data tanpa persetujuan pengguna.
- **Risiko:** Tinggi
- **Perbaikan:** Token acak per sesi, input tersembunyi di semua form, pemeriksaan di `before_request`, 400 saat gagal.
- **Status:** Diperbaiki pada Langkah 11.

### P-02 — Tidak ada batas percobaan login

- **Lokasi:** rute `login()` di `routes.py`
- **Kategori:** A07 Authentication Failures
- **Deskripsi:** Kredensial dapat dicoba terus-menerus tanpa pembatasan.
- **Bukti:** Lima kali POST `/login` dengan kata sandi salah selalu menghasilkan respons galat, bukan 429.
- **Dampak:** Serangan brute force terhadap akun.
- **Risiko:** Sedang
- **Perbaikan:** Maksimal 5 kegagalan per 5 menit per IP + username; respons 429.
- **Status:** Diperbaiki pada Langkah 12.

### P-03 — Kejadian keamanan belum dicatat

- **Lokasi:** `app.py` dan `routes.py`
- **Kategori:** A09 Security Logging & Alerting Failures
- **Deskripsi:** Login gagal, akun terkunci, dan akses ditolak tidak menghasilkan catatan.
- **Bukti:** Tidak ada konfigurasi `logging.basicConfig` atau `app.logger` pada kode.
- **Dampak:** Serangan tidak terdeteksi dan sulit diselidiki.
- **Risiko:** Sedang
- **Perbaikan:** Catat kejadian penting tanpa kata sandi; username memakai `%r`.
- **Status:** Diperbaiki pada Langkah 12.

### P-04 — Konfigurasi produksi dan cookie Secure belum diatur

- **Lokasi:** `app.py`
- **Kategori:** A02 Security Misconfiguration
- **Deskripsi:** `SESSION_COOKIE_SECURE` belum aktif untuk produksi; `debug=True` masih ditulis langsung di blok `__main__` dan tidak dikendalikan lingkungan.
- **Bukti:** `app.run(debug=True)`; tidak ada `APP_ENV`.
- **Dampak:** Cookie dapat dikirim lewat HTTP dan konsol debug dapat aktif di server.
- **Risiko:** Sedang
- **Perbaikan:** `APP_ENV=production` mewajibkan kunci dari lingkungan, `SESSION_COOKIE_SECURE=PRODUKSI`, `FLASK_DEBUG=1` hanya di luar produksi.
- **Status:** Diperbaiki pada Langkah 13.

### P-05 — Header keamanan dasar belum ditambahkan

- **Lokasi:** seluruh respons Flask
- **Kategori:** A02 Security Misconfiguration
- **Deskripsi:** Belum ada `X-Content-Type-Options`, `X-Frame-Options`, dan `Referrer-Policy`.
- **Bukti:** Respons tidak memuat ketiga header tersebut.
- **Dampak:** Risiko clickjacking dan MIME sniffing.
- **Risiko:** Rendah-Sedang
- **Perbaikan:** `after_request` menambahkan ketiga header.
- **Status:** Diperbaiki pada Langkah 13.

### P-06 — Atribut `onsubmit` sebaris menghalangi CSP ketat

- **Lokasi:** `kamar_list.html`, `penyewa_list.html`, `pembayaran_list.html`
- **Kategori:** A02 Security Misconfiguration
- **Deskripsi:** Konfirmasi hapus memakai JavaScript sebaris, sehingga Content-Security-Policy ketat tidak dapat diterapkan tanpa perombakan.
- **Bukti:** `onsubmit="return confirm(...)"` pada formulir hapus.
- **Dampak:** Risiko kecil; fitur tetap berjalan.
- **Risiko:** Rendah
- **Perbaikan:** Pindahkan konfirmasi ke berkas JS lokal atau dialog native yang diizinkan CSP.
- **Status:** Ditunda ke Pertemuan 14 (bersama HTTPS/CSP).

### P-07 — Pemeriksaan kepemilikan data per pengguna

- **Lokasi:** seluruh rute data
- **Kategori:** A01 Broken Access Control
- **Deskripsi:** Tidak ada filter `pengguna_id` pada data.
- **Bukti:** Skema tidak memiliki kolom kepemilikan; data kontrakan bersifat bersama untuk pemilik dan kasir.
- **Dampak:** Tidak ada data pribadi per akun yang dapat bocor antarpengguna.
- **Risiko:** Tidak berlaku
- **Perbaikan:** Tidak diperlukan; peran mengatur akses ke seluruh data bersama.
- **Status:** Ditolak dengan alasan (sesuai model data bersama).

### Yang sudah baik

SQL seluruhnya berparameter di `models.py`, keluaran memakai `{{ }}` Jinja2 tanpa `|safe`,
semua rute dalam matriks memakai decorator peran, kata sandi memakai hash Werkzeug, kunci
dari lingkungan, `requirements.txt` sudah berversi, dan uji otomatis mencakup jalur pelanggaran.

## Tinjauan silang dan triase (Langkah 9-10)

### Keterbatasan tinjauan silang

Pasangan kelompok peninjau belum ditetapkan di lingkungan ini dan saya tidak memiliki akses
baca ke repositori kelompok lain. Sesuai aturan etika Jobsheet 12, tinjauan tidak dilakukan
dengan menyerang aplikasi pihak lain. Oleh karena itu **5 Issue tinjauan silang belum dapat
dibuat/dikirim**. Sebagai latihan, lima draf Issue berikut disiapkan memakai templat D.2 dan
akan dikirim ke repositori kelompok yang ditunjuk dosen setelah pasangan diumumkan.

| Draf | Judul | Lokasi (baris pada commit `cafb5a3`) | Kategori | Risiko |
|---|---|---|---|---|
| I-01 | [Keamanan] Form POST belum memakai token CSRF | `templates/login.html`, `templates/base.html` | A01 | Tinggi |
| I-02 | [Keamanan] Belum ada batas percobaan login | `routes.py` fungsi `login()` | A07 | Sedang |
| I-03 | [Keamanan] Kejadian login gagal/akses ditolak tidak dicatat | `app.py`, `routes.py` | A09 | Sedang |
| I-04 | [Keamanan] Cookie Secure dan header keamanan belum ada | `app.py` | A02 | Sedang |
| I-05 | [Kualitas] Konfirmasi hapus memakai JS sebaris | `templates/kamar_list.html` baris 64 | A02 | Rendah |

Contoh isi draf I-01 (templat D.2):

> **Judul:** [Keamanan] Form POST belum memakai token CSRF
> **Lokasi:** `templates/base.html` form logout dan seluruh form tambah/ubah/hapus
> **Kategori:** A01 | **Risiko:** Tinggi
> **Mengapa ini masalah:** Permintaan POST hanya dilindungi decorator peran. Situs pihak ketiga
> dapat mengirim POST memakai cookie sesi korban.
> **Cara memeriksa (tanpa menyerang aplikasi):** Baca kode; tidak ada input `csrf_token`
> dan tidak ada pemeriksaan token pada `before_request`.
> **Usulan:** Token acak per sesi + input tersembunyi + `secrets.compare_digest`, tolak 400.
> **Wajib diperbaiki atau saran:** Wajib diperbaiki.

Dua hal yang sudah baik untuk disampaikan secara konstruktif: pemisahan SQL di `models.py`
dan validasi di `services.py` rapi, serta seluruh rute dalam matriks sudah memakai decorator peran.

### Tabel triase temuan yang diterima

| No | Temuan (ID) | Risiko | Keputusan | Alasan / rencana |
|---:|---|---|---|---|
| 1 | P-01 CSRF | Tinggi | Diperbaiki | Langkah 11: token per sesi, 400 + log |
| 2 | P-02 Batas login | Sedang | Diperbaiki | Langkah 12: 5 kegagalan/5 menit per IP+username |
| 3 | P-03 Logging | Sedang | Diperbaiki | Langkah 12: log tanpa kata sandi, username `%r` |
| 4 | P-04 Konfigurasi | Sedang | Diperbaiki | Langkah 13: APP_ENV, Secure, debug dari lingkungan |
| 5 | P-05 Header | Rendah-Sedang | Diperbaiki | Langkah 13: `after_request` |
| 6 | P-06 CSP/JS sebaris | Rendah | Ditunda | Pertemuan 14, bersama HTTPS |
| 7 | P-07 Kepemilikan data | - | Ditolak | Data kontrakan bersifat bersama; tidak ada data per akun |
| 8 | T-01...T-10 kasus latihan | campuran | Diperbaiki di folder latihan | Tidak disalin ke proyek; bukti di bagian kasus |

Setiap draf Issue akan ditanggapi dengan komentar bermakna bila sudah dikirim; tidak ada
Issue yang dihapus untuk menutupi masalah.

## Bukti perbaikan (Langkah 11-14)

| Temuan | Commit | Bukti perbaikan |
|---|---|---|
| P-01 CSRF | `280896d` | 9 formulir memuat `csrf_token`; POST tanpa token → 400; log `CSRF gagal path=...` |
| P-02 Batas login | `06b7ff9` | 5POST salah → 401; POST ke-6 dengan kata sandi benar → 429; uji kedaluwarsa dengan waktu suntikan lulus |
| P-03 Logging | `06b7ff9` | `Login gagal username='admin' ip=127.0.0.1`; uji `assertLogs` membuktikan kata sandi tidak tercatat |
| P-04 Konfigurasi | `14bc710` | Produksi tanpa kunci → `RuntimeError`; `SESSION_COOKIE_SECURE=True`; debug hanya bila `FLASK_DEBUG=1` dan bukan produksi |
| P-05 Header | `14bc710` | `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: same-origin` |

Potongan diff kunci (`app.py`):

```python
@app.before_request
def periksa_csrf():
    if request.method != "POST":
        return
    dikirim = request.form.get("csrf_token", "").encode()
    asli = session.get("csrf_token", "").encode()
    if not asli or not secrets.compare_digest(dikirim, asli):
        app.logger.warning("CSRF gagal path=%r ip=%s", request.path, request.remote_addr)
        abort(400)
```

```python
@app.after_request
def tambah_header_keamanan(respons):
    respons.headers["X-Content-Type-Options"] = "nosniff"
    respons.headers["X-Frame-Options"] = "DENY"
    respons.headers["Referrer-Policy"] = "same-origin"
    return respons
```

### Tinjau ulang diff dengan Lampiran C

- SQL tetap berparameter di `models.py`; tidak ada f-string SQL baru.
- Keluaran tetap lewat `{{ }}` Jinja2; tidak ada `|safe` atau `Markup`.
- Semua rute dalam matriks tetap memakai decorator; tidak ada perubahan data lewat GET.
- Kata sandi tetap berhash; kunci dari lingkungan; tidak ada rahasia di kode.
- Pesan galat login tetap sama; `session.clear()` tetap ada; batas percobaan ditambahkan.
- Tidak ada `debug=True` tetap; host tidak `0.0.0.0`; cookie HttpOnly/SameSite/Secure sesuai lingkungan.
- `requirements.txt` berversi dan hanya berisi Flask + dependensinya.
- Galat ditangkap dengan jenis spesifik; rincian ke log, pesan umum ke pengguna.
- Fungsi pendek dan berlapis; tidak ada duplikasi SQL di luar `models.py`.

Tidak ditemukan kelemahan baru. Dua hal sengaja ditunda: penyimpanan batas login di memori
(Sprint 3 untuk multi-proses) dan CSP ketat (Pertemuan 14 karena `onsubmit` sebaris).

### Hasil uji akhir

- `python tests/uji_cepat.py` → `SEMUA UJI LULUS` (21 kelompok uji).
- `python -m unittest discover -s tests` → 59 tests OK.
- Fitur lama (CRUD kamar/penyewa, sewa, pembayaran, laporan, dua peran) tetap lulus.
