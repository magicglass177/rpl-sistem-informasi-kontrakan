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

### Pembuatan dan Verifikasi Activity Diagram dengan Bantuan AI — Sesi 2

**Aktivitas:** Pembuatan, evaluasi, dan penyempurnaan Activity Diagram.

**Bantuan AI:**

- Membantu membuat draf Activity Diagram berdasarkan skenario Use Case UC-08, UC-09, dan UC-01.
- Menghasilkan kode Mermaid untuk menggambarkan alur aktivitas, keputusan, dan kondisi pengecualian.
- Membantu memeriksa kesesuaian diagram dengan skenario Use Case.

**Temuan dan Evaluasi:**

1. Draf UC-09 belum menggambarkan kondisi kegagalan penyimpanan pembayaran.
2. Draf UC-09 menggunakan keputusan pembayaran bertahap berdasarkan alur alternatif pada skenario.
3. Draf UC-01 menggambarkan pengulangan pengisian kredensial ketika data login belum lengkap.
4. Draf UC-08 mencakup pemeriksaan keberadaan data penyewa dan kamar sesuai kondisi pengecualian pada skenario.

**Perbaikan yang Dilakukan:**

Menambahkan cabang keputusan pada UC-09 untuk menangani kondisi penyimpanan pembayaran berhasil atau gagal. Ketiga diagram kemudian diperiksa kembali dan diekspor ke format PNG.

**Kesalahan AI yang Paling Berisiko:**

AI dapat melewatkan alur pengecualian yang sudah tercantum dalam skenario Use Case, seperti kegagalan penyimpanan pembayaran, sehingga diagram perlu diperiksa secara manual sebelum ditetapkan sebagai hasil akhir.

**Verifikasi:**

- Ketiga diagram berhasil dirender menggunakan Mermaid Live Editor.
- Alur aktivitas dan cabang keputusan diperiksa berdasarkan skenario Use Case.
- Setiap diagram memiliki file Mermaid (`.mmd`) dan PNG.
- Keenam file berhasil di-commit dan di-merge ke branch `main` melalui Pull Request #16.

**Status:** Tiga Activity Diagram final selesai dibuat, diperiksa, dan diintegrasikan ke branch `main`.


### Revisi SRS, PRD, dan Penyelarasan Dokumen UML

**Tanggal:** 12 November 2026

**Aktivitas:** Perapian SRS dan penyelarasan kebutuhan fungsional dengan PRD serta dokumen UML.

**Bantuan AI:**
- Membantu meninjau struktur, kejelasan, dan konsistensi isi SRS.
- Membantu memeriksa prioritas kebutuhan menggunakan metode MoSCoW.
- Membantu memeriksa matriks ketertelusuran kebutuhan terhadap Use Case.
- Membantu mengidentifikasi ketidaksesuaian KF-08 pada PRD dan dokumen UML.

**Perubahan yang dilakukan:**
1. Memperjelas KF-08 agar larangan penempatan penyewa baru berlaku ketika kamar masih ditempati dalam periode sewa yang sedang berlangsung.
2. Menetapkan prioritas KF-08 menjadi Must dan memperbarui perhitungan prioritas kebutuhan menjadi 13 dari 20 kebutuhan (65%).
3. Menambahkan alasan penetapan prioritas KF-08 pada SRS.
4. Menambahkan pemetaan Use Case pada matriks ketertelusuran SRS.
5. Menyelaraskan prioritas UC-08 dan catatan penjelas pada daftar serta skenario Use Case.
6. Memperjelas F-11 pada PRD agar sesuai dengan aturan KF-08 pada SRS.

**Evaluasi dan keputusan:**
Prioritas KF-08 ditetapkan sebagai Must berdasarkan keputusan rancangan proyek dan konsistensi kebutuhan saat ini. Catatan historis pada jurnal yang sebelumnya menyebut KF-08 sebagai Should tetap dipertahankan sebagai riwayat keputusan terdahulu. Simulasi wawancara PT dan BM tetap dinyatakan sebagai data fiktif, bukan validasi klien nyata.

**Verifikasi:**
- Memeriksa perubahan pada PRD, SRS, dan dokumen UML.
- Menjalankan `git diff --check`; tidak ditemukan kesalahan whitespace.
- Git menampilkan peringatan line ending LF/CRLF pada beberapa dokumen.

**Status:** Revisi dokumentasi selesai dan menunggu pemeriksaan akhir sebelum commit.

### Jobsheet 6 — Perancangan ERD, Normalisasi, dan Kamus Data

**Tanggal:** 13 November 2026

**Aktivitas:** Merancang struktur basis data untuk Sistem Informasi Pengelolaan Kontrakan melalui identifikasi entitas, atribut, relasi, ERD, normalisasi, dan kamus data.

**Bantuan AI:**
- Membantu mengidentifikasi entitas berdasarkan kebutuhan fungsional dan Use Case.
- Membantu menyusun atribut, primary key, foreign key, serta kardinalitas relasi.
- Membantu menyusun dan meninjau ERD menggunakan Mermaid.
- Membantu menjelaskan tahapan normalisasi UNF, 1NF, 2NF, dan 3NF.
- Membantu menyusun kamus data beserta tipe data, aturan nilai, dan keterkaitan kebutuhan.

**Perubahan yang dilakukan:**
1. Membuat daftar lima entitas: `akun_pengguna`, `kamar`, `penyewa`, `sewa`, dan `pembayaran`.
2. Mendefinisikan atribut dan kunci setiap entitas.
3. Mendokumentasikan tiga relasi 1:N beserta foreign key.
4. Membuat ERD dalam format Mermaid dan PNG.
5. Mendokumentasikan proses normalisasi dari UNF hingga 3NF menggunakan data simulasi.
6. Membuat kamus data untuk lima tabel hasil rancangan.
7. Mendokumentasikan atribut turunan yang dihitung saat diperlukan dan tidak disimpan sebagai kolom tersendiri.

**Evaluasi dan keputusan:**
- Entitas `sewa` menghubungkan kamar dan penyewa serta menyimpan periode sewa dan harga sewa yang disepakati.
- Satu periode sewa dapat memiliki beberapa catatan pembayaran untuk mendukung pembayaran bertahap.
- Ketersediaan kamar, status pembayaran, dan total pendapatan diperlakukan sebagai nilai turunan.
- Seluruh contoh data bersifat simulasi akademik dan bukan data dari klien nyata.

**Verifikasi:**
- Memeriksa konsistensi daftar entitas, atribut, relasi, ERD, hasil normalisasi, dan kamus data.
- Memeriksa whitespace menggunakan `git diff --check` dan `git diff --cached --check`.
- Pemeriksaan akhir dan integrasi ke branch `main` belum dilakukan.

**Status:** Dokumen rancangan data telah dibuat dan sedang dalam pemeriksaan akhir sebelum commit.

### Jobsheet 6 — Sesi 2: Skema SQLite dan DDL Manual

**Tanggal:** 13 November 2026

**Aktivitas:** Menyusun DDL secara manual untuk tabel induk `kamar` dan tabel anak `sewa` menggunakan SQLite.

**Bantuan AI:**
- Membantu menyusun struktur `CREATE TABLE` berdasarkan ERD dan kamus data.
- Membantu menentukan primary key, foreign key, tipe data, dan constraint.
- Membantu menyusun skrip pengujian DDL menggunakan modul `sqlite3` bawaan Python.
- Membantu memeriksa validitas constraint dan konsistensi skema.

**Perubahan yang dilakukan:**
1. Membuat file `docs/desain/schema.sql`.
2. Menambahkan `PRAGMA foreign_keys = ON;`.
3. Membuat tabel `kamar` dengan primary key, `NOT NULL`, `UNIQUE`, dan `CHECK`.
4. Membuat tabel `sewa` dengan primary key, foreign key ke `kamar` dan `penyewa`, serta constraint validasi periode dan tanggal sewa.
5. Menetapkan `tanggal_jatuh_tempo` sebagai kolom nullable sesuai prioritas kebutuhan KF-12.
6. Menggunakan `ON UPDATE CASCADE` dan `ON DELETE RESTRICT` pada relasi foreign key.

**Evaluasi dan keputusan:**
- Tabel `kamar` dipilih sebagai tabel induk dan `sewa` sebagai tabel anak.
- Foreign key `sewa.id_penyewa` tetap dicantumkan sesuai ERD, sedangkan tabel `penyewa` dibuat sementara saat pengujian karena Langkah 8 hanya meminta dua tabel.
- `harga_sewa_disepakati` tetap disimpan sebagai snapshot harga pada saat transaksi sewa dibuat.
- Pengujian dilakukan menggunakan database sementara di memori sehingga tidak mengubah database proyek.

**Verifikasi:**
- DDL berhasil dijalankan dan kedua tabel berhasil dibuat.
- Foreign key berhasil diaktifkan.
- Data sewa valid berhasil dimasukkan.
- Constraint `CHECK` harga dan periode sewa berhasil diuji.
- Constraint `UNIQUE` nomor kamar berhasil diuji.
- Foreign key `id_kamar` dan `id_penyewa` berhasil diuji.
- Validasi format tanggal berhasil diuji.
- Seluruh pengujian tambahan dinyatakan lulus.

**Status:** DDL dua tabel berhasil dibuat dan diuji. Pemeriksaan akhir dokumentasi serta commit masih menunggu penyelesaian.
