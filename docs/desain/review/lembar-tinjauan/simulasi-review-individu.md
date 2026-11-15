# Lembar Tinjauan Design Review
## Simulasi Design Review Individu

### 1. Identitas Kegiatan

- Nama proyek: Sistem Informasi Pengelolaan Kontrakan
- Jenis kegiatan: Simulasi design review individu
- Pelaksana: Pengembang proyek
- Reviewer: Simulasi reviewer independen (AI)
- Tanggal: 15 November 2026
- Metode: Tinjauan berdasarkan dokumen kebutuhan, wireframe, anotasi, dan rencana pengujian.

Catatan: Kegiatan ini merupakan simulasi untuk melengkapi dokumentasi Jobsheet. Bukan hasil presentasi atau tinjauan silang antarkelompok yang benar-benar dilaksanakan.

### 2. Kelebihan Desain

**Kelebihan 1: Konsistensi antarmuka**

Rancangan telah mencakup 11 halaman wireframe dengan pola tampilan yang konsisten. Hal ini membantu pengguna memahami navigasi dan fungsi setiap halaman.

### 3. Saran dan Temuan Reviewer

**Saran 1: Memperjelas informasi pembayaran**

Pada halaman pencatatan pembayaran, informasi harga sewa yang disepakati, total pembayaran yang sudah diterima, dan sisa kewajiban sebaiknya ditampilkan secara terpisah.

Alasan:

Satu periode sewa dapat memiliki beberapa catatan pembayaran. Pemisahan informasi tersebut membantu pengguna mengetahui jumlah yang sudah dibayar dan sisa kewajiban penyewa.

**Saran 2: Memperjelas validasi periode sewa**

Ketika pengguna memasukkan periode sewa yang bertumpang tindih dengan periode lain pada kamar yang sama, sistem perlu memberikan pesan kesalahan yang jelas.

Alasan:

Pengguna perlu mengetahui penyebab kegagalan penyimpanan agar dapat memperbaiki tanggal periode sewa yang dimasukkan.

### 4. Pertanyaan Reviewer

Bagaimana sistem menentukan status pembayaran apabila penyewa membayar secara bertahap, tetapi jumlah pembayaran yang diterima belum memenuhi seluruh harga sewa yang disepakati?

### 5. Evaluasi dan Keputusan terhadap Masukan

**5.1. Evaluasi Saran 1 — Diterima**

Saran diterima dan ditindaklanjuti dengan memperbarui anotasi halaman WF-10 — Form Catat Pembayaran.

Tiga informasi yang ditambahkan:
1. Harga Sewa Disepakati.
2. Total Pembayaran Diterima.
3. Sisa Pembayaran.

Ketiga informasi tersebut merupakan informasi baca-saja yang diperoleh dari data periode sewa dan catatan pembayaran. Tidak diperlukan penambahan kolom database untuk ketiga informasi tersebut.

Catatan: Penanganan kelebihan pembayaran belum ditetapkan dan masih memerlukan keputusan lebih lanjut.

**5.2. Evaluasi Saran 2 — Sudah Tercakup**

Saran tidak memerlukan perubahan tambahan karena kebutuhan validasi periode sewa yang bertumpang tindih sudah tercakup dalam rancangan.

Bukti yang mendukung:
- Anotasi WF-08 sudah mencantumkan pesan kesalahan ketika periode sewa bertumpang tindih.
- Test case TC-11 sudah menguji penolakan periode sewa yang bertumpang tindih pada kamar yang sama.

**5.3. Jawaban Pertanyaan Reviewer**

Status pembayaran ditentukan dengan membandingkan total kewajiban sewa dengan akumulasi seluruh pembayaran yang tercatat untuk periode sewa tersebut.

Gambaran status berdasarkan rancangan:
- Belum Dibayar: belum terdapat pembayaran yang tercatat.
- Belum Lunas: sudah terdapat pembayaran, tetapi jumlahnya belum memenuhi kewajiban sewa.
- Lunas: jumlah pembayaran telah memenuhi kewajiban sewa.

Pembayaran bertahap dicatat sebagai transaksi terpisah. Akumulasi pembayaran dihitung dari seluruh transaksi yang terkait dengan periode sewa.

Catatan: Aturan status terlambat dan penanganan kelebihan pembayaran belum ditetapkan karena masih memerlukan keputusan kebutuhan sistem lebih lanjut.

### 6. Kesimpulan

Simulasi design review menghasilkan satu saran yang diterima dan sudah ditindaklanjuti, satu saran yang dinilai sudah tercakup dalam rancangan, serta satu pertanyaan reviewer yang telah dijawab berdasarkan rancangan data dan kebutuhan sistem.

Perubahan yang dilakukan pada tahap ini terbatas pada anotasi WF-10. Tidak ada perubahan terhadap struktur database, SRS, atau test case.

Hasil ini merupakan evaluasi simulasi dan bukan pengganti tinjauan langsung oleh kelompok lain, pengguna, atau dosen.

### 7. Status Kegiatan

- [x] Satu kelebihan desain dicatat.
- [x] Dua saran perbaikan beserta alasannya dicatat.
- [x] Satu pertanyaan reviewer dicatat.
- [x] Hasil simulasi didokumentasikan.
- [x] Evaluasi dan keputusan terhadap setiap masukan dicatat.
- [x] Saran pertama ditindaklanjuti pada anotasi WF-10.
- [x] Saran kedua diverifikasi sudah tercakup pada WF-08 dan TC-11.
- [x] Jawaban pertanyaan reviewer didokumentasikan.
