"""Buat akun awal dari terminal.

Jalankan: python scripts/buat_pengguna.py

Kata sandi dibaca dengan getpass, tidak ditulis di kode, jurnal, atau repositori.
"""
import getpass
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import models
import services


def main():
    models.init_db()

    username = input("Nama pengguna: ").strip()
    peran = input("Peran (pemilik/kasir): ").strip()
    password = getpass.getpass("Kata sandi (min. 8 karakter): ")

    galat = services.buat_pengguna(username, password, peran)

    if galat:
        print("\n".join(galat))
        return

    print(f"Akun '{username}' dengan peran '{peran}' berhasil dibuat.")


if __name__ == "__main__":
    main()