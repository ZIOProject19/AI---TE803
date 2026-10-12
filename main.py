from collections import deque

rangkaian = {
    "Baterai+": ["R1"],
    "R1": ["Baterai+", "LED1"],
    "LED1": ["R1", "GND"],
    "GND": ["LED1"],
    "SENSOR": []
}

def cari_jalur(mulai, tujuan):
    antrean = deque([[mulai]])
    dikunjungi = {mulai}

    while antrean:
        jalur = antrean.popleft()
        titik = jalur[-1]

        
        if titik == tujuan:
            return jalur

    
        for tetangga in rangkaian.get(titik, []):
            if tetangga not in dikunjungi:
                dikunjungi.add(tetangga)
                antrean.append(jalur + [tetangga])

    return None
