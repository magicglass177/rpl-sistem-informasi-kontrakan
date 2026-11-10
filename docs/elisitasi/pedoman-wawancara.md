# Pedoman Wawancara

## A. Konteks

### 1. Identifikasi Stakeholder

Stakeholder merupakan pihak-pihak yang diperkirakan akan berhubungan dengan sistem informasi pengelolaan kontrakan. Identifikasi berikut masih bersifat sementara dan perlu dikonfirmasi melalui wawancara.

| No. | Stakeholder | Peran | Kepentingan | Metode Keterlibatan |
|---|---|---|---|---|
| 1 | Pemilik kontrakan | Mengelola usaha kontrakan dan bertanggung jawab atas data kamar serta penyewaan | Mempermudah pengelolaan data kamar, penyewa, pembayaran, dan laporan pendapatan | Wawancara dan observasi proses pengelolaan kontrakan |
| 2 | Penyewa kontrakan | Pihak yang menyewa kamar kontrakan dan melakukan pembayaran | Mendapatkan informasi mengenai kamar, masa sewa, dan status pembayaran | Wawancara untuk mengetahui kebutuhan dan kendala penyewa |
| 3 | Pengelola atau penjaga kontrakan (jika ada) | Membantu pemilik dalam mengelola kamar atau melayani penyewa | Mempermudah pencatatan informasi kamar dan aktivitas penyewaan | Wawancara apabila pihak tersebut tersedia |

### 2. Dugaan Permasalahan

Berdasarkan gambaran awal mengenai proses pengelolaan kontrakan, terdapat beberapa dugaan permasalahan yang perlu dikonfirmasi kepada pemilik kontrakan.

1. **Pencatatan data kontrakan masih berpotensi dilakukan secara manual.** Data kamar, informasi penyewa, dan masa sewa kemungkinan masih dicatat menggunakan buku atau media terpisah sehingga berpotensi menyulitkan pencarian dan pembaruan data.

2. **Pemantauan pembayaran sewa berpotensi kurang terorganisasi.** Pemilik kontrakan mungkin mengalami kesulitan dalam mengetahui penyewa yang sudah membayar, belum membayar, atau telah melewati batas waktu pembayaran.

3. **Penyusunan laporan dan pemantauan ketersediaan kamar berpotensi membutuhkan waktu lebih lama.** Informasi kamar kosong, kamar terisi, dan pendapatan kontrakan mungkin belum tersusun dalam satu sistem yang mudah diakses.

**Catatan:** Ketiga permasalahan di atas merupakan hipotesis awal, bukan hasil wawancara. Kebenarannya akan diperiksa kembali setelah proses elisitasi kebutuhan dilakukan.

### 3. Ruang Lingkup Sistem

**a. Termasuk dalam ruang lingkup (In-Scope)**

1. Pengelolaan data kamar kontrakan, meliputi nomor kamar, harga sewa, fasilitas, dan status ketersediaan.
2. Pengelolaan data penyewa, meliputi identitas dan informasi penyewaan.
3. Pencatatan transaksi pembayaran sewa serta pemantauan status pembayaran.
4. Pengelolaan informasi tanggal mulai dan berakhirnya masa sewa.
5. Penyajian laporan pendapatan dan ringkasan informasi pengelolaan kontrakan.
6. Fitur login untuk membatasi akses pengelolaan sistem.

**b. Tidak termasuk dalam ruang lingkup (Out-of-Scope)**

1. Pengelolaan keuangan pribadi pemilik kontrakan yang tidak berkaitan dengan pendapatan penyewaan.
2. Pembayaran sewa secara otomatis melalui payment gateway atau layanan perbankan.
3. Pengelolaan pembangunan, renovasi, dan perbaikan fisik bangunan kontrakan.
4. Integrasi dengan aplikasi pihak ketiga di luar kebutuhan utama sistem.

### 4. Kendala dan Batasan

Beberapa kendala dan batasan yang perlu diperhatikan dalam pengembangan sistem adalah sebagai berikut.

1. **Batas waktu pengembangan:** Sistem dikembangkan mengikuti jadwal perkuliahan dan harus diselesaikan paling lambat pada minggu ke-16.
2. **Perangkat yang digunakan:** Jenis perangkat yang dimiliki atau digunakan oleh pemilik kontrakan untuk mengakses sistem masih perlu dikonfirmasi.
3. **Koneksi internet:** Ketersediaan dan kestabilan koneksi internet di lokasi kontrakan masih perlu diketahui.
4. **Kemampuan pengguna:** Kemampuan pemilik kontrakan dalam menggunakan perangkat komputer atau smartphone dan aplikasi berbasis web perlu diketahui agar sistem mudah digunakan.
5. **Ketersediaan informasi:** Data kamar, data penyewa, dan riwayat pembayaran perlu diperoleh dari pemilik kontrakan apabila tersedia.

**Catatan:** Bagian kendala dan batasan yang belum diketahui akan dikonfirmasi melalui wawancara dengan calon pengguna sistem.


### B. Teknik Elisitasi

Berdasarkan kebutuhan awal pada proyek Sistem Informasi Pengelolaan Kontrakan, teknik elisitasi yang dipilih adalah wawancara dan observasi. Kedua teknik tersebut digunakan untuk memperoleh informasi mengenai proses pengelolaan kontrakan, permasalahan yang mungkin dihadapi, serta kebutuhan calon pengguna terhadap sistem yang akan dikembangkan.

| Teknik Dipilih | Siapa / Apa yang Menjadi Sumber | Alasan Memilih |
|---|---|---|
| Wawancara (Interview) | Pemilik kontrakan sebagai pihak yang bertanggung jawab atas pengelolaan kamar, data penyewa, pembayaran uang sewa, dan masa sewa. | Teknik wawancara dipilih untuk memperoleh informasi secara langsung dari pemilik kontrakan mengenai proses pengelolaan yang sedang berjalan. Melalui wawancara, pengembang dapat mengetahui kendala dalam pencatatan data kamar, pengelolaan penyewa, pemantauan pembayaran, serta kebutuhan dan harapan pemilik terhadap sistem informasi yang akan dibuat. |
| Observasi (Observation) | Aktivitas pengelolaan kontrakan secara langsung, termasuk proses pencatatan data kamar, pendataan penyewa, pencatatan pembayaran, dan pemeriksaan ketersediaan kamar. | Teknik observasi dipilih untuk mengetahui bagaimana proses pengelolaan kontrakan dilakukan dalam praktiknya. Melalui pengamatan langsung, pengembang dapat memahami alur kegiatan pemilik kontrakan serta mengidentifikasi kemungkinan kesulitan dalam proses pencatatan dan pengelolaan data yang mungkin tidak seluruhnya terungkap melalui wawancara. |

**Catatan:** Kedua teknik tersebut masih berupa rencana metode elisitasi dan belum dilaksanakan. Pelaksanaannya akan dilakukan setelah tersedia kesempatan untuk berkomunikasi dan melakukan pengamatan terhadap pemilik serta aktivitas pengelolaan kontrakan.

## C. Pedoman Pertanyaan Wawancara

Pedoman wawancara ini disusun untuk memperoleh informasi mengenai proses pengelolaan kontrakan yang sedang berjalan, permasalahan yang dihadapi, data yang digunakan, pihak yang terlibat, kendala, serta harapan pemilik kontrakan terhadap pengembangan sistem informasi. Pertanyaan disusun secara terbuka dan netral agar narasumber dapat memberikan jawaban berdasarkan pengalaman dan kondisi sebenarnya.

**Narasumber:** Pemilik kontrakan

**Estimasi waktu:** 30–45 menit

### 1. Kategori Proses Saat Ini

| No. | Pertanyaan | Pertanyaan Lanjutan |
|---|---|---|
| 1 | Bagaimana proses pengelolaan kontrakan yang Bapak/Ibu lakukan mulai dari menerima calon penyewa hingga penyewa menempati kamar? | Dapatkah Bapak/Ibu menceritakan tahapan proses penyewaan tersebut secara berurutan? |
| 2 | Bagaimana cara Bapak/Ibu mencatat dan memantau status ketersediaan kamar kontrakan? | Bagaimana Bapak/Ibu mengetahui kamar yang sedang kosong dan kamar yang sudah ditempati? |
| 3 | Bagaimana proses pencatatan dan pemantauan pembayaran uang sewa yang dilakukan selama ini? | Dapatkah Bapak/Ibu menceritakan proses pembayaran sewa yang terakhir dilakukan oleh penyewa? |

### 2. Kategori Masalah

| No. | Pertanyaan | Pertanyaan Lanjutan |
|---|---|---|
| 4 | Kesulitan apa saja yang pernah Bapak/Ibu alami ketika mengelola data kamar dan penyewa? | Dapatkah Bapak/Ibu menceritakan contoh kejadian ketika mengalami kesulitan tersebut? |
| 5 | Kendala apa yang pernah terjadi dalam proses pemantauan pembayaran uang sewa? | Bagaimana kendala tersebut memengaruhi proses pengelolaan pembayaran? |
| 6 | Bagaimana Bapak/Ibu menangani kesalahan atau ketidaksesuaian data dalam pencatatan kontrakan? | Apa yang biasanya Bapak/Ibu lakukan ketika menemukan data yang tidak sesuai? |

### 3. Kategori Data

| No. | Pertanyaan | Pertanyaan Lanjutan |
|---|---|---|
| 7 | Data apa saja yang biasanya dicatat ketika ada penyewa baru yang akan menempati kamar kontrakan? | Dapatkah Bapak/Ibu memberikan contoh catatan atau dokumen yang digunakan untuk mendata penyewa? |
| 8 | Dokumen atau catatan apa saja yang digunakan untuk mencatat pembayaran uang sewa? | Dapatkah Bapak/Ibu menunjukkan contoh catatan pembayaran yang biasa digunakan, tanpa memperlihatkan informasi pribadi penyewa? |
| 9 | Bagaimana Bapak/Ibu mencatat informasi kamar, harga sewa, fasilitas, dan masa sewa? | Apakah terdapat buku, formulir, atau berkas tertentu yang digunakan? Jika ada, dapatkah Bapak/Ibu memberikan contohnya? |

### 4. Kategori Pengguna

| No. | Pertanyaan | Pertanyaan Lanjutan |
|---|---|---|
| 10 | Siapa saja pihak yang terlibat dalam kegiatan pengelolaan kontrakan sehari-hari? | Apa saja tugas dan tanggung jawab masing-masing pihak tersebut? |
| 11 | Bagaimana pembagian tanggung jawab antara pemilik kontrakan, pengelola, atau penjaga dalam mengelola informasi penyewa dan kamar? | Siapa yang biasanya bertanggung jawab mencatat dan memperbarui informasi tersebut? |

### 5. Kategori Kendala

| No. | Pertanyaan | Pertanyaan Lanjutan |
|---|---|---|
| 12 | Kendala apa saja yang Bapak/Ibu hadapi ketika menggunakan perangkat komputer atau smartphone untuk membantu kegiatan pengelolaan kontrakan? | Aktivitas apa yang menurut Bapak/Ibu paling sulit dilakukan menggunakan perangkat tersebut? |
| 13 | Bagaimana kondisi akses internet di lingkungan kontrakan dalam mendukung kegiatan sehari-hari? | Pada kondisi seperti apa akses internet biasanya mengalami gangguan atau keterbatasan? |

### 6. Kategori Harapan

| No. | Pertanyaan | Pertanyaan Lanjutan |
|---|---|---|
| 14 | Informasi apa saja yang paling Bapak/Ibu butuhkan untuk membantu kegiatan pengelolaan kontrakan? | Informasi apa yang paling penting untuk diketahui setiap hari? |
| 15 | Perubahan atau perbaikan apa yang Bapak/Ibu harapkan dalam proses pengelolaan kontrakan ke depannya? | Bagaimana perubahan tersebut dapat membantu kegiatan pengelolaan kontrakan sehari-hari? |

**Catatan:** Seluruh pertanyaan di atas merupakan rancangan pedoman wawancara yang dihasilkan dengan bantuan AI dan telah ditinjau serta disesuaikan dengan konteks proyek. Pertanyaan akan digunakan sebagai panduan ketika wawancara langsung dengan pemilik kontrakan dilakukan. Jawaban narasumber akan dicatat secara terpisah pada dokumen catatan-wawancara.md.