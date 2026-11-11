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