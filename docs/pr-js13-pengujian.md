# PR Jobsheet 13 — Test Case, pytest, Laporan Cacat, dan Rencana UAT

Branch: `fitur/pengujian` → `main`
Issue yang ditutup: D-01, D-02, D-03 (`docs/pengujian/laporan-cacat.md`)

## Deskripsi Perubahan

- `docs/pengujian/test-case.md`: matriks 8 KF, **39 test case** dengan partisi
  ekuivalen dan nilai batas; harapan ditulis dari PRD/kamus data sebelum uji dijalankan;
  kolom hasil aktual dan status telah diisi.
- `requirements-dev.txt`: `pytest==9.1.1` (nama persis dan versi dikunci).
- `tests/conftest.py`: basis data sementara, fixture `basis_bersih`, `kirim`
  (POST + token CSRF), `tamu`, `pemilik`, `kasir`; `kontrakan.db` nyata tidak tersentuh.
- `tests/test_validasi.py` dan 5 berkas uji lainnya: **29 fungsi uji baru**
  (112 kasus/parametrize), mencakup validasi, alur inti, matriks akses,
  pembayaran/laporan, dan autentikasi. `uji_cepat.py` tetap dipertahankan.
- Pemeriksaan mandiri uji AI: 3 asersi lemah diperbaiki; **3 mutasi manual**
  (M1–M3) semuanya tertangkap.
- Perbaikan 3 cacat (commit terpisah, alur merah → hijau):
  - D-01 tolak format tanggal kompak `YYYYMMDD` → `866c8aa`
  - D-02 batasi uang ke `DECIMAL(12,2)` → `33480db`
  - D-03 escape `%`/`_` pada pencarian → `78e3131`
- `docs/pengujian/rencana-uat.md`: 7 skenario bahasa klien, 4 kriteria lulus,
  cara merekam temuan, dan status penjadwalan yang jujur (belum dikonfirmasi).
- Jurnal: 8 entri baru (Siklus 1–8), termasuk uji AI yang lemah dan dua
  kegagalan yang ternyata berasal dari uji itu sendiri, bukan dari kode.

## Jenis Perubahan

- [x] Perbaikan bug
- [x] Pengujian
- [x] Dokumentasi

## Pengujian

| Perintah | Hasil |
|---|---|
| `python -m pytest -q tests` | 111 passed, 23 subtests |
| `python tests/uji_cepat.py` | SEMUA UJI LULUS |
| `python -m unittest discover -s tests` | 59 tests OK |

Sebelum perbaikan: 3 failed, 108 passed — ketiganya cacat nyata. Dua kegagalan
lain pada putaran pertama ternyata berasal dari harapan uji yang saya tulis
keliru dan sudah dikoreksi secara transparan (lihat `laporan-cacat.md`).

## Penggunaan AI

AI dipakai untuk membuat draf uji dari tabel test case, mengusulkan perbaikan
cacat, dan merangkum dokumen. Tinjauan manusia menemukan: TC-27 salah lulus
karena asersi tidak spesifik, matriks akses `/penyewa` keliru, perbandingan HTML
login terlalu kuat, dan usulan mengubah pesan galat lama yang akan merusak uji
lama. Rincian pada `jurnal-vibe-coding.md` Siklus 1–8.

## Yang Belum Selesai (eksternal)

- UAT dengan klien nyata dan tanggapan jadwal: Pertemuan 14 (PT/BM).
- Kuesioner kegunaan: Pertemuan 14.
- Laporan PDF akhir di LMS: siap dicetak dari `docs/laporan-pengujian.html`.

## Checklist

- [x] ≥ 20 test case, terlacak ke KF, harapan dari PRD.
- [x] ≥ 8 fungsi uji otomatis lulus, asersi spesifik, pelanggaran diuji.
- [x] ≥ 3 mutasi manual, ≥ 3 cacat diperbaiki dengan uji regresi.
- [x] Rencana UAT ≥ 5 skenario dan kriteria lulus terukur.
- [x] Tidak ada kata sandi, kunci rahasia, atau berkas `.db` di repositori.
- [x] Uji lama tidak dihapus atau dilonggarkan.
