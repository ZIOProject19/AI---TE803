# Expert System: aturan IF-THEN berbasis hasil pencarian

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


def diagnosis(jalur):
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
