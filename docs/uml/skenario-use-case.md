# Skenario Use Case
## Sistem Informasi Pengelolaan Kontrakan

**Dokumen:** Skenario Use Case
**Lokasi:** `docs/uml/skenario-use-case.md`
**Aktor utama:** Pemilik Kontrakan

---

# UC-01 — Login

**Aktor dan KF**
- Aktor utama: Pemilik Kontrakan
- KF terkait: KF-01 — Login
- Prioritas: Must

**Prasyarat**
1. Pemilik Kontrakan telah memiliki akun yang disiapkan oleh administrator.
2. Pemilik Kontrakan belum login.
3. Sistem dapat diakses.

**Alur Utama**
1. Pemilik Kontrakan membuka halaman login.
2. Sistem menampilkan formulir login.
3. Pemilik Kontrakan memasukkan kredensial akun.
4. Sistem memeriksa kecocokan kredensial.
5. Sistem memvalidasi kredensial dan membuat sesi login.
6. Sistem mengarahkan Pemilik Kontrakan ke halaman utama atau dashboard.

**Alur Alternatif**
- Tidak ada alur alternatif yang ditetapkan berdasarkan kebutuhan yang tersedia.

**Pengecualian**
1. Jika kredensial tidak sesuai, sistem menolak login dan menampilkan pesan kesalahan.
2. Jika data login belum lengkap, sistem meminta Pemilik Kontrakan melengkapi formulir.

**Pascakondisi**
1. Pemilik Kontrakan berhasil login.
2. Sesi login aktif.
3. Halaman utama dapat diakses.

---

# UC-02 — Menambahkan Data Kamar

**Aktor dan KF**
- Aktor utama: Pemilik Kontrakan
- KF terkait: KF-02 — Menambahkan data kamar
- Prioritas: Must

**Prasyarat**
1. Pemilik Kontrakan sudah login.
2. Pemilik Kontrakan berada di halaman pengelolaan kamar.

**Alur Utama**
1. Pemilik Kontrakan memilih menu tambah kamar.
2. Sistem menampilkan formulir penambahan kamar.
3. Pemilik Kontrakan memasukkan nomor kamar dan harga sewa.
4. Sistem memeriksa kelengkapan dan keunikan nomor kamar.
5. Sistem menyimpan data kamar.
6. Sistem menampilkan pemberitahuan bahwa kamar berhasil ditambahkan.

**Alur Alternatif**
1. Pemilik Kontrakan membatalkan proses penambahan kamar sebelum menyimpan data.
2. Sistem membatalkan proses dan kembali ke halaman daftar kamar tanpa menyimpan data baru.

**Pengecualian**
1. Jika nomor kamar sudah digunakan, sistem menolak penyimpanan dan menampilkan pesan bahwa nomor kamar harus unik.
2. Jika data wajib belum lengkap, sistem meminta Pemilik Kontrakan melengkapi formulir.
3. Jika data tidak valid, sistem menolak penyimpanan dan menampilkan informasi kesalahan.

**Pascakondisi**
1. Data kamar baru tersimpan.
2. Kamar baru muncul dalam daftar kamar.
3. Data kamar dapat digunakan dalam proses pengelolaan kontrakan.

---

# UC-06 — Menambahkan Data Penyewa

**Aktor dan KF**
- Aktor utama: Pemilik Kontrakan
- KF terkait: KF-06 — Mengelola data penyewa
- Prioritas: Must

**Prasyarat**
1. Pemilik Kontrakan sudah login.
2. Pemilik Kontrakan berada di halaman pengelolaan penyewa.

**Alur Utama**
1. Pemilik Kontrakan memilih menu tambah penyewa.
2. Sistem menampilkan formulir data penyewa.
3. Pemilik Kontrakan memasukkan nama, nomor telepon, dan alamat penyewa.
4. Sistem memeriksa kelengkapan dan validitas data.
5. Sistem menyimpan data penyewa.
6. Sistem menampilkan pemberitahuan bahwa data penyewa berhasil ditambahkan.

**Alur Alternatif**
1. Pemilik Kontrakan membatalkan proses penambahan data penyewa.
2. Sistem membatalkan proses dan kembali ke halaman daftar penyewa tanpa menyimpan data baru.

**Pengecualian**
1. Jika data wajib belum lengkap, sistem meminta Pemilik Kontrakan melengkapi formulir.
2. Jika format data tidak valid, sistem menolak penyimpanan dan menampilkan informasi kesalahan.
3. Jika penyimpanan gagal, sistem menampilkan pemberitahuan bahwa data belum berhasil disimpan.

**Pascakondisi**
1. Data penyewa berhasil tersimpan.
2. Data penyewa muncul dalam daftar penyewa.
3. Data penyewa dapat digunakan dalam proses penghubungan penyewa dengan kamar.

---

# UC-08 — Menghubungkan Penyewa dengan Kamar

**Aktor dan KF**
- Aktor utama: Pemilik Kontrakan
- KF terkait: KF-07 — Menghubungkan penyewa dengan kamar; KF-08 — Mencegah penempatan pada kamar yang masih ditempati
- Prioritas: Must

**Prasyarat**
1. Pemilik Kontrakan sudah login.
2. Data penyewa sudah tersedia.
3. Data kamar sudah tersedia.

**Alur Utama**
1. Pemilik Kontrakan membuka menu penghubungan penyewa dengan kamar.
2. Sistem menampilkan daftar penyewa dan kamar.
3. Pemilik Kontrakan memilih penyewa yang akan menempati kamar.
4. Sistem menampilkan kamar yang dapat dipilih.
5. Pemilik Kontrakan memilih kamar yang tersedia.
6. Sistem memeriksa status penggunaan kamar berdasarkan penempatan penyewa dan periode sewanya.
7. Sistem menyimpan hubungan antara penyewa dan kamar.
8. Sistem memperbarui status kamar sesuai penempatan penyewa dan periode sewa.

**Alur Alternatif**
1. Pemilik Kontrakan memilih kamar lain apabila kamar yang diinginkan tidak tersedia.
2. Sistem menampilkan informasi ketersediaan kamar yang dipilih.
3. Pemilik Kontrakan melanjutkan proses dengan kamar yang tersedia.

**Pengecualian**
1. Jika kamar masih ditempati penyewa lain dalam periode sewa yang masih berlangsung, sistem menolak penghubungan tersebut.
2. Sistem menampilkan informasi bahwa kamar masih ditempati dan meminta Pemilik Kontrakan memilih kamar lain.
3. Jika data penyewa atau kamar tidak ditemukan, sistem membatalkan proses dan menampilkan pemberitahuan kesalahan.

**Pascakondisi**
1. Hubungan antara penyewa dan kamar berhasil tersimpan.
2. Status kamar diperbarui berdasarkan penempatan dan periode sewa.
3. Penyewa tercatat menempati kamar yang dipilih.

---

# UC-09 — Mencatat Pembayaran Sewa

**Aktor dan KF**
- Aktor utama: Pemilik Kontrakan
- KF terkait: KF-09 — Mencatat pembayaran sewa
- Prioritas: Must

**Prasyarat**
1. Pemilik Kontrakan sudah login.
2. Data penyewa sudah tersedia.
3. Periode sewa yang berkaitan dengan pembayaran sudah tersedia.

**Alur Utama**
1. Pemilik Kontrakan membuka menu pembayaran sewa.
2. Sistem menampilkan data penyewa dan informasi periode sewa.
3. Pemilik Kontrakan memilih penyewa yang melakukan pembayaran.
4. Sistem menampilkan informasi pembayaran yang berkaitan dengan penyewa tersebut.
5. Pemilik Kontrakan memasukkan tanggal pembayaran dan jumlah uang yang diterima.
6. Sistem memeriksa kelengkapan dan validitas data pembayaran.
7. Sistem menyimpan catatan pembayaran.
8. Sistem memperbarui informasi pembayaran berdasarkan catatan yang tersimpan.
9. Sistem menampilkan pemberitahuan bahwa pembayaran berhasil dicatat.

**Alur Alternatif**
1. Penyewa melakukan pembayaran secara bertahap.
2. Pemilik Kontrakan memasukkan jumlah pembayaran yang diterima sesuai nominal pembayaran tersebut.
3. Sistem menyimpan pembayaran sebagai catatan pembayaran.
4. Sistem mempertahankan informasi pembayaran sehingga pembayaran berikutnya dapat dicatat sebagai transaksi terpisah.

**Pengecualian**
1. Jika tanggal atau jumlah pembayaran belum diisi, sistem meminta Pemilik Kontrakan melengkapi data.
2. Jika jumlah pembayaran tidak valid, sistem menolak penyimpanan dan menampilkan pesan kesalahan.
3. Jika data pembayaran gagal disimpan, sistem menampilkan pemberitahuan bahwa pencatatan pembayaran belum berhasil.

**Pascakondisi**
1. Catatan pembayaran tersimpan.
2. Tanggal dan jumlah pembayaran tercatat.
3. Riwayat pembayaran dapat ditampilkan.
4. Informasi status pembayaran dapat diperbarui berdasarkan catatan pembayaran.

---

# UC-12 — Mengelola Periode Sewa

**Aktor dan KF**
- Aktor utama: Pemilik Kontrakan
- KF terkait: KF-13 — Mengelola periode sewa
- Prioritas: Must

**Prasyarat**
1. Pemilik Kontrakan sudah login.
2. Data penyewa sudah tersedia.
3. Data kamar sudah tersedia.

**Alur Utama**
1. Pemilik Kontrakan membuka menu pengelolaan periode sewa.
2. Sistem menampilkan daftar periode sewa.
3. Pemilik Kontrakan memilih penyewa yang akan dikelola periode sewanya.
4. Sistem menampilkan informasi periode sewa penyewa tersebut.
5. Pemilik Kontrakan memasukkan atau mengubah tanggal mulai dan tanggal berakhir sewa.
6. Sistem memeriksa kelengkapan dan validitas tanggal periode sewa.
7. Sistem menyimpan data periode sewa.
8. Sistem menampilkan pemberitahuan bahwa periode sewa berhasil disimpan.

**Alur Alternatif**
1. Pemilik Kontrakan memilih periode sewa yang sudah tersimpan.
2. Sistem menampilkan informasi periode tersebut.
3. Pemilik Kontrakan mengubah tanggal mulai atau tanggal berakhir.
4. Sistem memvalidasi dan menyimpan perubahan periode sewa.

**Pengecualian**
1. Jika tanggal mulai atau tanggal berakhir belum diisi, sistem meminta Pemilik Kontrakan melengkapi data.
2. Jika tanggal periode sewa tidak valid, sistem menolak penyimpanan dan menampilkan informasi kesalahan.
3. Jika data periode sewa gagal disimpan, sistem menampilkan pemberitahuan bahwa perubahan belum berhasil disimpan.

**Pascakondisi**
1. Data periode sewa berhasil tersimpan atau diperbarui.
2. Tanggal mulai dan tanggal berakhir sewa tercatat.
3. Informasi periode sewa dapat digunakan untuk menentukan status ketersediaan kamar dan pemantauan masa sewa.

---

## Catatan Verifikasi

1. Enam skenario di atas dipilih dari use case prioritas Must.
2. Setiap skenario memiliki aktor dan minimal satu kebutuhan fungsional (KF) yang dirujuk.
3. Setiap skenario memiliki alur utama dan minimal satu pengecualian.
4. Alur alternatif disertakan jika variasi proses dapat dijelaskan berdasarkan kebutuhan yang tersedia.
5. Detail teknis yang belum ditetapkan dalam PRD atau SRS tidak diasumsikan sebagai ketentuan final.
6. KF-08 berprioritas Must sesuai dengan penetapan prioritas pada dokumen SRS.
