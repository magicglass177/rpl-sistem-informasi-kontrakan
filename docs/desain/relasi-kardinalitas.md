# Relasi dan Kardinalitas

## Sistem Informasi Pengelolaan Kontrakan

**Status:** Rancangan Awal
**Sumber:** PRD v1.1, SRS v1.0, dan Dokumen Use Case

## 1. Daftar Relasi

### Relasi 1 — kamar dan sewa

**Entitas A — relasi — Entitas B:**
`kamar — memiliki riwayat — sewa`

**Kalimat dua arah:**
1. Satu kamar dapat memiliki nol atau banyak catatan sewa sepanjang waktu.
2. Satu catatan sewa harus mengacu pada tepat satu kamar.

**Kardinalitas:** 1 : N

**Foreign key:**
- `sewa.id_kamar` mengacu pada `kamar.id_kamar`.
- FK berada pada tabel `sewa`, yaitu sisi banyak.

**Catatan:**
- Satu kamar dapat disewa berkali-kali pada periode yang berbeda.
- Kamar tidak boleh mempunyai dua penyewa aktif dalam periode yang bertumpang tindih.
- Riwayat sewa sebelumnya tetap disimpan.

### Relasi 2 — penyewa dan sewa

**Entitas A — relasi — Entitas B:**
`penyewa — melakukan — sewa`

**Kalimat dua arah:**
1. Satu penyewa dapat memiliki nol atau banyak catatan sewa.
2. Satu catatan sewa harus dimiliki oleh tepat satu penyewa.

**Kardinalitas:** 1 : N

**Foreign key:**
- `sewa.id_penyewa` mengacu pada `penyewa.id_penyewa`.
- FK berada pada tabel `sewa`, yaitu sisi banyak.

**Catatan:**
- Riwayat sewa penyewa dapat terdiri dari beberapa periode.
- Data penyewa tetap dapat disimpan meskipun periode sewanya telah berakhir.

### Relasi 3 — sewa dan pembayaran

**Entitas A — relasi — Entitas B:**
`sewa — memiliki — pembayaran`

**Kalimat dua arah:**
1. Satu data sewa dapat memiliki nol atau banyak catatan pembayaran.
2. Satu catatan pembayaran harus terkait dengan tepat satu data sewa.

**Kardinalitas:** 1 : N

**Foreign key:**
- `pembayaran.id_sewa` mengacu pada `sewa.id_sewa`.
- FK berada pada tabel `pembayaran`, yaitu sisi banyak.

**Catatan:**
- Satu sewa dapat dibayar secara bertahap.
- Setiap pembayaran dicatat secara terpisah.
- Riwayat pembayaran tidak digabung menjadi satu catatan karena tanggal dan jumlah setiap pembayaran perlu dipertahankan.

## 2. Ringkasan Relasi dan Foreign Key

| No. | Entitas A | Relasi | Entitas B | Kardinalitas | Letak FK |
|---|---|---|---|---|---|
| 1 | kamar | memiliki riwayat | sewa | 1 : N | sewa.id_kamar |
| 2 | penyewa | melakukan | sewa | 1 : N | sewa.id_penyewa |
| 3 | sewa | memiliki | pembayaran | 1 : N | pembayaran.id_sewa |

## 3. Relasi Banyak-ke-Banyak

Pada rancangan saat ini tidak terdapat relasi banyak-ke-banyak secara langsung.

Hubungan antara `kamar` dan `penyewa` direpresentasikan melalui entitas `sewa`:
- Satu kamar dapat disewa oleh beberapa penyewa yang berbeda pada periode yang berbeda.
- Satu penyewa dapat menyewa kamar yang berbeda pada periode yang berbeda.
- Setiap transaksi hubungan tersebut dicatat sebagai satu record pada tabel `sewa`.

Dengan demikian, tabel `sewa` berfungsi sebagai penghubung antara `kamar` dan `penyewa`, sekaligus menyimpan atribut hubungan berupa tanggal periode sewa dan harga sewa yang disepakati.

## 4. Entitas Akun Pengguna

`akun_pengguna` belum memiliki relasi foreign key dengan entitas lainnya.

Alasannya:
- Kebutuhan yang tercatat menetapkan akun pemilik untuk autentikasi.
- Belum ada kebutuhan untuk mencatat akun pembuat atau pengubah setiap data.
- Tidak menambahkan foreign key yang belum didukung kebutuhan proyek.

## 5. Kesimpulan

Rancangan memiliki tiga relasi utama dengan kardinalitas 1 : N:
1. `kamar` ke `sewa`.
2. `penyewa` ke `sewa`.
3. `sewa` ke `pembayaran`.

Seluruh foreign key ditempatkan pada tabel di sisi banyak. Hubungan antara kamar dan penyewa direpresentasikan melalui tabel `sewa`, sehingga tidak ada relasi banyak-ke-banyak yang dibiarkan tanpa penghubung.
