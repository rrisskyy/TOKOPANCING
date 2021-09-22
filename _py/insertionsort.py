import os
def clr():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')



def insertionSort(listSaya):
    totalIterasi = []
    for i in range(1, len(listSaya)):
        iterasi = 0
        kanan = listSaya[i]
        kiri = i - 1
        while kiri >= 0 and listSaya[kiri] > kanan:
            listSaya[kiri + 1] = listSaya[kiri]
            kiri -= 1
            iterasi += 1
        totalIterasi.append(iterasi)
        listSaya[kiri + 1] = kanan
    return [listSaya, totalIterasi]
 
def descInsertionSort(listSaya):
    totalIterasi = []
    for i in range(1, len(listSaya)):
        iterasi = 0
        kanan = listSaya[i]
        kiri = i - 1
        while kiri >= 0 and listSaya[kiri] < kanan:
            listSaya[kiri + 1] = listSaya[kiri]
            kiri -= 1
            iterasi += 1
        totalIterasi.append(iterasi)
        listSaya[kiri + 1] = kanan
    return [listSaya, totalIterasi]

clr()
print("1. Ascending")
print("2. Descending")
pil = input("Masukkan Pilihan >>> \t")

if (pil == "1"):
    print("Masukkan angka anda, pisah dengan (Spasi)")
    print(">>>\t", end="")
    listSaya = filter(None, input().split(" "))
    listSaya = list(map(int, listSaya))  

    
    print ( "\n\nSebelum di sorting =" , end="\t")

    for i in range(len(listSaya)):
        print (listSaya[i]) if i == len(listSaya)-1 else print (listSaya[i], end=", ")

    sortedList = insertionSort(listSaya)
    print("\n\n")    
    print( f"Dari angka tersebut, terjadi {len(sortedList[1])} kali iterasi\n" )
    for i in range(len(sortedList[0])-1):
        print( f"Iterasi ke {i+1} terjadi sebanyak {sortedList[1][i]} Pemindahan ")

    print ( "\n\nSetelah di sorting =" , end="\t")    
    for j in range(len(sortedList[0])):
        print (sortedList[0][j]) if j == len(sortedList[0])-1 else print (sortedList[0][j], end=", ")
    print("\n"*7)

elif (pil == "2"):
    print("Masukkan angka anda, pisah dengan (Spasi)")
    print(">>>\t", end="")
    listSaya = filter(None, input().split(" "))
    listSaya = list(map(int, listSaya))  

    
    print ( "\n\nSebelum di sorting =" , end="\t")

    for i in range(len(listSaya)):
        print (listSaya[i]) if i == len(listSaya)-1 else print (listSaya[i], end=", ")
    descSortedList = descInsertionSort(listSaya)
    print("\n\n")    
    print( f"Dari angka tersebut, terjadi {len(descSortedList[1])} kali iterasi\n" )
    for i in range(len(descSortedList[0])-1):
        print( f"Iterasi ke {i} terjadi sebanyak {descSortedList[1][i]} Pemindahan ")

    print ( "\n\nSetelah di sorting =" , end="\t")    
    for j in range(len(descSortedList[0])):
        print (descSortedList[0][j]) if j == len(descSortedList[0])-1 else print (descSortedList[0][j], end=", ")
    print("\n"*7)