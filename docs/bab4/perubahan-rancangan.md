# Perubahan terhadap Rancangan Awal (Bab 3 → hasil akhir)

| Bagian rancangan | Rancangan awal (Bab 3) | Hasil akhir dan alasan | Dampak |
|---|---|---|---|
| ERD — tabel penjualan | Rancangan awal menyebut tabel penjualan | Tidak diimplementasi; laporan dibuat dari tabel pembayaran. Alasan: kebutuhan pendapatan dapat dipenuhi dari pembayaran yang tercatat | Bab 3 diperbarui |
| Tabel kamar — status ketersediaan | Rancangan awal menyimpan status ketersediaan sebagai kolom | Status dihitung dari periode sewa aktif. Alasan: menghindari data duplikat (KF-05) | Bab 3 diperbarui |
| Tabel sewa — harga_sewa_disepakati | Belum ada atribut rancangan | Ditambahkan untuk mempertahankan riwayat harga (usulan simulasi) | Bab 3 diperbarui |
| Tanggal jatuh tempo | Wajib | Opsional (boleh NULL) sesuai prioritas KF-12 | Bab 3 diperbarui |
| Penghapusan data induk | Belum ditetapkan | RESTRICT (kamar/penyewa yang masih dipakai sewa tidak dapat dihapus) | Bab 3 diperbarui |
| Batas percobaan login | Tidak ada pada PRD awal | Ditambahkan pada Jobsheet 12 (keamanan) | Dijelaskan di 4.3 |
| Token CSRF | Tidak ada pada PRD awal | Ditambahkan pada Jobsheet 12 (keamanan) | Dijelaskan di 4.3 |
| Unduh laporan (KF-16) | Could | Belum diimplementasi; ditunda ke v1.1 | Dijelaskan di 4.6 |
