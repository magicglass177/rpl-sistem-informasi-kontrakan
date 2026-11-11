# Aturan Proyek
## Sistem Informasi Pengelolaan Kontrakan

## 1. Tujuan

Dokumen ini menjadi pedoman pengembangan Sistem Informasi Pengelolaan Kontrakan agar proses pengembangan berjalan terstruktur, konsisten, dan sesuai kebutuhan proyek.

Aturan ini digunakan sebagai konteks bagi pengembang maupun AI ketika membantu pekerjaan proyek.

## 2. Informasi Teknologi

Teknologi yang digunakan dalam proyek:

- Bahasa pemrograman: Python 3.14 (minimal Python 3.10).
- Framework: Flask.
- Database: SQLite.
- Paket tambahan: Hanya boleh ditambahkan setelah mendapat persetujuan sesuai kesepakatan tim.

Ketentuan:

- Pengembangan harus menggunakan teknologi yang telah ditetapkan.
- Versi Python yang digunakan harus memenuhi persyaratan minimum.
- Penggunaan paket tambahan harus memiliki alasan dan persetujuan terlebih dahulu.
- AI tidak boleh memilih atau menambahkan teknologi dan dependensi sendiri.

## 3. Struktur Folder Proyek

Struktur folder aplikasi yang direncanakan:

```text
rpl-sistem-informasi-kontrakan/
├── app.py
├── templates/
├── static/
├── tests/
├── docs/
│   ├── elisitasi/
│   │   ├── catatan-wawancara.md
│   │   ├── pedoman-wawancara.md
│   │   └── user-story.md
│   ├── kesepakatan-tim.md
│   ├── product-backlog.md
│   └── srs.md
├── .github/
├── .gitignore
├── aturan-proyek.md
├── jurnal-vibe-coding.md
├── PRD.md
└── README.md
```

Ketentuan:

- `app.py` berisi konfigurasi dan kode utama aplikasi Flask.
- `templates/` menyimpan berkas template HTML.
- `static/` menyimpan CSS, JavaScript, dan aset statis.
- `tests/` menyimpan berkas pengujian otomatis.
- `docs/` menyimpan dokumentasi proyek.
- Struktur folder aplikasi dibuat sesuai kebutuhan implementasi.
- File baru harus ditempatkan sesuai fungsi dan jenisnya.

## 4. Aturan Penamaan

- Nama file dokumentasi menggunakan huruf kecil dan tanda hubung jika diperlukan.
- Gunakan format Markdown (`.md`) untuk dokumentasi proyek.
- ID kebutuhan fungsional menggunakan format `KF-01`, `KF-02`, dan seterusnya.
- ID kebutuhan nonfungsional menggunakan format `KNF-01`, `KNF-02`, dan seterusnya.
- ID User Story menggunakan format `US-01`, `US-02`, dan seterusnya.
- Nama branch menggunakan awalan:
  - `fitur-` untuk pengembangan fitur.
  - `perbaikan-` untuk perbaikan kesalahan.
  - `docs-` untuk perubahan dokumentasi.
- Pesan commit harus menjelaskan perubahan yang dilakukan.
- Komentar kode dan pesan antarmuka pengguna menggunakan Bahasa Indonesia.
- Nama variabel dan fungsi Python menggunakan `snake_case`.
- Nama class menggunakan `PascalCase`.
- Konstanta menggunakan `UPPER_SNAKE_CASE`.
- Nama file menggunakan huruf kecil dan tanda hubung atau garis bawah jika diperlukan.
- Setiap commit sebaiknya hanya memuat satu fitur atau satu kelompok perubahan yang saling berkaitan.

## 5. Aturan Penggunaan AI

AI digunakan sebagai alat bantu pengembangan dengan ketentuan:

1. Setiap penggunaan AI yang berkaitan dengan pekerjaan proyek dicatat dalam `jurnal-vibe-coding.md`.
2. AI tidak boleh dijadikan sumber utama untuk menentukan kebutuhan klien.
3. Kebutuhan yang belum didukung hasil konfirmasi klien harus diberi label `[Asumsi]`.
4. Saran AI harus diperiksa dan dievaluasi sebelum diterapkan.
5. Kode yang dihasilkan AI harus dipahami, diperiksa, dan diuji oleh pengembang sebelum di-commit.
6. AI tidak boleh mengarang hasil wawancara atau menyatakan data simulasi sebagai hasil wawancara nyata.
7. Data pribadi klien, kata sandi, token, dan kunci akses tidak boleh dimasukkan ke AI.
8. AI tidak boleh mengubah struktur proyek, memilih teknologi, atau menambahkan dependensi tanpa persetujuan pengembang.
9. AI tidak boleh mengubah atau menghapus berkas di luar ruang lingkup tugas yang diminta.
10. AI tidak boleh menghapus, melemahkan, atau melewati pengujian yang sudah tersedia.
11. AI tidak boleh menambahkan paket atau dependensi tanpa persetujuan pengembang.

## 6. Aturan Pengembangan

- Pengembangan harus mengacu pada PRD, SRS, User Story, dan Product Backlog.
- Setiap fitur harus memiliki kebutuhan dan kriteria penerimaan yang jelas.
- Implementasi tidak boleh menyimpang dari ruang lingkup proyek tanpa alasan dan keputusan yang terdokumentasi.
- Perubahan kebutuhan dan keputusan teknis harus dicatat dalam dokumentasi atau Jurnal Vibe Coding.
- Fitur yang belum diprioritaskan untuk proyek tidak boleh dikerjakan tanpa evaluasi ulang ruang lingkup.
- Dilarang menyimpan kata sandi, token, API key, atau informasi rahasia lainnya secara langsung di dalam kode.
- Informasi rahasia harus dikelola melalui konfigurasi lingkungan yang aman.
- Perubahan hanya boleh dilakukan pada berkas yang relevan dengan tugas.
- Penambahan dependensi harus mendapat persetujuan terlebih dahulu.

## 7. Aturan Pengujian

- Setiap fitur harus diuji berdasarkan kriteria penerimaan.
- Pengujian otomatis disimpan dalam folder `tests/`.
- Pengujian tidak boleh dihapus atau dilemahkan hanya untuk membuat fitur terlihat berhasil.
- Kesalahan pada fungsi utama harus diperbaiki sebelum fitur di-merge.
- Hasil pengujian harus diperiksa sebelum perubahan dinyatakan selesai.

## 8. Aturan Git dan Pull Request

1. Tidak melakukan perubahan langsung pada branch `main`.
2. Setiap pekerjaan dilakukan melalui branch terpisah.
3. Perubahan diajukan melalui Pull Request (PR) menuju branch `main`.
4. Setiap PR harus ditinjau secara mandiri sebelum di-merge.
5. Pesan commit harus menjelaskan isi perubahan.
6. Sebelum membuat branch atau mengerjakan perubahan baru, pastikan branch `main` sudah diperbarui.
7. Pastikan tidak ada perubahan yang belum disimpan atau tidak sengaja tertinggal sebelum berpindah branch.

## 9. Definition of Done

Sebuah fitur atau pekerjaan dianggap selesai apabila:

- Memenuhi kriteria penerimaan yang telah ditentukan.
- Kode atau dokumen sudah diperiksa.
- Pengujian telah dilakukan sesuai jenis perubahan.
- Tidak terdapat kesalahan yang mengganggu fungsi utama.
- Perubahan sudah ditinjau melalui Pull Request.
- Jurnal Vibe Coding sudah diperbarui jika menggunakan AI.
- Perubahan sudah berhasil di-merge ke branch `main`.

## 10. Batasan Proyek

Sistem Informasi Pengelolaan Kontrakan berfokus pada pengelolaan:

- Data kamar kontrakan.
- Data penyewa.
- Hubungan penyewa dengan kamar.
- Pembayaran uang sewa.
- Status pembayaran.
- Periode dan masa sewa.
- Laporan pendapatan kontrakan.

Fitur di luar ruang lingkup yang telah ditetapkan dalam SRS tidak boleh ditambahkan tanpa evaluasi dan persetujuan pengembang.

## 11. Status Dokumen

Dokumen ini merupakan pedoman awal pengembangan proyek dan dapat diperbarui apabila terdapat perubahan teknologi, kebutuhan, atau aturan berdasarkan arahan dosen dan hasil konfirmasi klien.

**Catatan validasi:** Sebagian kebutuhan proyek masih berasal dari simulasi wawancara dengan data fiktif dan belum dikonfirmasi kepada klien nyata.

## 12. Cara Menjalankan dan Menguji

Persiapan lingkungan:

1. Membuat virtual environment:

   ```powershell
   py -3.14 -m venv .venv
   ```

2. Mengaktifkan virtual environment di Windows:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Memasang Flask:

   ```powershell
   python -m pip install Flask
   ```

Menjalankan aplikasi:

```powershell
python app.py
```

Menjalankan pengujian otomatis:

```powershell
python -m unittest discover -s tests -v
```

Ketentuan:

- Perintah dijalankan dari direktori utama proyek.
- Pengujian otomatis menggunakan `unittest` dari pustaka standar Python.
- Pengujian aplikasi Flask dapat menggunakan test client bawaan Flask.
- Perintah pengujian dapat disesuaikan jika metode pengujian proyek berubah.

Catatan:

- Python 3.14 menjadi versi yang diutamakan.
- Jika Python 3.14 tidak tersedia, gunakan Python versi 3.10 atau lebih baru yang kompatibel dengan Flask.
- Sesuaikan perintah pembuatan virtual environment dengan versi Python yang terpasang.
