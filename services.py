import re
from decimal import Decimal, InvalidOperation


def validate_kamar(data):
    """
    Memvalidasi data kamar sebelum diteruskan ke model.

    Mengembalikan:
    - (data_bersih, {}) jika valid.
    - (data_bersih, errors) jika terdapat kesalahan.
    """
    nomor_kamar = data.get("nomor_kamar", "").strip()
    harga_input = data.get("harga_sewa", "").strip()

    errors = {}
    data_bersih = {
        "nomor_kamar": nomor_kamar,
        "harga_sewa": harga_input,
    }

    if not nomor_kamar:
        errors["nomor_kamar"] = "Nomor kamar wajib diisi."
    elif len(nomor_kamar) > 20:
        errors["nomor_kamar"] = (
            "Nomor kamar maksimal 20 karakter."
        )

    if not harga_input:
        errors["harga_sewa"] = "Harga sewa wajib diisi."
    else:
        try:
            harga = Decimal(harga_input)

            if not harga.is_finite():
                errors["harga_sewa"] = (
                    "Harga sewa harus berupa angka yang valid."
                )
            elif harga < 0:
                errors["harga_sewa"] = (
                    "Harga sewa tidak boleh negatif."
                )
            else:
                data_bersih["harga_sewa"] = str(harga)

        except InvalidOperation:
            errors["harga_sewa"] = (
                "Harga sewa harus berupa angka."
            )

    return data_bersih, errors


def _nomor_telepon_valid(no_telepon):
    """
    Memeriksa format nomor telepon sesuai kamus data:
    - 08 diikuti 8-11 digit (total 10-13 karakter), atau
    - +628 diikuti 8-11 digit (total 12-15 karakter).
    """
    if re.fullmatch(r"08[0-9]{8,11}", no_telepon):
        return True

    if re.fullmatch(r"\+628[0-9]{8,11}", no_telepon):
        return True

    return False


def validate_penyewa(data):
    """
    Memvalidasi data penyewa sebelum diteruskan ke model.

    Mengembalikan:
    - (data_bersih, {}) jika valid.
    - (data_bersih, errors) jika terdapat kesalahan.
    """
    nama = data.get("nama", "").strip()
    no_telepon = data.get("no_telepon", "").strip()
    alamat = data.get("alamat", "").strip()

    errors = {}
    data_bersih = {
        "nama": nama,
        "no_telepon": no_telepon,
        "alamat": alamat,
    }

    if not nama:
        errors["nama"] = "Nama penyewa wajib diisi."
    elif len(nama) > 100:
        errors["nama"] = "Nama penyewa maksimal 100 karakter."

    if not no_telepon:
        errors["no_telepon"] = "Nomor telepon wajib diisi."
    elif not _nomor_telepon_valid(no_telepon):
        errors["no_telepon"] = (
            "Nomor telepon harus diawali 08 (10-13 digit) "
            "atau +628 (12-15 karakter)."
        )

    if not alamat:
        errors["alamat"] = "Alamat wajib diisi."

    return data_bersih, errors
