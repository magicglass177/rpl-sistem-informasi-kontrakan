# Laporan Cacat â€” Jobsheet 13

Proyek: Sistem Informasi Pengelolaan Kontrakan
Ditemukan oleh: uji parametrize pada `tests/test_validasi.py`, uji alur pada
`tests/test_alur_kontrakan.py`, dan uji eksploratif (Lampiran E.2).
Basis data: berkas sementara dari `tests/conftest.py` â€” `kontrakan.db` nyata tidak tersentuh.

## Bukti sebelum perbaikan

Perintah: `python -m pytest -q tests`

```
3 failed, 108 passed, 23 subtests passed in 30.50s

FAILED tests/test_alur_kontrakan.py::test_pencarian_kamar_tidak_memakai_wildcard
FAILED tests/test_validasi.py::test_harga_sewa[10000000000.00-False]
FAILED tests/test_tanggal_sewa[20261108-False-tanggal_mulai]
```

---

### D-01 â€” Format tanggal kompak diterima oleh validasi sewa

- **Ditemukan:** 21 November 2026 oleh tim lewat TC-27 dan uji eksploratif no. 3.
- **Langkah:**
  1. Siapkan kamar dan penyewa.
  2. `POST /sewa/tambah` dengan `tanggal_mulai = 20261108`,
     `tanggal_selesai = 2026-12-31`, harga `850000`.
  3. Amati hasil validasi.
- **Aktual:** `services.validate_sewa` mengembalikan `{}` untuk `tanggal_mulai`
  (lolos). Saat disimpan, `CHECK` pada skema menolak karena panjang bukan 10 dan
  bukan pola `TTTT-BB-HH`; rute lalu menampilkan pesan umum "kesalahan database".
- **Diharapkan:** Ditolak oleh validasi dengan pesan
  "Tanggal mulai harus berformat TTTT-BB-HH." sesuai PRD F-08 dan kamus data.
- **Keparahan:** Sedang â€” satu transaksi gagal, pesan galat menyesatkan, tidak ada data rusak.
- **Prioritas:** Sprint ini.
- **Penyebab:** `date.fromisoformat()` pada Python 3.11+ menerima format ISO kompak
  `YYYYMMDD`, sehingga pemeriksaan format terlewat sebelum data sampai ke basis data.
- **Perbaikan:** commit `55e5351` â€” helper `_format_tanggal_valid()` memeriksa
  pola `TTTT-BB-HH` sebelum `date.fromisoformat()` pada keempat isian tanggal.
- **Uji regresi:** `tests/test_validasi.py::test_tanggal_sewa[20261108-False-tanggal_mulai]`
  â†’ lulus; seluruh uji tanggal terkait â†’ 4 passed.
- **Status:** Diperbaiki

### D-02 â€” Harga di atas batas `DECIMAL(12,2)` diterima

- **Ditemukan:** 21 November 2026 oleh tim lewat TC-06.
- **Langkah:**
  1. `POST /kamar/tambah` dengan `nomor_kamar = X-1`,
     `harga_sewa = 10000000000.00` (11 digit sebelum koma).
  2. Amati hasil validasi.
- **Aktual:** `services.validate_kamar` menerima nilai (galat `{}`). Nilai
  disimpan sebagai `REAL` pada kolom `NUMERIC`, melampaui kapasitas
  `DECIMAL(12,2)` yang ditetapkan kamus data.
- **Diharapkan:** Ditolak dengan pesan harga harus berupa angka dalam batas
  `DECIMAL(12,2)` (maksimal 10 digit sebelum koma dan 2 di belakang koma).
- **Keparahan:** Sedang â€” data tersimpan di luar batas tipe yang disepakati.
- **Prioritas:** Sprint ini.
- **Penyebab:** Validasi hanya memeriksa `is_finite()` dan `>= 0`; tidak ada
  pemeriksaan batas digit/presisi sesuai kamus data.
- **Perbaikan:** commit `08ca34c` — helper `_harga_dalam_batas()` dipakai
  pada tiga isian uang; pesan galat lama dipertahankan.
- **Uji regresi:** `tests/test_validasi.py::test_harga_sewa[10000000000.00-False]`
  → lulus; `uji_cepat.py` dan 59 unittest tetap lulus.
- **Status:** Diperbaiki

### D-03 â€” Karakter `%` pada pencarian kamar dianggap wildcard

- **Ditemukan:** 21 November 2026 oleh tim lewat TC-37 dan uji eksploratif no. 1.
- **Langkah:**
  1. Tambah kamar `A-01` dan `B-01`.
  2. Buka `/kamar?q=%`.
- **Aktual:** Kedua kamar tampil, karena `%` diteruskan ke `LIKE` tanpa escape.
- **Diharapkan:** Tidak ada kamar yang tampil (tidak ada nomor kamar yang benar-benar
  memuat `%`). Modul sewa dan pembayaran sudah melakukan escape dengan `_escape_like()`.
- **Keparahan:** Rendah â€” hasil pencarian menyesatkan, tidak ada data rusak.
- **Prioritas:** Sprint ini (perbaikannya satu baris, konsisten dengan modul lain).
- **Penyebab:** `get_all_kamar` dan `get_all_penyewa` menyusun pola `f"%{kata}%"`
  tanpa memanggil `_escape_like()`, berbeda dengan `get_all_sewa` dan
  `get_all_pembayaran`.
- **Perbaikan:** (diisi setelah commit perbaikan)
- **Uji regresi:** `tests/test_alur_kontrakan.py::test_pencarian_kamar_tidak_memakai_wildcard`
- **Status:** Terbuka

---

## Permintaan perubahan (bukan cacat)

Dicatat terpisah sesuai Bagian 2.5 jobsheet; memerlukan keputusan klien.

| No | Permintaan | Dasar | Keputusan yang dibutuhkan |
|---|---|---|---|
| PR-01 | Nama kamar `A-01` dan `a-01` saat ini dapat dibuat bersamaan | Skema `UNIQUE` bersifat case-sensitive; PRD hanya menyatakan "unik" | Apakah unik harus tidak membedakan huruf besar-kecil? |
| PR-02 | Batas maksimal pembayaran dan kelebihan bayar belum ditetapkan | Kamus data bagian 10.1 | Apakah kelebihan bayar diizinkan atau ditolak? |
| PR-03 | Hak akses ubah/hapus catatan pembayaran belum final | Kamus data bagian 10.1 | Apakah kasir boleh menghapus pembayaran? |

## Koreksi uji (bukan cacat aplikasi)

Dua kegagalan awal ternyata berasal dari uji yang saya tulis, bukan dari kode:

1. `test_matriks_akses[GET-/penyewa...]` â€” saya menuliskan 403 untuk kasir.
   Padahal sesuai matriks akses Jobshet 11, halaman **daftar** penyewa adalah
   `@semua_peran`; yang terlarang adalah **mutasi** penyewa. Harapan uji
   diperbaiki menjadi 200.
2. `test_pesan_galat_login_sama...` â€” asersi `ada.data == tidak_ada.data`
   terlalu kuat karena form mengisi ulang nilai username pada atribut `value`.
   Pesan galatnya tetap identik. Asersi diganti dengan pemeriksaan pesan spesifik
   dan ketiadaan kata "tidak ditemukan"/"tidak terdaftar".

Keduanya dicatat transparan; tidak ada uji yang dihapus atau dilonggarkan agar
cacat D-01 sampai D-03 tertutup.

