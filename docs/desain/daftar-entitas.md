# Daftar Entitas
## Sistem Informasi Pengelolaan Kontrakan

**Dokumen:** Identifikasi Entitas
**Status:** Rancangan Awal
**Dasar:** PRD versi 1.1, SRS versi 1.0, dan dokumen skenario Use Case.
**Catatan:** Kebutuhan proyek berasal dari simulasi akademik dan belum divalidasi oleh klien nyata.

## 1. Tujuan

Dokumen ini berisi identifikasi entitas yang diperlukan dalam basis data Sistem Informasi Pengelolaan Kontrakan. Setiap entitas ditentukan berdasarkan data yang perlu disimpan dan kebutuhan fungsional yang telah didokumentasikan.

## 2. Daftar Entitas

| No. | Entitas (Tabel) | Deskripsi | Sumber (KF / UC) |
|---:|---|---|---|
| 1 | `akun_pengguna` | Menyimpan akun pemilik kontrakan yang digunakan untuk login ke sistem. | KF-01, UC-01 |
| 2 | `kamar` | Menyimpan informasi kamar kontrakan, seperti nomor kamar dan harga sewa. | KF-02, KF-03, KF-04, KF-05; UC-02, UC-03, UC-04, UC-05 |
| 3 | `penyewa` | Menyimpan informasi identitas dan kontak penyewa, seperti nama lengkap, nomor telepon, dan alamat. | KF-06; UC-06, UC-07 |
| 4 | `sewa` | Menyimpan hubungan antara penyewa dan kamar, termasuk tanggal mulai, tanggal berakhir, serta tanggal jatuh tempo sewa. | KF-07, KF-08, KF-12, KF-13, KF-14; UC-08, UC-12, UC-13, UC-14 |
| 5 | `pembayaran` | Menyimpan catatan pembayaran sewa, termasuk tanggal pembayaran dan jumlah pembayaran. | KF-09, KF-10, KF-11, KF-15; UC-09, UC-10, UC-11, UC-15 |

## 3. Alasan Pemilihan Entitas

1. **Akun Pengguna:** Data akun perlu disimpan agar sistem dapat memverifikasi username dan password pemilik kontrakan.
2. **Kamar:** Data kamar perlu disimpan agar pemilik dapat mengelola informasi kamar dan memantau ketersediaannya.
3. **Penyewa:** Data penyewa perlu disimpan agar identitas dan informasi kontak penghuni dapat dikelola.
4. **Sewa:** Data sewa diperlukan untuk menghubungkan penyewa dengan kamar serta menyimpan periode penyewaan. Entitas ini juga memungkinkan sistem menyimpan riwayat penyewaan.
5. **Pembayaran:** Data pembayaran perlu disimpan sebagai catatan transaksi. Pemisahan pembayaran dari sewa memungkinkan satu periode sewa memiliki beberapa catatan pembayaran, termasuk pembayaran bertahap.

## 4. Kandidat yang Tidak Dijadikan Entitas

| Kandidat | Alasan |
|---|---|
| Laporan pendapatan | Merupakan hasil pengolahan data pembayaran berdasarkan periode tertentu, bukan data transaksi utama yang harus disimpan sebagai tabel tersendiri. |
| Status ketersediaan kamar | Dapat ditentukan berdasarkan data kamar dan periode sewa yang sedang berlangsung. Belum ditetapkan sebagai entitas tersendiri. |
| Status pembayaran | Merupakan informasi yang berkaitan dengan kewajiban sewa, jumlah pembayaran, dan tanggal jatuh tempo. Mekanisme penyimpanannya akan ditinjau pada tahap penentuan atribut dan normalisasi. |
| Pengelola atau penjaga kontrakan | Tidak termasuk pengguna dalam ruang lingkup proyek saat ini. |

## 5. Catatan untuk Perancangan Berikutnya

1. Entitas `sewa` perlu memiliki hubungan dengan `kamar` dan `penyewa`.
2. Entitas `pembayaran` perlu memiliki hubungan dengan `sewa` agar setiap transaksi pembayaran dapat ditelusuri ke periode sewa yang bersangkutan.
3. Penentuan primary key, foreign key, atribut, tipe data, dan kardinalitas akan dibahas pada tahap perancangan ERD.
4. Aturan pembayaran bertahap, tanggal jatuh tempo, dan perhitungan status pembayaran perlu diperhatikan saat menentukan atribut dan aturan bisnis.
5. Rancangan ini masih bersifat akademik berdasarkan kebutuhan simulasi dan dapat ditinjau kembali apabila terdapat perubahan kebutuhan.

## 6. Kesimpulan

Berdasarkan pemeriksaan PRD, SRS, dan dokumen Use Case, teridentifikasi lima entitas utama, yaitu `akun_pengguna`, `kamar`, `penyewa`, `sewa`, dan `pembayaran`.

Kelima entitas tersebut menjadi dasar untuk menyusun Entity Relationship Diagram (ERD), normalisasi, dan kamus data pada tahapan berikutnya.
