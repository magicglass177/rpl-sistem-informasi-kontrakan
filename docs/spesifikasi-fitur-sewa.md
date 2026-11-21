# Spesifikasi Fitur Kecil — Modul Periode Sewa (Jobsheet 10)

## Entitas Berelasi
Entitas pertama: `kamar` dan `penyewa`.
Entitas kedua: `sewa` (periode sewa), yang merujuk `kamar.id_kamar` dan `penyewa.id_penyewa`.

## Fitur Kecil

| No. | Fitur kecil | Kriteria penerimaan | Pelaksana |
|---|---|---|---|
| G1 | Daftar periode sewa dengan JOIN | Menampilkan tanggal mulai, tanggal selesai, nama penyewa, dan nomor kamar; keadaan kosong menampilkan "Belum ada periode sewa". | Bayu |
| G2 | Tambah periode sewa dengan pilihan induk | Kamar dan penyewa dipilih dari menu pilihan; tanggal valid; periode tidak boleh bertumpang tindih pada kamar yang sama; harga disepakati tidak negatif. | Bayu |
| G3 | Dampak pada tabel lain (transaksi) | Penyimpanan sewa dilakukan dalam satu transaksi; ID induk yang tidak ada ditolak tanpa meninggalkan baris sebagian. | Bayu |
| G4 | Pencarian dan penyaringan | Pencarian berdasarkan nama penyewa atau nomor kamar; penyaringan status periode (aktif/berakhir); dapat digabung. | Bayu |

## Batasan
- `id_kamar` dan `id_penyewa` wajib ada di tabel induk.
- `tanggal_mulai`, `tanggal_selesai`, dan opsional `tanggal_jatuh_tempo` harus berformat `YYYY-MM-DD`.
- `tanggal_selesai` tidak boleh lebih awal dari `tanggal_mulai`.
- Kamar tidak boleh memiliki periode sewa aktif yang bertumpang tindih.
- `harga_sewa_disepakati` tidak boleh negatif.
- `status ketersediaan` kamar tidak diubah langsung; dihitung dari periode sewa.
