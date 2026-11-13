PRAGMA foreign_keys = ON;

-- =====================================================
-- TABEL INDUK: KAMAR
-- =====================================================
CREATE TABLE IF NOT EXISTS kamar (
    id_kamar INTEGER PRIMARY KEY AUTOINCREMENT,
    nomor_kamar TEXT NOT NULL UNIQUE,
    harga_sewa NUMERIC NOT NULL
        CHECK (harga_sewa >= 0)
);

-- =====================================================
-- TABEL ANAK: SEWA
-- =====================================================
CREATE TABLE IF NOT EXISTS sewa (
    id_sewa INTEGER PRIMARY KEY AUTOINCREMENT,
    id_kamar INTEGER NOT NULL,
    id_penyewa INTEGER NOT NULL,
    tanggal_mulai TEXT NOT NULL,
    tanggal_selesai TEXT NOT NULL,
    tanggal_jatuh_tempo TEXT,
    harga_sewa_disepakati NUMERIC NOT NULL
        CHECK (harga_sewa_disepakati >= 0),

    CONSTRAINT fk_sewa_kamar
        FOREIGN KEY (id_kamar)
        REFERENCES kamar(id_kamar)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_sewa_penyewa
        FOREIGN KEY (id_penyewa)
        REFERENCES penyewa(id_penyewa)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_periode_sewa
        CHECK (
            date(tanggal_mulai) IS NOT NULL
            AND date(tanggal_selesai) IS NOT NULL
            AND date(tanggal_selesai) >= date(tanggal_mulai)
        ),

    CONSTRAINT chk_jatuh_tempo
        CHECK (
            tanggal_jatuh_tempo IS NULL
            OR date(tanggal_jatuh_tempo) IS NOT NULL
        )
);
