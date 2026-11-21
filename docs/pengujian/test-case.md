# Test Case — Jobsheet 13

Proyek: Sistem Informasi Pengelolaan Kontrakan
Sumber harapan: `PRD.md`, `docs/desain/kamus-data.md`, `docs/desain/schema.sql`
Teknik: EP = partisi ekuivalen; BVA = analisis nilai batas; Pelanggaran = masukan/peran yang harus ditolak.

## Matriks keterlacakan (Lampiran B.1)

| KF | Kebutuhan | Kriteria penerimaan (dari PRD) | Test case |
|---|---|---|---|
| KF-01 | Login pemilik | Kredensial benar → halaman utama; salah → pesan galat dan akses ditolak | TC-34, TC-35, TC-36 |
| KF-02 | Menambah data kamar | Nomor kamar wajib, unik, maks. 20 karakter; harga ≥ 0; data muncul di daftar | TC-01–TC-17 |
| KF-03 | Melihat & mencari kamar | Daftar menampilkan status Tersedia/Terisi; pencarian hanya mencocokkan isian | TC-18, TC-37 |
| KF-06 | Mengelola data penyewa | Nama wajib; telepon `08`+8–11 digit atau `+628`+8–11 digit; alamat wajib | TC-19–TC-25 |
| KF-07 | Menghubungkan penyewa dengan kamar | Pasangan kamar/penyewa valid tersimpan; kamar yang masih disewa tidak bisa dipakai lagi | TC-26, TC-29, TC-38 |
| KF-09 | Mencatat pembayaran sewa | Tanggal valid; jumlah bayar > 0; transaksi tersimpan | TC-30–TC-33 |
| KF-13 | Mengelola periode sewa | Tanggal mulai/selesai valid berformat `TTTT-BB-HH`; selesai ≥ mulai | TC-26–TC-29 |
| KF-15 | Melihat laporan pendapatan | Laporan menampilkan pembayaran pada periode yang dipilih | TC-39 |

KF tanpa test case: **0** (8 KF tercakup).

## Partisi dan nilai batas yang dipakai

| Isian | Partisi | Nilai batas yang diuji |
|---|---|---|
| `harga_sewa` (KF-02) | valid (≥ 0), negatif, bukan angka, kosong, Unicode, tak hingga, melebihi `DECIMAL(12,2)` | −1, 0, 1, 9999999999.99, 10000000000.00 |
| `nomor_kamar` (KF-02) | valid (1–20 char), kosong, duplikat, kepanjangan | 1 char, 20 char, 21 char |
| `no_telepon` (KF-06) | `08` (10–13 digit), `+628` (12–15 char), salah awalan, kepanjangan | 10, 11, 13, 14 digit |
| `tanggal_*` (KF-09/13) | valid `TTTT-BB-HH`, kompak, tidak ada di kalender, urutan terbalik | 2026-03-01, 20261108, 2026-02-30 |
| `jumlah_bayar` (KF-09) | valid (> 0), nol, negatif, bukan angka | 0, 1, −1 |

## Tabel test case (Lampiran B.2)

Harapan ditulis **sebelum** menjalankan uji, berdasarkan PRD/kamus data/skema — bukan dari keluaran kode.

| ID | KF | Teknik | Masukan / langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|---|---|---|
| TC-01 | KF-02 | BVA | `harga_sewa = "0"` | Diterima (batas bawah) | Sesuai harapan | Lulus |
| TC-02 | KF-02 | BVA | `harga_sewa = "1"` | Diterima | Sesuai harapan | Lulus |
| TC-03 | KF-02 | EP | `harga_sewa = "850000"` | Diterima | Sesuai harapan | Lulus |
| TC-04 | KF-02 | EP | `harga_sewa = " 850000 "` | Diterima sebagai 850000 (spasi pinggir dipangkas) | Sesuai harapan | Lulus |
| TC-05 | KF-02 | BVA | `harga_sewa = "9999999999.99"` | Diterima (batas atas `DECIMAL(12,2)`) | Sesuai harapan | Lulus |
| TC-06 | KF-02 | BVA | `harga_sewa = "10000000000.00"` | Ditolak, melebihi `DECIMAL(12,2)` | Awal gagal (D-02) | Lulus setelah perbaikan |
| TC-07 | KF-02 | Pelanggaran | `harga_sewa = "-1"` | Ditolak, pesan tidak boleh negatif | Sesuai harapan | Lulus |
| TC-08 | KF-02 | Pelanggaran | `harga_sewa = "abc"` | Ditolak, pesan harus angka | Sesuai harapan | Lulus |
| TC-09 | KF-02 | Pelanggaran | `harga_sewa = ""` | Ditolak, pesan wajib diisi | Sesuai harapan | Lulus |
| TC-10 | KF-02 | Pelanggaran | `harga_sewa = "²"` | Ditolak, bukan galat 500 | Sesuai harapan | Lulus |
| TC-11 | KF-02 | Pelanggaran | `harga_sewa = "Infinity"` | Ditolak, bukan galat 500 | Sesuai harapan | Lulus |
| TC-12 | KF-02 | BVA | `nomor_kamar = "A"` (1 char) | Diterima | Sesuai harapan | Lulus |
| TC-13 | KF-02 | BVA | `nomor_kamar` 20 karakter | Diterima | Sesuai harapan | Lulus |
| TC-14 | KF-02 | BVA | `nomor_kamar` 21 karakter | Ditolak, pesan maksimal 20 karakter | Sesuai harapan | Lulus |
| TC-15 | KF-02 | Pelanggaran | `nomor_kamar = ""` | Ditolak, pesan wajib diisi | Sesuai harapan | Lulus |
| TC-16 | KF-02 | Normal | Tambah kamar `A-01`, harga `850000` | Tersimpan dan muncul di daftar | Sesuai harapan | Lulus |
| TC-17 | KF-02 | Pelanggaran | Tambah dua kamar bernomor sama | Yang kedua ditolak, pesan "sudah ada" | Sesuai harapan | Lulus |
| TC-18 | KF-03 | Normal | Buka daftar kamar tanpa filter | Status Tersedia/Terisi tampil untuk tiap kamar | Sesuai harapan | Lulus |
| TC-19 | KF-06 | EP | `no_telepon = "081234567890"` | Diterima | Sesuai harapan | Lulus |
| TC-20 | KF-06 | BVA | `no_telepon = "0812345678"` (10 digit) | Diterima (batas bawah) | Sesuai harapan | Lulus |
| TC-21 | KF-06 | BVA | `no_telepon = "08123456789"` (11 digit) | Diterima | Sesuai harapan | Lulus |
| TC-22 | KF-06 | BVA | `no_telepon = "0812345678901"` (13 digit) | Diterima (batas atas) | Sesuai harapan | Lulus |
| TC-23 | KF-06 | BVA | `no_telepon = "08123456789012"` (14 digit) | Ditolak, melebihi batas | Sesuai harapan | Lulus |
| TC-24 | KF-06 | Pelanggaran | `no_telepon = "+621234567890"` | Ditolak, awalan harus +628 | Sesuai harapan | Lulus |
| TC-25 | KF-06 | Pelanggaran | `nama = ""` | Ditolak, pesan wajib diisi | Sesuai harapan | Lulus |
| TC-26 | KF-13 | BVA | `tanggal_mulai = "2026-03-01"` | Diterima | Sesuai harapan | Lulus |
| TC-27 | KF-13 | Pelanggaran | `tanggal_mulai = "20261108"` | Ditolak, harus berformat `TTTT-BB-HH` | Awal gagal (D-01) | Lulus setelah perbaikan |
| TC-28 | KF-13 | Pelanggaran | `tanggal_mulai = "2026-02-30"` | Ditolak, tanggal tidak ada di kalender | Sesuai harapan | Lulus |
| TC-29 | KF-13 | Pelanggaran | `tanggal_selesai = "2026-02-28"`, mulai `2026-03-01` | Ditolak, selesai sebelum mulai | Sesuai harapan | Lulus |
| TC-30 | KF-09 | BVA | `jumlah_bayar = "0"` | Ditolak, harus lebih dari 0 | Sesuai harapan | Lulus |
| TC-31 | KF-09 | BVA | `jumlah_bayar = "1"` | Diterima (batas bawah) | Sesuai harapan | Lulus |
| TC-32 | KF-09 | Pelanggaran | `jumlah_bayar = "-1"` | Ditolak | Sesuai harapan | Lulus |
| TC-33 | KF-09 | Normal | Catat pembayaran tanggal `2026-03-10`, jumlah `850000` | Tersimpan dan muncul di riwayat | Sesuai harapan | Lulus |
| TC-34 | KF-01 | Normal | Login dengan kredensial benar | Masuk ke halaman utama | Sesuai harapan | Lulus |
| TC-35 | KF-01 | Pelanggaran | Login dengan kata sandi salah | Pesan umum "Username atau password salah." | Sesuai harapan | Lulus |
| TC-36 | KF-01 | Pelanggaran | 5 kali login gagal, lalu kata sandi benar | Percobaan ke-6 ditolak 429 | Sesuai harapan | Lulus |
| TC-37 | KF-03 | Pelanggaran | Cari kamar dengan `q = "%"` | Hanya kamar yang benar-benar memuat `%` yang tampil (asumsi konsistensi dengan pencarian sewa) | Awal gagal (D-03) | Lulus setelah perbaikan |
| TC-38 | KF-07 | Pelanggaran | Dua sewa pada kamar sama dengan periode bertumpang tindih | Yang kedua ditolak, pesan tumpang tindih | Sesuai harapan | Lulus |
| TC-39 | KF-15 | Normal | Lihat laporan dengan periode yang memuat satu pembayaran | Pembayaran itu tampil dalam daftar laporan | Sesuai harapan | Lulus |

**Komposisi:** 39 test case; BVA 13 (TC-01, 02, 05, 06, 12, 13, 14, 20, 21, 22, 26, 30, 31), pelanggaran 19, normal 7. Memenuhi syarat ≥ 20, ≥ 6 BVA, ≥ 6 pelanggaran, ≥ 3 normal.

## Hasil menjalankan (Langkah 7 — diisi setelah pytest)

| Informasi | Nilai |
|---|---|
| Perintah | `python -m pytest -q tests/test_validasi.py` |
| Draf AI sebelum ditinjau | 1 failed, 29 passed |
| Setelah perbaikan asersi | 2 failed, 28 passed |
| Uji alur/akses diperbaiki | 3 failed, 108 passed (3 cacat nyata) |
| **Setelah perbaikan 3 cacat** | **111 passed, 23 subtests** |
| Fungsi uji pytest baru | 29 fungsi (termasuk 30+ kasus parametrize) |
| Uji lama tetap lulus | `uji_cepat.py` SEMUA UJI LULUS; 59 unittest OK |
| Mutasi manual | 3 dari 3 tertangkap (M1→TC-01, M2→TC-13, M3→TC-30) |
| Cacat | D-01, D-02, D-03 — semuanya Diperbaiki (lihat `laporan-cacat.md`) |

Catatan: TC-27 pada draf AI **salah lulus** karena galatnya berasal dari
`tanggal_selesai`, bukan dari format `tanggal_mulai`. Setelah asersi dibuat
spesifik (`assert "tanggal_mulai" in galat`), cacat D-01 baru terlihat.