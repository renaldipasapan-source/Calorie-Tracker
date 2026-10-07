# Calorie-Tracker
A Python modular CLI application to track daily food and exercise calories, built to demonstrate core Data Structures &amp; Algorithms (2D Arrays, Recursion, Linear Search, Bubble Sort, Binary Search).


Markdown# 🥗 Calorie Tracker

> Program manajemen dan pemantauan kalori harian berbasis *Command-Line Interface* (CLI) yang dibangun menggunakan bahasa pemrograman Python[cite: 3, 4]. Proyek ini dikembangkan sebagai *Mini Project* mata kuliah **Struktur Data** dengan menerapkan konsep pemrograman modular (*modular programming*)[cite: 3, 4].

---

## 📌 Tentang Proyek
Proyek ini dibuat untuk membantu mengelola dan memantau keseimbangan energi harian antara asupan makanan/minuman (kalori masuk) dan pembakaran kalori melalui aktivitas fisik atau olahraga (kalori keluar). 

Program ini dirancang agar bersih, efisien, dan menggunakan struktur data fundamental tanpa *library* bawaan yang rumit[cite: 3, 4].

---

## 🛠️ Konsep Struktur Data & Algoritma
Di dalam program ini, beberapa konsep algoritma utama diimplementasikan secara langsung:
1. **Array (List 2 Dimensi):** Menyimpan data log harian dalam format berpasangan `[Nama_Item, Jumlah_Kalori]`.
2. **Rekursif (Recursion):** Menghitung total akumulasi kalori keseluruhan secara rekursif melalui fungsi `hitung_total_kalori()`[cite: 3, 4].
3. **Linear Search:** Menemukan data makanan atau olahraga tertentu berdasarkan nama menggunakan pencarian berurutan (`.lower()`)[cite: 3, 4].
4. **Bubble Sort (Sorting):** Mengurutkan data dari jumlah kalori terkecil hingga terbesar[cite: 3, 4].
5. **Binary Search:** Mencari data berdasarkan angka kalori spesifik secara efisien setelah data diurutkan[cite: 3, 4].

---

## 📂 Struktur File
Proyek ini dibagi menjadi dua file terpisah untuk menjaga prinsip modularitas[cite: 3, 4]:
* `Modul_Fit.py` : Modul yang berisi kumpulan fungsi logika algoritma (Rekursif, Searching, dan Sorting)[cite: 4].
* `main_2.py` : Program utama yang mengatur tampilan menu interaktif (*User Interface*).

---

## 🚀 Cara Menjalankan Program
1. Pastikan komputer kamu sudah menginstal **Python**.
2. Unduh atau *clone* repository ini ke dalam satu folder yang sama:
   ```bash
   git clone [https://github.com/username-kamu/Calorie-Tracker.git](https://github.com/username-kamu/Calorie-Tracker.git)
Buka terminal/CMD di dalam folder tersebut, lalu jalankan file utama:Bashpython main_2.py

> ### 👨‍💻 Informasi Pengembang
> | Atribut | Keterangan |
> | :--- | :--- |
> | **Nama** | Renaldi Pasapan[cite: 3] |
> | **NIM** | `20255520009`[cite: 3] |
> | **Program Studi** | Informatika[cite: 3] |
> | **Institusi** | Universitas Matana[cite: 3] |