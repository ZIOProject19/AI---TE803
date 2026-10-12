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
    def diagnosis(jalur):
    aturan = [
        {
            "kondisi": lambda hasil: hasil is not None,
            "status": "TERHUBUNG DALAM MODEL",
            "saran": "Jalur koneksi berhasil ditemukan."
        },
        {
            "kondisi": lambda hasil: hasil is None,
            "status": "TIDAK TERHUBUNG DALAM MODEL",
            "saran": "Periksa kembali hubungan antartitik."
        }
    ]

    for aturan_pakar in aturan:
        if aturan_pakar["kondisi"](jalur):
            return (
                aturan_pakar["status"],
                aturan_pakar["saran"]
            )

    return (
        "DIAGNOSIS TIDAK DIKETAHUI",
        "Periksa kembali model rangkaian."
    )
