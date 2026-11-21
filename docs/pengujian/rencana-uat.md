# Rencana User Acceptance Test (UAT) — Jobsheet 13

Proyek: Sistem Informasi Pengelolaan Kontrakan
Tahap: **perencanaan** — pelaksanaan bersama klien dan kuesioner kegunaan
dilaksanakan pada Pertemuan 14.

## Identitas dan tujuan

- **Tujuan:** Memastikan pemilik dan kasir dapat memakai aplikasi untuk pekerjaan
  harian: mencatat kamar, menyimpan data penyewa, mengatur periode sewa,
  mencatat pembayaran, dan melihat laporan pendapatan.
- **Jenis pengujian:** Validasi — "apakah kita membangun produk yang benar?"
  (berbeda dari verifikasi yang sudah dilakukan lewat test case dan pytest).
- **Peserta pihak klien:** Pemilik kontrakan (peran pemilik), satu kasir (peran kasir).
- **Pengamat:** Anggota kelompok (mengisi lembar ini, tidak membantu menjalankan).
- **Waktu:** Minggu 14, hari/jam disepakati — **belum dikonfirmasi tertulis**.
- **Tempat:** Lokasi klien / laboratorium; durasi 60 menit.
- **Lingkungan:** Aplikasi berjalan di laptop kelompok atau server uji; browser
  mutakhir; basis data uji berisi **data karangan**; akun uji pemilik dan kasir.
- **Data karangan:** Kamar `A-01` (Rp850.000) dan `B-01` (Rp750.000);
  penyewa `Andi Pratama` (081234567890); sewa 1–31 Maret 2026;
  pembayaran 10 Maret 2026 sebesar Rp850.000.
- **Tidak dipakai:** data pribadi nyata pelanggan, kata sandi produksi, berkas `.db` nyata.

## Kriteria lulus

1. Semua enam skenario inti (UAT-1…UAT-6) dinyatakan **Lulus** oleh klien.
2. Tidak ada cacat berkeparahan **Kritis** atau **Tinggi** yang masih terbuka.
3. Klien menyatakan dapat memakai aplikasi untuk alur kerjanya sehari-hari.
4. Setiap temuan dicatat dan dipindah ke `docs/pengujian/laporan-cacat.md`
   sebagai cacat atau permintaan perubahan.

Jika kriteria 1 atau 2 tidak terpenuhi, UAT dinyatakan **Tidak Lulus** dan
dijadwalkan ulang setelah perbaikan.

## Skenario UAT (bahasa klien, bukan bahasa teknis)

| ID | KF | Skenario (bahasa klien) | Langkah | Hasil diharapkan | Lulus? | Catatan |
|---|---|---|---|---|---|---|
| UAT-1 | KF-01 | Saya masuk sebagai pemilik | 1) Buka halaman masuk 2) Tulis nama pengguna dan kata sandi 3) Tekan Masuk | Halaman utama tampil; nama dan peran saya terlihat |  |  |
| UAT-2 | KF-02 | Saya mendaftarkan kamar baru yang kosong | 1) Pilih Kamar 2) Tekan Tambah Kamar 3) Isi nomor `C-01` dan harga `800000` 4) Simpan | Kamar `C-01` muncul di daftar dengan status Tersedia |  |  |
| UAT-3 | KF-06 | Saya menyimpan data penyewa baru | 1) Pilih Penyewa 2) Tekan Tambah 3) Isi nama `Andi Pratama`, telepon `081234567890`, alamat 4) Simpan | Data penyewa muncul di daftar |  |  |
| UAT-4 | KF-13 | Saya menentukan masa sewa sebuah kamar | 1) Pilih Periode Sewa 2) Tambah 3) Pilih kamar `A-01` dan penyewa `Andi` 4) Isi mulai `2026-03-01`, selesai `2026-03-31` 5) Simpan | Periode sewa tersimpan dan tampil; kamar `A-01` berubah menjadi Terisi pada masa itu |  |  |
| UAT-5 | KF-09 | Saya mencatat pembayaran sewa yang masuk | 1) Pilih Pembayaran 2) Tambah 3) Pilih periode sewa `Andi` 4) Isi tanggal `2026-03-10` dan jumlah `850000` 5) Simpan | Pembayaran tercatat dan statusnya menjadi Lunas |  |  |
| UAT-6 | KF-15 | Saya melihat pendapatan bulan Maret | 1) Pilih Laporan 2) Isi periode `2026-03-01` sampai `2026-03-31` 3) Lihat daftar | Pembayaran `Andi` tampil bersama total pendapatan untuk periode itu |  |  |
| UAT-7 | KF-08 | Kasir mencoba menghapus kamar | 1) Masuk sebagai kasir 2) Buka daftar kamar 3) Cari tombol hapus; ketik alamat hapus langsung | Tombol tidak ada; alamat langsung ditolak dengan halaman "Akses Ditolak" |  |  |

## Cara merekam temuan

1. Pengamat mengisi kolom **Lulus?** (Ya / Tidak) dan **Catatan** pada tabel di atas.
2. Untuk setiap "Tidak", tulis langkah yang dipakai klien dan apa yang terjadi.
3. Temuan dipindah ke `docs/pengujian/laporan-cacat.md` dengan ID baru,
   keparahan, prioritas, dan keputusan: cacat atau permintaan perubahan.
4. Lembar hasil UAT dan kuesioner kegunaan dilampirkan pada laporan akhir
   (Pertemuan 14).

## Status penjadwalan (jujur)

- [ ] Tanggal dan jam disepakati dengan klien
- [ ] Tempat dikonfirmasi
- [ ] Peserta dari pihak klien dikonfirmasi
- [ ] Skenario dikirim untuk disetujui klien
- [ ] Balasan klien dicatat

**Belum tercentang.** Lingkungan ini tidak memiliki kontak klien nyata; dokumen
ini adalah rencana berbasis simulasi narasumber fiktif PT dan BM pada
`docs/elisitasi/catatan-wawancara.md`. Penjadwalan nyata menjadi tugas PT/BM
pada Langkah 15 dan Pertemuan 14.
