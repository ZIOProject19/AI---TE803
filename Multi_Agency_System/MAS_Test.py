
# ==========================================
# CIRCUITPATH SSF AI
# MODUL: MULTI-AGENT SYSTEM
# ==========================================

from Search_Algorthm.BFS_Test import cari_jalur
from Expert_System.IF_THEN_Tets import diagnosis


class SearchAgent:
    """Agen untuk mencari jalur koneksi."""

    def jalankan(self, titik_awal, titik_tujuan):
        print("\n[Search Agent] Mencari jalur...")
        return cari_jalur(titik_awal, titik_tujuan)


class ConnectionAnalysisAgent:
    """Agen untuk menganalisis hasil pencarian."""

    def jalankan(self, jalur):
        print("[Connection Analysis Agent] Menganalisis hasil...")

        if jalur is None:
            return "Input tidak valid"
        elif jalur:
            return "Jalur ditemukan"
        else:
            return "Jalur tidak ditemukan"


class DiagnosisAgent:
    """Agen untuk menjalankan sistem pakar."""

    def jalankan(self, titik_awal, titik_tujuan, jalur):
        print("[Diagnosis Agent] Menentukan diagnosis...")
        return diagnosis(titik_awal, titik_tujuan, jalur)


class MultiAgentSystem:
    """Koordinator agen CircuitPath SSF AI."""

    def __init__(self):
        self.search_agent = SearchAgent()
        self.analysis_agent = ConnectionAnalysisAgent()
        self.diagnosis_agent = DiagnosisAgent()

    def jalankan(self, titik_awal, titik_tujuan):
        jalur = self.search_agent.jalankan(
            titik_awal, titik_tujuan
        )

        analisis = self.analysis_agent.jalankan(jalur)

        hasil_diagnosis = self.diagnosis_agent.jalankan(
            titik_awal, titik_tujuan, jalur
        )

        return {
            "jalur": jalur,
            "analisis": analisis,
            "diagnosis": hasil_diagnosis
        }


# ==========================================
# PENGUJIAN MANDIRI
# ==========================================

if __name__ == "__main__":
    sistem = MultiAgentSystem()

    hasil = sistem.jalankan("Baterai+", "LED1")

    print("\n=== HASIL CIRCUITPATH SSF AI ===")
    print("Jalur     :", hasil["jalur"])
    print("Analisis  :", hasil["analisis"])
    print("Status    :", hasil["diagnosis"]["status"])
    print("Penjelasan:", hasil["diagnosis"]["penjelasan"])
    print("Saran     :", hasil["diagnosis"]["saran"])
