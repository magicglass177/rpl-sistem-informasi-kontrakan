# Normalisasi Basis Data

## Sistem Informasi Pengelolaan Kontrakan

**Status:** Rancangan Akademik
**Sumber data:** Contoh lembar catatan sewa dan pembayaran simulasi
**Catatan:** Data pada dokumen ini merupakan ilustrasi untuk keperluan pembelajaran, bukan dokumen atau data dari klien nyata.

## 1. Data Mentah (UNF)

Contoh lembar catatan sewa dan pembayaran yang disimulasikan:

| Kode sewa | Nomor kamar | Harga kamar | Nama penyewa | Telepon | Alamat | Tanggal mulai | Tanggal selesai | Jatuh tempo | Pembayaran |
|---|---|---:|---|---|---|---|---|---|---|
| SW001 | K-01 | 800000 | Andi | 081234567890 | Jl. Melati | 2026-01-01 | 2026-06-30 | 2026-01-05 | (2026-01-03, 400000), (2026-01-10, 400000) |
| SW002 | K-02 | 1000000 | Budi | 081298765432 | Jl. Mawar | 2026-02-01 | 2026-07-31 | 2026-02-05 | (2026-02-04, 1000000) |

### Masalah pada UNF

1. Kolom pembayaran memuat lebih dari satu kelompok nilai dalam satu sel.
2. Data kamar dan penyewa bercampur dengan data transaksi sewa.
3. Informasi kamar dan penyewa berpotensi ditulis berulang pada banyak catatan.
4. Perubahan informasi kamar atau penyewa dapat menyebabkan inkonsistensi data.

## 2. First Normal Form (1NF)

Syarat 1NF adalah setiap atribut memiliki nilai atomik atau satu nilai pada setiap sel. Kelompok pembayaran yang berulang dipisahkan menjadi baris tersendiri.

Contoh hasil 1NF:

| Kode sewa | No. urut bayar | Nomor kamar | Harga kamar | Nama penyewa | Telepon | Alamat | Tanggal mulai | Tanggal selesai | Jatuh tempo | Harga sewa disepakati | Tanggal pembayaran | Jumlah bayar |
|---|---:|---|---:|---|---|---|---|---|---|---:|---|---:|
| SW001 | 1 | K-01 | 800000 | Andi | 081234567890 | Jl. Melati | 2026-01-01 | 2026-06-30 | 2026-01-05 | 800000 | 2026-01-03 | 400000 |
| SW001 | 2 | K-01 | 800000 | Andi | 081234567890 | Jl. Melati | 2026-01-01 | 2026-06-30 | 2026-01-05 | 800000 | 2026-01-10 | 400000 |
| SW002 | 1 | K-02 | 1000000 | Budi | 081298765432 | Jl. Mawar | 2026-02-01 | 2026-07-31 | 2026-02-05 | 1000000 | 2026-02-04 | 1000000 |

**Kunci sementara:** kombinasi `kode_sewa` dan `no_urut_bayar`.
### Perbaikan pada 1NF

- Setiap pembayaran menjadi satu baris.
- Tidak ada lagi daftar pembayaran dalam satu sel.
- Data masih berulang karena informasi sewa, kamar, dan penyewa muncul pada setiap baris pembayaran.

## 3. Second Normal Form (2NF)

Syarat 2NF adalah sudah memenuhi 1NF dan setiap atribut nonkunci bergantung sepenuhnya pada seluruh bagian kunci utama.

Pada tabel 1NF, identitas periode sewa bergantung pada `kode_sewa`, sedangkan informasi pembayaran bergantung pada identitas pembayaran dalam suatu sewa.

Karena itu, data dipisahkan menjadi dua kelompok:

### Tabel SEWA_2NF

| Kode sewa | Nomor kamar | Harga kamar | Nama penyewa | Telepon | Alamat | Tanggal mulai | Tanggal selesai | Jatuh tempo | Harga sewa disepakati |
|---|---|---:|---|---|---|---|---|---|---:|
| SW001 | K-01 | 800000 | Andi | 081234567890 | Jl. Melati | 2026-01-01 | 2026-06-30 | 2026-01-05 | 800000 |
| SW002 | K-02 | 1000000 | Budi | 081298765432 | Jl. Mawar | 2026-02-01 | 2026-07-31 | 2026-02-05 | 1000000 |

Ketergantungan yang masih ditemukan:
- `kode_sewa` menentukan nomor kamar, sedangkan nomor kamar menentukan harga kamar.
- `kode_sewa` menentukan identitas penyewa, sedangkan identitas penyewa menentukan nama, telepon, dan alamat.

Ketergantungan tersebut menjadi dasar pemisahan data kamar dan penyewa ke tabel masing-masing pada tahap 3NF.

### Tabel PEMBAYARAN_2NF

| Kode sewa | No. urut bayar | Tanggal pembayaran | Jumlah bayar |
|---|---:|---|---:|
| SW001 | 1 | 2026-01-03 | 400000 |
| SW001 | 2 | 2026-01-10 | 400000 |
| SW002 | 1 | 2026-02-04 | 1000000 |

**Kunci sementara:**
- `SEWA_2NF`: `kode_sewa`.
- `PEMBAYARAN_2NF`: kombinasi `kode_sewa` dan `no_urut_bayar`.
### Perbaikan pada 2NF

- Data periode sewa dipisahkan dari detail pembayaran.
- Informasi pembayaran tidak perlu mengulang tanggal dan informasi utama periode sewa.
- Hubungan pembayaran dengan sewa dipertahankan melalui kode sewa.

### Masalah yang masih tersisa

Tabel `SEWA_2NF` masih menyimpan nama penyewa dan nomor kamar secara langsung. Informasi tersebut seharusnya bergantung pada identitas penyewa dan kamar, bukan pada identitas sewa. Data kamar dan penyewa juga masih berpotensi berulang pada beberapa periode sewa.

## 4. Third Normal Form (3NF)

Syarat 3NF adalah sudah memenuhi 2NF dan tidak terdapat ketergantungan transitif atribut nonkunci terhadap primary key.

Data kemudian dipisahkan menjadi tabel master dan tabel transaksi berikut.

### 4.1 Tabel KAMAR

| id_kamar (PK) | nomor_kamar (UK) | harga_sewa |
|---|---|---:|
| 1 | K-01 | 800000 |
| 2 | K-02 | 1000000 |

### 4.2 Tabel PENYEWA

| id_penyewa (PK) | nama | no_telepon | alamat |
|---|---|---|---|
| 1 | Andi | 081234567890 | Jl. Melati |
| 2 | Budi | 081298765432 | Jl. Mawar |

### 4.3 Tabel SEWA

| id_sewa (PK) | id_kamar (FK) | id_penyewa (FK) | tanggal_mulai | tanggal_selesai | tanggal_jatuh_tempo | harga_sewa_disepakati |
|---|---:|---:|---|---|---|---:|
| 1 | 1 | 1 | 2026-01-01 | 2026-06-30 | 2026-01-05 | 800000 |
| 2 | 2 | 2 | 2026-02-01 | 2026-07-31 | 2026-02-05 | 1000000 |

### 4.4 Tabel PEMBAYARAN

| id_pembayaran (PK) | id_sewa (FK) | tanggal_pembayaran | jumlah_bayar |
|---|---:|---|---:|
| 1 | 1 | 2026-01-03 | 400000 |
| 2 | 1 | 2026-01-10 | 400000 |
| 3 | 2 | 2026-02-04 | 1000000 |

### 4.5 Tabel AKUN_PENGGUNA

| id_akun (PK) | username (UK) | password_hash |
|---|---|---|
| 1 | pemilik | hash_password_simulasi |

Data akun di atas hanya contoh struktur. Nilai hash tersebut bukan kredensial untuk digunakan dalam aplikasi.

### Perbaikan pada 3NF

1. Informasi kamar disimpan pada tabel `kamar`.
2. Informasi penyewa disimpan pada tabel `penyewa`.
3. Data periode sewa menyimpan referensi kamar dan penyewa melalui foreign key.
4. Data pembayaran disimpan terpisah dan mengacu pada satu periode sewa.
5. Data akun pengguna disimpan terpisah untuk kebutuhan autentikasi.
6. Perubahan nama atau alamat penyewa tidak perlu mengubah catatan sewa.
7. Perubahan harga kamar tidak mengubah harga sewa historis yang sudah disepakati.

## 5. Hasil Akhir Normalisasi

Hasil akhir 3NF menghasilkan lima tabel:

| No. | Tabel | Fungsi |
|---|---|---|
| 1 | akun_pengguna | Menyimpan akun untuk autentikasi pemilik |
| 2 | kamar | Menyimpan informasi kamar |
| 3 | penyewa | Menyimpan identitas dan kontak penyewa |
| 4 | sewa | Menyimpan hubungan kamar, penyewa, dan periode sewa |
| 5 | pembayaran | Menyimpan riwayat pembayaran sewa |

Kelima tabel tersebut sama dengan lima entitas pada ERD `docs/desain/erd.mmd`.

## 6. Atribut Turunan yang Tidak Disimpan

Nilai berikut dihitung saat diperlukan dan tidak disimpan sebagai kolom tersendiri:

| Nilai | Dasar perhitungan |
|---|---|
| Status ketersediaan kamar | Periode sewa aktif dan tanggal saat pemeriksaan |
| Total pembayaran per sewa | Penjumlahan `jumlah_bayar` berdasarkan `id_sewa` |
| Sisa kewajiban pembayaran | Kewajiban sewa dikurangi total pembayaran |
| Status pembayaran | Sisa kewajiban dan tanggal jatuh tempo |
| Total pendapatan | Penjumlahan pembayaran berdasarkan tanggal pembayaran |

## 7. Kesimpulan

Normalisasi dilakukan bertahap dari UNF, 1NF, 2NF, hingga 3NF. Pengelompokan pembayaran berulang dipecah menjadi baris atomik, data sewa dipisahkan dari pembayaran, kemudian data kamar dan penyewa dipisahkan dari transaksi sewa.

Hasil akhir terdiri dari lima tabel yang konsisten dengan ERD. Data simulasi digunakan sebagai ilustrasi akademik dan tidak diklaim sebagai dokumen dari klien nyata.
