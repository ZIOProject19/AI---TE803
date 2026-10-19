
# Search Algorithm

## Deskripsi
Modul Search Algorithm merupakan bagian dari CircuitPath SSF AI yang digunakan untuk mencari jalur koneksi antara dua titik dalam model rangkaian listrik.

## Algoritma
Modul ini menggunakan Breadth-First Search (BFS), yaitu algoritma pencarian yang menelusuri titik-titik secara bertahap untuk menemukan jalur dengan jumlah sisi paling sedikit.

## Fungsi
- Mencari jalur koneksi dari titik awal ke titik tujuan.
- Menentukan apakah jalur tersedia dalam model rangkaian.
- Mengembalikan jalur yang ditemukan atau informasi bahwa jalur tidak tersedia.
- Menangani input titik koneksi yang tidak dikenal.

## Teknologi
- Bahasa pemrograman Python
- Breadth-First Search (BFS)

## Pengujian
- Baterai+ ke LED1: jalur ditemukan.
- Baterai+ ke SENSOR: jalur tidak ditemukan.
- Input titik yang tidak dikenal: ditangani sebagai input tidak valid.

## Cara Menjalankan
Dari direktori utama repository, jalankan:

    python3 Search_Algorthm/BFS_Test.py

## Pengembang
Developer Fedya
