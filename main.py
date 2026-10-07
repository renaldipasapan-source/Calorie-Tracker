# ==========================================
# Nama      : Renaldi Pasapan
# NIM       : 20255520009
# Prodi     : Informatika
# ==========================================

import Modul_Fit as fit

def main():
    # Array 2D dengan data makanan, minuman, dan olahraga beserta jumlah kalori
    log_harian = [
        ["Nasi Goreng", 450],
        ["Ayam Goreng", 300],
        ["Mie Ayam", 400],
        ["Jus Buah", 150],
        ["Matcha", 120],
        ["Air Putih", 0],
        ["Jogging", -250],
        ["Badminton", -300],
        ["Gym / Angkat Beban", -350]
    ]

    target_maksimal = 1800

    while True:
        print("\n======================================")
        print("   SMART FITNESS & CALORIE TRACKER")
        print("======================================")
        print("1. Lihat Log Kalori Harian")
        print("2. Hitung Total Rincian Kalori (Rekursif)")
        print("3. Cari Nama Makanan/Olahraga (Linear)")
        print("4. Urutkan Data Kalori (Sort)")
        print("5. Cari Berdasarkan Angka Kalori (Binary)")
        print("6. Tambah Catatan Baru")
        print("7. Keluar")
        print("======================================")

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            print("\n" + "="*30)
            print(" MAKANAN & MINUMAN")
            print("="*30)
            no = 1
            for item in log_harian:
                if item[1] >= 0:
                    print(f"{no}. {item[0]} : +{item[1]} kcal")
                    no += 1

            print("\n" + "="*30)
            print(" OLAHRAGA (PEMBAKARAN)")
            print("="*30)
            no = 1
            for item in log_harian:
                if item[1] < 0:
                    print(f"{no}. {item[0]} : {item[1]} kcal")
                    no += 1
            print("="*30)

        elif pilihan == "2":
            # Menghitung terpisah untuk rincian tampilan
            total_masuk = sum([item[1] for item in log_harian if item[1] > 0])
            total_keluar = sum([item[1] for item in log_harian if item[1] < 0])
            
            # Memanggil fungsi rekursif untuk total bersih
            total_bersih = fit.hitung_total_kalori(log_harian, len(log_harian))
            
            print("\n" + "="*35)
            print("       RINCIAN KALORI HARI INI")
            print("="*35)
            print(f"Total Kalori Masuk (Makanan)  : +{total_masuk} kcal")
            print(f"Total Kalori Keluar (Olahraga): {total_keluar} kcal")
            print("-" * 35)
            print(f"Total Bersih Kalori           : {total_bersih} kcal")
            print(f"Target Batas Maksimal         : {target_maksimal} kcal")
            print("="*35)
            
            if total_bersih > target_maksimal:
                print("-> STATUS: Peringatan! Kalori berlebih (Surplus).")
            else:
                print("-> STATUS: Bagus! Kalori harian masih dalam batas aman.")

        elif pilihan == "3":
            print("\n--- PANDUAN PENCARIAN ---")
            print("List : Nasi Goreng, Ayam Goreng, Mie Ayam, Jus Buah, Matcha, Air Putih, Jogging, Badminton, Gym / Angkat Beban")
            nama = input("Masukkan nama makanan/aktivitas yang dicari: ")
            
            indeks = fit.cari_data_fitness(log_harian, nama)
            if indeks != -1:
                print(f"-> Ditemukan! '{log_harian[indeks][0]}' memiliki nilai sebesar {log_harian[indeks][1]} kcal.")
            else:
                print("-> Data tidak ditemukan. Pastikan ejaan namanya sesuai.")

        elif pilihan == "4":
            log_harian = fit.urutkan_kalori(log_harian)
            print("\n-> Data berhasil diurutkan dari kalori terkecil ke terbesar!")
            for i in range(len(log_harian)):
                print(f"{i+1}. {log_harian[i][0]} : {log_harian[i][1]} kcal")

        elif pilihan == "5":
            print("\n--- PILIH ANGKA KALORI YANG TERSEDIA ---")
            print(" daftar angka kalori dalam data saat ini (setelah diurutkan):")
            
            # Tampilkan daftar data yang sudah diurutkan agar user tahu angka apa saja yang ada
            temp_urut = fit.urutkan_kalori(log_harian)
            for item in temp_urut:
                print(f"   • {item[0]} -> {item[1]} kcal")
                
            target = int(input("\nMasukkan angka kalori dari daftar di atas yang ingin dicari: "))
            
            log_harian = fit.urutkan_kalori(log_harian) 
            indeks = fit.cari_angka_kalori(log_harian, target)
            if indeks != -1:
                print(f"-> Ditemukan! Item dengan jumlah {target} kcal adalah: {log_harian[indeks][0]}")
            else:
                print("-> Tidak ada item dengan jumlah kalori tersebut.")

        elif pilihan == "6":
            nama_baru = input("\nNama Makanan/Aktivitas baru: ")
            kalori_baru = int(input("Jumlah Kalori (Gunakan tanda minus '-' jika itu olahraga, contoh: -200): "))
            log_harian.append([nama_baru, kalori_baru])
            print("-> Catatan berhasil ditambahkan ke dalam sistem!")

        elif pilihan == "7":
            print("\nSampai jumpa.")
            break

        else:
            print("\nPilihan tidak valid.")

if __name__ == "__main__":
    main()