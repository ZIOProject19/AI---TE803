
# ==========================================
# CIRCUITPATH SSF AI
# PROGRAM UTAMA
# Manager: Integrasi semua modul
# ==========================================

from Multi_Agency_System.MAS_Test import MultiAgentSystem


def main():
    print("=" * 45)
    print("          CIRCUITPATH SSF AI")
    print(" Sistem Diagnosis Konektivitas Rangkaian")
    print("=" * 45)

    print("\nTitik koneksi yang tersedia:")
    print("1. Baterai+")
    print("2. R1")
    print("3. LED1")
    print("4. GND")
    print("5. SENSOR")

    titik_awal = input("\nMasukkan titik awal: ").strip()
    titik_tujuan = input("Masukkan titik tujuan: ").strip()

    sistem = MultiAgentSystem()
    hasil = sistem.jalankan(titik_awal, titik_tujuan)

    print("\n========== HASIL DIAGNOSIS ==========")

    jalur = hasil["jalur"]

    if jalur:
        print("Jalur koneksi:", " -> ".join(jalur))
    else:
        print("Jalur koneksi: Tidak ditemukan")

    print("Analisis    :", hasil["analisis"])
    print("Status      :", hasil["diagnosis"]["status"])
    print("Penjelasan  :", hasil["diagnosis"]["penjelasan"])
    print("Saran       :", hasil["diagnosis"]["saran"])

    print("\nProgram selesai.")


if __name__ == "__main__":
    main()
