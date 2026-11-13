# Atribut dan Kunci Entitas

## Sistem Informasi Pengelolaan Kontrakan

**Status:** Rancangan Awal
**Sumber:** PRD v1.1, SRS v1.0, dan Dokumen Use Case

## 1. Daftar Atribut

### 1.1 Entitas akun_pengguna

| Atribut | Keterangan |
|---|---|
| **id_akun** (PK) | Identitas unik akun, dibuat otomatis |
| username | Nama pengguna untuk login |
| password_hash | Kata sandi yang sudah di-hash |

**Catatan batasan:**
- Semua atribut wajib diisi.
- `id_akun` menjadi primary key dan dibuat otomatis.
- `username` wajib unik.
- `password_hash` wajib berisi hasil hash, bukan kata sandi asli.

### 1.2 Entitas kamar

| Atribut | Keterangan |
|---|---|
| **id_kamar** (PK) | Identitas unik kamar, dibuat otomatis |
| nomor_kamar | Nomor atau kode kamar |
| harga_sewa | Harga sewa kamar |

**Catatan batasan:**
- Semua atribut wajib diisi.
- `id_kamar` menjadi primary key dan dibuat otomatis.
- `nomor_kamar` wajib unik.
- `harga_sewa` tidak boleh negatif.

### 1.3 Entitas penyewa

| Atribut | Keterangan |
|---|---|
| **id_penyewa** (PK) | Identitas unik penyewa, dibuat otomatis |
| nama | Nama lengkap penyewa |
| no_telepon | Nomor telepon penyewa |
| alamat | Alamat penyewa |

**Catatan batasan:**
- Semua atribut wajib diisi.
- `id_penyewa` menjadi primary key dan dibuat otomatis.
- `no_telepon` harus memiliki format nomor telepon yang valid.
- Nomor telepon tidak ditetapkan unik karena belum ada ketentuan bahwa satu nomor hanya boleh dimiliki satu penyewa.

### 1.4 Entitas sewa

| Atribut | Keterangan |
|---|---|
| **id_sewa** (PK) | Identitas unik data sewa, dibuat otomatis |
| id_kamar (FK) | Referensi ke kamar yang disewa |
| id_penyewa (FK) | Referensi ke penyewa |
| tanggal_mulai | Tanggal mulai periode sewa |
| tanggal_selesai | Tanggal berakhir periode sewa |
| tanggal_jatuh_tempo | Batas tanggal pembayaran |
| harga_sewa_disepakati | Harga sewa yang disepakati untuk periode tersebut |

**Catatan batasan:**
- Semua atribut wajib diisi.
- `id_sewa` menjadi primary key dan dibuat otomatis.
- `id_kamar` harus mengacu pada kamar yang tersedia.
- `id_penyewa` harus mengacu pada penyewa yang terdaftar.
- `tanggal_selesai` tidak boleh lebih awal daripada `tanggal_mulai`.
- `tanggal_jatuh_tempo` wajib berupa tanggal yang valid.
- `harga_sewa_disepakati` tidak boleh negatif.
- Kamar tidak boleh memiliki periode sewa aktif yang bertumpang tindih dengan penyewa lain.
- `harga_sewa_disepakati` merupakan nilai kesepakatan pada saat sewa dibuat agar perubahan harga kamar tidak mengubah riwayat sewa sebelumnya.

### 1.5 Entitas pembayaran

| Atribut | Keterangan |
|---|---|
| **id_pembayaran** (PK) | Identitas unik pembayaran, dibuat otomatis |
| id_sewa (FK) | Referensi ke data sewa |
| tanggal_pembayaran | Tanggal pembayaran diterima |
| jumlah_bayar | Jumlah uang yang dibayarkan |

**Catatan batasan:**
- Semua atribut wajib diisi.
- `id_pembayaran` menjadi primary key dan dibuat otomatis.
- `id_sewa` harus mengacu pada data sewa yang tersedia.
- `tanggal_pembayaran` wajib berupa tanggal yang valid.
- `jumlah_bayar` harus lebih besar dari nol.
- Satu data sewa dapat memiliki beberapa pembayaran untuk mendukung pembayaran secara bertahap atau cicilan.

## 2. Atribut yang Tidak Disimpan

Atribut berikut tidak dijadikan kolom tersendiri karena dapat diperoleh dari data lain:

| Atribut/nilai | Alasan |
|---|---|
| Status ketersediaan kamar | Dapat ditentukan dari periode sewa yang sedang aktif |
| Status pembayaran | Dapat dihitung dari kewajiban sewa, total pembayaran, dan tanggal jatuh tempo |
| Total pembayaran per sewa | Dapat dihitung dengan menjumlahkan seluruh pembayaran yang terkait dengan satu sewa |
| Total pendapatan | Dapat dihitung dari jumlah pembayaran yang diterima dalam periode tertentu |
| Jumlah sisa pembayaran | Dapat dihitung dari kewajiban sewa dikurangi total pembayaran |

## 3. Catatan Keputusan Desain

1. Setiap entitas menggunakan primary key berupa ID otomatis.
2. `sewa` menjadi penghubung antara `kamar` dan `penyewa`.
3. `pembayaran` terhubung dengan `sewa`, sehingga satu sewa dapat mempunyai beberapa catatan pembayaran.
4. Setiap satu record `sewa` pada rancangan ini mewakili satu periode sewa yang memiliki tanggal mulai, tanggal selesai, dan tanggal jatuh tempo.
5. `harga_sewa_disepakati` merupakan usulan atribut untuk menjaga riwayat harga. Penerapannya perlu diselaraskan dengan aturan perhitungan tagihan pada tahap berikutnya.
6. Aturan detail mengenai pembayaran yang terlambat dan pelunasan perlu ditetapkan sebelum implementasi.

## 4. Kesimpulan

Rancangan awal memiliki lima entitas, yaitu `akun_pengguna`, `kamar`, `penyewa`, `sewa`, dan `pembayaran`. Masing-masing memiliki primary key, atribut, serta batasan data. Nilai yang dapat dihitung tidak disimpan sebagai atribut tersendiri.
