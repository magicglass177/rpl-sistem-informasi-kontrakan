# Keputusan Revisi Berdasarkan Design Review

## 1. Konteks

Revisi dilakukan berdasarkan Simulasi Design Review Individu pada 15 November 2026.

Tinjauan ini merupakan simulasi dengan bantuan AI, bukan hasil review silang kelompok atau persetujuan langsung dari klien.

## 2. Tabel Keputusan Masukan

| No. | Masukan Penelaah | Keputusan | Alasan dan Tindak Lanjut |
|---|---|---|---|
| 1 | Form pembayaran perlu menampilkan harga sewa disepakati, total pembayaran diterima, dan sisa pembayaran. | Diterima | Informasi tersebut membantu pemilik kontrakan memahami kewajiban pembayaran sebelum mencatat transaksi. Anotasi WF-10 dan wireframe HTML/CSS diperbarui dengan tiga informasi ringkasan. |
| 2 | Validasi periode sewa yang bertumpang tindih harus memberikan pesan kesalahan yang jelas. | Diterima; sudah terpenuhi | Anotasi WF-08 telah memuat pesan penolakan periode yang bertumpang tindih dan TC-11 menguji kondisi tersebut. Tidak diperlukan perubahan tambahan. |
| 3 | Aturan penentuan status terlambat dan penanganan pembayaran melebihi kewajiban belum jelas. | Perlu dikonfirmasi kepada klien | Aturan bisnis belum ditetapkan. Perlu konfirmasi mengenai dasar perhitungan keterlambatan, masa tenggang jika ada, serta tindakan ketika pembayaran melebihi kewajiban. Tidak mengubah SRS, kamus data, atau test case sebelum keputusan diperoleh. |

## 3. Rincian Revisi yang Diterapkan

### WF-10 — Form Catat Pembayaran

Ditambahkan tiga informasi ringkasan:

1. Harga Sewa Disepakati.
2. Total Pembayaran Diterima.
3. Sisa Pembayaran.

Ketiga informasi ditampilkan sebagai ringkasan berdasarkan periode sewa yang dipilih. Nilai pada wireframe merupakan data ilustrasi, bukan hasil perhitungan aplikasi.

Penomoran elemen WF-10 diselaraskan dengan anotasi:

- 01 Periode Sewa
- 02 Harga Sewa Disepakati
- 03 Total Pembayaran Diterima
- 04 Sisa Pembayaran
- 05 Tanggal Pembayaran
- 06 Jumlah Bayar
- 07 Pesan Validasi
- 08 Simpan Pembayaran dan Batal

### WF-08 — Form Periode Sewa

Tidak ada perubahan tambahan karena pesan validasi periode bertumpang tindih telah tersedia dan diuji melalui TC-11.

## 4. Dokumen yang Tidak Diubah

- `docs/srs.md`: aturan keterlambatan dan kelebihan pembayaran masih menunggu konfirmasi.
- `docs/desain/kamus-data.md`: belum ada keputusan bisnis baru yang membenarkan perubahan struktur data.
- `docs/pengujian/rencana-uji.md`: TC-11 telah mencakup validasi periode bertumpang tindih. TC-14 belum menguji status terlambat karena aturan perhitungannya belum ditentukan.
- `docs/desain/wireframe/navigasi.mmd`: tidak ada perubahan alur navigasi.

## 5. Kesimpulan

Masukan pertama diterima dan diterapkan pada WF-10. Masukan kedua diterima dan dinyatakan telah tercakup dalam rancangan serta pengujian yang ada. Masukan ketiga ditunda sampai ada klarifikasi dari klien.

Revisi ini merupakan hasil simulasi pembelajaran individu. Implementasi aplikasi belum diubah dan belum dianggap telah lulus pengujian berdasarkan revisi desain ini.
