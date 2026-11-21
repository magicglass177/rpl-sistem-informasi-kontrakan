# PR Jobsheet 11 — Autentikasi, Peran, dan Antarmuka

Branch: `fitur/autentikasi-peran` → `main`

## Deskripsi Perubahan

- Menambahkan peran `pemilik` dan `kasir` pada skema, model, layanan, dan skrip akun.
- `services.buat_pengguna`, `services.autentikasi`, `services.validasi_pengguna_baru`
  memakai hash Werkzeug dan hash palsu untuk menyamakan waktu respons.
- Login: pesan galat tunggal, `session.clear()`, sesi hanya `pengguna_id`, `next`
  divalidasi (internal saja), cookie HttpOnly + SameSite=Lax, logout lewat POST.
- `peran_diperlukan(*peran)` dan `muat_pengguna()` menegakkan akses di server pada
  seluruh rute termasuk POST; halaman 403 ditambahkan.
- `base.html` memakai satu `static/style.css`, menu menurut peran, dan tombol aksi
  disembunyikan untuk kasir (penegakan tetap di server).
- Validasi dua lapis pada seluruh form; uji login/peran ditambahkan pada `uji_cepat.py`.

## Jenis Perubahan

- [x] Fitur baru
- [x] Perbaikan bug
- [x] Dokumentasi

## Pengujian

- `python tests/uji_cepat.py` → SEMUA UJI LULUS (17 kelompok uji, termasuk login dan peran).
- `python -m unittest discover -s tests` → 53 tests OK.
- Uji asap: seluruh halaman pemilik/kasir sesuai matriks akses; halaman 403 tampil.

## Penggunaan AI

AI dipakai untuk merancang fungsi autentikasi, decorator peran, dan templat. Tinjauan
manual menemukan dan memperbaiki: decorator `@hanya_pemilih` yang tidak terdefinisi,
escape backslash rusak pada `_tujuan_aman`, skrip akun yang membaca kata sandi dari
lingkungan, serta pesan galat login yang membedakan username dan kata sandi.
Rincian ada pada `jurnal-vibe-coding.md` Siklus 1-8.

## Temuan Keamanan yang Ditunda

- Batas percobaan login (brute force) → Pertemuan 12.
- Token CSRF untuk seluruh form POST → Pertemuan 12.
- Atribut `Secure` pada cookie sesi → Pertemuan 14 (HTTPS).

Rincian lengkap: `docs/temuan-keamanan.md`.

## Checklist

- [x] Kode sudah diperiksa.
- [x] Fitur sudah diuji.
- [x] Dokumentasi sudah diperbarui.
- [x] Tidak ada data pribadi, kata sandi, atau informasi rahasia yang disertakan.
