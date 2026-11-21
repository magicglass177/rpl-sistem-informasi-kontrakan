# Hasil Uji dan Tinjauan Modul CRUD

## Sistem Informasi Pengelolaan Kontrakan — Jobsheet 9

**Tanggal pengujian:** 21 November 2026
**Pengembang:** Bayu Nanda Pamungkas
**Lingkungan:** Windows, Python 3.14, Flask 3.1.3, SQLite, `unittest`
**Basis data pengujian:** database sementara (bukan `instance/kontrakan.db`)

---

## 1. Spesifikasi Fitur Kecil

| No. | Fitur kecil | Kriteria penerimaan | KF |
|---|---|---|---|
| F1 | Kerangka proyek | Aplikasi Flask berjalan; basis data dibuat dari `docs/desain/schema.sql`; kunci rahasia dari variabel lingkungan. | Dasar KF-02, KF-03 |
| F2 | Daftar kamar | Data kamar tersimpan ditampilkan; status ketersediaan dihitung dari periode sewa aktif; keadaan kosong menampilkan "Belum ada data". | KF-03, KF-05 |
| F3 | Tambah kamar | Nomor kamar unik dan harga sewa berupa angka tidak negatif; data valid tersimpan lalu dialihkan ke daftar; masukan tidak valid ditolak dengan pesan. | KF-02 |
| F4 | Ubah kamar | Form terisi data lama; hanya `nomor_kamar` dan `harga_sewa` yang dapat diubah; nomor duplikat ditolak; ID tidak ditemukan menghasilkan 404. | KF-04 |
| F5 | Hapus kamar | Hanya melalui `POST` dengan konfirmasi; kamar yang masih dirujuk data sewa tidak terhapus dan muncul pesan; ID tidak ditemukan menghasilkan 404. | Pendukung KF-07/KF-08 (aturan PRD masih terbuka) |
| F6 | Daftar penyewa | Data penyewa tersimpan ditampilkan dan dapat dicari berdasarkan nama, telepon, atau alamat. | KF-06 |
| F7 | Tambah penyewa | Nama, nomor telepon, dan alamat divalidasi sesuai kamus data; data valid tersimpan lalu dialihkan ke daftar. | KF-06 |
| F8 | Ubah penyewa | Form terisi data lama; validasi sama dengan tambah; ID tidak ditemukan menghasilkan 404. | KF-06 |
| F9 | Hapus penyewa | Hanya melalui `POST`; penyewa yang masih dirujuk data sewa tidak terhapus dan muncul pesan. | Pendukung KF-07 |

**Catatan:** F5 dan F9 merupakan keputusan implementasi untuk menjaga integritas referensial. Pertanyaan PRD tentang penghapusan data yang memiliki riwayat masih berstatus terbuka dan tidak dianggap sebagai keputusan final klien.

---

## 2. Hasil Uji Tambah Data (Langkah 6)

| No. | Masukan uji | Hasil diharapkan | Hasil nyata | Status |
|---:|---|---|---|---|
| 1 | Semua kolom valid: `C-01`, harga `850000` | Tersimpan; pesan sukses; tampil di daftar | Data tersimpan, respons dialihkan ke `/kamar`, pesan sukses tampil | Lulus |
| 2 | Nomor kamar kosong | Ditolak; pesan galat jelas; data tidak tersimpan | HTTP 400, pesan "Nomor kamar wajib diisi.", isian harga tetap ada | Lulus |
| 3 | Harga `-5` | Ditolak; pesan galat | HTTP 400, pesan "Harga sewa tidak boleh negatif." | Lulus |
| 4 | Harga `abc` | Ditolak; pesan galat | HTTP 400, pesan "Harga sewa harus berupa angka." | Lulus |
| 5 | Nomor kamar `A-01` yang sudah ada | Ditolak; pesan "sudah ada" | HTTP 400, pesan "Nomor kamar A-01 sudah ada." | Lulus |

Pengujian tambahan: nomor kamar lebih dari 20 karakter ditolak, harga `0` dan harga desimal diterima, `NaN` dan `Infinity` ditolak.

---

## 3. Hasil Uji Kriteria Penerimaan F2–F5 (Langkah 10)

| No. | Skenario | Hasil diharapkan | Hasil nyata | Status |
|---:|---|---|---|---|
| 1 | Buka `/kamar` dengan data tersimpan | Daftar kamar tampil dengan nomor, harga, dan status | HTTP 200; data dan format rupiah tampil | Lulus |
| 2 | Buka `/kamar` tanpa data | Pesan "Belum ada data" tampil | HTTP 200; pesan tampil | Lulus |
| 3 | Cari kamar `A-01` | Hanya `A-01` yang tampil | `A-01` tampil, `B-01` tidak tampil | Lulus |
| 4 | Kamar memiliki sewa aktif | Status "Terisi" | Status "Terisi" tampil | Lulus |
| 5 | Kamar tanpa sewa aktif | Status "Tersedia" | Status "Tersedia" tampil | Lulus |
| 6 | Tambah kamar valid | Tersimpan dan muncul di daftar | Tersimpan; redirect ke daftar; pesan sukses | Lulus |
| 7 | Tambah kamar tidak valid | Ditolak; isian dipertahankan | HTTP 400; pesan per kolom; isian tetap | Lulus |
| 8 | Tambah nomor duplikat | Ditolak | HTTP 400; pesan "sudah ada"; jumlah data tidak bertambah | Lulus |
| 9 | Buka form ubah | Data lama terisi | Nomor dan harga lama tampil | Lulus |
| 10 | Simpan perubahan valid | Data berubah dan tampil di daftar | Tersimpan; redirect; pesan sukses | Lulus |
| 11 | Ubah menjadi nomor duplikat | Ditolak; data lama tidak berubah | HTTP 400; data lama tetap | Lulus |
| 12 | Buka `/kamar/999999/ubah` | HTTP 404 | HTTP 404 | Lulus |
| 13 | Hapus kamar tidak terpakai melalui `POST` | Terhapus; redirect; pesan sukses | Terhapus; pesan sukses | Lulus |
| 14 | Hapus kamar melalui `GET` | Tidak menghapus; metode ditolak | HTTP 405; data tetap ada | Lulus |
| 15 | Hapus kamar yang dipakai sewa | Ditolak; pesan jelas | HTTP 200 setelah redirect; pesan "tidak dapat dihapus"; data tetap | Lulus |
| 16 | Hapus ID yang tidak ada | HTTP 404 | HTTP 404 | Lulus |

---

## 4. Uji Keamanan Dasar

| No. | Uji | Masukan | Hasil yang diperiksa | Status |
|---:|---|---|---|---|
| 1 | SQL injection pada nomor kamar | `';DROP TABLE kamar` (19 karakter, sesuai batas kolom) | Tersimpan sebagai teks biasa; tabel `kamar` tetap ada | Lulus |
| 2 | SQL injection pada alamat penyewa | `Robert'); DROP TABLE penyewa;--` | Tersimpan sebagai teks biasa; tabel `penyewa` tetap ada | Lulus |
| 3 | XSS pada nama | `<b>tes</b>` | Tampil sebagai `&lt;b&gt;tes&lt;/b&gt;`, bukan HTML tebal | Lulus |
| 4 | Penghapusan melalui `GET` | Buka URL hapus di peramban | HTTP 405; tidak ada data terhapus | Lulus |
| 5 | Kunci rahasia | Periksa kode sumber | Tidak ada kunci tertulis; dibaca dari `FLASK_SECRET_KEY` | Lulus |

Seluruh query menggunakan placeholder `?`. Tidak ada penyambungan teks masukan pengguna ke perintah SQL.

---

## 5. Uji Skema Basis Data

| Skrip | Cakupan | Hasil |
|---|---|---:|
| `tests/cek_skema.py` | Integritas, UNIQUE, FK, tanggal, pembayaran, periode tumpang tindih | 11/11 ditolak sesuai harapan; 0 gagal |
| `tests/cek_skema_lanjutan.py` | Pembayaran bertahap dan perlindungan riwayat transaksi | 8/8 berhasil; 0 gagal |
| `tests/cek_validasi_telepon.py` | Format nomor telepon valid dan tidak valid | 6 valid diterima; 10 tidak valid ditolak |
| `tests/test_crud_kamar.py` | CRUD kamar, validasi, keamanan, status ketersediaan | 25/25 lulus |
| `tests/test_crud_penyewa.py` | CRUD penyewa, validasi telepon, keamanan, FK | 28/28 lulus |
| **Total pengujian otomatis baru** | `python -m unittest discover -s tests -v` | **53/53 lulus** |

Perintah pengujian:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

---

## 6. Daftar Periksa Tinjauan Kode (Lampiran C)

| No. | Pertanyaan periksa | Ya | Tidak | Catatan |
|---:|---|---:|---:|---|
| 1 | Kode memenuhi kriteria penerimaan fitur dan hanya itu? | Ya | | Tidak ada fitur di luar CRUD dan pencarian dasar. |
| 2 | Nama tabel dan kolom sama dengan `schema.sql`; skema tidak diubah? | Ya | | Skema tidak diubah. |
| 3 | Semua query SQL berparameter? | Ya | | Seluruh query memakai `?`. |
| 4 | SQL hanya di `models.py`; validasi di `services.py`; rute tipis? | Ya | | Rute hanya menangani request/response. |
| 5 | Kegagalan ditangani: 404, duplikat, FK, masukan tidak valid? | Ya | | Diuji otomatis. |
| 6 | Penghapusan dan perubahan hanya lewat POST? | Ya | | Hapus `POST`; ubah `GET`/`POST`. |
| 7 | Tidak ada rahasia di kode; `debug=True` dicatat? | Ya | | Kunci dari lingkungan; `debug=True` dicatat untuk tinjauan keamanan Minggu 12. |
| 8 | Tidak ada paket baru; `requirements.txt` sesuai? | Ya | | Hanya Flask dan pustaka standar. |
| 9 | Hanya berkas yang diminta yang berubah? | Ya | | Perubahan pada models, routes, services, templates, tests, dan docs. |
| 10 | Teks pengguna ditampilkan lewat Jinja2? | Ya | | Tidak ada `\|safe` atau HTML mentah. |
| 11 | Pesan sukses dan galat muncul sesuai wireframe? | Ya | | Flash sukses, peringatan, dan galat tampil di area konten. |
| 12 | Saya dapat menjelaskan setiap fungsi tanpa melihat AI? | Ya | | Alur request → route → service → model → database → template dipahami. |

---

## 7. Temuan Tinjauan Seluruh Diff (Langkah 11)

| No. | Temuan | Kategori | Tindakan |
|---:|---|---|---|
| 1 | Kode rute hapus hasil AI ditempelkan ke `models.py`; `main`, `flash`, `redirect`, dan `url_for` tidak terdefinisi sehingga aplikasi gagal diimpor. | Kebenaran / Keterbacaan | **Diperbaiki sekarang.** Rute dipindahkan ke `routes.py`, fungsi `delete_kamar()` ditambahkan di `models.py`. |
| 2 | `routes.py` memiliki blok `from models import ...` ganda dan mengimpor `delete_kamar` yang belum ada. | Keterbacaan | **Diperbaiki sekarang.** Import digabung dan diurutkan. |
| 3 | Pesan flash dirender setelah `</main>` (di bawah footer) dan kategori `warning`/`danger` belum memiliki gaya. | Kesesuaian | **Diperbaiki sekarang.** Flash dipindahkan ke dalam area konten dan gayanya ditambahkan. |
| 4 | Konfirmasi hapus menyisipkan nomor kamar langsung ke JavaScript tanpa escaping; nomor yang mengandung tanda kutip dapat merusak skrip. | Keamanan | **Diperbaiki sekarang.** Konfirmasi memakai pesan statis tanpa interpolasi data pengguna. |
| 5 | Model hapus belum membedakan ID yang tidak ditemukan dari kegagalan database. | Kebenaran | **Diperbaiki sekarang.** `rowcount` diperiksa dan rute mengembalikan 404. |
| 6 | `debug=True` masih aktif dan belum ada autentikasi/otorisasi halaman pengelolaan (KNF-04). | Keamanan | **Dicatat untuk Minggu 12/Sprint 2.** Bukan ruang lingkup Jobsheet 9; sudah masuk rencana sprint. |

---

## 8. Ringkasan Sesi Debugging (Langkah 12)

**Gejala:** menjalankan `tests/cek_fitur_ubah_kamar.py` langsung gagal saat impor.

**Traceback inti:**

```text
File "models.py", line 189, in <module>
    @main.route("/kamar/<int:id_kamar>/hapus", methods=["POST"])
NameError: name 'main' is not defined. Did you mean: 'min'?
```

**Penyebab:** kode rute (lapisan controller) hasil AI ditempelkan ke `models.py` (lapisan data). Objek `main`, `flash`, `redirect`, dan `url_for` hanya tersedia di `routes.py`. Fungsi `delete_kamar()` yang dipanggil rute juga belum dibuat.

**Perbaikan:** rute dihapus dari `models.py`; fungsi `delete_kamar()` ditambahkan pada lapisan model; rute hapus ditulis ulang di `routes.py`; import ganda dibersihkan.

**Verifikasi:** seluruh 53 pengujian otomatis lulus, ditambah 4 skrip pengujian skema/validasi yang sudah ada. Tidak ada perubahan pada `instance/kontrakan.db` selama pengujian karena tes memakai database sementara.

---

## 9. Hasil Modul CRUD Entitas Kedua (Penyewa)

| Kelompok uji | Jumlah | Hasil |
|---|---:|---|
| Daftar dan pencarian penyewa | 5 | Lulus |
| Tambah dan validasi penyewa | 7 | Lulus |
| Ubah penyewa | 4 | Lulus |
| Hapus penyewa dan perlindungan FK | 4 | Lulus |
| Keamanan (SQL injection dan XSS) | 2 | Lulus |
| Validasi unit (batas nama dan telepon) | 6 | Lulus |
| **Total** | **28** | **Lulus** |

Batas nomor telepon yang diuji: `08` + 8–11 digit (10–13 karakter) dan `+628` + 8–11 digit (12–15 karakter). Nomor dengan spasi, tanda hubung, huruf, awalan salah, atau panjang di luar batas ditolak. Nomor telepon tidak dibuat UNIQUE karena kamus data menyatakan keunikannya belum diputuskan.

---

## 10. Kesimpulan

1. CRUD kamar (F2–F5) dan CRUD penyewa (F6–F9) berfungsi sesuai kriteria penerimaan.
2. Validasi server, penanganan duplikat, 404, dan kegagalan foreign key telah diuji.
3. SQL berparameter dan escape Jinja2 terbukti pada uji injeksi dan XSS.
4. Skema basis data tidak berubah.
5. Seluruh 53 pengujian otomatis baru lulus, ditambah pengujian skema yang sudah ada.
6. Temuan tinjauan telah diperbaiki atau dicatat dengan alasan yang jelas.
