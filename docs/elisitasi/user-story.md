# User Story — Sistem Informasi Pengelolaan Kontrakan

> **Status dokumen:** Draft berdasarkan simulasi wawancara (data fiktif).  
> **Catatan:** User story berikut belum divalidasi oleh klien nyata. Kebutuhan yang belum dikonfirmasi diberi tanda **[Asumsi]**.

## US-01 — Login Pemilik Kontrakan [Asumsi]

**Sebagai** pemilik kontrakan, **saya ingin** masuk ke sistem menggunakan akun, **agar** data kontrakan hanya dapat diakses oleh pengguna yang memiliki izin.

**Sumber:** Asumsi awal proyek; belum dibahas secara khusus dalam simulasi wawancara.

**Acceptance Criteria:**

1. **Given** pengguna memiliki akun terdaftar, **When** pengguna memasukkan username dan password yang benar, **Then** sistem menampilkan halaman utama.
2. **Given** pengguna memasukkan password yang salah, **When** pengguna menekan tombol login, **Then** sistem menampilkan pesan kesalahan dan tidak memberikan akses.

## US-02 — Mengelola Data Kamar

**Sebagai** pemilik kontrakan, **saya ingin** menambahkan, melihat, mengubah, dan menghapus data kamar, **agar** informasi seluruh kamar dapat dikelola dengan rapi.

**Sumber:** Catatan Wawancara bagian A — Pengelolaan Kamar.

**Acceptance Criteria:**

1. **Given** pemilik berada pada halaman data kamar, **When** pemilik mengisi nomor kamar dan harga sewa lalu menyimpan data, **Then** kamar baru ditampilkan dalam daftar kamar.
2. **Given** terdapat data kamar, **When** pemilik mengubah informasi kamar dan menyimpan perubahan, **Then** sistem menampilkan informasi kamar yang telah diperbarui.

## US-03 — Melihat Status Ketersediaan Kamar

**Sebagai** pemilik kontrakan, **saya ingin** melihat status setiap kamar, **agar** saya dapat mengetahui kamar yang tersedia dan sedang ditempati.

**Sumber:** Catatan Wawancara bagian A — Pengelolaan Kamar.

**Acceptance Criteria:**

1. **Given** terdapat beberapa data kamar, **When** pemilik membuka daftar kamar, **Then** sistem menampilkan status setiap kamar.
2. **Given** sebuah kamar telah ditempati penyewa, **When** pemilik memperbarui status kamar menjadi terisi, **Then** sistem menampilkan status kamar sebagai terisi.

## US-04 — Mengelola Data Penyewa

**Sebagai** pemilik kontrakan, **saya ingin** mencatat dan mengelola data penyewa, **agar** informasi penyewa dapat ditemukan kembali dengan mudah.

**Sumber:** Catatan Wawancara bagian B — Data Penyewa.

**Acceptance Criteria:**

1. **Given** pemilik berada pada halaman data penyewa, **When** pemilik mengisi nama dan informasi penyewa lalu menyimpan, **Then** data penyewa tersimpan dan ditampilkan.
2. **Given** data penyewa sudah tersimpan, **When** pemilik mengubah informasi penyewa, **Then** sistem menampilkan data terbaru.

## US-05 — Menghubungkan Penyewa dengan Kamar

**Sebagai** pemilik kontrakan, **saya ingin** mencatat kamar yang ditempati setiap penyewa, **agar** saya dapat mengetahui siapa yang menempati setiap kamar.

**Sumber:** Catatan Wawancara bagian B — Data Penyewa dan bagian A — Pengelolaan Kamar.

**Acceptance Criteria:**

1. **Given** terdapat data penyewa dan kamar yang tersedia, **When** pemilik memilih penyewa dan kamar, **Then** sistem menyimpan hubungan antara penyewa dan kamar tersebut.
2. **Given** sebuah kamar sudah ditempati, **When** pemilik mencoba menghubungkan penyewa lain ke kamar yang sama, **Then** sistem menolak penempatan tersebut atau meminta pemilik menyelesaikan penempatan sebelumnya.

## US-06 — Mencatat Pembayaran Sewa

**Sebagai** pemilik kontrakan, **saya ingin** mencatat pembayaran sewa penyewa, **agar** riwayat pembayaran dapat tersimpan dan diperiksa kembali.

**Sumber:** Catatan Wawancara bagian C — Pembayaran Sewa.

**Acceptance Criteria:**

1. **Given** terdapat data penyewa, **When** pemilik memasukkan tanggal dan jumlah pembayaran lalu menyimpan, **Then** sistem menyimpan transaksi pembayaran.
2. **Given** pembayaran telah tersimpan, **When** pemilik membuka riwayat pembayaran penyewa, **Then** sistem menampilkan informasi pembayaran yang pernah dicatat.

## US-07 — Melihat Status Pembayaran Penyewa

**Sebagai** pemilik kontrakan, **saya ingin** melihat status pembayaran setiap penyewa, **agar** saya dapat mengetahui penyewa yang sudah dan belum membayar.

**Sumber:** Catatan Wawancara bagian C — Pembayaran Sewa.

**Acceptance Criteria:**

1. **Given** terdapat data pembayaran penyewa, **When** pemilik membuka halaman pembayaran, **Then** sistem menampilkan status pembayaran berdasarkan data yang tercatat.
2. **Given** pembayaran seorang penyewa telah dicatat, **When** pemilik menyimpan pembayaran tersebut, **Then** status pembayaran penyewa diperbarui sesuai transaksi yang dicatat.

## US-08 — Mencatat Tanggal Jatuh Tempo Pembayaran [Asumsi]

**Sebagai** pemilik kontrakan, **saya ingin** mengetahui tanggal jatuh tempo pembayaran sewa, **agar** saya dapat memantau pembayaran yang belum dilakukan tepat waktu.

**Sumber:** Catatan Wawancara bagian C — Pembayaran Sewa. Aturan jatuh tempo belum dikonfirmasi secara khusus.

**Acceptance Criteria:**

1. **Given** data periode sewa memiliki tanggal jatuh tempo, **When** pemilik membuka informasi pembayaran, **Then** sistem menampilkan tanggal jatuh tempo tersebut.
2. **Given** tanggal jatuh tempo telah terlewati dan pembayaran belum dicatat, **When** sistem menampilkan status pembayaran, **Then** pembayaran ditandai terlambat.

## US-09 — Mengelola Periode Sewa

**Sebagai** pemilik kontrakan, **saya ingin** mencatat tanggal mulai dan berakhirnya masa sewa, **agar** masa sewa setiap penyewa dapat dipantau.

**Sumber:** Catatan Wawancara bagian D — Periode Sewa.

**Acceptance Criteria:**

1. **Given** pemilik sedang mencatat penyewaan kamar, **When** pemilik memasukkan tanggal mulai dan tanggal berakhir sewa, **Then** sistem menyimpan periode sewa.
2. **Given** periode sewa telah tersimpan, **When** pemilik membuka detail penyewa, **Then** sistem menampilkan tanggal mulai dan berakhir sewa.

## US-10 — Mendapatkan Informasi Masa Sewa yang Akan Berakhir [Asumsi]

**Sebagai** pemilik kontrakan, **saya ingin** mengetahui masa sewa yang akan segera berakhir, **agar** saya dapat mempersiapkan proses perpanjangan atau pergantian penyewa.

**Sumber:** Catatan Wawancara bagian D — Periode Sewa. Mekanisme pengingat otomatis belum dikonfirmasi.

**Acceptance Criteria:**

1. **Given** terdapat periode sewa yang mendekati tanggal berakhir, **When** pemilik membuka daftar periode sewa, **Then** sistem menampilkan informasi masa sewa yang akan segera berakhir.
2. **Given** periode sewa telah melewati tanggal berakhir, **When** pemilik melihat data periode sewa, **Then** sistem menampilkan bahwa periode tersebut telah berakhir.

## US-11 — Melihat Laporan Pendapatan

**Sebagai** pemilik kontrakan, **saya ingin** melihat rekapitulasi pendapatan berdasarkan periode tertentu, **agar** saya dapat mengetahui pemasukan kontrakan.

**Sumber:** Catatan Wawancara bagian E — Laporan Pendapatan.

**Acceptance Criteria:**

1. **Given** terdapat catatan pembayaran sewa, **When** pemilik memilih periode laporan, **Then** sistem menampilkan daftar pembayaran pada periode tersebut.
2. **Given** laporan pembayaran telah ditampilkan, **When** pemilik melihat total pendapatan, **Then** sistem menampilkan jumlah berdasarkan transaksi pembayaran yang tercatat dalam periode tersebut.

## US-12 — Mengunduh Laporan Pendapatan [Asumsi]

**Sebagai** pemilik kontrakan, **saya ingin** mengunduh laporan pendapatan, **agar** saya dapat menyimpan dan menggunakan laporan sebagai arsip.

**Sumber:** Catatan Wawancara bagian E — Laporan Pendapatan. Fitur unduh PDF belum dikonfirmasi dalam simulasi.

**Acceptance Criteria:**

1. **Given** laporan pendapatan telah ditampilkan, **When** pemilik memilih fitur unduh laporan, **Then** sistem menghasilkan file laporan yang dapat disimpan.
2. **Given** pemilik memilih periode laporan tertentu, **When** pemilik mengunduh laporan, **Then** isi laporan sesuai dengan periode yang dipilih.

---

## Hasil Peninjauan Awal

| No. | User Story | Status |
|---|---|---|
| 1 | Login Pemilik Kontrakan | [Asumsi] |
| 2 | Mengelola Data Kamar | Draft simulasi |
| 3 | Melihat Status Ketersediaan Kamar | Draft simulasi |
| 4 | Mengelola Data Penyewa | Draft simulasi |
| 5 | Menghubungkan Penyewa dengan Kamar | Draft simulasi |
| 6 | Mencatat Pembayaran Sewa | Draft simulasi |
| 7 | Melihat Status Pembayaran | Draft simulasi |
| 8 | Mencatat Jatuh Tempo | [Asumsi] |
| 9 | Mengelola Periode Sewa | Draft simulasi |
| 10 | Informasi Masa Sewa Berakhir | [Asumsi] |
| 11 | Melihat Laporan Pendapatan | Draft simulasi |
| 12 | Mengunduh Laporan Pendapatan | [Asumsi] |

## Catatan Validasi

Seluruh user story dalam dokumen ini disusun berdasarkan skenario simulasi wawancara pemilik kontrakan fiktif. Status "Draft simulasi" berarti kebutuhan tersebut muncul dalam skenario latihan, bukan berarti telah dikonfirmasi oleh klien nyata.

User story perlu ditinjau kembali setelah wawancara nyata atau setelah dosen menyetujui penggunaan responden alternatif/simulasi. Kebutuhan yang belum dikonfirmasi harus tetap ditandai sebagai asumsi.