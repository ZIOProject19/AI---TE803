
# Multi-Agent System (MAS)

## Deskripsi
Modul Multi-Agent System merupakan bagian dari CircuitPath SSF AI yang mengoordinasikan beberapa agen untuk membantu proses diagnosis konektivitas rangkaian listrik.

## Agen yang Digunakan
1. Search Agent: mencari jalur koneksi menggunakan algoritma BFS.
2. Connection Analysis Agent: menganalisis hasil pencarian jalur.
3. Diagnosis Agent: menentukan hasil diagnosis berdasarkan aturan IF-THEN.

## Alur Kerja
1. Pengguna memasukkan titik awal dan titik tujuan.
2. Search Agent mencari jalur koneksi.
3. Connection Analysis Agent menganalisis hasil pencarian.
4. Diagnosis Agent menentukan status, penjelasan, dan saran.
5. Hasil diagnosis ditampilkan kepada pengguna melalui main.py.

## Teknologi
- Bahasa pemrograman Python
- Breadth-First Search (BFS)
- Rule-Based Expert System
- Multi-Agent System

## Pengujian
- Jalur ditemukan: Baterai+ ke LED1.
- Jalur tidak ditemukan: Baterai+ ke SENSOR.
- Input tidak valid: ABC ke LED1.

## Cara Menjalankan
Dari direktori utama repository, jalankan:

    python3 -m Multi_Agency_System.MAS_Test

Untuk menjalankan seluruh sistem, gunakan:

    python3 main.py

## Pengembang
Manager
