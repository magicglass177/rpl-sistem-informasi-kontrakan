
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from models import get_all_kamar, create_kamar
from services import validate_kamar


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


@main.route("/kamar/tambah", methods=["GET", "POST"])
def tambah_kamar():
    if request.method == "POST":
        data_bersih, errors = validate_kamar(request.form)

        if errors:
            return render_template(
                "kamar_form.html",
                page_title="Tambah Kamar",
                active_page="kamar",
                data=data_bersih,
                errors=errors,
            ), 400

        berhasil, status = create_kamar(
            data_bersih["nomor_kamar"],
            data_bersih["harga_sewa"],
        )

        if berhasil:
            flash("Data kamar berhasil ditambahkan.", "success")
            return redirect(url_for("main.daftar_kamar"))

        if status == "duplicate":
            errors["nomor_kamar"] = (
                f"Nomor kamar {data_bersih['nomor_kamar']} sudah ada."
            )
        else:
            errors["database"] = (
                "Data kamar gagal disimpan karena terjadi "
                "kesalahan database."
            )

        return render_template(
            "kamar_form.html",
            page_title="Tambah Kamar",
            active_page="kamar",
            data=data_bersih,
            errors=errors,
        ), 400

    return render_template(
        "kamar_form.html",
        page_title="Tambah Kamar",
        active_page="kamar",
        data={"nomor_kamar": "", "harga_sewa": ""},
        errors={},
    )
