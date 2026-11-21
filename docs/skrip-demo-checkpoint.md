# Skrip Demo Checkpoint Minggu 12 — Jobsheet 12

Durasi target: **≤ 5 menit**. Jangan menampilkan kata sandi, `.env`, atau berkas `.db`.

## Pembagian waktu

| Menit | Pembicara | Isi |
|---|---|---|
| 0:00–0:30 | [Nama 1] | Klien: pemilik kontrakan. Masalah: data kamar, penyewa, sewa, dan pembayaran tersebar. Dua peran: pemilik (penuh) dan kasir (terbatas). |
| 0:30–2:30 | [Nama 2] | Alur peran pemilik: masuk → tambah kamar A-01 → ubah harga → cari "A-01" → catat penyewa + periode sewa → catat pembayaran → lihat laporan pendapatan. Tunjukkan pesan sukses. |
| 2:30–3:30 | [Nama 1] | Keluar, lalu masuk sebagai kasir. Tunjukkan menu lebih singkat (tanpa Penyewa dan Laporan), kolom Aksi tidak ada di daftar kamar. Ketik langsung `/kamar/tambah` → 403. Tunjukkan satu perbaikan hari ini: POST tanpa token CSRF ditolak 400 / percobaan login ke-6 ditolak 429. |
| 3:30–4:30 | [Nama 3] | Yang belum selesai: UAT, uji beban, rate limit multi-proses, CSP/HTTPS. Rencana Sprint 3: ≥20 test case (≥8 otomatis), UAT klien, rilis v1.0. |
| 4:30–5:00 | Semua | Pertanyaan dan umpan balik dosen. |

## Data uji karangan

- Kamar: `A-01` (Rp850.000), `B-01` (Rp750.000).
- Penyewa: `Andi Pratama`, telepon `081234567890`, alamat `Jalan Melati No. 10`.
- Sewa: `A-01`, 1–31 Maret 2026, harga disepakati `850000`.
- Pembayaran: 10 Maret 2026, `850000` → status `Lunas`.
- Akun: dibuat lokal lewat `python scripts/buat_pengguna.py` untuk peran `pemilik` dan `kasir`.

## Rencana cadangan

- Rekaman layar singkat (< 5 menit) bila internet/aplikasi bermasalah.
- Tangkapan layar: tampilan pemilik, tampilan kasir, halaman 403, pesan 400 CSRF.
- Jika demo terpotong, prioritaskan: login → dua peran → 403 → laporan.

## Daftar periksa checkpoint (Lampiran F.2)

| No | Butir | Ya / Tidak | Catatan |
|---:|---|---|---|
| 1 | Fitur inti sesuai PRD berjalan pada alur demo |  |  |
| 2 | Login dan dua peran berfungsi; aksi terlarang ditolak |  |  |
| 3 | Data tersimpan di basis data dan sesuai skema |  |  |
| 4 | Antarmuka konsisten dan sesuai wireframe |  |  |
| 5 | Kelompok jujur tentang batasan dan risiko |  |  |
| 6 | Setiap anggota dapat menjawab satu pertanyaan tentang kodenya |  |  |
| 7 | Demo selesai dalam ≤ 5 menit |  |  |

## Umpan balik dosen (Lampiran F.3)

| No | Umpan balik | Tindak lanjut | Tenggat |
|---:|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
