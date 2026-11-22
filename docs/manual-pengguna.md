# Manual Pengguna — Sistem Informasi Pengelolaan Kontrakan

Manual ini ditujukan untuk **pemilik kontrakan** dan **kasir**. Tidak diperlukan
pengetahuan teknis. Setiap langkah diuji sendiri oleh penulis sebelum dicetak.

Data contoh pada gambar memakai data karangan, bukan data pelanggan nyata.

## 1. Masuk ke aplikasi

1. Buka alamat aplikasi di peramban (mis. http://192.168.1.10:8000).
2. Ketik **Nama pengguna** dan **Kata sandi**.
3. Tekan tombol **Masuk**.

![Gambar 1 - Halaman masuk](gambar/manual-01-login.png)

Bila salah, muncul pesan "Username atau password salah." Setelah 5 kali salah,
tunggu 5 menit sebelum mencoba lagi.

## 2. Melihat dan mencari kamar

1. Pilih menu **Kamar**.
2. Daftar menampilkan semua kamar beserta harga dan status (Tersedia/Terisi).
3. Ketik nomor kamar pada kotak **Cari**, lalu tekan **Cari**.
4. Tekan **Atur ulang** untuk melihat semua kamar lagi.

![Gambar 2 - Daftar kamar](gambar/manual-02-daftar-kamar.png)

## 3. Menambah kamar (khusus pemilik)

1. Pilih menu **Kamar**, lalu tekan **+ Tambah Kamar**.
2. Isi **Nomor kamar** (maksimal 20 karakter) dan **Harga sewa** (angka, tidak negatif).
3. Tekan **Simpan**.

![Gambar 3 - Form tambah kamar](gambar/manual-03-form-kamar.png)

## 4. Mencatat penyewa (khusus pemilik)

1. Pilih menu **Penyewa**, lalu tekan **+ Tambah Penyewa**.
2. Isi **Nama**, **Nomor telepon** (diawali 08, 10–13 digit, atau +628),
   dan **Alamat**.
3. Tekan **Simpan**.

## 5. Mencatat periode sewa (khusus pemilik)

1. Pilih menu **Periode Sewa**, lalu tekan **+ Tambah Periode Sewa**.
2. Pilih **Kamar** dan **Penyewa**.
3. Isi **Tanggal mulai** dan **Tanggal selesai** (format TTTT-BB-HH).
4. Isi **Harga sewa disepakati** dan (opsional) **Tanggal jatuh tempo**.
5. Tekan **Simpan**. Jika periode bertumpang tindih dengan sewa lain, sistem
   menolak.

![Gambar 4 - Form periode sewa](gambar/manual-04-form-sewa.png)

## 6. Mencatat pembayaran (pemilik dan kasir)

1. Pilih menu **Pembayaran**, lalu tekan **+ Catat Pembayaran**.
2. Pilih **Periode sewa**, isi **Tanggal pembayaran** dan **Jumlah bayar**
   (lebih dari 0).
3. Tekan **Simpan**. Status otomatis menjadi Lunas/Belum Lunas/Terlambat.

![Gambar 5 - Form pembayaran](gambar/manual-05-form-pembayaran.png)

## 7. Melihat laporan pendapatan (khusus pemilik)

1. Pilih menu **Laporan**.
2. Isi **Periode** (tanggal mulai dan selesai), lalu tekan **Tampilkan**.
3. Daftar pembayaran dan total pendapatan pada periode itu tampil.

## 8. Bila ada masalah

| Gejala | Yang dilakukan |
|---|---|
| Lupa kata sandi | Hubungi pemilik; pemilik membuat akun baru |
| Muncul "Akses ditolak" | Fitur itu khusus pemilik |
| Halaman tidak terbuka | Pastikan komputer server menyala dan terhubung ke jaringan toko |
| Muncul pesan merah di bawah isian | Baca pesannya, perbaiki isian, lalu Simpan lagi |
| "Terlalu banyak percobaan login" | Tunggu 5 menit sebelum mencoba lagi |
| Status "Terlambat" | Pembayaran belum lunas dan jatuh tempo terlewati |
