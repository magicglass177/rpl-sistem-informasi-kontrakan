import logging
import os
import secrets
from pathlib import Path

from flask import Flask, abort, request, session

from models import init_db
from routes import main

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    secret_key = os.environ.get("FLASK_SECRET_KEY")
    if not secret_key:
        raise RuntimeError(
            "Variabel lingkungan FLASK_SECRET_KEY belum diatur."
        )

    app.config["SECRET_KEY"] = secret_key

    # HttpOnly dan SameSite=Lax pada cookie sesi (Werkzeug/Flask).
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

    def csrf_token():
        """Token acak per sesi untuk setiap formulir POST."""
        if "csrf_token" not in session:
            session["csrf_token"] = secrets.token_hex(16)
        return session["csrf_token"]

    app.jinja_env.globals["csrf_token"] = csrf_token

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

    Path(app.instance_path).mkdir(
        parents=True,
        exist_ok=True
    )

    init_db()
    app.register_blueprint(main)

    return app


app = create_app()


if __name__ == "__main__":
    # Hanya untuk pengembangan lokal, jangan aktifkan di produksi.
    app.run(debug=True)