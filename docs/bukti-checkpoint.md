# Bukti Verifikasi Antarmuka dan Daftar Screenshot Checkpoint — Jobsheet 12

## Keterbatasan pengambilan gambar

Percobaan mengambil screenshot otomatis gagal karena jendela browser desktop tidak terlihat
(`browser.screenshot` memerlukan tab yang terlihat). Oleh karena itu bukti di bawah
menggunakan **snapshot aksesibilitas browser** dan log server, bukan berkas gambar.
Pada saat checkpoint, tangkap gambar sesuai daftar di bagian kedua.

## Bukti verifikasi melalui browser (localhost:5000)

1. **Halaman login** (`/login`) dirender dengan benar: judul "Login Pengelola", dua label
   (`Username`, `Password`), tombol `Login`, dan pesan "Masuk untuk melihat menu." pada sidebar
   untuk tamu.
2. **Login pemilik** (`pemilikdemo`, peran `pemilik`) → flash `role="status"` berisi
   "Login berhasil."; sidebar menampilkan 6 menu: Dashboard, Kamar, Penyewa, Periode Sewa,
   Pembayaran, Laporan. Daftar kamar menampilkan tombol "+ Tambah Kamar" dan kolom Aksi.
3. **Logout POST** → redirect ke `/login`; log server mencatat `POST /logout 302`.
4. **Login kasir** (`kasirdemo`, peran `kasir`) → flash "Login berhasil."; sidebar hanya
   memuat Dashboard, Kamar, Periode Sewa, Pembayaran (tanpa Penyewa dan Laporan).
5. **Akses langsung ke `/kamar/tambah` sebagai kasir** → halaman "Akses Ditolak" dengan
   pesan `role="alert"` "Peran Anda tidak diizinkan membuka halaman ini." dan tautan
   "Kembali ke daftar kamar". Log server mencatat `GET /kamar/tambah 302` saat masih tamu,
   lalu 403 setelah login kasir. Bukti log:
   `Login berhasil username='kasirdemo' peran='kasir'`,
   `Akses ditolak path='/kamar/tambah' ip=127.0.0.1 pengguna='kasirdemo'`,
   `GET /kamar/tambah HTTP/1.1 403`.
6. **Log server** (tanpa kata sandi):
   `Login berhasil username='pemilikdemo' peran='pemilik'`,
   `Login berhasil username='kasirdemo' peran='kasir'`.

Catatan: akun di atas adalah data karangan lokal dibuat lewat skrip; kata sandi tidak
ditampilkan di repositori, jurnal, laporan, maupun tangkapan layar.

## Daftar screenshot yang perlu diambil saat checkpoint

| No | Nama berkas | Layar | Yang terlihat |
|---:|---|---|---|
| 1 | `01-login.png` | `/login` | Form login dengan label dan tombol; sidebar tamu |
| 2 | `02-pemilik-menu.png` | `/kamar` sebagai pemilik | Nama+peran pemilik, 6 menu, tombol "+ Tambah Kamar", kolom Aksi |
| 3 | `03-kasir-menu.png` | `/kamar` sebagai kasir | Menu lebih singkat, tanpa tombol tambah dan kolom Aksi |
| 4 | `04-403.png` | `/kamar/tambah` diketik langsung sebagai kasir | Halaman "Akses Ditolak" + tautan kembali |
| 5 | `05-csrf-400.png` | POST tanpa token lewat alat pengembang | Respons 400 + pesan di log |
| 6 | `06-login-429.png` | 6 kali login gagal lalu kata sandi benar | Pesan "Terlalu banyak percobaan login" |

Simpan gambar di folder lokal (tidak wajib di-repo), lalu sisipkan ke laporan PDF pada
bagian yang sesuai. Jangan tampilkan kata sandi atau isi `.env`/`.db`.
