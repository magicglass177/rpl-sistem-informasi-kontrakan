# Hasil UAT — Jobsheet 14 (SIMULASI)

> **Status: SIMULASI, bukan UAT nyata.** Lingkungan ini tidak memiliki klien nyata.
> Hasil di bawah diisi dengan narasumber fiktif (PT dan BM) sebagai latihan
> format dan perhitungan. Penjadwalan dan pelaksanaan UAT nyata menjadi tugas
> PT/BM (Langkah 11–12 dan Pertemuan 15). Jangan menampilkan dokumen ini
> sebagai bukti UAT nyata kepada dosen.

## Identitas

- Proyek: Sistem Informasi Pengelolaan Kontrakan
- Peserta simulasi: Pemilik kontrakan (fiktif), Kasir (fiktif)
- Pengamat: anggota kelompok
- Tanggal simulasi: 22 November 2026
- Durasi: 45 menit
- Lingkungan: aplikasi berjalan di laptop kelompok, data karangan, akun uji
- Persetujuan merekam hasil: ☐ (belum — simulasi)

## Lembar skenario (Lampiran F.1)

| ID | Skenario | Lulus? | Waktu (mnt) | Perlu bantuan? | Kesulitan / kutipan |
|---|---|---|---|---|---|
| UAT-1 | Masuk sebagai pemilik | Ya | 1 | Tidak | "Mudah, mirip aplikasi lain" |
| UAT-2 | Mendaftarkan kamar baru | Ya | 2 | Tidak | "Tombolnya jelas" |
| UAT-3 | Menyimpan data penyewa | Ya | 2 | Tidak | "Nomor telepon harus diawali 08, saya paham" |
| UAT-4 | Menentukan masa sewa | Ya | 3 | Ya (1x) | "Saya bingung urutan tanggal; dibantu pengamat" |
| UAT-5 | Mencatat pembayaran | Ya | 2 | Tidak | "Status langsung Lunas, senang" |
| UAT-6 | Melihat laporan pendapatan | Ya | 2 | Tidak | "Totalnya langsung terlihat" |
| UAT-7 | Kasir mencoba hapus kamar | Ya | 1 | Tidak | "Tombol tidak ada, aman" |

Semua 7 skenario lulus.

## Skor SUS (Lampiran F.2–F.3)

Jawaban (1–5) sesuai urutan butir 1–10.

| Responden | Jawaban | Skor SUS |
|---|---|---|
| Pemilik (fiktif) | [4, 2, 4, 1, 4, 2, 5, 2, 4, 1] | 82.5 |
| Kasir (fiktif) | [5, 1, 4, 2, 4, 1, 5, 1, 5, 2] | 90.0 |
| Rata-rata | — | 86.3 |

Skor dihitung dengan `docs/uat/hitung_sus.py` (salinan ada di Lampiran F.3 jobsheet).
Dengan 2 responden, skor hanya indikasi kasar.

## Catatan terbuka (kutipan pengguna)

1. "Tanggal mulai dan selesai saya sering tertukar. Mungkin urutannya bisa
   dibuat lebih jelas." (kesulitan penggunaan)
2. "Saya ingin bisa melihat kamar yang terisi tanpa membuka daftar semua."
   (permintaan perubahan)
3. "Tulisan merah pada stok menipis itu bagus." (positif)

## Tabel triase (Lampiran F.4)

| No | Temuan | Jenis | Keputusan | Penanggung jawab / tenggat |
|---|---|---|---|---|
| 1 | Tanggal mulai/selesai sering tertukar | Kesulitan penggunaan | Perbaiki manual (urutan field + contoh) | Anggota kelompok / sebelum rilis |
| 2 | Filter kamar terisi tanpa membuka semua | Permintaan perubahan | Calon v1.1 | Disepakati dengan klien |
| 3 | Tombol hapus tidak ada untuk kasir | — (sesuai rancangan) | Tolak dengan alasan: akses terbatas by design | — |
| 4 | Status pembayaran langsung tampil | Positif | Tidak ada tindakan | — |

Persetujuan klien untuk mencatat hasil: ☐ (belum — simulasi).

## Tindak lanjut

- Cacat UAT: tidak ada cacat baru yang menyimpang dari PRD.
- Kesulitan: perbaiki urutan field tanggal dan tambah contoh pada manual.
- Permintaan perubahan: masuk daftar calon v1.1, disepakati dengan klien.
- Rilis 1.0.0 tidak diubah mendadak.

## Keterbatasan (jujur)

- Ini simulasi, bukan UAT nyata. Tidak ada klien nyata, tidak ada persetujuan,
  tidak ada bukti foto lembar skenario.
- UAT nyata dijadwalkan pada Pertemuan 14 (PT/BM) dengan klien sebenarnya.
- Skor SUS 85.0 hanya indikasi kasar dengan 2 responden fiktif.
