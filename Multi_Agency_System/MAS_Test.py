
# ==========================================
# CIRCUITPATH SSF AI
# MULTI-AGENT SYSTEM
# ==========================================

from search_algorithm import cari_jalur, RANGKAIAN
from expert_system import diagnosis


class SearchAgent:
    """Agen pencari jalur koneksi."""

    def bekerja(self, awal, tujuan):
        jalur = cari_jalur(awal, tujuan)

        return {
            "nama_agen": "Search Agent",
            "jalur": jalur
        }


class ConnectionAnalysisAgent:
    """Agen analisis konektivitas."""

    def bekerja(self, awal, tujuan, jalur):
        if awal not in RANGKAIAN or tujuan not in RANGKAIAN:
            status = "INPUT TIDAK VALID"
            jumlah_titik = 0

        elif awal == tujuan:
            status = "TITIK SAMA"
            jumlah_titik = 1

        elif jalur:
            status = "JALUR DITEMUKAN"
            jumlah_titik = len(jalur)

        else:
            status = "JALUR TIDAK DITEMUKAN"
            jumlah_titik = 0

        return {
            "nama_agen": "Connection Analysis Agent",
            "status": status,
            "jumlah_titik": jumlah_titik
        }


class DiagnosisAgent:
    """Agen diagnosis berbasis sistem pakar."""

    def bekerja(self, awal, tujuan, jalur):
        hasil = diagnosis(awal, tujuan, jalur)

        return {
            "nama_agen": "Diagnosis Agent",
            "hasil": hasil
        }


class MultiAgentSystem:
    """Koordinator kerja sama antaragen."""

    def __init__(self):
        self.search_agent = SearchAgent()
        self.analysis_agent = ConnectionAnalysisAgent()
        self.diagnosis_agent = DiagnosisAgent()

    def jalankan(self, awal, tujuan):
        # Agen 1: mencari jalur
        hasil_pencarian = self.search_agent.bekerja(
            awal, tujuan
        )

        jalur = hasil_pencarian["jalur"]

        # Agen 2: menganalisis konektivitas
        hasil_analisis = self.analysis_agent.bekerja(
            awal, tujuan, jalur
        )

        # Agen 3: melakukan diagnosis
        hasil_diagnosis = self.diagnosis_agent.bekerja(
            awal, tujuan, jalur
        )

        # Menggabungkan hasil ketiga agen
        return {
            "pencarian": hasil_pencarian,
            "analisis": hasil_analisis,
            "diagnosis": hasil_diagnosis["hasil"]
        }

