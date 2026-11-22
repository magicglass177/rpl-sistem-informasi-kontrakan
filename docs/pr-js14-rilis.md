# PR Jobsheet 14 — Rilis v1.0.0, Deployment, Dokumentasi, dan UAT

Branch: `rilis/v1.0.0` → `main`

## Deskripsi Perubahan

- Konfigurasi rilis: `KONTRAKAN_DB` dari lingkungan, `versi.py` (1.0.0),
  `cadangkan.py` (API backup SQLite), `.gitignore` diperbarui, `CHANGELOG.md`,
  `requirements.txt` berversi termasuk `waitress==3.0.2`.
- `README.md`: instalasi, konfigurasi, akun pertama, menjalankan (dev & prod),
  pengujian, cadangan/pemulihan, struktur, keamanan.
- `docs/manual-pengguna.md`: 8 tugas bernomor, 5 referensi gambar, tabel masalah.
- `tests/test_rilis.py`: 6 uji (versi SemVer, versi tampil, changelog, .gitignore,
  requirements dikunci, cadangan berisi data yang sama).
- `docs/uat/hasil-uat.md`: lembar skenario, skor SUS, triase — **simulasi**
  dengan narasumber fiktif (bukan UAT nyata).
- Bukti: aplikasi berjalan lewat Waitress pada mode produksi (`APP_ENV=production`,
  `SECRET_KEY` dari lingkungan) dengan login pemilik dan kasir sukses;
  aplikasi menolak start tanpa `SECRET_KEY`; cadangan dan pemulihan teruji.

## Pengujian

| Perintah | Hasil |
|---|---|
| `python -m pytest -q tests` | 117 passed, 23 subtests |
| `python tests/uji_cepat.py` | SEMUA UJI LULUS |
| `python -m unittest discover -s tests` | 59 tests OK |

## Audit kesiapan rilis

- `git ls-files "*.db" ".env"` → kosong
- `git log --all -- "*.db" ".env"` → kosong
- `git grep` hanya menemukan contoh di docs dan data uji karangan
- Produksi tanpa `SECRET_KEY` menolak start dengan pesan jelas

## Uji orang asing

README dijalankan pada folder bersih dengan venv baru: pip install OK,
pytest 117 passed, versi import OK, dev server berjalan. Tidak ada langkah
yang macet; catatan perbaikan: tidak ada.

## Yang Belum Selesai (eksternal)

- UAT dengan klien nyata dan persetujuan (PT/BM, Pertemuan 14/15).
- Tangkapan layar manual pengguna (folder `docs/gambar/` disiapkan; gambar
  diambil saat UAT).
- Tag v1.0.0 diberikan setelah merge (Langkah 7/13).
- Laporan rilis PDF akhir di LMS (siap dicetak dari `docs/laporan-rilis.html`).

## Checklist

- [x] Tanpa kredensial dalam kode dan riwayat
- [x] requirements berversi
- [x] Cadangan teruji dan pemulihan berhasil
- [x] Berjalan di Waitress mode produksi
- [x] Akses dari komputer lain (uji lokal)
- [x] README lulus uji orang asing
- [x] Manual pengguna dengan tabel masalah
- [x] UAT simulasi terdokumentasi (jujur: bukan UAT nyata)
- [x] Uji lama tetap lulus
