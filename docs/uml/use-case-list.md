# Daftar Use Case
## Sistem Informasi Pengelolaan Kontrakan

| ID | Nama Use Case | Aktor | KF terkait | Prioritas |
|---|---|---|---|---|
| UC-01 | Login | Pemilik Kontrakan | KF-01 | Must |
| UC-02 | Menambahkan Data Kamar | Pemilik Kontrakan | KF-02 | Must |
| UC-03 | Melihat Daftar Kamar | Pemilik Kontrakan | KF-03 | Must |
| UC-04 | Mengubah Data Kamar | Pemilik Kontrakan | KF-04 | Should |
| UC-05 | Melihat Status Ketersediaan Kamar | Pemilik Kontrakan | KF-05 | Must |
| UC-06 | Menambahkan Data Penyewa | Pemilik Kontrakan | KF-06 | Must |
| UC-07 | Mengubah Data Penyewa | Pemilik Kontrakan | KF-06 | Must |
| UC-08 | Menghubungkan Penyewa dengan Kamar | Pemilik Kontrakan | KF-07, KF-08 | Must |
| UC-09 | Mencatat Pembayaran Sewa | Pemilik Kontrakan | KF-09 | Must |
| UC-10 | Melihat Status Pembayaran | Pemilik Kontrakan | KF-11 | Must |
| UC-11 | Melihat Riwayat Pembayaran | Pemilik Kontrakan | KF-10 | Should |
| UC-12 | Mengelola Periode Sewa | Pemilik Kontrakan | KF-13 | Must |
| UC-13 | Melihat Tanggal Jatuh Tempo | Pemilik Kontrakan | KF-12 | Should |
| UC-14 | Melihat Periode Sewa yang Mendekati atau Telah Berakhir | Pemilik Kontrakan | KF-14 | Should |
| UC-15 | Melihat Laporan Pendapatan | Pemilik Kontrakan | KF-15 | Must |
| UC-16 | Mengunduh Laporan Pendapatan | Pemilik Kontrakan | KF-16 | Could (Opsional) |

## Catatan

1. Aktor utama seluruh use case adalah Pemilik Kontrakan.
2. KF-08 merupakan aturan validasi dalam UC-08, bukan use case terpisah.
3. KF-08 berprioritas Must sesuai dengan tabel kebutuhan fungsional dan tabel prioritas pada SRS.
4. UC-16 merupakan fitur Could (opsional), tetapi tetap dicantumkan sebagai bagian dari daftar use case.
5. UC-06 dan UC-07 merupakan pemisahan aktivitas tambah dan ubah data penyewa berdasarkan KF-06.
