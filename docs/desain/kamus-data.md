# Kamus Data

## Sistem Informasi Pengelolaan Kontrakan

**Status:** Rancangan Awal
**Sumber:** PRD v1.1, SRS v1.0, dan Dokumen Use Case

## 1. Tabel akun_pengguna

| Nama kolom | Tipe data | Wajib | Kunci | Aturan nilai | Sumber KF |
|---|---|---|---|---|---|
| id_akun | INTEGER | Ya | PK | ID otomatis, unik, tidak boleh NULL | KF-01 |
| username | VARCHAR(50) | Ya | UK | Tidak boleh kosong dan harus unik | KF-01 |
| password_hash | VARCHAR(255) | Ya | — | Harus berisi hash kata sandi, bukan kata sandi asli | KF-01 |

**Keterangan:** Tabel menyimpan akun pemilik yang digunakan untuk autentikasi.

## 2. Tabel kamar

| Nama kolom | Tipe data | Wajib | Kunci | Aturan nilai | Sumber KF |
|---|---|---|---|---|---|
| id_kamar | INTEGER | Ya | PK | ID otomatis, unik, tidak boleh NULL | KF-02 |
| nomor_kamar | VARCHAR(20) | Ya | UK | Tidak boleh kosong dan harus unik | KF-02, KF-03 |
| harga_sewa | DECIMAL(12,2) | Ya | — | Nilai harus lebih besar atau sama dengan nol | KF-02, KF-04 |

**Keterangan:** Status ketersediaan kamar tidak disimpan sebagai kolom karena dapat ditentukan dari data periode sewa aktif (KF-05).

## 3. Tabel penyewa

| Nama kolom | Tipe data | Wajib | Kunci | Aturan nilai | Sumber KF |
|---|---|---|---|---|---|
| id_penyewa | INTEGER | Ya | PK | ID otomatis, unik, tidak boleh NULL | KF-06 |
| nama | VARCHAR(100) | Ya | — | Tidak boleh kosong | KF-06 |
| no_telepon | VARCHAR(20) | Ya | — | Harus mengikuti format nomor telepon yang valid | KF-06 |
| alamat | TEXT | Ya | — | Tidak boleh kosong | KF-06 |

**Keterangan:** Nomor telepon tidak ditetapkan unik karena kebutuhan proyek belum menetapkan bahwa satu nomor hanya boleh digunakan oleh satu penyewa.

## 4. Tabel sewa

| Nama kolom | Tipe data | Wajib | Kunci | Aturan nilai | Sumber KF |
|---|---|---|---|---|---|
| id_sewa | INTEGER | Ya | PK | ID otomatis, unik, tidak boleh NULL | KF-07 |
| id_kamar | INTEGER | Ya | FK | Harus mengacu pada `kamar.id_kamar` | KF-07, KF-08 |
| id_penyewa | INTEGER | Ya | FK | Harus mengacu pada `penyewa.id_penyewa` | KF-07 |
| tanggal_mulai | DATE | Ya | — | Harus berupa tanggal valid | KF-13 |
| tanggal_selesai | DATE | Ya | — | Harus berupa tanggal valid dan tidak lebih awal dari tanggal mulai | KF-13, KF-14 |
| tanggal_jatuh_tempo | DATE | Ya jika KF-12 diterapkan | — | Harus berupa tanggal valid sesuai aturan jatuh tempo | KF-12 |
| harga_sewa_disepakati | DECIMAL(12,2) | Ya | — | Nilai tidak boleh negatif; menyimpan harga kesepakatan saat sewa dibuat | KF-02, KF-07 |

**Keterangan:**
- Satu record sewa mewakili satu periode sewa.
- Kamar tidak boleh mempunyai periode sewa aktif yang bertumpang tindih dengan penyewa lain (KF-08).
- `harga_sewa_disepakati` merupakan atribut rancangan untuk mempertahankan riwayat harga ketika harga kamar berubah.
- Perpanjangan sewa dicatat sebagai periode sewa baru sesuai rancangan.

## 5. Tabel pembayaran

| Nama kolom | Tipe data | Wajib | Kunci | Aturan nilai | Sumber KF |
|---|---|---|---|---|---|
| id_pembayaran | INTEGER | Ya | PK | ID otomatis, unik, tidak boleh NULL | KF-09 |
| id_sewa | INTEGER | Ya | FK | Harus mengacu pada `sewa.id_sewa` | KF-09 |
| tanggal_pembayaran | DATE | Ya | — | Harus berupa tanggal valid ketika pembayaran diterima | KF-09, KF-15 |
| jumlah_bayar | DECIMAL(12,2) | Ya | — | Harus lebih besar dari nol | KF-09, KF-10 |

**Keterangan:**
- Satu sewa dapat memiliki beberapa catatan pembayaran.
- Pembayaran bertahap dicatat sebagai beberapa baris.
- Status pembayaran tidak disimpan sebagai kolom tersendiri karena dapat dihitung dari kewajiban sewa, total pembayaran, dan tanggal jatuh tempo (KF-11).
- Riwayat pembayaran diperoleh dari data pembayaran yang terkait dengan sewa (KF-10).
- Laporan pendapatan dihitung berdasarkan tanggal pembayaran diterima (KF-15).

## 6. Ringkasan Jumlah Kolom

| No. | Tabel | Jumlah kolom | Primary key | Foreign key | Unique key |
|---|---|---:|---|---|---|
| 1 | akun_pengguna | 3 | id_akun | — | username |
| 2 | kamar | 3 | id_kamar | — | nomor_kamar |
| 3 | penyewa | 4 | id_penyewa | — | — |
| 4 | sewa | 7 | id_sewa | id_kamar, id_penyewa | — |
| 5 | pembayaran | 4 | id_pembayaran | id_sewa | — |
| **Total** | **5 tabel** | **21 kolom** | | | |

## 7. Aturan Integritas Data

1. Setiap tabel harus memiliki primary key.
2. Nilai foreign key harus mengacu pada primary key tabel yang dituju.
3. `username` dan `nomor_kamar` tidak boleh memiliki duplikasi.
4. Harga sewa tidak boleh negatif.
5. Jumlah pembayaran harus lebih besar dari nol.
6. Tanggal selesai sewa tidak boleh lebih awal daripada tanggal mulai.
7. Periode sewa untuk kamar yang sama tidak boleh bertumpang tindih jika keduanya masih aktif.
8. Satu sewa dapat memiliki beberapa catatan pembayaran.
9. Penghapusan data induk harus mempertimbangkan riwayat transaksi agar integritas referensial tetap terjaga.
10. Nilai turunan seperti total pembayaran, sisa pembayaran, status pembayaran, dan total pendapatan dihitung ketika diperlukan, bukan disimpan sebagai kolom biasa.

## 8. Konsistensi dengan ERD dan Normalisasi

Kamus data ini menggunakan lima tabel yang sama dengan:
- `docs/desain/erd.mmd`
- `docs/desain/normalisasi.md`

Seluruh primary key, foreign key, dan unique key mengikuti rancangan ERD. Atribut yang dicatat juga mengikuti hasil normalisasi 3NF.

## 9. Catatan

Dokumen ini merupakan rancangan akademik. Tipe data, panjang karakter, serta batasan nilai dapat disesuaikan saat implementasi SQLite, selama tidak mengubah kebutuhan fungsional dan integritas data.
