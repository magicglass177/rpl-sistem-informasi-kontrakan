# Product Backlog
## Sistem Informasi Pengelolaan Kontrakan

**Tujuan Proyek:** Membantu pemilik kontrakan mengelola informasi kamar, data penyewa, pembayaran sewa, periode sewa, dan laporan pendapatan melalui aplikasi web.

**Target Pengguna:** Pemilik kontrakan.

**Dasar Penyusunan:** PRD versi 1.1 dan SRS.

**Catatan:** Product Backlog ini merupakan rancangan berdasarkan kebutuhan yang masih berstatus draft dan belum divalidasi kepada klien nyata. Prioritas dan sprint bersifat tentatif serta dapat ditinjau kembali setelah konfirmasi kebutuhan.

## 1. Product Backlog Berdasarkan MoSCoW

| No. | ID Kebutuhan | Butir Backlog | Prioritas MoSCoW | Sprint Tentatif |
|---:|---|---|---|---:|
| 1 | KF-01 | Menyediakan fitur login untuk pemilik kontrakan menggunakan username dan password. Akun pemilik disiapkan oleh administrator. | Must | 1 |
| 2 | KF-02 | Menambahkan data kamar berdasarkan nomor kamar yang unik dan harga sewa. | Must | 1 |
| 3 | KF-03 | Menampilkan daftar data kamar yang telah tersimpan. | Must | 1 |
| 4 | KF-06 | Menambahkan dan mengubah data penyewa yang mencakup nama lengkap, nomor telepon, dan alamat. | Must | 1 |
| 5 | KNF-03 | Memastikan seluruh data yang berhasil disimpan tetap tersedia setelah pengguna memuat ulang halaman atau login kembali. | Must | 1 |
| 6 | KNF-04 | Membatasi akses ke halaman pengelolaan data bagi pengguna yang belum berhasil login. | Must | 1 |
| 7 | KF-05 | Menampilkan status setiap kamar sebagai tersedia atau terisi berdasarkan kondisi penempatan penyewa dan masa sewa. | Must | 2 |
| 8 | KF-07 | Menghubungkan data penyewa dengan kamar yang ditempatinya serta memperbarui status kamar berdasarkan penempatan penyewa dan berakhirnya masa sewa. | Must | 2 |
| 9 | KF-08 | Mencegah penempatan penyewa baru pada kamar yang masih ditempati penyewa lain. | Must | 2 |
| 10 | KF-09 | Mencatat tanggal dan jumlah setiap pembayaran sewa serta mendukung pencatatan pembayaran secara bertahap. | Must | 2 |
| 11 | KF-11 | Menampilkan status pembayaran penyewa berdasarkan transaksi yang tercatat, yaitu lunas, belum lunas, atau terlambat. | Must | 2 |
| 12 | KF-13 | Mencatat dan menampilkan periode sewa berdasarkan tanggal mulai dan tanggal berakhir. | Must | 2 |
| 13 | KF-04 | Mengubah informasi kamar yang sudah tersimpan. | Should | 2 |
| 14 | KF-10 | Menampilkan riwayat transaksi pembayaran setiap penyewa. | Should | 3 |
| 15 | KF-12 | Menampilkan tanggal jatuh tempo pembayaran sewa untuk setiap periode sewa. | Should | 3 |
| 16 | KF-14 | Menampilkan periode sewa yang mendekati tanggal berakhir dan periode yang telah berakhir. | Should | 3 |
| 17 | KNF-01 | Memastikan proses penambahan data kamar dapat diselesaikan maksimal dalam lima langkah setelah pengguna berhasil login. | Should | 3 |
| 18 | KNF-02 | Memastikan halaman daftar kamar dapat ditampilkan maksimal dalam tiga detik pada kondisi pengujian dengan 100 data kamar. | Should | 3 |
| 19 | KF-15 | Menampilkan daftar pembayaran dan total pendapatan berdasarkan periode laporan yang dipilih, dengan perhitungan berdasarkan tanggal pembayaran diterima. | Must | 3 |

## 2. Rincian Tugas Sprint 1

Tugas Sprint 1 dipecah menjadi pekerjaan kecil. Setiap tugas direncanakan selesai maksimal satu hari kerja.

| No. | ID Kebutuhan | Tugas | Estimasi |
|---:|---|---|---|
| 1 | KF-01 | Menyiapkan struktur data akun pemilik berdasarkan atribut akun pada PRD. | 1 hari |
| 2 | KF-01 | Menyiapkan akun pemilik yang telah disediakan administrator agar dapat digunakan untuk login. | 1 hari |
| 3 | KF-01 | Membuat tampilan formulir login dengan input username dan password. | 1 hari |
| 4 | KF-01 | Membuat proses pemeriksaan username dan password terhadap akun terdaftar. | 1 hari |
| 5 | KF-01 | Menampilkan pesan kesalahan ketika kredensial login tidak benar. | 1 hari |
| 6 | KF-02 | Membuat formulir penambahan kamar dengan input nomor kamar dan harga sewa. | 1 hari |
| 7 | KF-02 | Membuat proses penyimpanan data kamar. | 1 hari |
| 8 | KF-02 | Membuat validasi input nomor kamar dan harga sewa. | 1 hari |
| 9 | KF-02 | Memastikan nomor kamar yang dimasukkan belum digunakan oleh kamar lain. | 1 hari |
| 10 | KF-02 | Menampilkan informasi bahwa data kamar berhasil disimpan. | 1 hari |
| 11 | KF-03 | Membuat proses pengambilan data kamar yang tersimpan. | 1 hari |
| 12 | KF-03 | Membuat tampilan daftar kamar. | 1 hari |
| 13 | KF-03 | Memeriksa kesesuaian data kamar yang ditampilkan dengan data tersimpan. | 1 hari |
| 14 | KF-06 | Membuat formulir penambahan data penyewa dengan input nama lengkap, nomor telepon, dan alamat. | 1 hari |
| 15 | KF-06 | Membuat proses penyimpanan data penyewa baru. | 1 hari |
| 16 | KF-06 | Membuat validasi input nama lengkap, nomor telepon, dan alamat penyewa. | 1 hari |
| 17 | KF-06 | Membuat tampilan informasi data penyewa yang telah tersimpan. | 1 hari |
| 18 | KF-06 | Membuat formulir perubahan informasi data penyewa. | 1 hari |
| 19 | KF-06 | Membuat proses penyimpanan perubahan informasi data penyewa. | 1 hari |
| 20 | KF-06 | Memeriksa apakah informasi penyewa terbaru tampil setelah perubahan disimpan. | 1 hari |
| 21 | KNF-03 | Menguji apakah data kamar dan penyewa tetap tersedia setelah halaman dimuat ulang. | 1 hari |
| 22 | KNF-03 | Menguji apakah data yang tersimpan tetap tersedia setelah pengguna login kembali. | 1 hari |
| 23 | KNF-04 | Membuat pembatasan akses ke halaman pengelolaan data bagi pengguna yang belum login. | 1 hari |
| 24 | KNF-04 | Menguji penolakan akses ketika pengguna belum login mencoba membuka halaman pengelolaan data. | 1 hari |

**Catatan Sprint 1:**
- Rincian tugas merupakan usulan pemecahan pekerjaan, bukan penambahan kebutuhan baru.
- Akun pemilik disiapkan oleh administrator sesuai kebutuhan KF-01. Mekanisme teknis penyiapan akun mengikuti keputusan implementasi.
- Data penyewa mencakup nama lengkap, nomor telepon, dan alamat sesuai kebutuhan KF-06.
- Setiap tugas memiliki estimasi target maksimal satu hari kerja. Estimasi tersebut merupakan target perencanaan, bukan jaminan durasi pengerjaan.

## 3. Rencana Sprint

Proyek direncanakan berlangsung selama empat sprint dengan durasi dua minggu untuk setiap sprint.

| Sprint | Fokus Pekerjaan | Target Kebutuhan |
|---:|---|---|
| Sprint 1 | Autentikasi pemilik, penambahan dan penampilan data kamar, pengelolaan data penyewa, serta pengujian keandalan penyimpanan dan keamanan akses. | KF-01, KF-02, KF-03, KF-06, KNF-03, KNF-04 |
| Sprint 2 | Pengubahan informasi kamar, pengelolaan ketersediaan kamar, hubungan penyewa dan kamar, pencegahan penempatan ganda, pencatatan pembayaran bertahap, status pembayaran, dan periode sewa. | KF-04, KF-05, KF-07, KF-08, KF-09, KF-11, KF-13 |
| Sprint 3 | Riwayat pembayaran, tanggal jatuh tempo, informasi akhir masa sewa, laporan pendapatan, serta pengujian kualitas usability dan performance. | KF-10, KF-12, KF-14, KF-15, KNF-01, KNF-02 |
| Sprint 4 | Cadangan untuk penyelesaian pekerjaan, pengujian, perbaikan, dan peninjauan hasil berdasarkan kebutuhan yang telah disetujui. | Tidak menambahkan kebutuhan atau fitur baru tanpa persetujuan |

## 4. Kebutuhan di Luar Prioritas Must dan Should

| ID Kebutuhan | Butir Kebutuhan | Prioritas | Keterangan |
|---|---|---|---|
| KF-16 | Mengunduh laporan pendapatan. | Could | Belum dijadwalkan pada Sprint 1–3. |

Kebutuhan berprioritas Won't yang tercantum pada PRD tidak dimasukkan sebagai pekerjaan pengembangan dalam backlog ini.

## 5. Catatan Pengembangan

1. Setiap butir backlog harus dapat ditelusuri ke ID kebutuhan dalam SRS dan PRD.
2. Prioritas menggunakan metode MoSCoW, yaitu Must, Should, Could, dan Won't.
3. Sprint tentatif dapat berubah berdasarkan hasil evaluasi kapasitas dan ketergantungan pekerjaan.
4. Tugas Sprint 1 dirancang agar setiap tugas dapat diselesaikan maksimal dalam satu hari kerja.
5. Pertanyaan terbuka pada PRD harus dikonfirmasi sebelum keputusan implementasi yang bergantung padanya dibuat.
6. Saran AI yang tidak memiliki dasar dalam PRD tidak dimasukkan ke backlog.
7. Setiap perubahan backlog perlu ditinjau dan dicatat dalam Jurnal Vibe Coding.

**Kesimpulan:**

Product Backlog ini diperbarui berdasarkan PRD versi 1.1 dengan pemetaan ID kebutuhan, prioritas MoSCoW, dan rencana sprint tentatif. Rincian Sprint 1 telah dipecah menjadi tugas-tugas kecil dengan estimasi maksimal satu hari kerja per tugas. Backlog tetap berstatus rancangan sampai kebutuhan dikonfirmasi oleh pihak terkait.