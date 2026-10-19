
# ==========================================
# CIRCUITPATH SSF AI
# EXPERT SYSTEM
# ==========================================

ATURAN_DIAGNOSIS = [
    {
        "nama": "RULE 1",
        "kondisi": "Input tidak valid",
        "status": "INPUT TIDAK VALID",
        "penjelasan": "Titik koneksi tidak dikenal.",
        "saran": "Gunakan nama titik yang tersedia."
    },
    {
        "nama": "RULE 2",
        "kondisi": "Titik awal dan tujuan sama",
        "status": "TITIK SAMA",
        "penjelasan": "Titik awal dan tujuan identik.",
        "saran": "Pilih dua titik berbeda."
    },
    {
        "nama": "RULE 3",
        "kondisi": "Jalur ditemukan",
        "status": "TERHUBUNG DALAM MODEL",
        "penjelasan": "Terdapat jalur koneksi dalam model.",
        "saran": (
            "Periksa wiring dan kondisi komponen "
            "untuk memastikan rangkaian fisik berfungsi."
        )
    },
    {
        "nama": "RULE 4",
        "kondisi": "Jalur tidak ditemukan",
        "status": "TIDAK TERHUBUNG DALAM MODEL",
        "penjelasan": "Jalur koneksi tidak ditemukan.",
        "saran": (
            "Periksa kemungkinan koneksi terputus "
            "atau data koneksi yang belum dicatat."
        )
    }
]


def diagnosis(titik_awal, titik_tujuan, jalur):
    """Menentukan diagnosis berdasarkan aturan IF-THEN."""

    if jalur is None:
        aturan = ATURAN_DIAGNOSIS[0]

    elif titik_awal == titik_tujuan:
        aturan = ATURAN_DIAGNOSIS[1]

    elif jalur:
        aturan = ATURAN_DIAGNOSIS[2]

    else:
        aturan = ATURAN_DIAGNOSIS[3]

    return {
        "aturan": aturan["nama"],
        "status": aturan["status"],
        "penjelasan": aturan["penjelasan"],
        "saran": aturan["saran"]
    }
