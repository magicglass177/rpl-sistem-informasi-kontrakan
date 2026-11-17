from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
)

from models import get_all_kamar


main = Blueprint("main", __name__)


@main.route("/")
def beranda():
    return redirect(url_for("main.daftar_kamar"))


@main.route("/kamar")
def daftar_kamar():
    kata_kunci = request.args.get("q", "").strip()
    daftar_kamar = get_all_kamar(kata_kunci)

    return render_template(
        "kamar_list.html",
        page_title="Daftar Kamar",
        active_page="kamar",
        daftar_kamar=daftar_kamar,
        kata_kunci=kata_kunci,
    )