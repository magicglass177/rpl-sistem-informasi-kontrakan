
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS akun_pengguna (
    id_akun INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE
        CHECK (length(trim(username)) BETWEEN 1 AND 50),
    password_hash TEXT NOT NULL
        CHECK (length(trim(password_hash)) BETWEEN 1 AND 255)
);

CREATE TABLE IF NOT EXISTS kamar (
    id_kamar INTEGER PRIMARY KEY AUTOINCREMENT,
    nomor_kamar TEXT NOT NULL UNIQUE
        CHECK (length(trim(nomor_kamar)) BETWEEN 1 AND 20),
    harga_sewa INTEGER NOT NULL
        CHECK (typeof(harga_sewa) = 'integer' AND harga_sewa >= 0)
);

CREATE TABLE IF NOT EXISTS penyewa (
    id_penyewa INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL
        CHECK (length(trim(nama)) BETWEEN 1 AND 100),
    no_telepon TEXT NOT NULL
        CHECK (length(trim(no_telepon)) BETWEEN 1 AND 20),
    alamat TEXT NOT NULL
        CHECK (length(trim(alamat)) > 0)
);

CREATE TABLE IF NOT EXISTS sewa (
    id_sewa INTEGER PRIMARY KEY AUTOINCREMENT,
    id_kamar INTEGER NOT NULL,
    id_penyewa INTEGER NOT NULL,
    tanggal_mulai TEXT NOT NULL
        CHECK (
            length(tanggal_mulai) = 10
            AND tanggal_mulai GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
            AND date(tanggal_mulai) IS NOT NULL
        ),
    tanggal_selesai TEXT NOT NULL
        CHECK (
            length(tanggal_selesai) = 10
            AND tanggal_selesai GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
            AND date(tanggal_selesai) IS NOT NULL
        ),
    tanggal_jatuh_tempo TEXT
        CHECK (
            tanggal_jatuh_tempo IS NULL
            OR (
                length(tanggal_jatuh_tempo) = 10
                AND tanggal_jatuh_tempo GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
                AND date(tanggal_jatuh_tempo) IS NOT NULL
            )
        ),
    harga_sewa_disepakati INTEGER NOT NULL
        CHECK (
            typeof(harga_sewa_disepakati) = 'integer'
            AND harga_sewa_disepakati >= 0
        ),

    CONSTRAINT chk_periode_sewa
        CHECK (date(tanggal_selesai) >= date(tanggal_mulai)),

    CONSTRAINT fk_sewa_kamar
        FOREIGN KEY (id_kamar)
        REFERENCES kamar(id_kamar)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_sewa_penyewa
        FOREIGN KEY (id_penyewa)
        REFERENCES penyewa(id_penyewa)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS pembayaran (
    id_pembayaran INTEGER PRIMARY KEY AUTOINCREMENT,
    id_sewa INTEGER NOT NULL,
    tanggal_pembayaran TEXT NOT NULL
        CHECK (
            length(tanggal_pembayaran) = 10
            AND tanggal_pembayaran GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
            AND date(tanggal_pembayaran) IS NOT NULL
        ),
    jumlah_bayar INTEGER NOT NULL
        CHECK (
            typeof(jumlah_bayar) = 'integer'
            AND jumlah_bayar > 0
        ),

    CONSTRAINT fk_pembayaran_sewa
        FOREIGN KEY (id_sewa)
        REFERENCES sewa(id_sewa)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
