# Product Requirements Document (PRD)
# Sistem Informasi Pengelolaan Kontrakan

**Versi:** 1.0  
**Status:** Draft  
**Dasar:** SRS dan user story berdasarkan simulasi wawancara (data fiktif), belum divalidasi klien nyata.

## 1. Ringkasan Produk dan Tujuan

Sistem Informasi Pengelolaan Kontrakan merupakan aplikasi berbasis web untuk membantu pemilik kontrakan mengelola kamar, penyewa, pembayaran, dan periode sewa secara terstruktur. Sistem juga menyediakan informasi ketersediaan kamar serta laporan pendapatan berdasarkan periode tertentu.

Tujuan produk:
- Mempermudah pengelolaan data kamar dan penyewa.
- Memantau ketersediaan kamar dan periode sewa.
- Mempermudah pencatatan serta pemantauan pembayaran.
- Menyediakan rekapitulasi pendapatan kontrakan.

## 2. Pengguna dan Peran

**Pemilik kontrakan (pengguna utama):**
- Login ke sistem.
- Mengelola data kamar dan penyewa.
- Menghubungkan penyewa dengan kamar.
- Mencatat dan memantau pembayaran.
- Mengelola periode sewa.
- Melihat laporan pendapatan.

**Pengelola atau penjaga kontrakan:** Calon pengguna tambahan. Hak akses dan kebutuhannya belum ditentukan sehingga belum termasuk ruang lingkup pengembangan.

## 3. Fitur Berdasarkan Prioritas dan Kriteria Penerimaan

Kriteria penerimaan ditulis menggunakan format Given–When–Then.

### 3.1 Must Have (Prioritas Wajib)

**F-01 — Login pemilik (US-01, KF-01)**

Given pengguna memiliki akun terdaftar, When memasukkan username dan password yang benar, Then sistem menampilkan halaman utama. Jika password salah, sistem menampilkan pesan kesalahan dan menolak akses.

**F-02 — Menambah dan melihat data kamar (US-02, KF-02, KF-03)**

Given pemilik berada pada halaman data kamar, When mengisi nomor kamar dan harga sewa lalu menyimpan, Then data kamar tersimpan dan muncul dalam daftar kamar.

**F-03 — Melihat ketersediaan kamar (US-03, KF-05)**

Given terdapat data kamar, When pemilik membuka daftar kamar, Then sistem menampilkan status setiap kamar sebagai tersedia atau terisi.

**F-04 — Mengelola data penyewa (US-04, KF-06)**

Given data penyewa sudah tersimpan, When pemilik mengubah informasi penyewa dan menyimpan perubahan, Then sistem menampilkan data penyewa terbaru.

**F-05 — Menghubungkan penyewa dengan kamar (US-05, KF-07)**

Given tersedia data penyewa dan kamar, When pemilik memilih penyewa serta kamar yang tersedia, Then sistem menyimpan hubungan penyewa dengan kamar tersebut.

**F-06 — Mencatat pembayaran sewa (US-06, KF-09)**

Given terdapat data penyewa, When pemilik memasukkan tanggal dan jumlah pembayaran lalu menyimpan, Then sistem menyimpan transaksi pembayaran.

**F-07 — Melihat status pembayaran (US-07, KF-11)**

Given terdapat data pembayaran, When pemilik membuka halaman pembayaran, Then sistem menampilkan status pembayaran berdasarkan transaksi yang tercatat.

**F-08 — Mengelola periode sewa (US-09, KF-13)**

Given pemilik sedang mencatat penyewaan kamar, When memasukkan tanggal mulai dan tanggal berakhir sewa, Then sistem menyimpan dan menampilkan periode sewa tersebut.

**F-09 — Melihat laporan pendapatan (US-11, KF-15)**

Given terdapat catatan pembayaran, When pemilik memilih periode laporan, Then sistem menampilkan daftar pembayaran dan total pendapatan pada periode tersebut.

### 3.2 Should Have (Prioritas Dianjurkan)

**F-10 — Mengubah data kamar (US-02, KF-04)**

Given terdapat data kamar, When pemilik mengubah informasi dan menyimpan perubahan, Then sistem menampilkan informasi kamar terbaru.

**F-11 — Mencegah penempatan kamar yang sudah terisi (US-05, KF-08)**

Given kamar sudah ditempati, When pemilik mencoba menempatkan penyewa lain pada kamar yang sama, Then sistem menolak penempatan tersebut.

**F-12 — Melihat riwayat pembayaran (US-06, KF-10)**

Given pembayaran telah tersimpan, When pemilik membuka riwayat pembayaran penyewa, Then sistem menampilkan transaksi pembayaran yang pernah dicatat.

**F-13 — Menampilkan tanggal jatuh tempo (US-08, KF-12)**

Given periode sewa memiliki tanggal jatuh tempo, When pemilik membuka informasi pembayaran, Then sistem menampilkan tanggal jatuh tempo. Jika tanggal tersebut terlewati tanpa pembayaran, sistem menandai pembayaran terlambat.

**F-14 — Menampilkan masa sewa yang akan berakhir (US-10, KF-14)**

Given terdapat periode sewa yang mendekati atau melewati tanggal berakhir, When pemilik membuka daftar periode sewa, Then sistem menampilkan periode yang mendekati akhir atau telah berakhir.

**F-15 — Kemudahan penggunaan (KNF-01)**

Given pemilik ingin menambahkan kamar, When mengikuti proses penambahan data, Then proses tersebut dapat diselesaikan maksimal dalam lima langkah.

**F-16 — Kinerja sistem (KNF-02)**

Given terdapat 100 data kamar, When pemilik membuka daftar kamar, Then sistem menampilkan daftar dalam waktu maksimal tiga detik pada kondisi pengujian yang ditentukan.

### 3.3 Persyaratan Kualitas Prioritas Wajib

**Keandalan (KNF-03):** Given data telah disimpan, When halaman dimuat ulang atau pengguna login kembali, Then data tetap tersedia.

**Keamanan (KNF-04):** Given pengguna belum login, When mencoba membuka halaman pengelolaan, Then sistem menolak akses dan mengarahkan pengguna ke proses login.

## 4. Data Awal

Entitas utama dan atribut penting yang direncanakan:

1. **Kamar:** ID kamar, nomor kamar, harga sewa, status ketersediaan.
2. **Penyewa:** ID penyewa, nama, informasi kontak atau identitas yang diperlukan.
3. **Sewa:** ID sewa, ID penyewa, ID kamar, tanggal mulai, tanggal berakhir, tanggal jatuh tempo.
4. **Pembayaran:** ID pembayaran, ID sewa, tanggal pembayaran, jumlah pembayaran, status pembayaran.
5. **Akun pengguna:** ID akun, username, dan informasi autentikasi.

Atribut tersebut masih berupa rancangan awal dan akan disesuaikan setelah kebutuhan dikonfirmasi. Struktur basis data lengkap akan dibahas pada tahap perancangan ERD.

## 5. Di Luar Lingkup

Fitur berikut belum termasuk dalam pengembangan saat ini:

- **Could:** Mengunduh laporan pendapatan (US-12, KF-16).
- **Won't:** Integrasi payment gateway atau pembayaran otomatis.
- **Won't:** Pengelolaan keuangan pribadi pemilik.
- **Won't:** Pengelolaan pemeliharaan dan renovasi bangunan.
- **Won't:** Integrasi dengan layanan pihak ketiga.

## 6. Pertanyaan Terbuka

Hal-hal berikut masih menunggu konfirmasi dari klien:

1. Apakah login hanya digunakan oleh pemilik atau juga pengelola/penjaga?
2. Apakah data kamar perlu memiliki fitur hapus?
3. Bagaimana aturan penentuan tanggal jatuh tempo pembayaran?
4. Berapa lama sebelum masa sewa berakhir informasi perlu ditampilkan?
5. Apakah status pembayaran cukup berupa sudah membayar dan belum membayar?
6. Apakah laporan pendapatan perlu dapat diunduh, dan dalam format apa?
7. Apakah kriteria kinerja tiga detik untuk 100 data kamar sudah sesuai kebutuhan?

**Catatan validasi:** Dokumen ini merupakan rancangan awal berdasarkan simulasi wawancara fiktif. Prioritas dan asumsi perlu ditinjau kembali bersama klien atau dosen sebelum ditetapkan sebagai kebutuhan final.