# Deskripsi Pull Request — Jobsheet 9

## Ringkasan
Menyelesaikan kerangka proyek dan modul CRUD entitas kamar serta entitas penyewa untuk Sistem Informasi Pengelolaan Kontrakan. Perubahan mencakup lapisan model, service, route, template, pengujian otomatis, dan dokumentasi hasil uji.

## Fitur yang Selesai
- F1 — Kerangka proyek Flask + SQLite.
- F2 — Daftar kamar dengan status ketersediaan dan pencarian.
- F3 — Tambah kamar dengan validasi dan penanganan duplikat.
- F4 — Ubah kamar dengan form terisi data lama dan 404 untuk ID tidak ditemukan.
- F5 — Hapus kamar melalui `POST`, dengan konfirmasi, penanganan foreign key, dan 404.
- F6 — Daftar penyewa dengan pencarian.
- F7 — Tambah penyewa dengan validasi nama, nomor telepon, dan alamat.
- F8 — Ubah penyewa.
- F9 — Hapus penyewa dengan penanganan foreign key.

## Berkas yang Diubah
- `models.py`
- `routes.py`
- `services.py`
- `templates/base.html`
- `templates/kamar_list.html`
- `templates/penyewa_list.html`
- `templates/penyewa_form.html`
- `tests/test_crud_kamar.py`
- `tests/test_crud_penyewa.py`
- `docs/pengujian/hasil-uji-modul-crud.md`
- `docs/rencana-sprint.md`
- `docs/pr-js9-crud-kamar.md`
- `jurnal-vibe-coding.md`

## Cara Menguji
1. Aktifkan virtual environment.
2. Jalankan `python -m unittest discover -s tests -v`.
3. Jalankan `python tests/cek_skema.py`.
4. Jalankan `python tests/cek_skema_lanjutan.py`.
5. Jalankan `python tests/cek_validasi_telepon.py`.
6. Jalankan `python app.py` dengan `FLASK_SECRET_KEY` terpasang.
7. Buka `/kamar` dan `/penyewa`.

## Penggunaan AI
- Bagian yang dibantu AI: kerangka proyek, rute CRUD, validasi, template, dan perbaikan bug.
- Bagian yang diubah: rute hapus dipindahkan dari `models.py` ke `routes.py`; import dibersihkan; flash dipindahkan ke area konten; konfirmasi hapus diubah menjadi pesan statis; validasi penyewa diperketat.
- Bagian yang ditolak: rute hapus hasil AI yang ditempelkan pada lapisan model.
- Entri jurnal: 1–16.

## Daftar Periksa
- [x] Lapisan benar: SQL hanya di `models.py`, validasi di `services.py`, rute tipis.
- [x] SQL berparameter.
- [x] Tidak ada rahasia di kode.
- [x] Saya paham semua kode.
- [x] 53 pengujian otomatis lulus.
- [x] Skema basis data tidak berubah.
