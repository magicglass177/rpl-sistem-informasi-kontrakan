import logging
import os
import secrets
from pathlib import Path

from flask import Flask, abort, request, session

from models import init_db
from routes import main
from versi import VERSI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

PRODUKSI = os.environ.get("APP_ENV") == "production"


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Kunci rahasia dari lingkungan. Nama FLASK_SECRET_KEY dipakai proyek;
    # SECRET_KEY juga diterima agar sesuai konvensi Jobsheet 12.
    secret_key = os.environ.get("FLASK_SECRET_KEY") or os.environ.get("SECRET_KEY")

    if not secret_key:
        if PRODUKSI:
            raise RuntimeError(
                "FLASK_SECRET_KEY/SECRET_KEY wajib diatur pada lingkungan produksi."
            )
        raise RuntimeError(
            "Variabel lingkungan FLASK_SECRET_KEY belum diatur."
        )

    app.config["SECRET_KEY"] = secret_key

    # HttpOnly dan SameSite=Lax selalu aktif; Secure hanya pada produksi (HTTPS).
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    app.config["SESSION_COOKIE_SECURE"] = PRODUKSI

    def csrf_token():
        """Token acak per sesi untuk setiap formulir POST."""
        if "csrf_token" not in session:
            session["csrf_token"] = secrets.token_hex(16)
        return session["csrf_token"]

    app.jinja_env.globals["csrf_token"] = csrf_token
    app.jinja_env.globals["versi"] = VERSI

    @app.before_request
    def periksa_csrf():
        """Menolak POST tanpa token yang cocok dengan token sesi."""
        if request.method != "POST":
            return

        dikirim = request.form.get("csrf_token", "").encode()
        asli = session.get("csrf_token", "").encode()

        if not asli or not secrets.compare_digest(dikirim, asli):
            app.logger.warning(
                "CSRF gagal path=%r ip=%s",
                request.path,
                request.remote_addr,
            )
            abort(400)

    @app.after_request
    def tambah_header_keamanan(respons):
        """Header dasar pada setiap respons."""
        respons.headers["X-Content-Type-Options"] = "nosniff"
        respons.headers["X-Frame-Options"] = "DENY"
        respons.headers["Referrer-Policy"] = "same-origin"
        return respons

    Path(app.instance_path).mkdir(
        parents=True,
        exist_ok=True
    )

    init_db()
    app.register_blueprint(main)

    return app


app = create_app()


if __name__ == "__main__":
    # Debug hanya bila diminta lewat lingkungan dan tidak pernah pada produksi.
    # Tidak memakai host 0.0.0.0.
    debug = os.environ.get("FLASK_DEBUG") == "1" and not PRODUKSI
    app.run(debug=debug)