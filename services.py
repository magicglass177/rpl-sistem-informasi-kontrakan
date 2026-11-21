import re
from datetime import date
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


def validate_sewa(data):
    """
    Memvalidasi data periode sewa sebelum diteruskan ke model.

    Mengembalikan:
    - (data_bersih, {}) jika valid.
    - (data_bersih, errors) jika terdapat kesalahan.
    """
    id_kamar_raw = data.get("id_kamar", "").strip()
    id_penyewa_raw = data.get("id_penyewa", "").strip()
    tanggal_mulai = data.get("tanggal_mulai", "").strip()
    tanggal_selesai = data.get("tanggal_selesai", "").strip()
    tanggal_jatuh_tempo = data.get("tanggal_jatuh_tempo", "").strip()
    harga_input = data.get("harga_sewa_disepakati", "").strip()

    errors = {}
    data_bersih = {
        "id_kamar": id_kamar_raw,
        "id_penyewa": id_penyewa_raw,
        "tanggal_mulai": tanggal_mulai,
        "tanggal_selesai": tanggal_selesai,
        "tanggal_jatuh_tempo": tanggal_jatuh_tempo,
        "harga_sewa_disepakati": harga_input,
    }

    try:
        id_kamar = int(id_kamar_raw)
        if id_kamar <= 0:
            raise ValueError
        data_bersih["id_kamar"] = id_kamar
    except (TypeError, ValueError):
        errors["id_kamar"] = "Pilih kamar."

    try:
        id_penyewa = int(id_penyewa_raw)
        if id_penyewa <= 0:
            raise ValueError
        data_bersih["id_penyewa"] = id_penyewa
    except (TypeError, ValueError):
        errors["id_penyewa"] = "Pilih penyewa."

    try:
        tanggal_mulai_obj = date.fromisoformat(tanggal_mulai)
    except ValueError:
        errors["tanggal_mulai"] = "Tanggal mulai harus berformat TTTT-BB-HH."
        tanggal_mulai_obj = None

    try:
        tanggal_selesai_obj = date.fromisoformat(tanggal_selesai)
    except ValueError:
        errors["tanggal_selesai"] = "Tanggal selesai harus berformat TTTT-BB-HH."
        tanggal_selesai_obj = None

    if (
        tanggal_mulai_obj is not None
        and tanggal_selesai_obj is not None
        and tanggal_selesai_obj < tanggal_mulai_obj
    ):
        errors["tanggal_selesai"] = (
            "Tanggal selesai tidak boleh lebih awal dari tanggal mulai."
        )

    if tanggal_jatuh_tempo:
        try:
            date.fromisoformat(tanggal_jatuh_tempo)
        except ValueError:
            errors["tanggal_jatuh_tempo"] = (
                "Tanggal jatuh tempo harus berformat TTTT-BB-HH."
            )

    if not harga_input:
        errors["harga_sewa_disepakati"] = "Harga sewa disepakati wajib diisi."
    else:
        try:
            harga = Decimal(harga_input)

            if not harga.is_finite():
                errors["harga_sewa_disepakati"] = (
                    "Harga sewa harus berupa angka yang valid."
                )
            elif harga < 0:
                errors["harga_sewa_disepakati"] = (
                    "Harga sewa tidak boleh negatif."
                )
            else:
                data_bersih["harga_sewa_disepakati"] = str(harga)

        except InvalidOperation:
            errors["harga_sewa_disepakati"] = (
                "Harga sewa harus berupa angka."
            )

    return data_bersih, errors


def validate_pembayaran(data):
    """Memvalidasi data pembayaran sebelum diteruskan ke model."""
    id_sewa_raw = data.get("id_sewa", "").strip()
    tanggal_pembayaran = data.get("tanggal_pembayaran", "").strip()
    jumlah_input = data.get("jumlah_bayar", "").strip()

    errors = {}
    data_bersih = {
        "id_sewa": id_sewa_raw,
        "tanggal_pembayaran": tanggal_pembayaran,
        "jumlah_bayar": jumlah_input,
    }

    try:
        id_sewa = int(id_sewa_raw)
        if id_sewa <= 0:
            raise ValueError
        data_bersih["id_sewa"] = id_sewa
    except (TypeError, ValueError):
        errors["id_sewa"] = "Pilih periode sewa."

    try:
        from datetime import date

        date.fromisoformat(tanggal_pembayaran)
    except ValueError:
        errors["tanggal_pembayaran"] = (
            "Tanggal pembayaran harus berformat TTTT-BB-HH."
        )

    if not jumlah_input:
        errors["jumlah_bayar"] = "Jumlah bayar wajib diisi."
    else:
        try:
            from decimal import Decimal, InvalidOperation

            jumlah = Decimal(jumlah_input)

            if not jumlah.is_finite():
                errors["jumlah_bayar"] = "Jumlah bayar harus berupa angka yang valid."
            elif jumlah <= 0:
                errors["jumlah_bayar"] = "Jumlah bayar harus lebih dari 0."
            else:
                data_bersih["jumlah_bayar"] = str(jumlah)

        except InvalidOperation:
            errors["jumlah_bayar"] = "Jumlah bayar harus berupa angka."

    return data_bersih, errors
