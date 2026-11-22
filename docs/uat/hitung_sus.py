"""Hitung skor SUS (System Usability Scale).

python docs/uat/hitung_sus.py

Isi JAWABAN: satu daftar 10 angka (1-5) per responden, sesuai urutan butir 1-10.
"""
JAWABAN = {
    "Pemilik": [4, 2, 4, 1, 4, 2, 5, 2, 4, 1],
    "Kasir": [5, 1, 4, 2, 4, 1, 5, 1, 5, 2],
}


def skor_sus(j):
    assert len(j) == 10 and all(1 <= x <= 5 for x in j), "harus 10 jawaban bernilai 1-5"
    # butir ganjil (1,3,5,..): jawaban - 1 ; butir genap (2,4,..): 5 - jawaban
    jumlah = sum((x - 1) if i % 2 == 0 else (5 - x) for i, x in enumerate(j))
    return jumlah * 2.5


if __name__ == "__main__":
    skor = {nama: skor_sus(j) for nama, j in JAWABAN.items()}
    for nama, s in skor.items():
        print(f"{nama:10s} {s:5.1f}")
    print(f"{'Rata-rata':10s} {sum(skor.values()) / len(skor):5.1f}")
