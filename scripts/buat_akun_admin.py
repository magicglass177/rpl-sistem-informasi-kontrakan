import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault("FLASK_SECRET_KEY", "test-only-secret-key")

import models

username = os.environ.get("ADMIN_USERNAME", "admin")
password = os.environ.get("ADMIN_PASSWORD")

if not password:
    raise SystemExit("Set ADMIN_PASSWORD terlebih dahulu.")

berhasil, status = models.create_akun(username, password)

if berhasil:
    print(f"Akun '{username}' berhasil dibuat.")
elif status == "duplicate":
    print(f"Akun '{username}' sudah ada.")
else:
    raise SystemExit("Gagal membuat akun karena kesalahan database.")