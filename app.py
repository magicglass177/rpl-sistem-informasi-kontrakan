import os
from pathlib import Path

from flask import Flask

from models import init_db
from routes import main


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