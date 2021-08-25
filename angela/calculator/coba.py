import os
os.system('color 0c')
def partisi(arr, low, high):
    # Mengatur pivot
    # Untuk program ini, akan selalu menjadikan
    # elemen terakhir sebagai pivot
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if asc:
            # Jika ingin mengurutkan secara ascending
            if arr[j] <= pivot:
                # Menaikkan indeks elemen terkecil
                i += 1
                # Menukar tempat
                arr[i], arr[j] = arr[j], arr[i]
        else:
            # Jika ingin mengurutkan secara descending
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # Me-return index yang akan dipartisi
    return i + 1

# Fungsi Quick Sort
# arr -> Array yang akan disortir
# low -> Indeks akhir
# high -> Indeks awal
def quick_sort(arr, low, high):
    if low < high:
        # Index pembelah partisi array
        index = partisi(arr, low, high)        
        # Melakukan Quick Sort lagi pada array
        # yang telah dipartisi
        quick_sort(arr, low, index - 1)
        quick_sort(arr, index + 1, high)

# Keterangan program
print("=" * 70)
print("|" + "PROGRAM QUICK SORT".center(68) + "|")
print("=" * 70)
print("|" + "OLEH KELOMPOK 27".center(68) + "|")
print("=" * 70)
print("|" + " RISKY KURNIAWAN".ljust(34) + "(2009106050)".ljust(34) + "|")
print("|" + " FERRY FATHURRAHMAN".ljust(34) + "(2009106051)".ljust(34) + "|")
print("|" + " PUTRI WAHDANIYAH ISKANDAR".ljust(34) + "(2009106077)".ljust(34) + "|")
print("|" + " ALINDA AZZAHRA".ljust(34) + "(2009106092)".ljust(34) + "|")
print("|" + " AL-INAYYA".ljust(34) + "(2009106127)".ljust(34) + "|")
print("=" * 70)
print("|" + " PROGRAM INI DIKERJAKAN OLEH FERRY FATHURRAHMAN (2009106051) ".center(68) + "|")
print("=" * 70)

# Minta inputan user
print("Masukkan deretan bilangan bulat dan pisahlah dengan spasi!: ")
arr = filter(None, input().split(" "))
arr = list(map(int, arr))
n = len(arr)

# Menyalin arr ke variabel arr_awal
arr_awal = arr.copy()

# Melakukan quick sort secara ascending
asc = True
quick_sort(arr, 0, n - 1)
arr_asc = arr.copy()

# Melakukan quick sort secara descending
asc = False
quick_sort(arr, 0, n - 1)
arr_des = arr.copy()

# Mencetak hasil
print("\n" + "=" * 70)
print("\nArray awal:")
print(*arr_awal)
print("\nArray ascending:")
print(*arr_asc)
print("\nArray descending:")
print(*arr_des)
input("\nTekan enter untuk mengakhiri...")
