# User Story — Sistem Informasi Pengelolaan Kontrakan

**Status:** Draf awal berdasarkan hipotesis proyek, belum tervalidasi melalui wawancara.

## US-01 — Login Pemilik Kontrakan

**User Story:**

Sebagai pemilik kontrakan, saya ingin masuk ke sistem menggunakan akun saya agar data pengelolaan kontrakan hanya dapat diakses oleh pihak yang memiliki hak akses.

**Kriteria Penerimaan:**

1. **Given** pemilik memiliki akun yang terdaftar dan aktif, **When** pemilik memasukkan username dan password yang benar, **Then** sistem menampilkan halaman utama.
2. **Given** pemilik memasukkan password yang salah, **When** menekan tombol masuk, **Then** sistem menolak akses dan menampilkan pesan kesalahan.

**Sumber:** Hipotesis awal proyek — belum ada nomor catatan wawancara.

## US-02 — Mengelola Data Kamar

**User Story:**

Sebagai pemilik kontrakan, saya ingin mencatat dan memperbarui data kamar agar saya dapat mengetahui informasi dan ketersediaan setiap kamar.

**Kriteria Penerimaan:**

1. **Given** pemilik berada pada halaman data kamar, **When** pemilik mengisi nomor kamar dan informasi kamar yang wajib diisi lalu menyimpan, **Then** data kamar tersimpan dan tampil pada daftar kamar.
2. **Given** terdapat data kamar yang sudah tersimpan, **When** pemilik mengubah status kamar menjadi terisi, **Then** status kamar pada daftar berubah menjadi terisi.

**Sumber:** Hipotesis awal proyek — belum ada nomor catatan wawancara.

## US-03 — Mengelola Data Penyewa

**User Story:**

Sebagai pemilik kontrakan, saya ingin mencatat dan memperbarui data penyewa agar informasi penghuni setiap kamar tersimpan dengan teratur.

**Kriteria Penerimaan:**

1. **Given** pemilik berada pada halaman data penyewa, **When** pemilik mengisi nama dan informasi wajib penyewa lalu menyimpan, **Then** data penyewa tersimpan dan tampil pada daftar penyewa.
2. **Given** data penyewa sudah tersimpan, **When** pemilik memperbarui informasi penyewa dan menyimpan perubahan, **Then** sistem menampilkan informasi terbaru.

**Sumber:** Hipotesis awal proyek — belum ada nomor catatan wawancara.

## US-04 — Mencatat Pembayaran Sewa

**User Story:**

Sebagai pemilik kontrakan, saya ingin mencatat pembayaran sewa penyewa agar saya dapat memantau pembayaran yang sudah dilakukan dan yang belum dilakukan.

**Kriteria Penerimaan:**

1. **Given** penyewa memiliki tagihan sewa yang belum dibayar, **When** pemilik mencatat pembayaran dengan nominal yang sesuai, **Then** sistem menyimpan transaksi dan memperbarui status pembayaran menjadi dibayar.
2. **Given** terdapat tagihan sewa yang belum dibayar, **When** pemilik melihat daftar pembayaran, **Then** sistem menampilkan status tagihan tersebut sebagai belum dibayar.

**Sumber:** Hipotesis awal proyek — belum ada nomor catatan wawancara.

## US-05 — Mengelola Periode Sewa

**User Story:**

Sebagai pemilik kontrakan, saya ingin mencatat tanggal mulai dan berakhirnya masa sewa agar saya dapat mengetahui periode sewa setiap penyewa.

**Kriteria Penerimaan:**

1. **Given** pemilik sedang menambahkan data periode sewa, **When** pemilik mengisi tanggal mulai dan tanggal berakhir yang valid lalu menyimpan, **Then** sistem menyimpan kedua tanggal tersebut.
2. **Given** periode sewa sudah tersimpan, **When** pemilik membuka data penyewa terkait, **Then** sistem menampilkan tanggal mulai dan tanggal berakhir masa sewa.

**Sumber:** Hipotesis awal proyek — belum ada nomor catatan wawancara.

## US-06 — Melihat Laporan Pendapatan

**User Story:**

Sebagai pemilik kontrakan, saya ingin melihat laporan pendapatan sewa berdasarkan periode tertentu agar saya dapat mengetahui jumlah pemasukan dari usaha kontrakan.

**Kriteria Penerimaan:**

1. **Given** terdapat transaksi pembayaran sewa yang sudah tercatat, **When** pemilik memilih periode laporan, **Then** sistem menampilkan total pembayaran yang berstatus dibayar dalam periode tersebut.
2. **Given** pemilik memilih periode yang tidak memiliki transaksi pembayaran, **When** laporan ditampilkan, **Then** sistem menampilkan total pendapatan sebesar Rp0 untuk periode tersebut.

**Sumber:** Hipotesis awal proyek — belum ada nomor catatan wawancara.

---

**Catatan:** Semua user story di atas masih perlu divalidasi kepada pemilik kontrakan. Ganti bagian Sumber dengan nomor catatan wawancara setelah data wawancara tersedia.