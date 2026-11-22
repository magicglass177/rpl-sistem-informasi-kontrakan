# Catatan Perubahan

Format: [versi] - tanggal. Bagian: Ditambahkan, Diubah, Diperbaiki, Keamanan.

## [1.0.0] - 2026-11-22

### Ditambahkan
- Login dengan dua peran (pemilik, kasir) dan pembatasan akses per peran.
- Kelola kamar: tambah, ubah, hapus, cari, dan status ketersediaan.
- Kelola penyewa: tambah, ubah, hapus, cari.
- Periode sewa: tambah, cek tumpang tindih, status aktif/berakhir.
- Catat pembayaran; status Lunas/Belum Lunas/Terlambat; riwayat.
- Laporan pendapatan berdasarkan periode pembayaran.
- Pencadangan basis data (`python cadangkan.py`).
- Versi aplikasi terlihat di kaki halaman (v1.0.0).

### Diperbaiki
- Validasi harga dan jumlah dibatasi ke DECIMAL(12,2).
- Tanggal hanya menerima format TTTT-BB-HH (Python 3.11+).
- Pencarian kamar/penyewa membaca `%` dan `_` sebagai huruf biasa.

### Keamanan
- Token CSRF pada semua form POST.
- Batas percobaan login (5 gagal/5 menit) dan logging tanpa kata sandi.
- Konfigurasi produksi: kunci rahasia dari lingkungan, cookie Secure, header keamanan.
- Konfirmasi hapus via POST; decorator peran di seluruh rute.

### Pengujian
- 39 test case dengan partisi ekuivalen dan nilai batas.
- 29 fungsi uji pytest (111 lulus) + 59 unittest + uji asap.
- 3 cacat diperbaiki dengan uji regresi (D-01, D-02, D-03).
- Mutasi manual 3 dari 3 tertangkap.
