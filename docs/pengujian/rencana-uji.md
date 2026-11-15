# Rencana Pengujian
## Sistem Informasi Pengelolaan Kontrakan

**Versi:** 1.0
**Status:** Rencana Pengujian
**Acuan:** PRD, SRS, skenario use case, dan aturan proyek.

---

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan Sistem Informasi Pengelolaan Kontrakan berjalan sesuai kebutuhan fungsional dan kebutuhan nonfungsional yang telah ditetapkan.

Tujuan pengujian adalah:

1. Memastikan setiap fungsi utama sistem berjalan sesuai kebutuhan pemilik kontrakan.
2. Memastikan sistem dapat menerima data yang valid dan menolak data yang tidak valid.
3. Memastikan data kamar, penyewa, periode sewa, dan pembayaran tersimpan dengan benar.
4. Memastikan hubungan antara penyewa dan kamar tidak menyebabkan penempatan penyewa ganda.
5. Memastikan perhitungan status pembayaran dan laporan pendapatan sesuai data transaksi.
6. Mengidentifikasi kesalahan sistem sebelum aplikasi digunakan oleh pengguna.

## 2. Ruang Lingkup Pengujian

Pengujian difokuskan pada kebutuhan fungsional (KF) berdasarkan prioritas MoSCoW dalam SRS.

### 2.1 Kebutuhan Must

Seluruh kebutuhan Must wajib diuji dan harus lulus sebelum sistem dinyatakan memenuhi kriteria penerimaan utama.

| ID | Kebutuhan yang Diuji | Fokus Pengujian |
|---|---|---|
| KF-01 | Login pemilik kontrakan | Verifikasi username dan password serta penolakan akses jika kredensial salah. |
| KF-02 | Menambahkan data kamar | Penambahan kamar, validasi nomor kamar unik, dan harga sewa. |
| KF-03 | Menampilkan daftar kamar | Memastikan daftar kamar menampilkan data yang telah tersimpan. |
| KF-05 | Menampilkan status kamar | Memastikan status kamar tersedia atau terisi sesuai kondisi penyewaan. |
| KF-06 | Mengelola data penyewa | Penambahan dan perubahan nama lengkap, nomor telepon, serta alamat penyewa. |
| KF-07 | Menghubungkan penyewa dengan kamar | Memastikan hubungan penyewa dan kamar tersimpan serta status kamar diperbarui. |
| KF-08 | Mencegah penempatan penyewa ganda | Memastikan kamar yang masih ditempati tidak dapat ditempati penyewa lain pada periode yang bertumpang tindih. |
| KF-09 | Mencatat pembayaran sewa | Memastikan tanggal dan jumlah pembayaran tersimpan serta mendukung pembayaran bertahap. |
| KF-11 | Menampilkan status pembayaran | Memastikan status lunas, belum lunas, atau terlambat ditampilkan berdasarkan transaksi. |
| KF-13 | Menyimpan periode sewa | Memastikan tanggal mulai dan tanggal berakhir periode sewa tersimpan dengan benar. |
| KF-15 | Menampilkan laporan pendapatan | Memastikan daftar pembayaran dan total pendapatan sesuai periode laporan dan tanggal pembayaran diterima. |

### 2.2 Kebutuhan Should

Kebutuhan Should tetap menjadi cakupan pengujian, tetapi prioritas kelulusannya berada setelah seluruh kebutuhan Must terpenuhi.

| ID | Kebutuhan yang Diuji | Fokus Pengujian |
|---|---|---|
| KF-04 | Mengubah informasi kamar | Memastikan informasi kamar yang telah tersimpan dapat diperbarui. |
| KF-10 | Menampilkan riwayat pembayaran | Memastikan riwayat pembayaran penyewa ditampilkan sesuai transaksi. |
| KF-12 | Menampilkan tanggal jatuh tempo | Memastikan tanggal jatuh tempo ditampilkan sesuai periode sewa dan data yang tersedia. |
| KF-14 | Menampilkan masa sewa berakhir | Memastikan periode yang mendekati tanggal berakhir dan yang telah berakhir dapat ditampilkan. |

### 2.3 Batasan Pengujian

1. KF-16 (mengunduh laporan pendapatan) memiliki prioritas Could sehingga bukan persyaratan kelulusan utama.
2. Integrasi payment gateway dan layanan pihak ketiga tidak termasuk ruang lingkup pengujian.
3. Pengujian dilakukan terhadap aplikasi dan data fiktif.
4. Pengujian tidak menggunakan data pribadi penyewa yang sebenarnya.
5. Pengujian kebutuhan yang masih berupa asumsi harus mencatat hasil dan keterbatasan validasinya.

## 3. Strategi Pengujian

Pengujian menggunakan tiga pendekatan utama.

### 3.1 Pengujian Black-Box Manual

Pengujian black-box dilakukan dengan menjalankan aplikasi melalui antarmuka pengguna tanpa memeriksa implementasi kode secara langsung.

Penguji memberikan masukan dan memeriksa keluaran sistem berdasarkan test case.

Aktivitas pengujian meliputi:

- Menguji login dengan data benar, salah, dan kosong.
- Menguji penambahan kamar dengan nomor unik dan nomor duplikat.
- Menguji penambahan serta perubahan data penyewa.
- Menguji hubungan penyewa dengan kamar.
- Menguji penolakan periode sewa yang bertumpang tindih.
- Menguji pencatatan pembayaran secara bertahap.
- Menguji status pembayaran.
- Menguji laporan pendapatan berdasarkan periode.
- Menguji validasi formulir dan pesan kesalahan.

Setiap test case dicatat dengan hasil aktual dan status Lulus atau Gagal.

### 3.2 Pengujian Otomatis Dasar

Pengujian otomatis digunakan untuk memeriksa logika inti sistem secara berulang dan mengurangi risiko kesalahan.

Strategi yang digunakan:

1. Menggunakan modul `unittest` bawaan Python untuk pengujian otomatis.
2. Menguji validasi data kamar, penyewa, periode sewa, dan pembayaran.
3. Menguji aturan nomor kamar unik.
4. Menguji validasi tanggal dan jumlah pembayaran.
5. Menguji pencegahan periode sewa yang bertumpang tindih.
6. Menguji hubungan antarentitas dan penyimpanan data pada SQLite.
7. Menjalankan kembali pengujian setelah terdapat perubahan kode yang memengaruhi fungsi inti.

Skrip verifikasi skema database yang telah tersedia dapat digunakan sebagai pengujian pendukung, tetapi tidak menggantikan pengujian otomatis terhadap logika aplikasi.

### 3.3 User Acceptance Testing (UAT)

UAT dilakukan untuk mengetahui apakah sistem telah memenuhi kebutuhan pengguna utama, yaitu pemilik kontrakan.

Aktivitas UAT meliputi:

1. Pengguna mencoba login ke aplikasi.
2. Pengguna mencoba mengelola data kamar dan penyewa.
3. Pengguna mencoba menghubungkan penyewa dengan kamar.
4. Pengguna mencoba mencatat pembayaran.
5. Pengguna memeriksa status pembayaran dan laporan pendapatan.
6. Pengguna memberikan penilaian terhadap kemudahan penggunaan dan kesesuaian fungsi.

Hasil UAT dicatat dalam lembar evaluasi dan digunakan sebagai dasar perbaikan sistem.

**Catatan:** UAT dengan klien nyata masih harus dijadwalkan. Narasumber PT dan BM yang digunakan pada tahap simulasi kebutuhan merupakan narasumber fiktif, sehingga simulasi tersebut tidak dianggap sebagai persetujuan UAT dari klien nyata.

## 4. Lingkungan Pengujian

Pengujian direncanakan menggunakan lingkungan lokal pengembangan.

### 4.1 Perangkat Keras

| Perangkat | Keterangan |
|---|---|
| Komputer/Laptop | Perangkat utama untuk menjalankan aplikasi dan pengujian. |
| Smartphone | Perangkat tambahan untuk pemeriksaan tampilan responsif jika tersedia. |

### 4.2 Perangkat Lunak

| Komponen | Teknologi |
|---|---|
| Sistem Operasi | Windows |
| Bahasa Pemrograman | Python 3.14 |
| Framework | Flask |
| Database | SQLite |
| Browser utama | Google Chrome |
| Browser tambahan | Microsoft Edge |
| Pengujian otomatis | `unittest` bawaan Python |
| Pengelolaan kode | Git dan GitHub |

### 4.3 Data Pengujian

Pengujian menggunakan data karangan atau data fiktif, antara lain:

| Jenis Data | Contoh Data |
|---|---|
| Akun pemilik | pemilik_test |
| Nomor kamar | A01, A02, A03 |
| Nama penyewa | Andi Pratama, Budi Santoso |
| Nomor telepon | 081234567890 |
| Alamat | Jalan Melati No. 10 |
| Harga sewa | Rp1.000.000 |
| Tanggal mulai | 2026-11-01 |
| Tanggal berakhir | 2027-10-31 |
| Pembayaran | Rp500.000 dan Rp500.000 |

Data tersebut hanya contoh untuk pengujian dan bukan data pengguna sebenarnya.

### 4.4 Kondisi Pengujian

- Aplikasi dijalankan pada lingkungan lokal.
- Database menggunakan SQLite dengan data pengujian.
- Pengujian dilakukan menggunakan browser yang tersedia.
- Setiap pengujian dimulai dengan kondisi data yang diketahui agar hasil dapat diulang.
- Data pengujian dapat diatur ulang apabila diperlukan untuk skenario berikutnya.

## 5. Kriteria Lulus Pengujian

Sistem dinyatakan memenuhi kriteria pengujian apabila:

1. Seluruh test case untuk kebutuhan Must berhasil dijalankan dan memperoleh hasil Lulus.
2. Tidak terdapat kesalahan kritis yang menghambat fungsi utama sistem.
3. Data yang berhasil disimpan tetap tersedia setelah halaman dimuat ulang atau pengguna masuk kembali.
4. Sistem menolak data yang tidak valid sesuai aturan validasi.
5. Sistem mencegah penempatan penyewa ganda pada kamar dalam periode yang bertumpang tindih.
6. Status pembayaran dan laporan pendapatan menampilkan hasil sesuai data transaksi.
7. Akses ke halaman pengelolaan data ditolak apabila pengguna belum berhasil login.
8. Hasil pengujian Should dicatat dan dievaluasi untuk menentukan tindak lanjut.
9. UAT memperoleh persetujuan dari pemilik kontrakan atau perwakilan pengguna yang berwenang sebelum penerimaan akhir sistem.

Jika terdapat test case Must yang gagal, sistem belum dapat dinyatakan lulus pengujian utama. Kesalahan harus diperbaiki dan test case terkait dijalankan kembali.

## 6. Pembagian Tugas Penguji

Pembagian tanggung jawab pengujian direncanakan sebagai berikut:

| Peran | Tanggung Jawab |
|---|---|
| Pengembang/Penguji Internal | Menyiapkan lingkungan dan data uji, menyusun test case, menjalankan pengujian manual dan otomatis, memperbaiki kesalahan, serta mendokumentasikan hasil. |
| Reviewer/Anggota Tim | Meninjau kelengkapan test case, memeriksa hasil pengujian, dan memberikan masukan terhadap temuan. |
| Pemilik Kontrakan/Klien | Menjalankan UAT, menilai kesesuaian fungsi dengan kebutuhan operasional, dan memberikan persetujuan penerimaan sistem. |

Untuk proyek yang dikerjakan oleh satu pengembang, pengujian internal dapat dilaksanakan oleh pengembang, sedangkan reviewer dan pemilik kontrakan dilibatkan sesuai ketersediaan.

**Catatan:** Pembagian tugas ini merupakan rencana. Nama penguji, jadwal pelaksanaan, dan persetujuan UAT akan dicatat setelah pelaksanaan pengujian.

---

## 7. Referensi

1. `PRD.md` — Product Requirements Document.
2. `docs/srs.md` — Software Requirements Specification.
3. `docs/uml/skenario-use-case.md` — Skenario Use Case.
4. `aturan-proyek.md` — Aturan pengembangan dan pengujian proyek.



## 8. Daftar Test Case

Test case disusun berdasarkan kriteria penerimaan pada PRD versi 1.1, kebutuhan fungsional dalam SRS, prioritas Product Backlog, dan aturan data pada kamus data.

Cakupan pengujian meliputi seluruh kebutuhan fungsional Must, yaitu KF-01, KF-02, KF-03, KF-05, KF-06, KF-07, KF-08, KF-09, KF-11, KF-13, dan KF-15. Pengujian KNF-03 dan KNF-04 juga disertakan sebagai pengujian pendukung karena keduanya merupakan kebutuhan nonfungsional Must.

### 8.1 Tabel Test Case

| ID | KF | Prasyarat/data uji | Langkah | Hasil diharapkan | Teknik |
|---|---|---|---|---|---|
| TC-01 | KF-01 | Akun pemilik terdaftar; username `pemilik_test`; password benar | Buka halaman login, masukkan kredensial benar, lalu klik Login | Sistem menampilkan halaman utama dan pengguna berhasil masuk | Partisi ekuivalen |
| TC-02 | KF-01 | Akun terdaftar, tetapi password yang dimasukkan salah | Masukkan username benar dan password salah, lalu klik Login | Sistem menampilkan pesan kesalahan dan tidak memberikan akses ke halaman utama | Partisi ekuivalen |
| TC-03 | KF-02 | Nomor kamar belum digunakan; harga sewa diuji dengan nilai `0` dan `0,01` | Tambahkan kamar dengan masing-masing nilai harga, lalu simpan | Kedua data kamar berhasil disimpan karena harga sewa minimal yang diizinkan adalah nol | Nilai batas |
| TC-04 | KF-02 | Kamar dengan nomor `A01` sudah tersimpan | Tambahkan kamar baru dengan nomor `A01` | Sistem menolak nomor kamar duplikat dan tidak menyimpan data baru | Partisi ekuivalen |
| TC-05 | KF-02 | Nomor kamar baru; harga sewa `-0,01` | Isi formulir kamar dengan harga negatif, lalu simpan | Sistem menolak harga negatif dan tidak menyimpan kamar | Nilai batas |
| TC-06 | KF-03 | Terdapat kamar `A01`, `A02`, dan `A03` yang telah tersimpan | Buka halaman daftar kamar | Ketiga kamar ditampilkan dengan nomor dan harga sewa sesuai data tersimpan | Partisi ekuivalen |
| TC-07 | KF-05 | Tanggal pengujian 15 November 2026. Kamar A01 memiliki sewa aktif 1–30 November 2026; A02 tidak memiliki sewa aktif | Buka daftar kamar | A01 ditampilkan sebagai terisi dan A02 sebagai tersedia | Partisi ekuivalen |
| TC-08 | KF-06 | Data penyewa Andi sudah tersimpan. Nomor telepon valid: `0812345678` (10 digit), `0812345678901` (13 digit), `+62812345678` (12 karakter), dan `+62812345678901` (15 karakter) | Ubah nama, nomor telepon, dan alamat penyewa menggunakan data valid tersebut, lalu simpan | Perubahan berhasil disimpan dan data terbaru tampil. Keempat nomor telepon pada batas minimum dan maksimum diterima | Nilai batas |
| TC-09 | KF-06 | Data penyewa tersedia; nomor telepon `081234567` (9 digit), `08123456789012` (14 digit), dan `0712345678` (awalan tidak valid) | Ubah nomor telepon menggunakan masing-masing data tidak valid, lalu coba simpan | Sistem menolak ketiga nomor telepon tersebut dan tidak menyimpan perubahan yang tidak valid | Partisi ekuivalen dan nilai batas |
| TC-10 | KF-07 | Penyewa Andi dan kamar A02 tersedia | Pilih penyewa Andi, pilih kamar A02, lalu simpan hubungan sewa | Sistem menyimpan hubungan antara penyewa Andi dan kamar A02 | Partisi ekuivalen |
| TC-11 | KF-08 | Kamar A01 ditempati Andi selama 1–30 November 2026. Periode tersebut masih berlangsung pada tanggal pengujian 15 November 2026 | Coba tempatkan penyewa Budi pada kamar A01 dalam periode yang bertumpang tindih | Sistem menolak penempatan Budi dan tidak menyimpan hubungan sewa yang bertumpang tindih | Partisi ekuivalen |
| TC-12 | KF-09 | Data sewa tersedia dengan kewajiban pembayaran Rp1.000.000 | Catat pembayaran pertama Rp400.000, kemudian catat pembayaran kedua Rp600.000 dengan tanggal pembayaran valid | Kedua transaksi tersimpan sebagai dua catatan pembayaran yang berbeda dan jumlahnya Rp1.000.000 | Partisi ekuivalen |
| TC-13 | KF-09 | Data sewa tersedia; jumlah pembayaran diuji dengan `0`, `-0,01`, dan `0,01` | Masukkan setiap nilai sebagai jumlah pembayaran dan coba simpan | Nilai nol dan negatif ditolak; nilai positif Rp0,01 diterima sesuai batas minimal jumlah pembayaran | Nilai batas |
| TC-14 | KF-11 | Sewa dengan kewajiban Rp1.000.000 dan tanggal jatuh tempo yang belum terlewati; siapkan satu data tanpa pembayaran dan satu data dengan pembayaran penuh | Buka halaman pembayaran dan periksa status kedua penyewa | Sewa tanpa pembayaran ditampilkan belum lunas, sedangkan sewa dengan pembayaran Rp1.000.000 ditampilkan lunas | Partisi ekuivalen |
| TC-15 | KF-13 | Data penyewa dan kamar tersedia; tanggal mulai dan selesai sama-sama 15 November 2026 | Buat periode sewa dengan tanggal mulai dan selesai yang sama, lalu simpan | Sistem menerima periode satu hari karena tanggal selesai tidak lebih awal daripada tanggal mulai | Nilai batas |
| TC-16 | KF-13 | Data penyewa dan kamar tersedia; tanggal mulai 15 November 2026 dan tanggal selesai 14 November 2026 | Masukkan periode tersebut dan coba simpan | Sistem menolak periode sewa karena tanggal selesai lebih awal daripada tanggal mulai | Nilai batas |
| TC-17 | KF-15 | Catatan pembayaran: 31 Oktober Rp100.000, 1 November Rp200.000, 15 November Rp300.000, dan 16 November Rp400.000 | Pilih periode laporan 1–15 November 2026 | Daftar laporan hanya memuat pembayaran tanggal 1 dan 15 November, dengan total pendapatan Rp500.000 | Partisi ekuivalen |
| TC-18 | KNF-03 | Data kamar dan penyewa sudah berhasil disimpan | Muat ulang halaman, kemudian keluar dan login kembali; buka data kamar dan penyewa | Data yang sebelumnya tersimpan tetap tersedia dan nilainya tidak berubah | Partisi ekuivalen |
| TC-19 | KNF-04 | Pengguna belum login | Coba akses langsung URL halaman pengelolaan data | Sistem menolak akses dan mengarahkan pengguna ke halaman login | Partisi ekuivalen |

### 8.2 Hasil Pemeriksaan Test Case

Hasil pemeriksaan draf test case:

1. Seluruh 11 kebutuhan fungsional Must telah memiliki minimal satu test case.
2. Terdapat lebih dari dua kasus tidak valid, termasuk kredensial salah, nomor kamar duplikat, harga negatif, nomor telepon tidak valid, pembayaran tidak valid, dan tanggal sewa yang tidak valid.
3. Terdapat pengujian nilai batas pada harga sewa, jumlah pembayaran, format nomor telepon, serta tanggal mulai dan selesai sewa.
4. Hasil yang diharapkan menggunakan keluaran yang dapat diperiksa, seperti data tersimpan, data ditolak, status kamar, status pembayaran, dan jumlah pendapatan.
5. Tidak terdapat test case untuk fitur Could, integrasi payment gateway, atau fitur lain yang tidak ditetapkan dalam SRS.

### 8.3 Catatan Kesalahan AI dan Perbaikannya

Satu kesalahan AI ditemukan ketika mengidentifikasi prioritas KF-08. PRD versi 1.1 masih menempatkan F-11 (KF-08) pada kelompok Should Have, sedangkan SRS dan Product Backlog telah menetapkan KF-08 sebagai Must.

Kesalahan tersebut diperbaiki dengan mengikuti keputusan prioritas terbaru yang terdokumentasi pada SRS dan Product Backlog. Test case TC-11 kemudian dimasukkan ke cakupan pengujian Must.

### 8.4 Aturan yang Masih Memerlukan Konfirmasi

1. Aturan penentuan status pembayaran terlambat belum ditetapkan secara rinci. Karena itu, pengujian status terlambat belum dapat memiliki hasil yang pasti.
2. Batas maksimal pembayaran dan penanganan kelebihan pembayaran belum diputuskan.
3. Batas inklusif atau eksklusif untuk periode sewa yang bersebelahan perlu dipastikan sebelum membuat pengujian batas khusus untuk KF-08.
4. TC-17 mengasumsikan tanggal awal dan tanggal akhir periode laporan ikut dihitung (inklusif). Asumsi ini perlu dikonfirmasi pada spesifikasi atau implementasi laporan.

Aturan yang belum diputuskan tidak boleh dianggap sebagai ketentuan final atau ditambahkan sebagai constraint tanpa persetujuan.

## 9. Matriks Keterlacakan Pengujian

Matriks ini menghubungkan setiap Kebutuhan Fungsional (KF) dengan Use Case, halaman wireframe, prioritas, dan test case. Pemetaan mengacu pada `docs/srs.md`, `docs/uml/use-case-list.md`, serta dokumen wireframe pada `docs/desain/wireframe/`.

### 9.1 Matriks KF → Use Case → Halaman → Prioritas → Test Case

| KF | Use Case | Halaman Wireframe | Prioritas | Test Case |
|---|---|---|---|---|
| KF-01 | UC-01 | wf-01 Login | Must | TC-01, TC-02 |
| KF-02 | UC-02 | wf-04 Form Kamar | Must | TC-03, TC-04, TC-05 |
| KF-03 | UC-03 | wf-03 Daftar Kamar | Must | TC-06 |
| KF-04 | UC-04 | wf-04 Form Kamar | Should | Belum dibuat (Should) |
| KF-05 | UC-05 | wf-03 Daftar Kamar | Must | TC-07 |
| KF-06 | UC-06, UC-07 | wf-05 Daftar Penyewa; wf-06 Form Penyewa | Must | TC-08, TC-09 |
| KF-07 | UC-08 | wf-08 Form Periode Sewa | Must | TC-10 |
| KF-08 | UC-08 | wf-08 Form Periode Sewa | Must | TC-11 |
| KF-09 | UC-09 | wf-10 Form Catat Pembayaran | Must | TC-12, TC-13 |
| KF-10 | UC-11 | wf-09 Daftar Pembayaran | Should | Belum dibuat (Should) |
| KF-11 | UC-10 | wf-09 Daftar Pembayaran | Must | TC-14 |
| KF-12 | UC-13 | wf-07 Daftar Periode Sewa | Should | Belum dibuat (Should) |
| KF-13 | UC-12 | wf-07 Daftar Periode Sewa; wf-08 Form Periode Sewa | Must | TC-15, TC-16 |
| KF-14 | UC-14 | wf-07 Daftar Periode Sewa | Should | Belum dibuat (Should) |
| KF-15 | UC-15 | wf-11 Laporan Pendapatan | Must | TC-17 |

### 9.2 Keterlacakan Pengujian Nonfungsional

TC-18 dan TC-19 menguji kebutuhan nonfungsional, sehingga dicatat terpisah dari matriks KF.

| Kebutuhan | Use Case terkait | Halaman Wireframe terkait | Prioritas | Test Case |
|---|---|---|---|---|
| KNF-03 | UC-02, UC-06, UC-07 | wf-03 Daftar Kamar, wf-05 Daftar Penyewa, wf-06 Form Penyewa | Must | TC-18 |
| KNF-04 | UC-01 | wf-01 Login | Must | TC-19 |

### 9.3 Pemeriksaan Keterlacakan

1. Seluruh 15 KF dengan prioritas Must dan Should telah dicantumkan dalam matriks.
2. Seluruh 11 KF Must memiliki minimal satu test case.
3. Empat KF Should dicantumkan, tetapi belum memiliki test case karena belum termasuk cakupan penyusunan test case pada Langkah 8.
4. Setiap test case TC-01 sampai TC-17 pada matriks KF memiliki keterkaitan dengan KF yang sesuai.
5. TC-18 dan TC-19 dicatat secara terpisah karena menguji KNF-03 dan KNF-04, bukan kebutuhan fungsional.
6. KF-16 dengan prioritas Could dan UC-16 tidak dimasukkan ke matriks pengujian wajib.
7. KF-08 tetap menggunakan prioritas Must sesuai keputusan terbaru pada SRS dan Product Backlog.

### 9.4 Catatan

Pemetaan halaman menunjukkan halaman wireframe yang mendukung aktivitas Use Case, bukan klaim bahwa seluruh fungsi telah diimplementasikan. Test case yang berstatus belum dibuat harus disusun dan dieksekusi pada tahap pengujian berikutnya sesuai prioritas proyek.
