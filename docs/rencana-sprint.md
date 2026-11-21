# Rencana Sprint RTM-2

## Sistem Informasi Pengelolaan Kontrakan

**Disusun:** 21 November 2026
**Dasar:** `PRD.md` v1.1, `docs/product-backlog.md`, SRS, dan ketentuan RTM-2 pada Jobsheet 9.
**Pengembang:** Bayu Nanda Pamungkas (Product Owner, Scrum Master, Developer).

---

## 1. Sasaran RTM-2

| Butir | Target |
|---|---|
| Aplikasi | Minimal 10 KF dan 4 KNF terimplementasi dan teruji |
| Autentikasi | Minimal 2 peran |
| Validasi | Validasi masukan di sisi server untuk seluruh form |
| Basis data | Relasional, sesuai ERD dan `docs/desain/schema.sql` |
| Pengujian | Minimal 20 test case, minimal 8 di antaranya otomatis, ditambah UAT |
| Dokumentasi | README, manual pengguna, dan Laporan Bab 4 |
| Proses | Riwayat Git dengan kontribusi jelas dan Jurnal Vibe Coding minimal 30 entri |

**Catatan peran:** PRD saat ini hanya menetapkan peran pemilik kontrakan. Target dua peran pada RTM-2 ditandai **[Asumsi]** dan perlu dikonfirmasi kepada dosen. Rencana awal menggunakan peran **Pemilik** dan **Pengelola**.

---

## 2. Status Baseline per 21 November 2026

| Komponen | Status |
|---|---|
| Kerangka Flask, koneksi SQLite, `init_db()` | Selesai |
| Skema 5 tabel dan 2 trigger | Selesai, tidak berubah |
| CRUD kamar (KF-02, KF-03, KF-04, KF-05) | Selesai dan diuji |
| CRUD penyewa (KF-06) | Selesai dan diuji |
| Pengujian otomatis | 53 tes baru lulus + 4 skrip skema/validasi |
| Autentikasi dan otorisasi (KF-01, KNF-04) | Belum |
| Relasi sewa, pembayaran, laporan | Belum |
| Jurnal Vibe Coding | 16 siklus Jobsheet 9 tercatat |

---

## 3. Rencana Sprint 1–4

### Sprint 1 — Minggu 9–10: Kerangka, CRUD, dan Relasi

| Target | Kebutuhan | Status |
|---|---|---|
| Kerangka proyek dan skema | Dasar KF-02, KF-03 | Selesai |
| CRUD kamar | KF-02, KF-03, KF-04, KF-05 | Selesai |
| CRUD penyewa | KF-06, KNF-03 | Selesai |
| Form dan validasi periode sewa | KF-07, KF-13 | Minggu 10 |
| Pencegahan periode sewa bertumpang tindih | KF-08 | Minggu 10 |
| Pencatatan pembayaran bertahap | KF-09 | Minggu 10 |
| Pencarian dan penyaringan daftar | Pendukung KF-03, KF-06 | Sebagian selesai |

**Definition of Done Sprint 1:** CRUD kamar dan penyewa berada di `main`; form sewa dan pembayaran berfungsi; seluruh validasi server diuji; PR ditinjau dan digabung.

### Sprint 2 — Minggu 11–12: Antarmuka, Autentikasi, dan Code Review

| Target | Kebutuhan | Catatan |
|---|---|---|
| Login dan logout | KF-01, KNF-04 | Password memakai hash; sesi Flask |
| Pembatasan akses halaman pengelolaan | KNF-04 | Seluruh rute `/kamar`, `/penyewa`, `/sewa`, `/pembayaran` dilindungi |
| Peran pemilik dan pengelola | **[Asumsi]** target RTM-2 | Perlu konfirmasi dosen |
| Penyempurnaan antarmuka sesuai wireframe | KNF-01 | Form maksimal lima langkah |
| Code review dan perbaikan keamanan | KNF-04 | Tinjau `debug`, sesi, CSRF, pesan galat |
| Status pembayaran | KF-11 | Lunas, belum lunas, terlambat |

**Checkpoint Minggu 12:** minimal 10 KF dan 4 KNF sudah terimplementasi; autentikasi berjalan; tidak ada temuan keamanan kritis; pengujian otomatis minimal 8 test case.

### Sprint 3 — Minggu 13–14: Pengujian, UAT, dan Rilis v1.0

| Target | Kebutuhan |
|---|---|
| Riwayat pembayaran | KF-10 |
| Tanggal jatuh tempo dan penanda terlambat | KF-12 |
| Periode sewa yang akan berakhir | KF-14 |
| Laporan pendapatan berdasarkan periode | KF-15 |
| Uji kinerja daftar kamar (100 data, maksimal 3 detik) | KNF-02 |
| Minimal 20 test case dan minimal 8 otomatis | Seluruh KF/KNF |
| UAT dengan pengguna/perwakilan | Seluruh alur utama |
| Rilis v1.0 | Seluruh fitur Must dan Should |

### Sprint 4 — Minggu 15–16: Perbaikan, Laporan Bab 4, dan Demo

| Target | Keterangan |
|---|---|
| Perbaikan hasil UAT dan progress check | Tidak menambah fitur baru tanpa persetujuan |
| Laporan Bab 4 (Implementasi dan Pengujian) | Memuat bukti uji, temuan, debugging, dan analisis jurnal |
| README dan manual pengguna | Cara memasang, menjalankan, dan menguji |
| Demo Minggu 16 | Menunjukkan aplikasi dan menjelaskan kode secara perorangan |

---

## 4. Papan Tugas Ringkas

| Prioritas | Tugas | Sprint | Status |
|---:|---|---:|---|
| 1 | CRUD kamar dan penyewa | 1 | Selesai |
| 2 | Form periode sewa dan validasi tanggal | 1 | Belum |
| 3 | Pencegahan sewa bertumpang tindih (trigger + pesan) | 1 | Sebagian (trigger sudah ada) |
| 4 | Form pembayaran bertahap | 1 | Belum |
| 5 | Login, logout, dan pembatasan akses | 2 | Belum |
| 6 | Peran pemilik dan pengelola **[Asumsi]** | 2 | Belum |
| 7 | Penyempurnaan antarmuka dan pesan galat | 2 | Sebagian |
| 8 | Status pembayaran | 2 | Belum |
| 9 | Riwayat pembayaran dan jatuh tempo | 3 | Belum |
| 10 | Laporan pendapatan | 3 | Belum |
| 11 | Uji beban 100 kamar | 3 | Belum |
| 12 | UAT dan rilis v1.0 | 3 | Belum |
| 13 | Laporan Bab 4 dan demo | 4 | Belum |

---

## 5. Risiko dan Rencana Mitigasi

| Risiko | Dampak | Mitigasi |
|---|---|---|
| Target dua peran belum ada di PRD | Pekerjaan autentikasi bisa berubah arah | Konfirmasi dosen pada Minggu 10; tandai sebagai asumsi |
| Aturan hapus data yang memiliki riwayat belum final | Perilaku hapus dapat berubah | Gunakan `ON DELETE RESTRICT` sementara dan catat keputusan |
| Waktu pengerjaan individu terbatas | Sprint 2–3 berpotensi mundur | Prioritaskan KF Must; Should dikerjakan setelah Must stabil |
| UAT dengan klien nyata belum terjadwal | Syarat RTM-2 belum terpenuhi | Jadwalkan UAT pada Minggu 13–14 dengan perwakilan pengguna |
| Perubahan skema saat implementasi | Merusak data dan pengujian | Skema dibekukan; perubahan harus melalui keputusan dan migrasi |

---

## 6. Pembagian Fokus Minggu Berikutnya (Pertemuan 10)

1. Membuat modul periode sewa (KF-07, KF-13) dengan pilihan kamar dan penyewa.
2. Menampilkan pesan yang jelas saat trigger menolak periode bertumpang tindih (KF-08).
3. Menambahkan pencarian dan penyaringan pada daftar kamar dan penyewa.
4. Menyiapkan struktur autentikasi dan hash kata sandi untuk Sprint 2.


## 7. Status Setelah Jobsheet 10 (Minggu 10)

- Modul periode sewa (`sewa`) berjalan dengan JOIN, form pilihan induk, transaksi, pencarian, dan penyaringan.
- Uji regresi `tests/uji_cepat.py` lulus ("SEMUA UJI LULUS").
- 53 pengujian unit lulus.
- Refactoring `_render_form_kamar` selesai.
- Latihan konflik merge selesai.
- `main` telah diperbarui dan di-push.

### Prioritas Sprint 2 (Minggu 11–12)

1. Autentikasi dan peran (KF-01, KNF-04).
2. Penyempurnaan antarmuka sesuai wireframe (KNF-01).
3. Validasi sisi server untuk seluruh form.
4. Code review dan penanganan temuan keamanan.
5. Status pembayaran (KF-11).

**Checkpoint Minggu 12:** minimal 10 KF dan 4 KNF terimplementasi; autentikasi berjalan; tidak ada temuan keamanan kritis; pengujian otomatis minimal 8 test case.
PY