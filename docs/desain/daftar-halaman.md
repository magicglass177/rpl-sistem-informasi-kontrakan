# Daftar Halaman Aplikasi
## Sistem Informasi Pengelolaan Kontrakan

**Aktor utama:** Pemilik Kontrakan

**Dasar penyusunan:** Daftar Use Case Jobsheet 5, SRS, ERD, dan Kamus Data Jobsheet 6.

## 1. Daftar Halaman

| No. | Halaman | Use Case | Aktor | Data yang Ditampilkan |
|---:|---|---|---|---|
| 1 | Login | UC-01 | Pemilik Kontrakan | `username`, input password. `password_hash` tidak ditampilkan. |
| 2 | Dashboard / Beranda | UC-05, UC-10, UC-14, UC-15 | Pemilik Kontrakan | Ringkasan jumlah kamar, status kamar, status pembayaran, periode sewa berakhir, dan total pendapatan. |
| 3 | Daftar Kamar | UC-03, UC-05 | Pemilik Kontrakan | `id_kamar`, `nomor_kamar`, `harga_sewa`, status ketersediaan (hasil perhitungan). |
| 4 | Form Kamar | UC-02, UC-04 | Pemilik Kontrakan | `nomor_kamar`, `harga_sewa`. |
| 5 | Daftar Penyewa | UC-06, UC-07 | Pemilik Kontrakan | `id_penyewa`, `nama`, `no_telepon`, `alamat`. |
| 6 | Form Penyewa | UC-06, UC-07 | Pemilik Kontrakan | `nama`, `no_telepon`, `alamat`. |
| 7 | Daftar Periode Sewa | UC-12, UC-13, UC-14 | Pemilik Kontrakan | `id_sewa`, `id_kamar`, `id_penyewa`, `tanggal_mulai`, `tanggal_selesai`, `tanggal_jatuh_tempo`, `harga_sewa_disepakati`, status periode sewa (hasil perhitungan). |
| 8 | Form Periode Sewa | UC-08, UC-12, UC-13 | Pemilik Kontrakan | `id_kamar`, `id_penyewa`, `tanggal_mulai`, `tanggal_selesai`, `tanggal_jatuh_tempo`, `harga_sewa_disepakati`. |
| 9 | Daftar Pembayaran | UC-10, UC-11 | Pemilik Kontrakan | `id_pembayaran`, `id_sewa`, `tanggal_pembayaran`, `jumlah_bayar`, nama penyewa, nomor kamar, status pembayaran (hasil perhitungan). |
| 10 | Form Catat Pembayaran | UC-09 | Pemilik Kontrakan | `id_sewa`, `tanggal_pembayaran`, `jumlah_bayar`. |
| 11 | Laporan Pendapatan | UC-15, UC-16 | Pemilik Kontrakan | Filter periode, daftar transaksi berdasarkan `tanggal_pembayaran`, `jumlah_bayar`, total pendapatan (hasil perhitungan). |

## 2. Aturan dan Catatan Antarmuka

1. Seluruh halaman pengelolaan hanya dapat diakses oleh Pemilik Kontrakan setelah login.
2. Dashboard menampilkan ringkasan informasi dan menyediakan navigasi menuju halaman pengelolaan.
3. Status ketersediaan kamar dihitung berdasarkan penempatan penyewa dan periode sewa.
4. Form Periode Sewa harus memvalidasi agar tidak terjadi periode sewa yang bertumpang tindih pada kamar yang sama.
5. `tanggal_jatuh_tempo` bersifat opsional sesuai KF-12.
6. Status pembayaran dihitung dari catatan pembayaran dan aturan jatuh tempo, bukan disimpan sebagai kolom tersendiri.
7. Satu periode sewa dapat memiliki beberapa catatan pembayaran untuk mendukung pembayaran bertahap.
8. Laporan pendapatan dihitung berdasarkan tanggal pembayaran diterima.
9. Fitur unduh laporan pada UC-16 merupakan fitur opsional dengan prioritas Could.

## 3. Cakupan Use Case

| Prioritas | Use Case | Cakupan |
|---|---|---|
| Must | UC-01 sampai UC-09 | Tercakup |
| Must / Should | UC-10 sampai UC-15 | Tercakup |
| Could | UC-16 | Tercakup sebagai fitur opsional |

## 4. Ringkasan

Rancangan awal menghasilkan 11 halaman yang mencakup seluruh 15 Use Case berprioritas Must dan Should serta satu Use Case berprioritas Could. Setiap halaman dirancang berdasarkan kebutuhan fungsional dan atribut yang terdapat pada kamus data. Rancangan ini menjadi dasar pembuatan peta navigasi dan wireframe pada langkah berikutnya.
