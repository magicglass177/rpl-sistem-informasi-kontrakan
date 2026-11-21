# Tinjauan Modul Periode Sewa (Jobsheet 10)

## Daftar Periksa Relasi

| No. | Pertanyaan | Ya | Tidak | Catatan |
|---:|---|---:|---:|---|
| 1 | Perubahan dua tabel berada dalam satu transaksi? | Ya | | `create_sewa()` memakai satu koneksi dan satu `commit`. |
| 2 | Ada query di luar `models.py`? | | Tidak | Query hanya di `models.py`. |
| 3 | Kolom yang hanya berubah lewat transaksi tidak diubah dari form? | Ya | | Tidak ada kolom status yang diubah langsung. |
| 4 | Semua query SQL berparameter? | Ya | | Termasuk pencarian dan penyaringan. |
| 5 | Kunci asing ditangani dengan pesan ramah? | Ya | | Kamar/penyewa tidak ada dan periode bertumpang tindih ditangani. |

## Temuan

| No. | Temuan | Kategori | Tindakan |
|---:|---|---|---|
| 1 | Pencarian awal memakai `f"%{kata}%"` tanpa escape, sehingga `%` dan `_` dianggap wildcard. | Keamanan / Kebenaran | Diperbaiki sekarang dengan `_escape_like` dan `ESCAPE '\'`. |
| 2 | Form tambah sewa belum menampilkan pesan khusus saat periode bertumpang tindih. | Kesesuaian | Diperbaiki sekarang dengan pesan pada kolom tanggal selesai. |
| 3 | `get_all_sewa` awal tidak mendukung penyaringan status. | Kesesuaian | Diperbaiki sekarang dengan parameter `status` tetap di kode. |

## Keputusan
- **Ubah** untuk temuan 1–3.
- Perilaku program tidak berubah; hanya pencarian, pesan, dan penyaringan yang diperbaiki.
