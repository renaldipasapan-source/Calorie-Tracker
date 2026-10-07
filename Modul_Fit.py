
# 1. RECURSION (Menghitung total akumulasi kalori)
def hitung_total_kalori(array, n):
    if n == 0:
        return 0
    return array[n-1][1] + hitung_total_kalori(array, n-1)

# 2. LINEAR SEARCH (Cari nama makanan/aktivitas)
def cari_data_fitness(array, target_nama):
    for i in range(len(array)):
        if array[i][0].lower() == target_nama.lower():
            return i 
    return -1

# 3. SORTING (Bubble Sort: urutkan dari kalori terkecil ke terbesar)
def urutkan_kalori(array):
    arr_urut = array.copy() 
    n = len(arr_urut)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr_urut[j][1] > arr_urut[j+1][1]:
                arr_urut[j], arr_urut[j+1] = arr_urut[j+1], arr_urut[j]
    return arr_urut

# 4. BINARY SEARCH (Cari nilai kalori spesifik pada data yang urut)
def cari_angka_kalori(array, target_kalori):
    awal = 0
    akhir = len(array) - 1
    while awal <= akhir:
        tengah = (awal + akhir) // 2
        if array[tengah][1] == target_kalori:
            return tengah 
        elif array[tengah][1] < target_kalori:
            awal = tengah + 1
        else:
            akhir = tengah - 1
    return -1