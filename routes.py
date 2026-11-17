from flask import Blueprint, redirect, render_template, url_for

main = Blueprint("main", __name__)


@main.route("/")
def beranda():
    return redirect(url_for("main.daftar_kamar"))


@main.route("/kamar")
def daftar_kamar():
    return render_template(
        "base.html",
        page_title="Data Kamar",
        active_page="kamar"
    )