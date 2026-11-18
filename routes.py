from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from models import (
    get_all_kamar,
    create_kamar,
    get_kamar_by_id,
    update_kamar,
)
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
            judul_form="Tambah Kamar",
            action_url=url_for("main.tambah_kamar"),
            teks_tombol="Simpan",
        ), 400

    return render_template(
        "kamar_form.html",
        page_title="Tambah Kamar",
        active_page="kamar",
        data={"nomor_kamar": "", "harga_sewa": ""},
        errors={},
        judul_form="Tambah Kamar",
        action_url=url_for("main.tambah_kamar"),
        teks_tombol="Simpan",
    )

@main.route("/kamar/<int:id_kamar>/ubah", methods=["GET", "POST"])
def ubah_kamar(id_kamar):
    kamar = get_kamar_by_id(id_kamar)

    # Jika data tidak ditemukan, tampilkan halaman 404.
    if kamar is None:
        abort(404)

    if request.method == "POST":
        data_bersih, errors = validate_kamar(request.form)

        if errors:
            return render_template(
                "kamar_form.html",
                page_title="Ubah Kamar",
                active_page="kamar",
                data=data_bersih,
                errors=errors,
                judul_form="Ubah Kamar",
                action_url=url_for(
                    "main.ubah_kamar",
                    id_kamar=id_kamar
                ),
                teks_tombol="Simpan Perubahan",
            ), 400

        berhasil, status = update_kamar(
            id_kamar,
            data_bersih["nomor_kamar"],
            data_bersih["harga_sewa"],
        )

        if berhasil:
            flash("Data kamar berhasil diperbarui.", "success")
            return redirect(url_for("main.daftar_kamar"))

        if status == "duplicate":
            errors["nomor_kamar"] = (
                f"Nomor kamar {data_bersih['nomor_kamar']} sudah ada."
            )
        else:
            errors["database"] = (
                "Data kamar gagal diperbarui karena terjadi "
                "kesalahan database."
            )

        return render_template(
            "kamar_form.html",
            page_title="Ubah Kamar",
            active_page="kamar",
            data=data_bersih,
            errors=errors,
            judul_form="Ubah Kamar",
            action_url=url_for(
                "main.ubah_kamar",
                id_kamar=id_kamar
            ),
            teks_tombol="Simpan Perubahan",
        ), 400

    # GET: isi form dengan data lama.
    return render_template(
        "kamar_form.html",
        page_title="Ubah Kamar",
        active_page="kamar",
        data={
            "nomor_kamar": kamar["nomor_kamar"],
            "harga_sewa": str(kamar["harga_sewa"]),
        },
        errors={},
        judul_form="Ubah Kamar",
        action_url=url_for(
            "main.ubah_kamar",
            id_kamar=id_kamar
        ),
        teks_tombol="Simpan Perubahan",
    )
