# Search Algorithm: Breadth-First Search (BFS)

from collections import deque

def cari_jalur(graf, mulai, tujuan):
    antrean = deque([[mulai]])
    dikunjungi = {mulai}

    while antrean:
        jalur = antrean.popleft()
        titik = jalur[-1]

        if titik == tujuan:
            return jalur

        for tetangga in graf.get(titik, []):
            if tetangga not in dikunjungi:
                dikunjungi.add(tetangga)
                antrean.append(jalur + [tetangga])

    return None
