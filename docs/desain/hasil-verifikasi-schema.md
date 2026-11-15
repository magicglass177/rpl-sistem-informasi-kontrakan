# Hasil Verifikasi dan Pengujian Skema Database

## 1. Tujuan

Verifikasi dilakukan untuk memeriksa kesesuaian draf skema database
dengan ERD, kamus data, dan kebutuhan fungsional Sistem Informasi
Pengelolaan Kontrakan.

Lampiran B.2 dan Lampiran E tidak tersedia pada bahan jobsheet.
Oleh karena itu, dibuat skrip pengujian pengganti dan checklist
verifikasi berdasarkan dokumen proyek.

## 2. Berkas yang Digunakan

- `docs/desain/erd.mmd`
- `docs/desain/kamus-data.md`
- `docs/desain/schema.sql`
- `tests/cek_skema.py`
- `tests/cek_skema_lanjutan.py`
- `tests/cek_validasi_telepon.py`

## 3. Checklist Verifikasi Skema

| No. | Pemeriksaan | Hasil |
|---|---|---|
| 1 | Terdapat lima tabel sesuai rancangan | Lulus |
| 2 | Setiap tabel memiliki primary key | Lulus |
| 3 | `sewa.id_kamar` mengacu ke `kamar.id_kamar` | Lulus |
| 4 | `sewa.id_penyewa` mengacu ke `penyewa.id_penyewa` | Lulus |
| 5 | `pembayaran.id_sewa` mengacu ke `sewa.id_sewa` | Lulus |
| 6 | Username bersifat unik | Lulus |
| 7 | Nomor kamar bersifat unik | Lulus |
| 8 | Harga sewa tidak boleh negatif | Lulus |
| 9 | Jumlah pembayaran harus lebih besar dari nol | Lulus |
| 10 | Tanggal selesai tidak boleh sebelum tanggal mulai | Lulus |
| 11 | Tanggal jatuh tempo boleh kosong sesuai prioritas KF-12 | Lulus |
| 12 | Tanggal kalender tidak valid ditolak | Lulus |
| 13 | Periode sewa bertumpang tindih ditolak | Lulus |
| 14 | Perubahan periode yang menyebabkan tumpang tindih ditolak | Lulus |
| 15 | Satu sewa dapat memiliki beberapa pembayaran | Lulus |
| 16 | Penghapusan data yang memiliki riwayat transaksi dibatasi | Lulus |
| 17 | Nomor telepon penyewa mengikuti format yang ditentukan | Lulus |

## 4. Hasil Pengujian

### 4.1 Pengujian Utama

Berkas: `tests/cek_skema.py`

| Keterangan | Jumlah |
|---|---:|
| Data valid diterima | 1 |
| Pengujian penolakan berhasil | 11 |
| Pengujian gagal | 0 |

Seluruh sebelas pengujian penolakan menghasilkan keluaran
`OK ditolak`.

### 4.2 Pengujian Lanjutan

Berkas: `tests/cek_skema_lanjutan.py`

| Keterangan | Jumlah |
|---|---:|
| Pengujian berhasil | 8 |
| Pengujian gagal | 0 |

Pengujian mencakup periode sewa berurutan, periode pada kamar
berbeda, perubahan periode sewa, pembayaran bertahap, dan
pembatasan penghapusan data yang memiliki riwayat transaksi.

### 4.3 Pengujian Validasi Nomor Telepon

Berkas: `tests/cek_validasi_telepon.py`

| Keterangan | Jumlah |
|---|---:|
| Nomor telepon valid diterima | 6 |
| Nomor telepon tidak valid ditolak | 10 |
| Pengujian gagal | 0 |

Pengujian memastikan format nomor telepon Indonesia yang
diperbolehkan diterima dan format yang tidak sesuai ditolak.

### 4.4 Ringkasan

| Keterangan | Jumlah |
|---|---:|
| Data valid diterima | 1 |
| Pengujian penolakan skema berhasil | 11 |
| Pengujian lanjutan berhasil | 8 |
| Pengujian nomor telepon berhasil | 16 |
| Total skenario berhasil | 36 |
| Total skenario gagal | 0 |

Status: seluruh skenario pengujian yang dijalankan berhasil.

## 5. Temuan dan Perbaikan

| No. | Temuan pada draf AI | Tabel/Kolom | Valid? | Perbaikan |
|---|---|---|---|---|
| 1 | Draf awal belum memuat seluruh lima tabel | Seluruh tabel | Tidak | Melengkapi lima tabel sesuai ERD |
| 2 | Belum ada pencegahan periode sewa bertumpang tindih | `sewa` | Tidak | Menambahkan trigger INSERT dan UPDATE sesuai KF-08 |
| 3 | Validasi tanggal kalender belum cukup ketat | Kolom tanggal | Tidak | Menambahkan pemeriksaan tanggal kalender |
| 4 | Tipe data uang belum konsisten dengan kamus data | Kolom nominal | Tidak | Menyesuaikan menjadi NUMERIC |
| 5 | Tanggal jatuh tempo bersifat opsional | `sewa.tanggal_jatuh_tempo` | Ya | Dipertahankan karena KF-12 berprioritas Should |

## 6. Analisis Risiko Kesalahan AI

Kesalahan paling berisiko adalah tidak adanya mekanisme
pencegahan periode sewa yang bertumpang tindih.

Jika aturan KF-08 tidak diterapkan, satu kamar dapat tercatat
disewakan kepada dua penyewa dalam periode yang sama. Hal ini
dapat menimbulkan konflik pengelolaan kamar, ketidaksesuaian
riwayat sewa, dan masalah pencatatan transaksi.

Perbaikan dilakukan dengan menambahkan dua trigger SQLite,
yaitu trigger INSERT dan UPDATE, untuk memeriksa periode sewa
ketika data baru ditambahkan atau periode sewa diubah.

## 7. Kesimpulan

Skema telah melewati 36 skenario pengujian dengan nol kegagalan.

Pengujian mencakup constraint, foreign key, validasi tanggal,
pencegahan periode sewa bertumpang tindih, pembayaran bertahap,
perlindungan riwayat transaksi, dan validasi nomor telepon.

Hasil ini merupakan verifikasi terhadap skenario yang diuji
dan bukan jaminan bahwa seluruh kemungkinan kesalahan telah
tercakup.
