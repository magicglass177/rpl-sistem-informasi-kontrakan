# Software Requirements Specification (SRS)
# Sistem Informasi Pengelolaan Kontrakan

**Status Dokumen:** Draft  
**Versi:** 1.0  
**Dasar Penyusunan:** User story berdasarkan simulasi wawancara (data fiktif), belum divalidasi oleh klien nyata.

---

## 1. Pendahuluan

### 1.1 Tujuan

Dokumen Software Requirements Specification (SRS) ini menjelaskan kebutuhan fungsional dan nonfungsional dari Sistem Informasi Pengelolaan Kontrakan. Dokumen ini digunakan sebagai acuan dalam proses perancangan, pengembangan, dan pengujian sistem.

### 1.2 Ruang Lingkup Produk

Sistem Informasi Pengelolaan Kontrakan merupakan aplikasi berbasis web yang dibangun untuk membantu pemilik kontrakan dalam mengelola data kamar, data penyewa, hubungan penyewa dengan kamar, pembayaran uang sewa, periode sewa, status pembayaran, dan laporan pendapatan. Sistem ini ditujukan terutama bagi pemilik kontrakan sebagai pengguna utama. Ruang lingkup pengembangan mencakup pencatatan, pengubahan, pencarian, dan pemantauan data administrasi kontrakan. Sistem tidak mencakup integrasi payment gateway, pengelolaan keuangan pribadi pemilik, pemeliharaan bangunan, maupun integrasi dengan layanan pihak ketiga.

### 1.3 Definisi dan Singkatan

- **SRS:** Software Requirements Specification.
- **KF:** Kebutuhan Fungsional.
- **KNF:** Kebutuhan Nonfungsional.
- **US:** User Story.
- **Must:** Kebutuhan yang wajib dipenuhi.
- **Should:** Kebutuhan penting yang diutamakan.
- **Could:** Kebutuhan tambahan jika waktu memungkinkan.
- **Won't:** Kebutuhan yang tidak dikerjakan dalam proyek ini.

---

## 2. Gambaran Umum

### 2.1 Perspektif Produk

Sistem Informasi Pengelolaan Kontrakan dikembangkan untuk membantu proses pengelolaan kontrakan yang sebelumnya dilakukan secara manual. Sistem berfokus pada pencatatan dan pemantauan informasi kamar, penyewa, pembayaran, periode sewa, serta pendapatan.

### 2.2 Karakteristik Pengguna

Pengguna sistem yang direncanakan terdiri atas:

1. **Pemilik Kontrakan**
   - Peran: Pengguna utama yang memiliki hak akses untuk mengelola data kamar, data penyewa, pembayaran, periode sewa, dan laporan pendapatan.
   - Kemampuan teknis: [Asumsi] Memiliki kemampuan dasar dalam menggunakan komputer atau smartphone, menjalankan browser, mengisi formulir, dan mengoperasikan aplikasi berbasis web.
   - Hak akses: Mengelola seluruh data dan mengakses fitur utama sistem.

2. **Pengelola atau Penjaga Kontrakan**
   - Peran: Calon pengguna tambahan yang mungkin membantu pemilik dalam pencatatan data dan pembayaran.
   - Kemampuan teknis: [Asumsi] Memiliki kemampuan dasar dalam menggunakan perangkat dan aplikasi berbasis web.
   - Hak akses: Belum ditentukan dan perlu dikonfirmasi kepada pemilik kontrakan.

**Catatan:** Pemilik kontrakan merupakan satu-satunya peran pengguna yang telah ditetapkan dalam kebutuhan awal proyek. Keterlibatan pengelola atau penjaga kontrakan masih berupa asumsi.

### 2.3 Lingkungan Operasi

Lingkungan operasi yang direncanakan untuk Sistem Informasi Pengelolaan Kontrakan adalah sebagai berikut:

1. **Perangkat Keras**
   - [Asumsi] Komputer atau laptop untuk mengakses dan mengelola sistem.
   - [Asumsi] Smartphone sebagai alternatif perangkat untuk mengakses sistem.
   - Spesifikasi minimum perangkat belum ditentukan dan akan disesuaikan dengan teknologi yang digunakan.

2. **Perangkat Lunak**
   - [Asumsi] Sistem dapat diakses melalui browser seperti Google Chrome atau Microsoft Edge.
   - Sistem operasi yang digunakan dapat berupa Windows, Android, atau sistem operasi lain yang mendukung browser modern.
   - Sistem operasi dan versi browser yang digunakan klien perlu dikonfirmasi.

3. **Jaringan dan Listrik**
   - [Asumsi] Sistem memerlukan koneksi internet apabila aplikasi ditempatkan pada server online.
   - [Asumsi] Perangkat pengguna memerlukan sumber daya listrik atau baterai yang mencukupi selama penggunaan.
   - Ketersediaan jaringan internet dan kondisi listrik di lokasi kontrakan perlu dikonfirmasi.

**Catatan:** Lingkungan operasi di atas merupakan rancangan awal. Spesifikasi perangkat, sistem operasi, browser, jaringan, dan kondisi listrik belum dikonfirmasi kepada klien nyata.

### 2.4 Batasan dan Asumsi

#### 2.4.1 Batasan Proyek

Batasan yang memengaruhi proses pengembangan Sistem Informasi Pengelolaan Kontrakan adalah:

1. **Batasan Waktu:** Pengembangan proyek harus diselesaikan paling lambat pada Minggu ke-16 sesuai jadwal kegiatan perkuliahan.
2. **Batasan Anggaran:** [Asumsi] Pengembangan dilakukan dengan anggaran terbatas sebagai proyek tugas perkuliahan. Ketersediaan anggaran untuk hosting, domain, dan layanan tambahan belum dikonfirmasi.
3. **Batasan Perangkat:** [Asumsi] Pengembangan dan pengujian dilakukan menggunakan perangkat komputer atau laptop yang tersedia bagi pengembang. Kemampuan perangkat milik klien belum diketahui.
4. **Batasan Kemampuan Pengguna:** [Asumsi] Sistem dirancang agar dapat digunakan oleh pemilik kontrakan dengan kemampuan dasar mengoperasikan komputer atau smartphone. Tingkat kemampuan teknis pengguna sebenarnya perlu dikonfirmasi.
5. **Batasan Ruang Lingkup:** Sistem difokuskan pada administrasi pengelolaan kontrakan dan tidak mencakup payment gateway, pengelolaan keuangan pribadi, pemeliharaan bangunan, serta integrasi layanan pihak ketiga.

#### 2.4.2 Asumsi Proyek dan Rencana Konfirmasi

Asumsi merupakan hal yang sementara dianggap benar untuk mendukung perencanaan proyek. Status asumsi berikut diperbarui berdasarkan hasil simulasi konfirmasi kebutuhan, bukan hasil wawancara dengan klien nyata.

| ID | Asumsi | Rencana Konfirmasi | Status |
|---|---|---|---|
| A-01 | Pemilik kontrakan menjadi satu-satunya pengguna aplikasi. | Simulasi wawancara untuk memastikan pihak yang menggunakan sistem. | Terjawab dalam simulasi |
| A-02 | Pemilik kontrakan memiliki komputer, laptop, atau smartphone untuk mengakses sistem. | Menanyakan perangkat yang tersedia dan biasa digunakan oleh pemilik kontrakan. | Belum terjawab |
| A-03 | Pengguna memiliki kemampuan dasar dalam mengoperasikan aplikasi berbasis web. | Meminta pengguna mencoba rancangan antarmuka. | Belum terjawab |
| A-04 | Lokasi penggunaan sistem memiliki akses internet dan sumber listrik yang memadai. | Menanyakan kondisi jaringan internet dan listrik di lokasi kontrakan. | Belum terjawab |
| A-05 | Pengembangan dapat dilakukan menggunakan anggaran terbatas tanpa layanan berbayar tambahan. | Mengonfirmasi anggaran serta kebutuhan biaya hosting dan domain. | Belum terjawab |
| A-06 | Pengelola atau penjaga kontrakan mungkin membutuhkan akses ke sistem. | Simulasi wawancara untuk memastikan pihak yang menggunakan sistem. | Terjawab dalam simulasi: tidak diperlukan |
| A-07 | Sistem akan diakses melalui browser modern. | Mengonfirmasi perangkat, sistem operasi, dan browser yang biasa digunakan. | Belum terjawab |

**Catatan:** Status "Terjawab dalam simulasi" hanya menunjukkan bahwa asumsi telah memperoleh jawaban dalam skenario latihan. Status tersebut bukan bukti validasi dari klien nyata. Asumsi yang belum terjawab tetap perlu dikonfirmasi apabila proyek dilanjutkan bersama klien sebenarnya.

---

## 3. Kebutuhan Fungsional (KF)

| ID | Pernyataan Kebutuhan | Sumber | Prioritas | Asumsi? |
|---|---|---|---|---|
| KF-01 | Sistem harus memverifikasi username dan password pemilik kontrakan sebelum memberikan akses ke halaman utama. Akun pemilik disiapkan oleh administrator. | US-01 | Must | Ya |
| KF-02 | Sistem harus menyediakan fungsi untuk menambahkan data kamar berdasarkan nomor kamar yang unik dan harga sewa. | US-02 | Must | Tidak |
| KF-03 | Sistem harus menampilkan daftar data kamar yang telah tersimpan. | US-02 | Must | Tidak |
| KF-04 | Sistem harus menyediakan fungsi untuk mengubah informasi kamar yang telah tersimpan. | US-02 | Should | Tidak |
| KF-05 | Sistem harus menampilkan status setiap kamar sebagai tersedia atau terisi berdasarkan kondisi penempatan penyewa dan masa sewa. | US-03 | Must | Tidak |
| KF-06 | Sistem harus menyediakan fungsi untuk menambahkan dan mengubah data penyewa yang mencakup nama lengkap, nomor telepon, dan alamat. | US-04 | Must | Tidak |
| KF-07 | Sistem harus menyimpan hubungan antara penyewa dan kamar yang ditempatinya serta memperbarui status kamar berdasarkan penempatan penyewa dan berakhirnya masa sewa. | US-05 | Must | Tidak |
| KF-08 | Sistem harus menolak penempatan penyewa baru pada kamar yang masih ditempati penyewa lain. | US-05 | Must | Tidak |
| KF-09 | Sistem harus menyimpan tanggal dan jumlah setiap pembayaran sewa yang dicatat serta mendukung pencatatan pembayaran secara bertahap. | US-06 | Must | Tidak |
| KF-10 | Sistem harus menampilkan riwayat pembayaran setiap penyewa. | US-06 | Should | Tidak |
| KF-11 | Sistem harus menampilkan status pembayaran penyewa berdasarkan transaksi yang tercatat, yaitu lunas, belum lunas, atau terlambat. | US-07 | Must | Tidak |
| KF-12 | Sistem harus menampilkan tanggal jatuh tempo pembayaran sewa untuk setiap periode sewa. | US-08 | Should | Ya |
| KF-13 | Sistem harus menyimpan tanggal mulai dan tanggal berakhir setiap periode sewa. | US-09 | Must | Tidak |
| KF-14 | Sistem harus menampilkan periode sewa yang mendekati tanggal berakhir dan periode yang telah berakhir. | US-10 | Should | Ya |
| KF-15 | Sistem harus menampilkan daftar pembayaran dan total pendapatan berdasarkan periode laporan yang dipilih, dengan perhitungan berdasarkan tanggal pembayaran diterima. | US-11 | Must | Tidak |
| KF-16 | Sistem harus menyediakan fungsi untuk mengunduh laporan pendapatan berdasarkan periode yang dipilih. | US-12 | Could | Ya |

**Catatan:** Kebutuhan ini telah diperbarui berdasarkan skenario simulasi wawancara dan belum divalidasi oleh klien nyata. Detail aturan pembayaran sebagian dan penghitungan keterlambatan masih memerlukan penetapan lebih lanjut.

---

## 4. Kebutuhan Nonfungsional (KNF)

Kebutuhan berikut merupakan target awal proyek dan masih berstatus asumsi karena belum divalidasi oleh klien nyata.

| ID | Kategori | Pernyataan Kebutuhan | Sumber | Prioritas |
|---|---|---|---|---|
| KNF-01 | Usability | Pengguna harus dapat menyelesaikan proses penambahan data kamar dalam maksimal 5 langkah setelah berhasil masuk ke sistem. | US-02, target usability proyek | Should |
| KNF-02 | Performance | Sistem harus menampilkan halaman daftar kamar dalam waktu maksimal 3 detik pada kondisi pengujian dengan 100 data kamar. | US-03, target kinerja proyek | Should |
| KNF-03 | Reliability | Sistem harus mempertahankan seluruh data yang berhasil disimpan setelah pengguna memuat ulang halaman atau masuk kembali ke sistem. | Asumsi keandalan data proyek | Must |
| KNF-04 | Security | Sistem harus menolak akses ke halaman pengelolaan data apabila pengguna belum berhasil melakukan login. | US-01 | Must |

**Catatan:** Seluruh target KNF merupakan usulan awal dan belum dikonfirmasi oleh klien nyata. Prioritas MoSCoW akan ditentukan pada bagian berikutnya.

## 5. Batasan Proyek dan Prioritas

### 5.1 Metode Prioritas MoSCoW

Penentuan prioritas kebutuhan menggunakan metode MoSCoW dengan empat kategori:

- **Must:** Kebutuhan wajib yang harus dipenuhi agar fungsi utama sistem dapat berjalan.
- **Should:** Kebutuhan penting yang diutamakan setelah kebutuhan Must terpenuhi.
- **Could:** Kebutuhan tambahan yang dikerjakan apabila waktu dan sumber daya memungkinkan.
- **Won't:** Kebutuhan yang tidak dikerjakan dalam ruang lingkup proyek ini.

### 5.2 Rekapitulasi Prioritas Kebutuhan

| ID | Prioritas |
|---|---|
| KF-01 | Must |
| KF-02 | Must |
| KF-03 | Must |
| KF-04 | Should |
| KF-05 | Must |
| KF-06 | Must |
| KF-07 | Must |
| KF-08 | Should |
| KF-09 | Must |
| KF-10 | Should |
| KF-11 | Must |
| KF-12 | Should |
| KF-13 | Must |
| KF-14 | Should |
| KF-15 | Must |
| KF-16 | Could |
| KNF-01 | Should |
| KNF-02 | Should |
| KNF-03 | Must |
| KNF-04 | Must |

### 5.3 Perhitungan Persentase Must

Jumlah seluruh kebutuhan adalah 20, terdiri atas 16 kebutuhan fungsional dan 4 kebutuhan nonfungsional.

Jumlah kebutuhan dengan prioritas Must adalah 12.

Persentase Must dihitung menggunakan rumus:

Persentase Must = (Jumlah kebutuhan Must / Total seluruh kebutuhan) × 100%

Persentase Must = (12 / 20) × 100% = 60%

Dengan demikian, persentase kebutuhan Must adalah 60% dan masih sesuai dengan target maksimal sekitar 60%.

### 5.4 Alasan Penetapan Prioritas Must

1. **KF-01:** Login wajib tersedia untuk membatasi akses ke data kontrakan.
2. **KF-02:** Penambahan data kamar merupakan fungsi utama pengelolaan kamar.
3. **KF-03:** Daftar kamar diperlukan agar pemilik dapat melihat seluruh kamar yang dikelola.
4. **KF-05:** Status kamar diperlukan untuk mengetahui kamar tersedia dan terisi.
5. **KF-06:** Data penyewa diperlukan untuk mencatat identitas penghuni kontrakan.
6. **KF-07:** Hubungan penyewa dengan kamar diperlukan untuk mengetahui penghuni setiap kamar.
7. **KF-09:** Pencatatan pembayaran merupakan fungsi utama administrasi penyewaan.
8. **KF-11:** Status pembayaran diperlukan untuk memantau pembayaran penyewa.
9. **KF-13:** Periode sewa diperlukan untuk mengetahui tanggal mulai dan berakhirnya masa sewa.
10. **KF-15:** Laporan pendapatan diperlukan untuk mengetahui pemasukan kontrakan.
11. **KNF-03:** Keandalan penyimpanan data wajib dijaga agar data yang sudah disimpan tidak hilang.
12. **KNF-04:** Pembatasan akses tanpa login diperlukan untuk melindungi data sistem.

### 5.5 Kebutuhan yang Tidak Dikerjakan (Won't)

| ID | Kebutuhan | Prioritas | Alasan |
|---|---|---|---|
| W-01 | Sistem harus menyediakan integrasi payment gateway untuk menerima pembayaran otomatis. | Won't | Integrasi pembayaran tidak termasuk ruang lingkup utama proyek. |
| W-02 | Sistem harus mengelola keuangan pribadi pemilik kontrakan. | Won't | Tidak berkaitan langsung dengan administrasi penyewaan kontrakan. |
| W-03 | Sistem harus mengelola jadwal pemeliharaan dan renovasi bangunan. | Won't | Pengelolaan pemeliharaan bangunan berada di luar fokus sistem. |
| W-04 | Sistem harus terintegrasi dengan layanan pihak ketiga. | Won't | Integrasi eksternal menambah kompleksitas dan bukan kebutuhan utama proyek. |

**Catatan:** Prioritas MoSCoW merupakan usulan awal proyek berdasarkan ruang lingkup dan perkiraan waktu pengerjaan. Prioritas belum dikonfirmasi oleh klien nyata dan dapat berubah setelah validasi.

## 6. Matriks Ketertelusuran (Traceability Matrix)

Matriks ketertelusuran digunakan untuk menghubungkan setiap User Story dengan kebutuhan fungsional dan nonfungsional yang mendukungnya. Matriks ini memastikan seluruh kebutuhan sistem memiliki sumber yang jelas dan dapat digunakan sebagai dasar penyusunan test case.

| User Story | Kebutuhan Fungsional | Kebutuhan Nonfungsional | Test Case |
|---|---|---|---|
| US-01 | KF-01 | KNF-04 | Belum dibuat |
| US-02 | KF-02, KF-03, KF-04 | KNF-01, KNF-03 | Belum dibuat |
| US-03 | KF-05 | KNF-01, KNF-02 | Belum dibuat |
| US-04 | KF-06 | KNF-01, KNF-04 | Belum dibuat |
| US-05 | KF-07, KF-08 | KNF-03 | Belum dibuat |
| US-06 | KF-09, KF-10 | KNF-03 | Belum dibuat |
| US-07 | KF-11 | KNF-01 | Belum dibuat |
| US-08 | KF-12 | KNF-01 | Belum dibuat |
| US-09 | KF-13 | KNF-03 | Belum dibuat |
| US-10 | KF-14 | KNF-01 | Belum dibuat |
| US-11 | KF-15 | - | Belum dibuat |
| US-12 | KF-16 | - | Belum dibuat |

### 6.1 Pemeriksaan Ketertelusuran

Berdasarkan matriks di atas:

1. Seluruh 12 User Story (US-01 sampai US-12) telah memiliki kebutuhan fungsional yang terkait.
2. Setiap kebutuhan fungsional KF-01 sampai KF-16 telah memiliki sumber User Story.
3. Kebutuhan nonfungsional KNF-01 sampai KNF-04 digunakan untuk mendukung kualitas sistem.
4. Kebutuhan yang berasal dari asumsi tetap harus divalidasi sebelum implementasi.
5. Test case akan disusun pada tahap pengujian sistem berdasarkan kebutuhan dan acceptance criteria masing-masing User Story.

**Catatan:** Matriks ini merupakan rancangan awal berdasarkan simulasi wawancara dan belum divalidasi oleh klien nyata.

## Riwayat Konfirmasi Klien

### Simulasi Konfirmasi Kebutuhan — PT dan BM

**Tanggal:** 11 November 2026
**Metode:** Simulasi wawancara
**Narasumber:** PT dan BM (narasumber fiktif)
**Status:** Data simulasi, bukan hasil konfirmasi klien nyata.

**Ringkasan Tanggapan:**

Berdasarkan skenario simulasi, kedua narasumber menyepakati bahwa aplikasi digunakan oleh pemilik kontrakan. Akun pemilik disiapkan oleh administrator. Nomor kamar harus unik, sedangkan data penyewa mencakup nama lengkap, nomor telepon, dan alamat.

Kedua narasumber menginginkan perubahan status kamar secara otomatis berdasarkan penempatan penyewa dan berakhirnya masa sewa. Sistem pembayaran menggunakan periode bulanan dan mendukung pembayaran bertahap. Status pembayaran perlu dibedakan menjadi lunas, belum lunas, dan terlambat.

Pendapatan dihitung berdasarkan tanggal pembayaran diterima. Informasi masa sewa yang mendekati akhir juga diperlukan.

**Perubahan Kebutuhan:**

1. KF-02: Menambahkan aturan bahwa nomor kamar harus unik.
2. KF-06: Memperjelas informasi penyewa yang dicatat, yaitu nama lengkap, nomor telepon, dan alamat.
3. KF-07: Memperjelas perubahan status kamar berdasarkan penempatan penyewa dan berakhirnya masa sewa.
4. KF-08: Prioritas dinaikkan dari Should menjadi Must karena pencegahan penempatan penyewa ganda dianggap penting.
5. KF-09: Memperjelas bahwa sistem mendukung pencatatan pembayaran bertahap.
6. KF-11: Memperjelas status pembayaran menjadi lunas, belum lunas, dan terlambat.
7. KF-15: Memperjelas bahwa pendapatan dihitung berdasarkan tanggal pembayaran diterima.
8. KF-16: Tetap menjadi Could dan belum wajib dikembangkan.

**Asumsi yang Terjawab dalam Simulasi:**

- Pengguna aplikasi hanya pemilik kontrakan.
- Akun disiapkan oleh administrator.
- Nomor kamar harus unik.
- Data penyewa tidak dihapus jika masih memiliki riwayat.
- Pembayaran dilakukan bulanan dan dapat bertahap.
- Status kamar mengikuti penempatan dan berakhirnya masa sewa.
- Pendapatan dihitung berdasarkan tanggal pembayaran diterima.

**Pertanyaan yang Masih Terbuka:**

- Jangka waktu pengingat sebelum masa sewa berakhir.
- Aturan rinci pembayaran sebagian.
- Pencatatan perubahan transaksi pembayaran.
- Format unduhan laporan.
- Aturan penghapusan kamar yang memiliki riwayat penyewaan.

**Catatan:** Seluruh tanggapan dan perubahan pada bagian ini merupakan hasil simulasi untuk keperluan latihan Jobsheet. Tidak ada konfirmasi atau persetujuan dari klien nyata.