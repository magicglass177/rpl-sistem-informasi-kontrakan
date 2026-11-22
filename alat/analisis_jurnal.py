"""Rekap Jurnal Vibe Coding.

python alat/analisis_jurnal.py jurnal/*.md

Setiap berkas jurnal berisi tabel Markdown dengan kolom (urutan bebas,
nama tetap): No | Tujuan | Prompt | Hasil AI | Keputusan | Alasan.
Keputusan diawali Terima / Ubah / Tolak. Tag pada kolom Tujuan atau Alasan,
mis. [Debug], [Keamanan]; jenis galat AI ditulis [Galat: acuan-salah], dll.
"""
import re
import sys
from collections import Counter
from pathlib import Path

KEPUTUSAN = ("terima", "ubah", "tolak")


def baca_entri(berkas):
    """Kembalikan daftar entri (dict nama-kolom -> isi) dari satu berkas jurnal."""
    entri, kolom = [], None
    for baris in Path(berkas).read_text(encoding="utf-8").splitlines():
        if not baris.strip().startswith("|"):
            continue
        sel = [s.strip() for s in baris.strip().strip("|").split("|")]
        if all(set(s) <= set("-: ") for s in sel):
            continue  # baris pemisah |---|---|
        if kolom is None:
            nama = [s.lower() for s in sel]
            if "keputusan" in nama:
                kolom = {n: i for i, n in enumerate(nama)}
            continue
        if len(sel) >= len(kolom):
            entri.append({n: sel[i] for n, i in kolom.items()})
    return entri


def rekap(entri):
    """Hitung keputusan, tag, dan jenis galat AI."""
    keputusan, tag, galat = Counter(), Counter(), Counter()
    for e in entri:
        k = e.get("keputusan", "").lower()
        keputusan[next((x for x in KEPUTUSAN if k.startswith(x)), "lain")] += 1
        for t in re.findall(r"\[([^\]]+)\]", e.get("tujuan", "") + " " + e.get("alasan", "")):
            if t.lower().startswith("galat:"):
                galat[t.split(":", 1)[1].strip().lower()] += 1
            else:
                tag[t.lower()] += 1
    return keputusan, tag, galat


def persen(n, total):
    return f"{100 * n / total:.1f}%" if total else "-"


def cetak(judul, entri):
    total = len(entri)
    keputusan, tag, galat = rekap(entri)
    print(f"\n## {judul}  ({total} entri)")
    print("| Keputusan | Jumlah | Persen |")
    print("|---|---|---|")
    for k in (*KEPUTUSAN, "lain"):
        if keputusan[k] or k != "lain":
            print(f"| {k.capitalize()} | {keputusan[k]} | {persen(keputusan[k], total)} |")
    if tag:
        print("\nTag (jumlah):")
        for t, n in tag.most_common():
            print(f"  - {t}: {n}")
    if galat:
        print("\nJenis galat AI (jumlah):")
        for g, n in galat.most_common():
            print(f"  - {g}: {n}")


def main():
    berkas = [Path(b) for b in sys.argv[1:]] if len(sys.argv) > 1 else []
    if not berkas:
        print("Pakai: python alat/analisis_jurnal.py jurnal/*.md")
        return
    semua = []
    for b in berkas:
        e = baca_entri(b)
        cetak(b.name, e)
        semua.extend(e)
    if len(berkas) > 1:
        cetak("GABUNGAN", semua)


if __name__ == "__main__":
    main()
