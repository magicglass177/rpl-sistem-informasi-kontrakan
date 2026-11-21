# PR Jobsheet 12 — Code Review dan Perbaikan Keamanan

Branch: `fitur/perbaikan-keamanan` → `main`
Issue yang ditutup: P-01, P-02, P-03, P-04, P-05 (triase di `docs/laporan-temuan.md`)

## Deskripsi Perubahan

- `docs/laporan-temuan.md`: prediksi OWASP, tabel 10 temuan kasus `kasus_rentan.py`,
  tiga bukti, lima temuan utama, catatan kualitas perbaikan AI, tujuh temuan mandiri,
  triase, dan bukti perbaikan.
- CSRF: token acak per sesi di `app.py`, input tersembunyi pada 9 formulir POST,
  penolakan 400 + log saat token tidak cocok.
- Batas percobaan login: modul `percobaan.py` (5 kegagalan/5 menit per IP+username),
  respons 429 saat terkunci, dan uji kedaluwarsa dengan waktu suntikan.
- Logging: login gagal/berhasil, akun terkunci, akses 403, dan CSRF gagal tanpa kata sandi.
- Konfigurasi: `APP_ENV=production` mewajibkan kunci, `SECRET_KEY` diterima sebagai
  alternatif `FLASK_SECRET_KEY`, `SESSION_COOKIE_SECURE` pada produksi, debug dari
  lingkungan, serta header `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`.
- Pengujian: `uji_cepat.py` menjadi 21 kelompok uji; `test_keamanan.py` baru; total 59 uji unit.
- Jurnal: 8 entri baru; rencana Sprint 3 dan skrip demo checkpoint.

## Jenis Perubahan

- [x] Perbaikan bug / keamanan
- [x] Dokumentasi
- [x] Pengujian

## Pengujian

- `python tests/uji_cepat.py` → SEMUA UJI LULUS
- `python -m unittest discover -s tests` → 59 tests OK
- Uji produksi tanpa kunci → `RuntimeError`; `SESSION_COOKIE_SECURE=True` saat produksi.

## Penggunaan AI

AI dipakai untuk menganalisis kasus rentan, menghasilkan draf perbaikan, dan merangkum
dokumen. Tinjauan manusia menemukan: pemeriksaan `next` yang tidak lengkap, IDOR yang
terlewat, form logout yang tidak mendapat token, username log tanpa `%r`, dan saran penghapusan
uji lama. Rincian pada `jurnal-vibe-coding.md` Siklus 1-7.

## Tinjauan Silang

Tidak ada pasangan kelompok/akses repositori lain di lingkungan ini, sehingga **5 Issue
silang belum dibuat dan dikirim**. Lima draf Issue beserta dua catatan positif sudah
disiapkan pada `docs/laporan-temuan.md` dan akan dikirim setelah dosen menetapkan pasangan.
Tidak ada aplikasi pihak lain yang diserang atau dipindai.

## Temuan yang Ditunda

- Penyimpanan batas login di memori → Sprint 3 (multi-proses).
- CSP ketat karena `onsubmit` sebaris → Minggu 14 bersama HTTPS.
- `pip-audit` tidak tersedia → Sprint 3 bila lingkungan mengizinkan.
- UAT klien dan uji beban → Minggu 13-14.

## Checklist

- [x] Kode sudah ditinjau dengan Lampiran C.
- [x] Fitur sudah diuji; uji lama tidak dihapus.
- [x] Dokumentasi dan jurnal diperbarui.
- [x] Tidak ada kata sandi, kunci rahasia, atau berkas `.db` di repositori.
