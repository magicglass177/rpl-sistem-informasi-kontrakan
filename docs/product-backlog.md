# Product Backlog
## Sistem Informasi Pengelolaan Kontrakan

**Tujuan Proyek:** Membantu pemilik kontrakan mengelola informasi kamar, data penyewa, pembayaran sewa, periode sewa, dan laporan pendapatan melalui aplikasi web.

**Target Pengguna:** Pemilik kontrakan.

**Dasar Penyusunan:** PRD versi 1.1 dan SRS.

**Catatan:** Product Backlog ini merupakan rancangan berdasarkan kebutuhan yang masih berstatus draft dan belum divalidasi kepada klien nyata. Prioritas dan sprint bersifat tentatif serta dapat ditinjau kembali setelah konfirmasi kebutuhan.

## 1. Product Backlog Berdasarkan MoSCoW

| No. | ID Kebutuhan | Butir Backlog | Prioritas MoSCoW | Sprint Tentatif |
|---:|---|---|---|---:|
| 1 | KF-01 | Menyediakan fitur login untuk pemilik kontrakan menggunakan username dan password. | Must | 1 |
| 2 | KF-02 | Menambahkan data kamar dengan informasi nomor kamar dan harga sewa. | Must | 1 |
| 3 | KF-03 | Menampilkan daftar data kamar yang tersimpan. | Must | 1 |
| 4 | KF-06 | Mengelola informasi data penyewa. | Must | 1 |
| 5 | KNF-03 | Memastikan data yang telah disimpan tetap tersedia setelah halaman dimuat ulang atau pengguna login kembali. | Must | 1 |
| 6 | KNF-04 | Membatasi akses ke halaman pengelolaan bagi pengguna yang belum login. | Must | 1 |
| 7 | KF-05 | Menampilkan status ketersediaan setiap kamar, yaitu tersedia atau terisi. | Must | 2 |
| 8 | KF-07 | Menghubungkan data penyewa dengan kamar yang tersedia. | Must | 2 |
| 9 | KF-09 | Mencatat transaksi pembayaran sewa berdasarkan tanggal dan jumlah pembayaran. | Must | 2 |
| 10 | KF-11 | Menampilkan status pembayaran berdasarkan transaksi yang tercatat. | Must | 2 |
| 11 | KF-13 | Mencatat dan menampilkan periode sewa berdasarkan tanggal mulai dan tanggal berakhir. | Must | 2 |
| 12 | KF-15 | Menampilkan laporan daftar pembayaran dan total pendapatan berdasarkan periode yang dipilih. | Must | 3 |
| 13 | KF-04 | Mengubah informasi data kamar yang sudah tersimpan. | Should | 2 |
| 14 | KF-08 | Mencegah penempatan penyewa lain pada kamar yang sudah ditempati. | Should | 2 |
| 15 | KF-10 | Menampilkan riwayat transaksi pembayaran penyewa. | Should | 3 |
| 16 | KF-12 | Menampilkan tanggal jatuh tempo dan menandai pembayaran yang terlambat. | Should | 3 |
| 17 | KF-14 | Menampilkan informasi periode sewa yang mendekati akhir atau telah berakhir. | Should | 3 |
| 18 | KNF-01 | Memastikan proses penambahan kamar dapat diselesaikan maksimal dalam lima langkah. | Should | 3 |
| 19 | KNF-02 | Memastikan daftar 100 kamar dapat ditampilkan maksimal dalam tiga detik pada kondisi pengujian yang ditentukan. | Should | 3 |

## 2. Rincian Tugas Sprint 1

Tugas Sprint 1 dipecah menjadi pekerjaan kecil. Setiap tugas direncanakan selesai maksimal satu hari kerja.

| No. | ID Kebutuhan | Tugas | Estimasi |
|---:|---|---|---|
| 1 | KF-01 | Menyiapkan struktur data akun berdasarkan atribut akun pada PRD. | 1 hari |
| 2 | KF-01 | Membuat tampilan formulir login dengan input username dan password. | 1 hari |
| 3 | KF-01 | Membuat proses pemeriksaan username dan password terhadap akun terdaftar. | 1 hari |
| 4 | KF-01 | Menampilkan pesan kesalahan ketika kredensial login tidak benar. | 1 hari |
| 5 | KF-02 | Membuat formulir penambahan kamar dengan input nomor kamar dan harga sewa. | 1 hari |
| 6 | KF-02 | Membuat proses penyimpanan data kamar. | 1 hari |
| 7 | KF-02 | Membuat validasi input nomor kamar dan harga sewa. | 1 hari |
| 8 | KF-02 | Menampilkan informasi bahwa data kamar berhasil disimpan. | 1 hari |
| 9 | KF-03 | Membuat proses pengambilan data kamar yang tersimpan. | 1 hari |
| 10 | KF-03 | Membuat tampilan daftar kamar. | 1 hari |
| 11 | KF-03 | Memeriksa kesesuaian data kamar yang ditampilkan dengan data tersimpan. | 1 hari |
| 12 | KF-06 | Membuat tampilan informasi data penyewa. | 1 hari |
| 13 | KF-06 | Membuat formulir perubahan informasi penyewa. | 1 hari |
| 14 | KF-06 | Membuat proses penyimpanan perubahan informasi penyewa. | 1 hari |
| 15 | KF-06 | Memeriksa apakah informasi penyewa terbaru tampil setelah perubahan disimpan. | 1 hari |
| 16 | KNF-03 | Menguji apakah data kamar tetap tersedia setelah halaman dimuat ulang. | 1 hari |
| 17 | KNF-03 | Menguji apakah data yang tersimpan tetap tersedia setelah pengguna login kembali. | 1 hari |
| 18 | KNF-04 | Membuat pembatasan akses ke halaman pengelolaan bagi pengguna yang belum login. | 1 hari |
| 19 | KNF-04 | Menguji penolakan akses ketika pengguna belum login mencoba membuka halaman pengelolaan. | 1 hari |

**Catatan Sprint 1:**
- Rincian tugas merupakan usulan pemecahan pekerjaan, bukan penambahan fitur baru.
- Mekanisme pembuatan akun belum ditetapkan karena masih menjadi pertanyaan terbuka pada PRD.
- Atribut wajib data penyewa juga belum ditentukan. Detail formulir penyewa harus mengikuti keputusan kebutuhan yang telah dikonfirmasi.
- Estimasi satu hari merupakan target perencanaan, bukan jaminan durasi pengerjaan.

## 3. Rencana Sprint

Proyek direncanakan berlangsung selama empat sprint dengan durasi dua minggu untuk setiap sprint.

| Sprint | Fokus Pekerjaan | Target Kebutuhan |
|---:|---|---|
| Sprint 1 | Autentikasi, data kamar, pengelolaan penyewa, dan persyaratan keandalan serta keamanan. | KF-01, KF-02, KF-03, KF-06, KNF-03, KNF-04 |
| Sprint 2 | Ketersediaan kamar, hubungan penyewa dan kamar, pembayaran, status pembayaran, serta periode sewa. | KF-04, KF-05, KF-07, KF-08, KF-09, KF-11, KF-13 |
| Sprint 3 | Laporan pendapatan, riwayat pembayaran, jatuh tempo, informasi akhir masa sewa, dan pengujian kualitas. | KF-10, KF-12, KF-14, KF-15, KNF-01, KNF-02 |
| Sprint 4 | Cadangan untuk penyelesaian, pengujian, perbaikan, dan peninjauan hasil berdasarkan kebutuhan yang telah disetujui. | Tidak menambahkan kebutuhan atau fitur baru tanpa persetujuan |

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