# Anotasi Wireframe
## Sistem Informasi Pengelolaan Kontrakan

**Dokumen:** Anotasi dan Penerapan Prinsip Antarmuka
**Lokasi:** `docs/desain/wireframe/anotasi.md`
**Aktor utama:** Pemilik Kontrakan
**Jumlah halaman:** 11 halaman

## 1. Tujuan

Dokumen ini menjelaskan elemen penting pada setiap wireframe, data atau aksi yang dilakukan, aturan validasi, pesan sistem, serta prinsip antarmuka yang diterapkan.

Nomor anotasi pada gambar dimulai kembali dari 01 untuk setiap halaman.

## 2. Tabel Anotasi

### WF-01 — Login

| No. | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 01 | Username | Memasukkan nama akun | Wajib diisi. Pesan: Lengkapi username. | Pencegahan galat |
| 02 | Password | Memasukkan kata sandi | Wajib diisi dan karakter disamarkan. | Pencegahan galat |
| 03 | Tombol Login | Mengirim kredensial untuk diperiksa | Jika benar, masuk ke Dashboard. Jika salah: Username atau password salah. | Umpan balik |

### WF-02 — Dashboard

| No. | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 01 | Ringkasan kontrakan | Melihat total kamar, kamar tersedia, kamar terisi, dan pendapatan | Angka ditampilkan sebagai ringkasan informasi. | Keterbacaan |
| 02 | Ringkasan pembayaran | Melihat jumlah pembayaran lunas, belum lunas, dan terlambat | Informasi dihitung berdasarkan catatan pembayaran. | Konsistensi |
| 03 | Periode sewa mendekati akhir | Melihat kamar dan tanggal berakhir sewa | Tampilkan periode yang perlu diperhatikan. | Umpan balik |
| 04 | Pesan informasi | Membaca pemberitahuan sistem | Pesan: Terdapat periode sewa yang mendekati tanggal berakhir. | Umpan balik |

### WF-03 — Daftar Kamar

| No. | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 01 | Tombol Tambah Kamar | Membuka Form Kamar | Menggunakan label aksi yang konsisten. | Konsistensi |
| 02 | Pencarian kamar | Memasukkan nomor kamar dan menjalankan pencarian | Hasil pencarian sesuai kata kunci. | Keterbacaan |
| 03 | Tabel kamar | Melihat nomor kamar, harga sewa, dan ketersediaan | Status ketersediaan dihitung berdasarkan periode sewa. | Konsistensi |
| 04 | Tombol Edit | Membuka data kamar untuk diubah | Data yang dipilih harus sesuai baris. | Pencegahan galat |
| 05 | Area pesan | Menampilkan hasil pengelolaan kamar | Berhasil: Data kamar tersimpan. Gagal: Nomor kamar sudah digunakan, data wajib belum lengkap, atau data tidak valid. | Umpan balik |

### WF-04 — Form Kamar

| No. | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 01 | Nomor Kamar | Memasukkan identitas nomor kamar | Wajib diisi dan harus unik. Pesan: Nomor kamar sudah digunakan. | Pencegahan galat |
| 02 | Harga Sewa | Memasukkan harga sewa kamar | Wajib angka lebih dari 0. | Pencegahan galat |
| 03 | Pesan validasi | Membaca kesalahan input | Pesan: Lengkapi data wajib / Nomor kamar sudah digunakan / Harga sewa tidak valid. | Umpan balik |
| 04 | Simpan dan Batal | Menyimpan atau membatalkan formulir | Simpan hanya jika data valid. Batal tidak menyimpan perubahan. | Konsistensi |

### WF-05 — Daftar Penyewa

| No. | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 01 | Tombol Tambah Penyewa | Membuka Form Penyewa | Label dan gaya tombol mengikuti halaman daftar lainnya. | Konsistensi |
| 02 | Pencarian penyewa | Mencari berdasarkan nama penyewa | Hasil pencarian sesuai kata kunci. | Keterbacaan |
| 03 | Tabel penyewa | Melihat nama, nomor telepon, dan alamat | Informasi ditampilkan dalam kolom berlabel jelas. | Keterbacaan |
| 04 | Tombol Edit | Membuka data penyewa yang dipilih | Perubahan mengacu pada baris yang benar. | Pencegahan galat |
| 05 | Area pesan | Menampilkan hasil pengelolaan penyewa | Berhasil: Data penyewa berhasil disimpan. Gagal: Data wajib belum lengkap, format tidak valid, atau penyimpanan gagal. | Umpan balik |

### WF-06 — Form Penyewa

| No. | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 01 | Nama Penyewa | Memasukkan nama lengkap | Wajib diisi. | Pencegahan galat |
| 02 | Nomor Telepon | Memasukkan nomor telepon | Wajib diisi dan menggunakan format angka yang benar. | Pencegahan galat |
| 03 | Alamat | Memasukkan alamat penyewa | Wajib diisi. | Pencegahan galat |
| 04 | Pesan validasi | Membaca kesalahan formulir | Pesan: Lengkapi data wajib / Format nomor telepon tidak valid / Data belum berhasil disimpan. | Umpan balik |
| 05 | Simpan dan Batal | Menyimpan atau membatalkan data | Simpan setelah validasi berhasil. Batal kembali tanpa menyimpan. | Konsistensi |

### WF-07 — Daftar Periode Sewa

| No. | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 01 | Tambah Periode Sewa | Membuka Form Periode Sewa | Tombol menggunakan pola yang sama dengan halaman daftar lain. | Konsistensi |
| 02 | Pencarian | Mencari penyewa atau kamar | Pencarian menggunakan kata kunci. | Keterbacaan |
| 03 | Tabel periode sewa | Melihat penyewa, kamar, tanggal mulai, tanggal selesai, jatuh tempo, dan harga | Kolom memiliki judul yang jelas. | Keterbacaan |
| 04 | Status periode | Melihat status periode sewa | Status ditentukan berdasarkan tanggal periode sewa. | Konsistensi |
| 05 | Area pesan | Membaca informasi pengelolaan periode | Pesan: Data penyewa atau kamar tidak ditemukan. | Umpan balik |

### WF-08 — Form Periode Sewa

| No. | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 01 | Pilihan Penyewa | Memilih penyewa | Harus memilih penyewa yang tersedia. | Pencegahan galat |
| 02 | Pilihan Kamar | Memilih kamar | Kamar harus tersedia untuk rentang periode yang dipilih. | Pencegahan galat |
| 03 | Tanggal Mulai dan Selesai | Menentukan rentang sewa | Keduanya wajib diisi. Tanggal selesai harus setelah tanggal mulai. | Pencegahan galat |
| 04 | Tanggal Jatuh Tempo | Menentukan tanggal jatuh tempo pembayaran | Opsional sesuai kebutuhan periode sewa. | Keterbacaan |
| 05 | Harga Sewa Disepakati | Memasukkan nominal sewa | Wajib berupa angka lebih dari 0. | Pencegahan galat |
| 06 | Pesan validasi | Menampilkan kesalahan periode sewa | Pesan: Lengkapi tanggal mulai dan tanggal berakhir. / Tanggal periode sewa tidak valid. Periksa kembali tanggal yang dipilih. / Kamar masih ditempati pada periode tersebut. Silakan pilih kamar lain. / Gagal menyimpan periode sewa. Kamar sudah memiliki periode sewa lain yang bertumpang tindih dengan tanggal yang dipilih. / Data penyewa atau kamar tidak ditemukan. Muat ulang data dan coba kembali. / Periode sewa belum berhasil disimpan. Silakan coba kembali. | Umpan balik |
| 07 | Simpan dan Batal | Menyimpan atau membatalkan periode sewa | Simpan hanya jika seluruh validasi berhasil. | Konsistensi |

### WF-09 — Daftar Pembayaran

| No. | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 01 | Catat Pembayaran | Membuka Form Catat Pembayaran | Tombol mengikuti pola halaman daftar lainnya. | Konsistensi |
| 02 | Pencarian pembayaran | Mencari berdasarkan nama penyewa atau kamar | Hasil sesuai kata kunci. | Keterbacaan |
| 03 | Tabel pembayaran | Melihat penyewa, kamar, tanggal, jumlah, dan status pembayaran | Pembayaran bertahap ditampilkan sebagai transaksi terpisah. | Konsistensi |
| 04 | Area pesan | Menampilkan informasi transaksi | Pesan: Pembayaran berhasil dicatat atau pencatatan pembayaran belum berhasil. | Umpan balik |

### WF-10 — Form Catat Pembayaran

| No. | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 01 | Periode Sewa | Memilih periode sewa yang dibayar | Wajib dipilih dari data yang tersedia. | Pencegahan galat |
| 02 | Tanggal Pembayaran | Memasukkan tanggal penerimaan uang | Wajib diisi dengan tanggal valid. | Pencegahan galat |
| 03 | Jumlah Bayar | Memasukkan nominal uang yang diterima | Wajib berupa angka lebih dari 0. Pembayaran bertahap diperbolehkan. | Pencegahan galat |
| 04 | Pesan validasi | Menampilkan kesalahan input atau penyimpanan | Pesan: Lengkapi tanggal atau jumlah / Jumlah pembayaran tidak valid / Pencatatan pembayaran belum berhasil. | Umpan balik |
| 05 | Simpan Pembayaran dan Batal | Menyimpan atau membatalkan transaksi | Setiap pembayaran disimpan sebagai catatan terpisah. | Konsistensi |

### WF-11 — Laporan Pendapatan

| No. | Elemen | Data / Aksi | Aturan / Pesan | Prinsip |
|---|---|---|---|---|
| 01 | Filter tanggal | Memasukkan tanggal mulai dan selesai | Kedua tanggal wajib diisi; rentang harus valid. | Pencegahan galat |
| 02 | Tampilkan Laporan | Menjalankan filter pendapatan | Hasil mengikuti rentang tanggal pembayaran. | Umpan balik |
| 03 | Rincian pendapatan | Melihat tanggal dan jumlah pembayaran | Hanya pembayaran dalam rentang terpilih yang ditampilkan. | Keterbacaan |
| 04 | Total Pendapatan | Melihat akumulasi pendapatan | Total merupakan penjumlahan transaksi pada hasil filter. | Keterbacaan |
| 05 | Unduh Laporan | Mengunduh hasil laporan | Laporan mengikuti filter yang sedang digunakan. | Konsistensi |
| 06 | Area pesan | Membaca hasil filter atau kesalahan | Pesan: Laporan berhasil ditampilkan / Tanggal wajib diisi / Rentang tanggal tidak valid. | Umpan balik |

## 3. Pemeriksaan Prinsip Antarmuka

| Prinsip | Penerapan pada wireframe | Hasil pemeriksaan |
|---|---|---|
| Konsistensi | Header, navigasi, istilah menu, tombol, dan pola formulir digunakan secara seragam. | Diterapkan |
| Umpan balik | Area pesan tersedia untuk hasil tindakan, kesalahan validasi, dan informasi sistem. | Diperjelas |
| Keterbacaan | Judul, label, kolom tabel, dan istilah menggunakan bahasa Indonesia yang jelas. | Diterapkan |
| Pencegahan galat | Formulir menggunakan tipe input sesuai data, pilihan dari data tersedia, dan aturan validasi. | Diperjelas |

## 4. Pencatatan Sebelum–Sesudah

### Contoh: Form Catat Pembayaran (WF-10)

**Sebelum:**
- Pesan validasi masih berupa keterangan umum.
- Belum membedakan data kosong, jumlah tidak valid, dan kegagalan penyimpanan.
- Aturan pembayaran bertahap belum dijelaskan pada anotasi.

**Sesudah:**
- Periode sewa dan tanggal pembayaran dinyatakan wajib diisi.
- Jumlah pembayaran harus berupa angka lebih dari 0.
- Pembayaran bertahap diperbolehkan dan dicatat sebagai transaksi terpisah.
- Pesan kesalahan dibedakan menjadi data wajib belum lengkap, jumlah pembayaran tidak valid, dan pencatatan pembayaran belum berhasil.

**Prinsip yang diterapkan:** pencegahan galat dan umpan balik.

## 5. Catatan Verifikasi Use Case

| Use Case | Pengecualian yang harus terlihat |
|---|---|
| UC-01 Login | Kredensial salah dan data login belum lengkap. |
| UC-02 Menambahkan Data Kamar | Nomor kamar duplikat, data wajib kosong, dan data tidak valid. |
| UC-06 Menambahkan Data Penyewa | Data wajib kosong, format data tidak valid, dan penyimpanan gagal. |
| UC-08 Menghubungkan Penyewa dengan Kamar | Kamar masih ditempati, periode sewa bertumpang tindih, serta data penyewa atau kamar tidak ditemukan. |
| UC-09 Mencatat Pembayaran Sewa | Tanggal atau jumlah kosong, jumlah tidak valid, dan penyimpanan gagal. |
| UC-12 Mengelola Periode Sewa | Tanggal kosong, tanggal tidak valid, dan penyimpanan gagal. |

**Catatan:** Pesan pada wireframe merupakan contoh umpan balik antarmuka untuk setiap pengecualian. Implementasi final harus menggunakan validasi dan kondisi yang sesuai dengan kebutuhan sistem.

---

## 6. Matriks Pesan Validasi Use Case

Pesan berikut merupakan contoh umpan balik yang ditampilkan pada kondisi
validasi atau kegagalan sesuai skenario use case. Pesan dapat ditampilkan
sebagai variasi keadaan antarmuka, bukan seluruhnya secara bersamaan.

| Use Case | Halaman | Kondisi | Pesan pada antarmuka |
|---|---|---|---|
| UC-01 Login | WF-01 | Kredensial salah | Username atau password tidak sesuai. |
| UC-01 Login | WF-01 | Isian login kosong | Lengkapi username dan password. |
| UC-02 Menambahkan Data Kamar | WF-04 | Nomor kamar duplikat | Nomor kamar sudah digunakan. Gunakan nomor kamar lain. |
| UC-02 Menambahkan Data Kamar | WF-04 | Data wajib kosong | Lengkapi semua data wajib. |
| UC-02 Menambahkan Data Kamar | WF-04 | Data tidak valid | Data kamar tidak valid. Periksa kembali isian Anda. |
| UC-06 Menambahkan Data Penyewa | WF-06 | Data wajib kosong | Lengkapi semua data wajib. |
| UC-06 Menambahkan Data Penyewa | WF-06 | Format data salah | Format data tidak valid. Periksa kembali nama atau nomor telepon. |
| UC-06 Menambahkan Data Penyewa | WF-06 | Penyimpanan gagal | Data penyewa belum berhasil disimpan. Silakan coba kembali. |
| UC-08 Menghubungkan Penyewa dengan Kamar | WF-08 | Kamar masih ditempati | Kamar masih ditempati pada periode tersebut. Silakan pilih kamar lain. |
| UC-08 Menghubungkan Penyewa dengan Kamar | WF-08 | Data tidak ditemukan | Data penyewa atau kamar tidak ditemukan. Muat ulang data dan coba kembali. |
| UC-08 Menghubungkan Penyewa dengan Kamar | WF-08 | Periode sewa bertumpang tindih | Gagal menyimpan periode sewa. Kamar sudah memiliki periode sewa lain yang bertumpang tindih dengan tanggal yang dipilih. |
| UC-09 Mencatat Pembayaran Sewa | WF-10 | Tanggal atau jumlah kosong | Lengkapi tanggal dan jumlah pembayaran. |
| UC-09 Mencatat Pembayaran Sewa | WF-10 | Jumlah tidak valid | Jumlah pembayaran tidak valid. Masukkan angka lebih dari 0. |
| UC-09 Mencatat Pembayaran Sewa | WF-10 | Penyimpanan gagal | Pembayaran belum berhasil dicatat. Silakan coba kembali. |
| UC-12 Mengelola Periode Sewa | WF-08 | Tanggal mulai atau selesai kosong | Lengkapi tanggal mulai dan tanggal berakhir. |
| UC-12 Mengelola Periode Sewa | WF-08 | Tanggal tidak valid | Tanggal periode sewa tidak valid. Periksa kembali tanggal yang dipilih. |
| UC-12 Mengelola Periode Sewa | WF-08 | Penyimpanan gagal | Periode sewa belum berhasil disimpan. Silakan coba kembali. |

