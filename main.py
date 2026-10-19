
from collections import deque

# Model hubungan antartitik rangkaian
rangkaian = {
    "Baterai+": ["R1"],
    "R1": ["Baterai+", "LED1"],
    "LED1": ["R1", "GND"],
    "GND": ["LED1"],
    "SENSOR": []
}


# Algoritma BFS untuk mencari jalur koneksi
def cari_jalur(mulai, tujuan):
    antrean = deque([[mulai]])
    dikunjungi = {mulai}

    while antrean:
        jalur = antrean.popleft()
        titik = jalur[-1]

        # Jika titik tujuan ditemukan
        if titik == tujuan:
            return jalur

        # Periksa tetangga dari titik saat ini
        for tetangga in rangkaian.get(titik, []):
            if tetangga not in dikunjungi:
                dikunjungi.add(tetangga)
                antrean.append(jalur + [tetangga])

    return None


# Sistem pakar sederhana untuk diagnosis
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


# Program utama
def main():
    print("=" * 45)
    print("          CIRCUIT 803 AI")
    print(" Diagnosis Konektivitas Rangkaian")
    print("=" * 45)

    print("\nDaftar titik yang tersedia:")
    for titik in rangkaian:
        print("-", titik)

    # Membuat pencarian input tidak sensitif huruf besar/kecil
    daftar_titik = {
        titik.lower(): titik for titik in rangkaian
    }

    input_mulai = input(
        "\nMasukkan titik awal: "
    ).strip().lower()

    input_tujuan = input(
        "Masukkan titik tujuan: "
    ).strip().lower()

    mulai = daftar_titik.get(input_mulai)
    tujuan = daftar_titik.get(input_tujuan)

    # Validasi input
    if mulai is None or tujuan is None:
        print("\n=== HASIL DIAGNOSIS ===")
        print("Status : INPUT TIDAK VALID")
        print("Saran  : Gunakan nama titik yang tersedia.")
        return

    # Pencarian jalur dan diagnosis
    hasil = cari_jalur(mulai, tujuan)
    status, saran = diagnosis(hasil)

    # Menampilkan hasil
    print("\n" + "=" * 45)
    print("             HASIL DIAGNOSIS")
    print("=" * 45)

    print("Titik awal  :", mulai)
    print("Titik tujuan:", tujuan)
    print("Status      :", status)
    print("Saran       :", saran)

    if hasil is not None:
        print("Jalur       :", " -> ".join(hasil))
    else:
        print("Jalur       : Tidak ditemukan")

    print("=" * 45)


if __name__ == "__main__":
    main()
