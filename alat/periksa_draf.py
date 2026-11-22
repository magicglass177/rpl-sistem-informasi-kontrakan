"""Periksa kelengkapan draf Bab 4.

python alat/periksa_draf.py docs/bab4 PRD.md

Berkas draf diberi nama 4.1-lingkungan.md ... 4.6-pembahasan.md.
Sebuah subbab dianggap SELESAI bila: (1) berkasnya ada, (2) memuat >= 150 kata
uraian (tabel dan kode tidak dihitung), (3) tidak ada penanda [ISI], dan
(4) memuat >= 1 bukti: tabel, gambar, atau blok kode.
Draf dianggap siap progress check bila >= 80% subbab selesai (>= 5 dari 6).
Alat ini juga mencari kode KF-xx pada draf yang tidak ada di PRD.md.
"""
import re
import sys
from pathlib import Path

SUBBAB = {
    "4.1": "Lingkungan Implementasi",
    "4.2": "Implementasi Sistem",
    "4.3": "Tinjauan Kode dan Keamanan",
    "4.4": "Pengujian",
    "4.5": "Rilis dan Dokumentasi",
    "4.6": "Pembahasan",
}
MIN_KATA = 150


def analisis(teks):
    """Kembalikan (jumlah kata uraian, ada_penanda_ISI, ada_bukti)."""
    uraian, dalam_kode, bukti = [], False, False
    for baris in teks.splitlines():
        if baris.strip().startswith("```"):
            dalam_kode, bukti = not dalam_kode, True
            continue
        if dalam_kode:
            continue
        if baris.strip().startswith("|") or baris.strip().startswith("!["):
            bukti = True
            continue
        if not baris.lstrip().startswith("#"):
            uraian.append(baris)
    return len(" ".join(uraian).split()), "[ISI]" in teks, bukti


def main():
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("docs/bab4")
    prd = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    kf_prd = set()
    if prd and prd.exists():
        kf_prd = set(re.findall(r"KF-\d+", prd.read_text(encoding="utf-8")))
    selesai, semua_teks = 0, ""
    print(f"{'Subbab':8s}{'Judul':32s}{'Kata':>6s}  Status")
    print("-" * 60)
    for kode, judul in SUBBAB.items():
        berkas = next(iter(sorted(folder.glob(f"{kode}-*.md"))), None)
        if berkas is None:
            print(f"{kode:8s}{judul:32s}{'-':>6s}  BELUM ADA BERKAS")
            continue
        teks = berkas.read_text(encoding="utf-8")
        semua_teks += teks
        kata, isi, bukti = analisis(teks)
        masalah = []
        if kata < MIN_KATA:
            masalah.append(f"kurang kata (<{MIN_KATA})")
        if isi:
            masalah.append("masih ada [ISI]")
        if not bukti:
            masalah.append("belum ada bukti (tabel/gambar/kode)")
        selesai += not masalah
        print(f"{kode:8s}{judul:32s}{kata:>6d}  {'SELESAI' if not masalah else '; '.join(masalah)}")
    print("-" * 60)
    print(f"Subbab selesai: {selesai}/6 = {100 * selesai // 6}%")
    if selesai >= 5:
        print("-> SIAP progress check (>= 80%)")
    else:
        print("-> BELUM mencapai 80%")
    if kf_prd:
        kf_draf = set(re.findall(r"KF-\d+", semua_teks))
        asing = kf_draf - kf_prd
        if asing:
            print(f"KF pada draf yang tidak ada di PRD: {sorted(asing)}")
        else:
            print("Semua KF pada draf ada di PRD.")


if __name__ == "__main__":
    main()
