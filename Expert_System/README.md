
# Expert System

## Deskripsi
Modul Expert System merupakan bagian dari CircuitPath SSF AI yang digunakan untuk menentukan diagnosis konektivitas berdasarkan titik awal, titik tujuan, dan hasil pencarian jalur.

## Metode
Sistem menggunakan Rule-Based System dengan aturan IF-THEN untuk menentukan hasil diagnosis.

## Aturan Diagnosis
- RULE 1: Input tidak valid.
- RULE 2: Titik awal dan tujuan sama.
- RULE 3: Jalur koneksi ditemukan.
- RULE 4: Jalur koneksi tidak ditemukan.

## Fungsi
- Memeriksa validitas titik koneksi.
- Menentukan status konektivitas dalam model.
- Memberikan penjelasan dan saran berdasarkan hasil diagnosis.

## Teknologi
- Bahasa pemrograman Python
- Rule-Based System (IF-THEN)

## Pengujian
Modul telah diuji untuk kondisi jalur ditemukan, jalur tidak ditemukan, dan input tidak valid.

## Cara Menjalankan
Dari direktori utama repository, jalankan:

    python3 Expert_System/IF_THEN_Tets.py

## Pengembang
Developer Steven
