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
