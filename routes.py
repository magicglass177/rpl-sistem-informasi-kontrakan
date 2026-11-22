from functools import wraps
from flask import (
    Blueprint,
    abort,
    current_app,
    flash,
    g,
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
    get_laporan_pembayaran,
    get_all_penyewa,
    get_all_sewa,
    get_kamar_by_id,
    get_pembayaran_by_id,
    ambil_pengguna,
    get_penyewa_by_id,
    get_sewa_by_id,
    update_kamar,
    update_penyewa,
)
from datetime import date

import percobaan
import services
from services import (
    validate_kamar,
    validate_pembayaran,
    validate_penyewa,
    validate_sewa,
)


main = Blueprint("main", __name__)

@main.before_request
def muat_pengguna():
    """Memuat pengguna dari sesi untuk kebutuhan otorisasi."""
    pengguna_id = session.get("pengguna_id")
    g.pengguna = ambil_pengguna(pengguna_id) if pengguna_id else None


@main.context_processor
def konteks_pengguna():
    """Membuat data pengguna tersedia ke semua template."""
    return {"pengguna": g.pengguna}


def _tujuan_aman(tujuan):
    """Menerima hanya alamat internal yang aman untuk redirect."""
    if (
        tujuan
        and tujuan.startswith("/")
        and not tujuan.startswith("//")
        and "\\" not in tujuan
    ):
        return tujuan
    return None


def peran_diperlukan(*peran):
    """Mengeksekusi penegakan otorisasi di sisi server."""

    def decorator(fungsi):
        @wraps(fungsi)
        def bungkus(*args, **kwargs):
            if g.pengguna is None:
                return redirect(
                    url_for(
                        "main.login",
                        next=request.full_path.rstrip("?"),
                    )
                )

            if g.pengguna["peran"] not in peran:
                abort(403)

            return fungsi(*args, **kwargs)

        return bungkus

    return decorator


semua_peran = peran_diperlukan(*services.PERAN)
hanya_pemilik = peran_diperlukan("pemilik")


def _render_login(status=200):
    """Merender halaman login dengan status tertentu."""
    return render_template(
        "login.html",
        page_title="Login",
        active_page=None,
        data={
            "username": request.form.get("username", "")
            if request.method == "POST"
            else "",
        },
        errors={},
    ), status


@main.route("/login", methods=["GET", "POST"])
def login():
    if g.pengguna is not None:
        return redirect(url_for("main.daftar_kamar"))

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        kunci = f"{request.remote_addr}|{username.strip().lower()}"

        if percobaan.terkunci(kunci):
            current_app.logger.warning(
                "Login terkunci username=%r ip=%s",
                username,
                request.remote_addr,
            )
            flash(
                "Terlalu banyak percobaan login. Coba lagi beberapa saat lagi.",
                "danger",
            )
            return _render_login(429)

        pengguna = services.autentikasi(username, password)

        if pengguna is not None:
            percobaan.reset(kunci)
            current_app.logger.info(
                "Login berhasil username=%r peran=%r",
                pengguna["username"],
                pengguna["peran"],
            )

            session.clear()
            session["pengguna_id"] = pengguna["id_akun"]
            flash("Login berhasil.", "success")

            tujuan = _tujuan_aman(request.args.get("next"))
            return redirect(tujuan or url_for("main.daftar_kamar"))

        percobaan.catat_gagal(kunci)
        current_app.logger.warning(
            "Login gagal username=%r ip=%s",
            username,
            request.remote_addr,
        )
        flash("Username atau password salah.", "danger")
        return _render_login(401)

    return _render_login()


@main.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("Anda telah logout.", "success")
    return redirect(url_for("main.login"))


@main.errorhandler(403)
def akses_ditolak(_galat):
    """Halaman akses ditolak untuk peran yang tidak berhak."""
    current_app.logger.warning(
        "Akses ditolak path=%r ip=%s pengguna=%r",
        request.path,
        request.remote_addr,
        g.pengguna["username"] if g.pengguna else None,
    )
    return render_template("403.html"), 403


@main.route("/")
@semua_peran
def beranda():
    daftar_kamar = get_all_kamar()
    total_unit = len(daftar_kamar)
    unit_tersewa = sum(1 for k in daftar_kamar if k["status_ketersediaan"] == "Terisi")
    unit_tersedia = total_unit - unit_tersewa

    # Aktivitas dan jadwal: sewa yang akan mulai / berakhir / pembayaran jatuh tempo.
    aktivitas = []
    hari_ini = date.today().isoformat()
    for sewa in get_all_sewa():
        if sewa["tanggal_mulai"] >= hari_ini:
            aktivitas.append({
                "judul": "Mulai sewa",
                "nama": sewa["nama_penyewa"],
                "detail": f"Kamar {sewa['nomor_kamar']}",
                "tanggal": sewa["tanggal_mulai"],
                "status": "Terjadwal",
                "badge": "info",
            })
        if sewa["tanggal_selesai"] >= hari_ini and sewa["tanggal_selesai"] <= _tambah_hari(hari_ini, 30):
            aktivitas.append({
                "judul": "Sewa berakhir",
                "nama": sewa["nama_penyewa"],
                "detail": f"Kamar {sewa['nomor_kamar']}",
                "tanggal": sewa["tanggal_selesai"],
                "status": "Mendekati",
                "badge": "warning",
            })
    for bayar in get_all_pembayaran():
        if bayar.get("tanggal_jatuh_tempo"):
            if hari_ini <= str(bayar["tanggal_jatuh_tempo"]) <= _tambah_hari(hari_ini, 30):
                aktivitas.append({
                    "judul": "Jatuh tempo",
                    "nama": bayar["nama_penyewa"],
                    "detail": f"Kamar {bayar['nomor_kamar']}",
                    "tanggal": bayar["tanggal_jatuh_tempo"],
                    "status": bayar["status_pembayaran"],
                    "badge": "danger" if bayar["status_pembayaran"] == "Terlambat" else "warning",
                })
    aktivitas = aktivitas[:8]

    pembayaran_terbaru = list(get_all_pembayaran())[:5]
    penghuni_terbaru = sorted(
        get_all_penyewa(), key=lambda p: p["id_penyewa"], reverse=True
    )[:5]

    return render_template(
        "dashboard.html",
        page_title="Dashboard",
        active_page="dashboard",
        total_unit=total_unit,
        unit_tersewa=unit_tersewa,
        unit_tersedia=unit_tersedia,
        daftar_kamar=daftar_kamar[:6],
        aktivitas=aktivitas,
        pembayaran_terbaru=pembayaran_terbaru,
        penghuni_terbaru=penghuni_terbaru,
    )


def _tambah_hari(iso, hari):
    from datetime import date, timedelta
    return (date.fromisoformat(iso) + timedelta(days=hari)).isoformat()


@main.route("/pengaturan")
@semua_peran
def pengaturan():
    return render_template(
        "pengaturan.html",
        page_title="Pengaturan",
        active_page="pengaturan",
    )


@main.route("/kamar")
@semua_peran
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
@hanya_pemilik
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
@hanya_pemilik
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
@hanya_pemilik
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
@semua_peran
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
@hanya_pemilik
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
@hanya_pemilik
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
@hanya_pemilik
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
@semua_peran
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
@semua_peran
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
@semua_peran
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
@semua_peran
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
@semua_peran
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


@main.route("/laporan")
@hanya_pemilik
def laporan_pembayaran():
    tanggal_mulai = request.args.get("tanggal_mulai", "").strip()
    tanggal_selesai = request.args.get("tanggal_selesai", "").strip()
    kata_kunci = request.args.get("q", "").strip()

    errors = {}

    if tanggal_mulai:
        try:
            from datetime import date

            date.fromisoformat(tanggal_mulai)
        except ValueError:
            errors["tanggal_mulai"] = "Tanggal mulai harus berformat TTTT-BB-HH."

    if tanggal_selesai:
        try:
            from datetime import date

            date.fromisoformat(tanggal_selesai)
        except ValueError:
            errors["tanggal_selesai"] = "Tanggal selesai harus berformat TTTT-BB-HH."

    if (
        tanggal_mulai
        and tanggal_selesai
        and not errors
        and tanggal_mulai > tanggal_selesai
    ):
        errors["tanggal_selesai"] = (
            "Tanggal selesai tidak boleh lebih awal dari tanggal mulai."
        )

    if errors:
        daftar_laporan = []
    else:
        daftar_laporan = get_laporan_pembayaran(
            tanggal_mulai,
            tanggal_selesai,
            kata_kunci,
        )

    total_pendapatan = sum(
        float(item["jumlah_bayar"]) for item in daftar_laporan
    )

    return render_template(
        "laporan.html",
        page_title="Laporan Pendapatan",
        active_page="laporan",
        daftar_laporan=daftar_laporan,
        tanggal_mulai=tanggal_mulai,
        tanggal_selesai=tanggal_selesai,
        kata_kunci=kata_kunci,
        errors=errors,
        total_pendapatan=total_pendapatan,
    )
