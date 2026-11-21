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
| 5 | Login, logout, dan pembatasan akses | 2 | Selesai |
| 6 | Peran pemilik dan kasir | 2 | Selesai |
| 7 | Penyempurnaan antarmuka dan pesan galat | 2 | Selesai |
| 8 | Status pembayaran | 2 | Selesai |
| 9 | Riwayat pembayaran dan jatuh tempo | 3 | Belum |
| 10 | Laporan pendapatan | 3 | Selesai |
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


---

## 8. Checkpoint Minggu 12 — Jobsheet 11 (RTM-2)

### Fitur yang didemokan (prototipe 5 menit)

1. Login dengan kata sandi ter-hash; pesan galat sama untuk username dan kata sandi salah.
2. Dua peran: pemilik (akses penuh) dan kasir (akses terbatas), dengan menu yang berubah.
3. Fitur inti: CRUD kamar dan penyewa, periode sewa, pembayaran, serta laporan pendapatan.
4. Penegakan akses di server: tamu dialihkan ke login, peran salah mendapat halaman 403,
   termasuk untuk permintaan POST.
5. Validasi dua lapis dan pesan sukses/galat dengan `role="status"`/`role="alert"`.

### Bukti yang disiapkan

- Hash kata sandi pada basis data (tanpa menampilkan kata sandi asli).
- Tabel uji login dan uji peran pada `docs/spesifikasi-fitur-akses.md`.
- Tangkapan layar tampilan pemilik, tampilan kasir, dan halaman 403.
- `docs/temuan-keamanan.md` berisi delapan temuan dengan tindakan.
- `SEMUA UJI LULUS` dan 53 pengujian unit dengan status OK.

### Fitur tertunda dan rencana

| Fitur tertunda | Rencana penyelesaian |
|---|---|
| Batas percobaan login | Pertemuan 12: pembatasan percobaan + jeda waktu, disertai uji pencegah |
| Token CSRF untuk POST | Pertemuan 12: token pada semua form dan penolakan permintaan tanpa token |
| Cookie `Secure` | Pertemuan 14: aktifkan bersama HTTPS saat deployment |
| UAT dengan klien nyata | Minggu 13-14 sesuai jadwal dosen |
| Uji beban 100 kamar | Sprint 3, setelah UAT awal |


---

## 9. Sprint 3 (Minggu 13-14) — Tindak Lanjut Checkpoint

| No | Item | Target | Rencana / tenggat |
|---:|---|---|---|
| 1 | Pengujian | ≥ 20 test case, ≥ 8 otomatis | Sudah terpenuhi: 21 kelompok uji di `uji_cepat.py` dan 59 pengujian unit; tambah uji UAT dari klien |
| 2 | UAT dengan klien nyata | Skenario dan tanda tangan/ Tanggapan | Minggu 13, jadwal menyesuaikan dosen |
| 3 | Rilis v1.0 | Tag `v1.0.0` di `main` | Minggu 14 setelah UAT dan perbaikan kecil |
| 4 | Rate limit multi-proses | Penyimpanan bersama (basis data/cache) | Minggu 13; `percobaan.py` tetap dipakai sebagai acuan logika |
| 5 | CSP ketat + HTTPS | Pindahkan `onsubmit` ke JS lokal, aktifkan Secure | Minggu 14, bersamaan dengan deployment produksi |
| 6 | Audit dependensi | `pip-audit` atau catatan hasil | Minggu 13 bila lingkungan mengizinkan pemasangan |
| 7 | Umpan balik dosen | Tabel F.3 di `docs/skrip-demo-checkpoint.md` | Diisi saat checkpoint, ditindaklanjuti Minggu 13 |

### Status temuan tertunda Jobsheet 12

- P-06 / temuan 12 (CSP ketat): minggu 14.
- Temuan 11 (penyimpanan batas login di memori): minggu 13.
- Temuan 13 (`pip-audit` tidak tersedia): minggu 13.
- UAT klien dan uji beban: minggu 13-14.

---

## 10. Penutup Sprint 3 — Hasil Jobsheet 13

| No | Item | Status | Keterangan |
|---:|---|---|---|
| 1 | Test case | Selesai | 39 test case, 8 KF terlacak, KF tanpa uji = 0 |
| 2 | Uji otomatis | Selesai | 29 fungsi uji baru; 111 passed + 23 subtests |
| 3 | Mutasi manual | Selesai | 3 dari 3 tertangkap; M1→TC-01, M2→TC-13, M3→TC-30 |
| 4 | Cacat | Selesai | 3 cacat diperbaiki dengan commit terpisah dan uji regresi |
| 5 | Rilis v1.0 | Minggu 14 | Tag `v1.0.0` setelah UAT dan perbaikan kecil |
| 6 | UAT klien | Minggu 14 | Rencana 7 skenario siap; jadwal belum dikonfirmasi klien |
| 7 | Kuesioner kegunaan | Minggu 14 | Dilaksanakan bersama UAT |
| 8 | Rate limit multi-proses | Minggu 13-14 | Penyimpanan bersama untuk `percobaan.py` |
| 9 | CSP ketat + HTTPS | Minggu 14 | Pindahkan `onsubmit` ke JS lokal |
| 10 | Audit dependensi | Minggu 13-14 | `pip-audit` bila lingkungan mengizinkan |

### Catatan

Dokumen `docs/laporan-pengujian.html` siap dicetak ke PDF untuk LMS.
Tidak ada kata sandi, kunci rahasia, atau berkas `.db` yang ditambahkan.

