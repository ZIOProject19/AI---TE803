
# ==========================================
# CIRCUITPATH SSF AI
# MAIN PROGRAM
# ==========================================

from search_algorithm import RANGKAIAN
from multi_agent_system import MultiAgentSystem


def main():
    sistem = MultiAgentSystem()

    print("=" * 60)
    print("          CIRCUITPATH SSF AI")
    print(" Search Algorithm | Expert System | Multi-Agent System")
    print("=" * 60)

    print("\nDaftar titik koneksi:")
    for titik in RANGKAIAN:
        print(f"- {titik}")

    print("\nMasukkan titik koneksi yang ingin diperiksa.")
    awal = input("Titik awal: ").strip()
    tujuan = input("Titik tujuan: ").strip()

    hasil = sistem.jalankan(awal, tujuan)

    print("\n" + "=" * 60)
    print("HASIL ANALISIS CIRCUITPATH SSF AI")
    print("=" * 60)

    # Hasil Search Algorithm
    print("\n[1] SEARCH AGENT")
    jalur = hasil["pencarian"]["jalur"]

    if jalur is None:
        print("Status pencarian: Input tidak valid.")
    elif jalur:
        print("Jalur:", " -> ".join(jalur))
    else:
        print("Jalur tidak ditemukan.")

    # Hasil Connection Analysis Agent
    print("\n[2] CONNECTION ANALYSIS AGENT")
    analisis = hasil["analisis"]

    print("Status:", analisis["status"])
    print("Jumlah titik:", analisis["jumlah_titik"])

    # Hasil Expert System melalui Diagnosis Agent
    print("\n[3] DIAGNOSIS AGENT / EXPERT SYSTEM")
    hasil_diagnosis = hasil["diagnosis"]

    print("Aturan:", hasil_diagnosis["aturan"])
    print("Diagnosis:", hasil_diagnosis["status"])
    print("Penjelasan:", hasil_diagnosis["penjelasan"])
    print("Saran:", hasil_diagnosis["saran"])

    print("\n" + "=" * 60)
    print("Analisis selesai.")
    print("Terima kasih telah menggunakan CircuitPath SSF AI.")
    print("=" * 60)


if __name__ == "__main__":
    main()
