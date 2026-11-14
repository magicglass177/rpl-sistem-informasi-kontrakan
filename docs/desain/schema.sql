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
    harga_sewa NUMERIC NOT NULL
        CHECK (
            typeof(harga_sewa) IN ('integer', 'real')
            AND harga_sewa >= 0
        )
);

CREATE TABLE IF NOT EXISTS penyewa (
    id_penyewa INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT NOT NULL
        CHECK (length(trim(nama)) BETWEEN 1 AND 100),
    no_telepon TEXT NOT NULL
        CHECK (
            (
                length(trim(no_telepon)) BETWEEN 10 AND 13
                AND substr(trim(no_telepon), 1, 2) = '08'
                AND trim(no_telepon) NOT GLOB '*[^0-9]*'
            )
            OR
            (
                length(trim(no_telepon)) BETWEEN 12 AND 15
                AND substr(trim(no_telepon), 1, 4) = '+628'
                AND substr(trim(no_telepon), 2) NOT GLOB '*[^0-9]*'
            )
        ),
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
            AND tanggal_mulai GLOB
                '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
            AND date(tanggal_mulai, '+0 days') = tanggal_mulai
        ),

    tanggal_selesai TEXT NOT NULL
        CHECK (
            length(tanggal_selesai) = 10
            AND tanggal_selesai GLOB
                '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
            AND date(tanggal_selesai, '+0 days') = tanggal_selesai
        ),

    tanggal_jatuh_tempo TEXT
        CHECK (
            tanggal_jatuh_tempo IS NULL
            OR (
                length(tanggal_jatuh_tempo) = 10
                AND tanggal_jatuh_tempo GLOB
                    '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
                AND date(tanggal_jatuh_tempo, '+0 days')
                    = tanggal_jatuh_tempo
            )
        ),

    harga_sewa_disepakati NUMERIC NOT NULL
        CHECK (
            typeof(harga_sewa_disepakati) IN ('integer', 'real')
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
            AND tanggal_pembayaran GLOB
                '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
            AND date(tanggal_pembayaran, '+0 days')
                = tanggal_pembayaran
        ),

    jumlah_bayar NUMERIC NOT NULL
        CHECK (
            typeof(jumlah_bayar) IN ('integer', 'real')
            AND jumlah_bayar > 0
        ),

    CONSTRAINT fk_pembayaran_sewa
        FOREIGN KEY (id_sewa)
        REFERENCES sewa(id_sewa)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- KF-08: Tolak periode sewa yang bertumpang tindih
-- pada kamar yang sama.
CREATE TRIGGER IF NOT EXISTS cegah_sewa_tumpang_tindih_insert
BEFORE INSERT ON sewa
FOR EACH ROW
WHEN EXISTS (
    SELECT 1
    FROM sewa AS s
    WHERE s.id_kamar = NEW.id_kamar
      AND date(NEW.tanggal_mulai) <= date(s.tanggal_selesai)
      AND date(NEW.tanggal_selesai) >= date(s.tanggal_mulai)
)
BEGIN
    SELECT RAISE(ABORT, 'Periode sewa kamar bertumpang tindih');
END;

CREATE TRIGGER IF NOT EXISTS cegah_sewa_tumpang_tindih_update
BEFORE UPDATE OF id_kamar, tanggal_mulai, tanggal_selesai ON sewa
FOR EACH ROW
WHEN EXISTS (
    SELECT 1
    FROM sewa AS s
    WHERE s.id_kamar = NEW.id_kamar
      AND s.id_sewa <> OLD.id_sewa
      AND date(NEW.tanggal_mulai) <= date(s.tanggal_selesai)
      AND date(NEW.tanggal_selesai) >= date(s.tanggal_mulai)
)
BEGIN
    SELECT RAISE(ABORT, 'Periode sewa kamar bertumpang tindih');
END;
