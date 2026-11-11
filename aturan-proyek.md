# Aturan Proyek
## Sistem Informasi Pengelolaan Kontrakan

## 1. Tujuan
Dokumen ini menjadi pedoman pengembangan Sistem Informasi Pengelolaan Kontrakan agar proses pengembangan berjalan terstruktur, konsisten, dan sesuai kebutuhan proyek.

Aturan ini digunakan sebagai konteks bagi pengembang maupun AI ketika membantu pekerjaan proyek.

## 2. Informasi Teknologi

- Jenis aplikasi: Aplikasi berbasis web.
- Bahasa pemrograman: Belum ditentukan.
- Framework: Belum ditentukan.
- Database: Belum ditentukan.
- Versi teknologi: Akan ditentukan setelah pemilihan stack proyek.

**Catatan:** Pemilihan teknologi harus mempertimbangkan kebutuhan aplikasi, kemampuan pengembang, waktu pengerjaan, dan arahan dosen. AI tidak boleh menganggap teknologi tertentu sudah dipilih sebelum ada keputusan.

## 3. Struktur Folder Proyek

Struktur folder dan file yang digunakan saat ini:

```text
rpl-sistem-informasi-kontrakan/
├── .github/
├── docs/
│   ├── elisitasi/
│   │   ├── catatan-wawancara.md
│   │   ├── pedoman-wawancara.md
│   │   └── user-story.md
│   ├── kesepakatan-tim.md
│   ├── product-backlog.md
│   └── srs.md
├── .gitignore
├── aturan-proyek.md
├── jurnal-vibe-coding.md
├── PRD.md
└── README.md
```

Ketentuan:
- Dokumentasi kebutuhan disimpan di folder `docs/`.
- Dokumen elisitasi disimpan di `docs/elisitasi/`.
- Dokumen PRD dan aturan proyek disimpan di direktori utama.
- File baru harus ditempatkan sesuai fungsi dan jenis dokumennya.
- Struktur folder aplikasi akan ditambahkan setelah tahap implementasi dimulai.

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

## 6. Aturan Pengembangan

- Pengembangan harus mengacu pada PRD, SRS, User Story, dan Product Backlog.
- Setiap fitur harus memiliki kebutuhan dan kriteria penerimaan yang jelas.
- Implementasi tidak boleh menyimpang dari ruang lingkup proyek tanpa alasan dan keputusan yang terdokumentasi.
- Perubahan kebutuhan dan keputusan teknis harus dicatat dalam dokumentasi atau Jurnal Vibe Coding.
- Fitur yang belum diprioritaskan untuk proyek tidak boleh dikerjakan tanpa evaluasi ulang ruang lingkup.

## 7. Aturan Pengujian

- Setiap fitur harus diuji berdasarkan kriteria penerimaan yang telah ditentukan.
- Hasil pengujian harus diperiksa sebelum perubahan dinyatakan selesai.
- Kesalahan yang memengaruhi fungsi utama harus diperbaiki sebelum fitur di-merge.
- Metode dan perintah pengujian akan disesuaikan setelah bahasa pemrograman dan framework ditentukan.

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