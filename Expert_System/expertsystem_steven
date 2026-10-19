
# ==========================================
# CIRCUITPATH SSF AI
# MODUL: EXPERT SYSTEM
# Metode: Rule-Based System (IF-THEN)
# ==========================================

ATURAN_DIAGNOSIS = [
    {
        "nama": "RULE 1",
        "status": "INPUT TIDAK VALID",
        "penjelasan": "Titik koneksi tidak dikenal.",
        "saran": "Gunakan nama titik koneksi yang tersedia."
    },
    {
        "nama": "RULE 2",
        "status": "TITIK SAMA",
        "penjelasan": "Titik awal dan tujuan sama.",
        "saran": "Pilih titik awal dan tujuan yang berbeda."
    },
    {
        "nama": "RULE 3",
        "status": "TERHUBUNG DALAM MODEL",
        "penjelasan": "Jalur koneksi ditemukan dalam model.",
        "saran": (
            "Periksa wiring dan komponen fisik "
            "untuk memastikan rangkaian benar-benar berfungsi."
        )
    },
    {
        "nama": "RULE 4",
        "status": "TIDAK TERHUBUNG DALAM MODEL",
        "penjelasan": "Jalur koneksi tidak ditemukan.",
        "saran": (
            "Periksa kemungkinan koneksi terputus "
            "atau data koneksi yang belum dicatat."
        )
    }
]


def diagnosis(titik_awal, titik_tujuan, jalur):
    """
    Menentukan diagnosis berdasarkan aturan IF-THEN.

    jalur:
    - None: input tidak valid
    - List berisi jalur: koneksi ditemukan
    - List kosong: jalur tidak ditemukan
    """

    titik_valid = {"Baterai+", "R1", "LED1", "GND", "SENSOR"}

    # RULE 1: Input tidak valid
    if titik_awal not in titik_valid or titik_tujuan not in titik_valid:
        aturan = ATURAN_DIAGNOSIS[0]

    # RULE 2: Titik awal dan tujuan sama
    elif titik_awal == titik_tujuan:
        aturan = ATURAN_DIAGNOSIS[1]

    # RULE 3: Jalur ditemukan
    elif jalur:
        aturan = ATURAN_DIAGNOSIS[2]

    # RULE 4: Jalur tidak ditemukan
    else:
        aturan = ATURAN_DIAGNOSIS[3]

    return {
        "aturan": aturan["nama"],
        "status": aturan["status"],
        "penjelasan": aturan["penjelasan"],
        "saran": aturan["saran"]
    }


def tampilkan_diagnosis(hasil):
    """Menampilkan hasil diagnosis ke terminal."""

    print("\n=== HASIL EXPERT SYSTEM ===")
    print("Aturan     :", hasil["aturan"])
    print("Status     :", hasil["status"])
    print("Penjelasan :", hasil["penjelasan"])
    print("Saran      :", hasil["saran"])


# ==========================================
# PENGUJIAN MANDIRI
# ==========================================

if __name__ == "__main__":
    print("CIRCUITPATH SSF AI")
    print("Pengujian Modul Expert System")

    hasil = diagnosis(
        "Baterai+",
        "LED1",
        ["Baterai+", "R1", "LED1"]
    )

    tampilkan_diagnosis(hasil)
