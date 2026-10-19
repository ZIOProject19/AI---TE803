
from collections import deque

# ==========================================
# CIRCUITPATH SSF AI
# SEARCH ALGORITHM: BREADTH-FIRST SEARCH
# ==========================================

RANGKAIAN = {
    "Baterai+": ["R1"],
    "R1": ["Baterai+", "LED1"],
    "LED1": ["R1", "GND"],
    "GND": ["LED1"],
    "SENSOR": []
}


def cari_jalur(titik_awal, titik_tujuan):
    """Mencari jalur terpendek menggunakan BFS."""

    if titik_awal not in RANGKAIAN:
        return None

    if titik_tujuan not in RANGKAIAN:
        return None

    antrian = deque([[titik_awal]])
    dikunjungi = {titik_awal}

    while antrian:
        jalur = antrian.popleft()
        titik_sekarang = jalur[-1]

        if titik_sekarang == titik_tujuan:
            return jalur

        for tetangga in RANGKAIAN[titik_sekarang]:
            if tetangga not in dikunjungi:
                dikunjungi.add(tetangga)
                antrian.append(jalur + [tetangga])

    return []


if __name__ == "__main__":
    print("=== CIRCUITPATH SSF AI ===")

    awal = input("Titik awal: ").strip()
    tujuan = input("Titik tujuan: ").strip()

    hasil = cari_jalur(awal, tujuan)

    if hasil is None:
        print("Input tidak valid.")
    elif hasil:
        print("Jalur ditemukan:", " -> ".join(hasil))
    else:
        print("Jalur tidak ditemukan.")
