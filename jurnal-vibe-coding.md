### Catatan Evaluasi Hasil AI

**Pertanyaan awal yang perlu diperbaiki:**

"Apakah Bapak/Ibu membutuhkan aplikasi berbasis web untuk mempermudah pengelolaan kontrakan?"

**Pertanyaan setelah diperbaiki:**

"Perubahan atau perbaikan apa yang Bapak/Ibu harapkan dalam proses pengelolaan kontrakan ke depannya?"

**Alasan perubahan:**

Pertanyaan awal diubah karena bersifat mengarahkan narasumber pada solusi tertentu, yaitu aplikasi berbasis web, dan dapat menghasilkan jawaban singkat berupa ya atau tidak. Pertanyaan tersebut kemudian diperbaiki menjadi pertanyaan terbuka dan netral agar narasumber dapat menyampaikan kebutuhan serta harapannya berdasarkan pengalaman sendiri tanpa diarahkan pada solusi teknologi tertentu.


## Jurnal Vibe Coding — Entri Penyusunan Pedoman Wawancara

**Kegiatan:** Penyusunan Pedoman Wawancara dengan Bantuan AI

**Proyek:** Sistem Informasi Pengelolaan Kontrakan

**Tahapan:** Sesi 1 – Langkah 4

### 1. Prompt
Memberikan instruksi kepada AI untuk menghasilkan 15 pertanyaan wawancara berdasarkan konteks proyek Sistem Informasi Pengelolaan Kontrakan dengan narasumber pemilik kontrakan.

### 2. Hasil Generate
AI menghasilkan 15 pertanyaan wawancara yang dikelompokkan ke dalam enam kategori, yaitu proses saat ini, masalah, data, pengguna, kendala, dan harapan.

### 3. Hasil Tinjauan
Hasil pertanyaan diperiksa berdasarkan lima kriteria, yaitu terbuka, netral, satu topik per pertanyaan, relevan dengan klien, dan mampu menggali contoh nyata.

Selain itu, diperiksa juga kesesuaian jumlah pertanyaan, pertanyaan lanjutan, serta permintaan contoh dokumen atau data yang digunakan dalam pengelolaan kontrakan.

### 4. Perubahan Hasil AI
Pertanyaan "Apakah Bapak/Ibu membutuhkan aplikasi berbasis web untuk mempermudah pengelolaan kontrakan?" diperbaiki menjadi "Perubahan atau perbaikan apa yang Bapak/Ibu harapkan dalam proses pengelolaan kontrakan ke depannya?"

Perubahan dilakukan karena pertanyaan awal bersifat mengarahkan narasumber pada solusi teknologi tertentu dan hanya memungkinkan jawaban ya atau tidak. Pertanyaan hasil perbaikan lebih terbuka dan netral sehingga dapat menggali kebutuhan pengguna secara lebih mendalam.

### 5. Hasil Akhir
Pedoman wawancara berhasil disusun dengan 15 pertanyaan yang terbagi dalam enam kategori. Hasilnya telah disesuaikan dengan konteks proyek dan direncanakan untuk digunakan dalam wawancara langsung dengan pemilik kontrakan.

**Status:** Draft pedoman wawancara selesai dan belum digunakan untuk wawancara langsung.

## Vibe Coding Journal — Kritik AI dan Review User Story

### 1. Tujuan Penggunaan AI

AI digunakan untuk melakukan evaluasi terhadap 12 user story pada dokumen `user-story.md` berdasarkan hasil simulasi wawancara pemilik kontrakan.

Evaluasi dilakukan untuk memeriksa kejelasan kebutuhan, acceptance criteria, keterujian, dan kesesuaian dengan sumber catatan wawancara.

### 2. Prompt yang Digunakan

"Periksa 12 user story pada dokumen user-story.md untuk Sistem Informasi Pengelolaan Kontrakan. Evaluasi apakah setiap user story sudah berorientasi pada kebutuhan pengguna, memiliki acceptance criteria Given–When–Then yang jelas dan dapat diuji, serta memiliki sumber kebutuhan yang sesuai. Berikan kritik dan saran perbaikan untuk setiap user story. Jangan menambahkan kebutuhan baru seolah-olah sudah dikonfirmasi oleh klien."

### 3. Ringkasan Hasil Kritik AI

AI memberikan beberapa masukan, yaitu:

1. US-01 perlu memperjelas aturan akun pengguna.
2. US-02 perlu memperjelas aturan penghapusan kamar.
3. US-03 perlu memperjelas perubahan status kamar.
4. US-04 perlu menentukan data penyewa yang wajib dicatat.
5. US-05 perlu mencegah penempatan lebih dari satu penyewa aktif pada kamar yang sama.
6. US-06 perlu memperjelas aturan pembayaran sebagian atau sekaligus.
7. US-07 perlu memperjelas penentuan status pembayaran.
8. US-08 perlu menentukan aturan jatuh tempo pembayaran.
9. US-09 perlu menambahkan validasi tanggal periode sewa.
10. US-10 perlu menentukan batas waktu informasi masa sewa berakhir.
11. US-11 perlu memperjelas dasar perhitungan pendapatan.
12. US-12 perlu menentukan format dan isi file laporan.

### 4. Review dan Keputusan

| User Story | Keputusan | Alasan |
|---|---|---|
| US-01 | Terima | Kriteria login sudah dapat diuji. |
| US-02 | Ubah | Aturan penghapusan kamar perlu diperjelas. |
| US-03 | Ubah | Perubahan status kamar perlu diperjelas. |
| US-04 | Terima | Kebutuhan pengelolaan penyewa sudah sesuai skenario. |
| US-05 | Ubah | Perlu aturan kamar hanya memiliki satu penyewa aktif. |
| US-06 | Ubah | Aturan pembayaran perlu diperjelas. |
| US-07 | Ubah | Status pembayaran perlu memiliki definisi yang jelas. |
| US-08 | Ubah | Aturan jatuh tempo belum ditentukan. |
| US-09 | Terima | Kriteria periode sewa sudah dapat dipahami. |
| US-10 | Ubah | Waktu pemberitahuan belum ditentukan. |
| US-11 | Ubah | Perhitungan pendapatan perlu diperjelas. |
| US-12 | Ubah | Format laporan belum ditentukan. |

### 5. Perubahan yang Akan Dilakukan

Perbaikan akan difokuskan pada penambahan aturan dan validasi agar acceptance criteria lebih jelas serta dapat diuji.

Kebutuhan yang belum memiliki dasar dari catatan simulasi tidak akan dianggap sebagai fakta. Kebutuhan tersebut tetap diberi tanda [Asumsi] sampai dikonfirmasi melalui wawancara nyata atau mendapat persetujuan dosen.

### 6. Hasil Akhir

AI membantu menemukan bagian user story yang masih ambigu dan memberikan saran perbaikan. Keputusan akhir tetap ditentukan melalui proses review dokumen.

Seluruh user story masih berstatus draft berdasarkan simulasi wawancara fiktif dan belum divalidasi oleh klien nyata.

### Pengujian PRD Menggunakan AI — Sesi 4

**Prompt:**

"Tinjau dokumen PRD Sistem Informasi Pengelolaan Kontrakan. Buat ringkasan produk berdasarkan dokumen, identifikasi asumsi yang belum dikonfirmasi, dan temukan bagian yang masih ambigu atau belum lengkap. Jangan menambahkan fitur yang tidak tercantum dalam PRD."

**Hasil AI:**

AI merangkum bahwa produk merupakan sistem untuk membantu pemilik kontrakan mengelola kamar, penyewa, pembayaran sewa, periode sewa, dan laporan pendapatan.

AI menemukan beberapa asumsi, yaitu penggunaan akun login, aturan jatuh tempo pembayaran, informasi masa sewa berakhir, fitur unduh laporan, dan kemungkinan akses bagi penjaga kontrakan.

AI juga menemukan beberapa bagian yang masih perlu diperjelas, seperti atribut wajib data penyewa, aturan pembayaran cicilan, penentuan jatuh tempo, batas waktu informasi masa sewa berakhir, format laporan, dan hak akses pengguna.

**Evaluasi:**

Hasil ringkasan AI sesuai dengan tujuan dan ruang lingkup produk dalam PRD. Namun, beberapa aturan operasional masih belum dijelaskan secara terperinci.

**Keputusan:**

PRD dipertahankan dengan beberapa catatan validasi. Asumsi yang belum dikonfirmasi tetap diberi label asumsi dan tidak dianggap sebagai kebutuhan final klien.

**Status:** Pengujian PRD selesai berdasarkan rancangan dokumen simulasi. Validasi dengan klien nyata masih diperlukan.

### Penyempurnaan Aturan Proyek — Jobsheet Step 9

**Tanggal:** 11 November 2026

**Tujuan:**

Memperbarui `aturan-proyek.md` agar sesuai dengan ketentuan teknologi, struktur proyek, konvensi penulisan, keamanan, penggunaan AI, dan pengujian.

**Bantuan AI yang digunakan:**

AI membantu meninjau dan menyempurnakan aturan proyek berdasarkan ketentuan Jobsheet Step 9.

**Perubahan yang dilakukan:**

1. Menetapkan Python 3.14 sebagai versi utama dengan minimum Python 3.10.
2. Menetapkan Flask sebagai framework dan SQLite sebagai database.
3. Menambahkan struktur folder aplikasi, termasuk `app.py`, `templates/`, `static/`, `tests/`, dan `docs/`.
4. Memperjelas aturan penamaan variabel, fungsi, class, konstanta, dan file.
5. Menambahkan ketentuan komentar kode dan pesan antarmuka menggunakan Bahasa Indonesia.
6. Memperkuat aturan penggunaan AI, termasuk larangan mengubah file di luar ruang lingkup tugas dan melemahkan pengujian.
7. Memperjelas aturan keamanan agar kata sandi, token, dan API key tidak disimpan langsung dalam kode.
8. Menambahkan petunjuk pembuatan virtual environment, instalasi Flask, menjalankan aplikasi, dan menjalankan pengujian otomatis.

**Pemeriksaan:**

- `Pemeriksaan akhir git diff --check berhasil tanpa kesalahan whitespace setelah perbaikan format.
- `git status` menunjukkan hanya `aturan-proyek.md` yang berubah sebelum pembaruan jurnal.
- Perubahan belum di-commit dan masih berada pada branch `docs-aturan-proyek-stack`.

**Evaluasi:**

Aturan proyek telah disesuaikan dengan ketentuan Jobsheet Step 9. Perintah menjalankan aplikasi dan pengujian telah dicantumkan sebagai pedoman untuk tahap implementasi.

**Keputusan:**

Perubahan diterima untuk dilanjutkan ke pemeriksaan akhir sebelum commit. Penggunaan AI dan perubahan dokumen tetap harus ditinjau oleh pengembang.

**Status:** Penyempurnaan aturan proyek selesai; menunggu pemeriksaan akhir dan commit.

### Pengujian PRD Menggunakan AI Reverse Summary — Iterasi 1

**Tanggal:** 11 November 2026

**Metode:** AI Reverse Summary menggunakan PRD.md dan aturan-proyek.md pada percakapan AI baru.

**Hasil pengujian:**
1. AI berhasil memahami tujuan dan ruang lingkup umum Sistem Informasi Pengelolaan Kontrakan.
2. AI mengidentifikasi 12 asumsi, 16 bagian ambigu, dan sejumlah pertanyaan klarifikasi sebelum coding.
3. AI menemukan ketidakjelasan terkait hak akses pengguna, pengelolaan kamar dan penyewa, pembayaran, jatuh tempo, masa sewa, serta laporan pendapatan.
4. Evaluasi menemukan bahwa ringkasan AI belum membedakan secara tegas fitur Must Have dan Should Have.

**Evaluasi:** Hasil pengujian pertama secara umum sesuai dengan maksud proyek. Beberapa temuan AI sudah tercantum dalam Open Questions PRD sehingga tidak seluruhnya membutuhkan penambahan baru.

**Tindakan:** Mempertahankan pertanyaan yang belum terjawab sebagai Open Questions dan memperjelas prioritas fitur serta aturan operasional yang masih ambigu pada revisi PRD berikutnya.

**Status:** Iterasi 1 selesai. Dilanjutkan ke Jobsheet Step 11 untuk revisi PRD dan pengujian ulang.

### Revisi PRD — Versi 1.1

**Tanggal:** 11 November 2026

**Dasar revisi:** Hasil evaluasi AI Reverse Summary Iterasi 1.

**Perubahan yang dilakukan:**
1. Menambahkan penjelasan mengenai prioritas Must Have dan Should Have.
2. Memperluas pertanyaan terbuka terkait pengguna, autentikasi, kamar, penyewa, periode sewa, pembayaran, laporan pendapatan, serta kualitas dan pengujian.
3. Memperjelas bahwa hubungan antarentitas akan dibahas pada tahap perancangan ERD.
4. Mempertahankan pertanyaan yang belum terjawab sebagai hal terbuka, bukan menetapkannya berdasarkan asumsi AI.

**Status:** PRD versi 1.1 selesai direvisi dan menunggu pengujian ulang melalui AI Reverse Summary pada Jobsheet Step 11.

### Pengujian PRD Menggunakan AI Reverse Summary — Iterasi 2

**Tanggal:** 11 November 2026

**Metode:** AI Reverse Summary menggunakan PRD.md versi 1.1 dan aturan-proyek.md pada percakapan AI baru.

**Hasil pengujian:**
1. AI berhasil memahami tujuan, pengguna, ruang lingkup, dan teknologi Sistem Informasi Pengelolaan Kontrakan.
2. AI berhasil membedakan fitur Must Have dan Should Have secara jelas.
3. AI mengidentifikasi 7 asumsi yang belum tertulis dan 10 bagian yang masih ambigu.
4. AI menghasilkan 35 pertanyaan klarifikasi terkait pengguna, autentikasi, kamar, penyewa, periode sewa, pembayaran, laporan pendapatan, kualitas, dan proses proyek.
5. AI mengidentifikasi bahwa aturan pembayaran, penentuan status kamar, jatuh tempo, dan perhitungan pendapatan masih membutuhkan keputusan.
6. AI memahami bahwa prioritas dan kebutuhan dalam PRD masih berupa rancangan yang belum divalidasi.

**Evaluasi:** Hasil Iterasi 2 menunjukkan peningkatan pemahaman dibandingkan Iterasi 1. Revisi PRD versi 1.1 berhasil memperjelas pengelompokan prioritas fitur dan memperluas pertanyaan terbuka. Namun, beberapa asumsi dan ambiguitas tetap ditemukan karena kebutuhan tersebut memang belum dikonfirmasi.

**Tindakan:** Mempertahankan hal-hal yang belum terjawab sebagai pertanyaan terbuka. Temuan AI akan digunakan sebagai bahan evaluasi sebelum implementasi, bukan sebagai keputusan kebutuhan final.

**Status:** Pengujian AI Reverse Summary Iterasi 2 selesai. Hasil pengujian diterima dan didokumentasikan untuk melanjutkan tahapan proyek.

### Pembaruan Product Backlog — Jobsheet Langkah 12

**Aktivitas:** Memperbarui Product Backlog berdasarkan PRD versi 1.1 dan SRS.

**Bantuan AI:**
- Membantu memetakan kebutuhan KF dan KNF ke dalam Product Backlog.
- Memberikan rekomendasi prioritas menggunakan metode MoSCoW.
- Membantu membagi kebutuhan ke dalam empat sprint dengan durasi dua minggu.
- Memberikan usulan pemecahan tugas Sprint 1 dengan estimasi maksimal satu hari kerja per tugas.

**Keputusan Pengembang:**
- Menerima pemetaan kebutuhan dan pembagian sprint sebagai rancangan awal.
- Menghapus kebutuhan fasilitas kamar, pencarian, dan dashboard karena belum tercantum dalam PRD.
- Mempertahankan KF-08 sebagai Should sesuai PRD versi 1.1.
- Mempertahankan KF-16 sebagai Could dan tidak menjadwalkannya pada Sprint 1–3.
- Meninjau kembali keputusan yang masih bergantung pada pertanyaan terbuka PRD.

**Verifikasi:** Perubahan diperiksa menggunakan `git diff --check` dan `git diff`. Tidak ditemukan masalah whitespace. Isi backlog tetap perlu dikonfirmasi kepada klien sebelum implementasi.

**Status:** Draf Product Backlog diperbarui, belum di-commit dan belum di-merge.
