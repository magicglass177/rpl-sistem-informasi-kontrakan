from flask import (
    Blueprint,
    abort,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from models import (
    create_akun,
    get_akun_by_username,
    create_kamar,
    create_pembayaran,
    create_penyewa,
    create_sewa,
    delete_kamar,
    delete_pembayaran,
    delete_penyewa,
    get_all_kamar,
    get_all_pembayaran,
    get_all_penyewa,
    get_all_sewa,
    get_kamar_by_id,
    get_pembayaran_by_id,
    verify_password,
    get_penyewa_by_id,
    get_sewa_by_id,
    update_kamar,
    update_penyewa,
)
from datetime import date

from services import (
    validate_kamar,
    validate_pembayaran,
    validate_penyewa,
    validate_sewa,
)


main = Blueprint("main", __name__)

@main.before_request
def wajib_login():
    """Membatasi akses ke halaman pengelolaan bagi pengguna yang belum login."""
    if request.endpoint in {"main.login"}:
        return

    if request.endpoint and request.endpoint.startswith("static"):
        return

    if not session.get("id_akun"):
        return redirect(url_for("main.login", next=request.path))


@main.route("/login", methods=["GET", "POST"])
def login():
    if session.get("id_akun"):
        return redirect(url_for("main.daftar_kamar"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        akun = get_akun_by_username(username)

        if akun and verify_password(akun["password_hash"], password):
            session.clear()
            session["id_akun"] = akun["id_akun"]
            session["username"] = akun["username"]
            flash("Login berhasil.", "success")

            tujuan = request.args.get("next", "")
            if tujuan.startswith("/"):
                return redirect(tujuan)

            return redirect(url_for("main.daftar_kamar"))

        flash("Username atau password salah.", "danger")

    return render_template(
        "login.html",
        page_title="Login",
        active_page=None,
        data={"username": request.form.get("username", "") if request.method == "POST" else ""},
        errors={},
    )


@main.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("Anda telah logout.", "success")
    return redirect(url_for("main.login"))


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


def _render_form_kamar(data, errors, judul_form, action_url, teks_tombol):
    """Menghilangkan duplikasi render_template pada rute tambah dan ubah kamar."""
    return render_template(
        "kamar_form.html",
        page_title=judul_form,
        active_page="kamar",
        data=data,
        errors=errors,
        judul_form=judul_form,
        action_url=action_url,
        teks_tombol=teks_tombol,
    )


@main.route("/kamar/tambah", methods=["GET", "POST"])
def tambah_kamar():
    if request.method == "POST":
        data_bersih, errors = validate_kamar(request.form)

        if errors:
            return _render_form_kamar(
                data_bersih,
                errors,
                "Tambah Kamar",
                url_for("main.tambah_kamar"),
                "Simpan",
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

        return _render_form_kamar(
            data_bersih,
            errors,
            "Tambah Kamar",
            url_for("main.tambah_kamar"),
            "Simpan",
        ), 400

    return _render_form_kamar(
        {"nomor_kamar": "", "harga_sewa": ""},
        {},
        "Tambah Kamar",
        url_for("main.tambah_kamar"),
        "Simpan",
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
            return _render_form_kamar(
                data_bersih,
                errors,
                "Ubah Kamar",
                url_for("main.ubah_kamar", id_kamar=id_kamar),
                "Simpan Perubahan",
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

        return _render_form_kamar(
            data_bersih,
            errors,
            "Ubah Kamar",
            url_for("main.ubah_kamar", id_kamar=id_kamar),
            "Simpan Perubahan",
        ), 400

    # GET: isi form dengan data lama.
    return _render_form_kamar(
        {
            "nomor_kamar": kamar["nomor_kamar"],
            "harga_sewa": str(kamar["harga_sewa"]),
        },
        {},
        "Ubah Kamar",
        url_for("main.ubah_kamar", id_kamar=id_kamar),
        "Simpan Perubahan",
    )


@main.route("/kamar/<int:id_kamar>/hapus", methods=["POST"])
def hapus_kamar(id_kamar):
    berhasil, status = delete_kamar(id_kamar)

    if berhasil:
        flash("Data kamar berhasil dihapus.", "success")

    elif status == "not_found":
        # Sesuai Lampiran A.5: ID yang tidak ditemukan menghasilkan 404.
        abort(404)

    elif status == "in_use":
        flash(
            "Data kamar tidak dapat dihapus karena masih digunakan "
            "dalam riwayat sewa. Hapus atau selesaikan data terkait "
            "sesuai prosedur terlebih dahulu.",
            "warning"
        )

    else:
        flash(
            "Data kamar gagal dihapus karena terjadi kesalahan "
            "database. Silakan coba kembali.",
            "danger"
        )

    return redirect(url_for("main.daftar_kamar"))


@main.route("/penyewa")
def daftar_penyewa():
    kata_kunci = request.args.get("q", "").strip()
    daftar_penyewa = get_all_penyewa(kata_kunci)

    return render_template(
        "penyewa_list.html",
        page_title="Daftar Penyewa",
        active_page="penyewa",
        daftar_penyewa=daftar_penyewa,
        kata_kunci=kata_kunci,
    )


@main.route("/penyewa/tambah", methods=["GET", "POST"])
def tambah_penyewa():
    if request.method == "POST":
        data_bersih, errors = validate_penyewa(request.form)

        if errors:
            return render_template(
                "penyewa_form.html",
                page_title="Tambah Penyewa",
                active_page="penyewa",
                data=data_bersih,
                errors=errors,
                judul_form="Tambah Penyewa",
                action_url=url_for("main.tambah_penyewa"),
                teks_tombol="Simpan",
            ), 400

        berhasil, status = create_penyewa(
            data_bersih["nama"],
            data_bersih["no_telepon"],
            data_bersih["alamat"],
        )

        if berhasil:
            flash("Data penyewa berhasil ditambahkan.", "success")
            return redirect(url_for("main.daftar_penyewa"))

        errors["database"] = (
            "Data penyewa gagal disimpan karena terjadi "
            "kesalahan database."
        )

        return render_template(
            "penyewa_form.html",
            page_title="Tambah Penyewa",
            active_page="penyewa",
            data=data_bersih,
            errors=errors,
            judul_form="Tambah Penyewa",
            action_url=url_for("main.tambah_penyewa"),
            teks_tombol="Simpan",
        ), 400

    return render_template(
        "penyewa_form.html",
        page_title="Tambah Penyewa",
        active_page="penyewa",
        data={"nama": "", "no_telepon": "", "alamat": ""},
        errors={},
        judul_form="Tambah Penyewa",
        action_url=url_for("main.tambah_penyewa"),
        teks_tombol="Simpan",
    )


@main.route("/penyewa/<int:id_penyewa>/ubah", methods=["GET", "POST"])
def ubah_penyewa(id_penyewa):
    penyewa = get_penyewa_by_id(id_penyewa)

    if penyewa is None:
        abort(404)

    if request.method == "POST":
        data_bersih, errors = validate_penyewa(request.form)

        if errors:
            return render_template(
                "penyewa_form.html",
                page_title="Ubah Penyewa",
                active_page="penyewa",
                data=data_bersih,
                errors=errors,
                judul_form="Ubah Penyewa",
                action_url=url_for(
                    "main.ubah_penyewa",
                    id_penyewa=id_penyewa
                ),
                teks_tombol="Simpan Perubahan",
            ), 400

        berhasil, status = update_penyewa(
            id_penyewa,
            data_bersih["nama"],
            data_bersih["no_telepon"],
            data_bersih["alamat"],
        )

        if berhasil:
            flash("Data penyewa berhasil diperbarui.", "success")
            return redirect(url_for("main.daftar_penyewa"))

        if status == "not_found":
            abort(404)

        errors["database"] = (
            "Data penyewa gagal diperbarui karena terjadi "
            "kesalahan database."
        )

        return render_template(
            "penyewa_form.html",
            page_title="Ubah Penyewa",
            active_page="penyewa",
            data=data_bersih,
            errors=errors,
            judul_form="Ubah Penyewa",
            action_url=url_for(
                "main.ubah_penyewa",
                id_penyewa=id_penyewa
            ),
            teks_tombol="Simpan Perubahan",
        ), 400

    return render_template(
        "penyewa_form.html",
        page_title="Ubah Penyewa",
        active_page="penyewa",
        data={
            "nama": penyewa["nama"],
            "no_telepon": penyewa["no_telepon"],
            "alamat": penyewa["alamat"],
        },
        errors={},
        judul_form="Ubah Penyewa",
        action_url=url_for(
            "main.ubah_penyewa",
            id_penyewa=id_penyewa
        ),
        teks_tombol="Simpan Perubahan",
    )


@main.route("/penyewa/<int:id_penyewa>/hapus", methods=["POST"])
def hapus_penyewa(id_penyewa):
    berhasil, status = delete_penyewa(id_penyewa)

    if berhasil:
        flash("Data penyewa berhasil dihapus.", "success")

    elif status == "not_found":
        abort(404)

    elif status == "in_use":
        flash(
            "Data penyewa tidak dapat dihapus karena masih digunakan "
            "dalam riwayat sewa. Hapus atau selesaikan data terkait "
            "sesuai prosedur terlebih dahulu.",
            "warning"
        )

    else:
        flash(
            "Data penyewa gagal dihapus karena terjadi kesalahan "
            "database. Silakan coba kembali.",
            "danger"
        )

    return redirect(url_for("main.daftar_penyewa"))



@main.route("/sewa")
def daftar_sewa():
    kata_kunci = request.args.get("q", "").strip()
    status = request.args.get("status", "").strip()
    daftar_sewa = get_all_sewa(kata_kunci, status)

    return render_template(
        "sewa_list.html",
        page_title="Daftar Periode Sewa",
        active_page="sewa",
        daftar_sewa=daftar_sewa,
        kata_kunci=kata_kunci,
        status=status,
    )



@main.route("/sewa/tambah", methods=["GET", "POST"])
def tambah_sewa():
    daftar_kamar = get_all_kamar()
    daftar_penyewa = get_all_penyewa()

    if request.method == "POST":
        data_bersih, errors = validate_sewa(request.form)

        if errors:
            return render_template(
                "sewa_form.html",
                page_title="Tambah Periode Sewa",
                active_page="sewa",
                data=data_bersih,
                errors=errors,
                daftar_kamar=daftar_kamar,
                daftar_penyewa=daftar_penyewa,
                judul_form="Tambah Periode Sewa",
                action_url=url_for("main.tambah_sewa"),
                teks_tombol="Simpan",
            ), 400

        berhasil, status = create_sewa(
            data_bersih["id_kamar"],
            data_bersih["id_penyewa"],
            data_bersih["tanggal_mulai"],
            data_bersih["tanggal_selesai"],
            data_bersih["tanggal_jatuh_tempo"],
            data_bersih["harga_sewa_disepakati"],
        )

        if berhasil:
            flash("Data periode sewa berhasil ditambahkan.", "success")
            return redirect(url_for("main.daftar_sewa"))

        if status == "kamar_not_found":
            errors["id_kamar"] = "Kamar tidak ditemukan."
        elif status == "penyewa_not_found":
            errors["id_penyewa"] = "Penyewa tidak ditemukan."
        elif status == "overlap":
            errors["tanggal_selesai"] = (
                "Periode sewa kamar bertumpang tindih."
            )
        else:
            errors["database"] = (
                "Data periode sewa gagal disimpan karena terjadi "
                "kesalahan database."
            )

        return render_template(
            "sewa_form.html",
            page_title="Tambah Periode Sewa",
            active_page="sewa",
            data=data_bersih,
            errors=errors,
            daftar_kamar=daftar_kamar,
            daftar_penyewa=daftar_penyewa,
            judul_form="Tambah Periode Sewa",
            action_url=url_for("main.tambah_sewa"),
            teks_tombol="Simpan",
        ), 400

    data_awal = {
        "id_kamar": "",
        "id_penyewa": "",
        "tanggal_mulai": date.today().isoformat(),
        "tanggal_selesai": "",
        "tanggal_jatuh_tempo": "",
        "harga_sewa_disepakati": "",
    }

    return render_template(
        "sewa_form.html",
        page_title="Tambah Periode Sewa",
        active_page="sewa",
        data=data_awal,
        errors={},
        daftar_kamar=daftar_kamar,
        daftar_penyewa=daftar_penyewa,
        judul_form="Tambah Periode Sewa",
        action_url=url_for("main.tambah_sewa"),
        teks_tombol="Simpan",
    )


@main.route("/pembayaran")
def daftar_pembayaran():
    kata_kunci = request.args.get("q", "").strip()
    status = request.args.get("status", "").strip()
    daftar_pembayaran = get_all_pembayaran(kata_kunci, status)

    return render_template(
        "pembayaran_list.html",
        page_title="Daftar Pembayaran",
        active_page="pembayaran",
        daftar_pembayaran=daftar_pembayaran,
        kata_kunci=kata_kunci,
        status=status,
    )


@main.route("/pembayaran/tambah", methods=["GET", "POST"])
def tambah_pembayaran():
    daftar_sewa = get_all_sewa()

    if request.method == "POST":
        data_bersih, errors = validate_pembayaran(request.form)

        if errors:
            return render_template(
                "pembayaran_form.html",
                page_title="Tambah Pembayaran",
                active_page="pembayaran",
                data=data_bersih,
                errors=errors,
                daftar_sewa=daftar_sewa,
                judul_form="Tambah Pembayaran",
                action_url=url_for("main.tambah_pembayaran"),
                teks_tombol="Simpan",
            ), 400

        berhasil, status = create_pembayaran(
            data_bersih["id_sewa"],
            data_bersih["tanggal_pembayaran"],
            data_bersih["jumlah_bayar"],
        )

        if berhasil:
            flash("Data pembayaran berhasil ditambahkan.", "success")
            return redirect(url_for("main.daftar_pembayaran"))

        if status == "sewa_not_found":
            errors["id_sewa"] = "Periode sewa tidak ditemukan."
        else:
            errors["database"] = (
                "Data pembayaran gagal disimpan karena terjadi "
                "kesalahan database."
            )

        return render_template(
            "pembayaran_form.html",
            page_title="Tambah Pembayaran",
            active_page="pembayaran",
            data=data_bersih,
            errors=errors,
            daftar_sewa=daftar_sewa,
            judul_form="Tambah Pembayaran",
            action_url=url_for("main.tambah_pembayaran"),
            teks_tombol="Simpan",
        ), 400

    data_awal = {
        "id_sewa": "",
        "tanggal_pembayaran": "",
        "jumlah_bayar": "",
    }

    return render_template(
        "pembayaran_form.html",
        page_title="Tambah Pembayaran",
        active_page="pembayaran",
        data=data_awal,
        errors={},
        daftar_sewa=daftar_sewa,
        judul_form="Tambah Pembayaran",
        action_url=url_for("main.tambah_pembayaran"),
        teks_tombol="Simpan",
    )


@main.route("/pembayaran/<int:id_pembayaran>/hapus", methods=["POST"])
def hapus_pembayaran(id_pembayaran):
    berhasil, status = delete_pembayaran(id_pembayaran)

    if berhasil:
        flash("Data pembayaran berhasil dihapus.", "success")
    elif status == "not_found":
        abort(404)
    else:
        flash(
            "Data pembayaran gagal dihapus karena terjadi kesalahan "
            "database. Silakan coba kembali.",
            "danger",
        )

    return redirect(url_for("main.daftar_pembayaran"))
