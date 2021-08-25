import os
import csv

csv_filename = r"produks.csv"

datacustomer = []
isi = []

def clear_screen():
    os.system("cls")

def awal():
    clear_screen()
    print("==========================================================")
    print("     ||     SELAMAT DATANG DI TOKO SKINCARE      || ")
    print("==========================================================")
    print("     ||    Program ini dibuat oleh kelompok 5:   ||")
    print("     ||      Ega Sulfika       2009106011        ||")
    print("     ||      Mitha Amalia      2009106011        ||")
    print("     ||      Mira Sartika L.   2009106011        ||")
    print("==========================================================")
    print("\n")
    input("Silahkan Tekan Enter Untuk Membaca Keterangan...")
    keterangan()

def keterangan():
    clear_screen()
    print("====================================================================") 
    login_dict = {"1": "[1] Silahkan pilih jika Anda adalah Admin", "2": "[2] Silahkan pilih jika Anda adalah Customer"}
    print(login_dict ["1"])
    print(login_dict ["2"])  
    print("====================================================================") 
    keterangann =  str(input("Silahkan Masukkan: "))
    if(keterangann == "1"):
        clear_screen()
        print("\n==================================================================")
        print("\t   Masukkan Username dan Password Admin Anda")
        print("====================================================================")
        i = 3 
        while i > 0:
            Username = str(input(">>> Username : "))
            Password = str(input(">>> Password : "))
            if (Username == "admin" and Password == "1234"):
                print("===================================")
                print("Anda Login Sebagai Admin")
                menuadmin()
            else:
                i -= 1
                print("    Usename dan Password Salah | Kesempatan anda tersedia : ", i, "kali" )
                if i == 0:
                    print("==================================")  
                    print("Anda Kami Kembalikan Ke Menu Awal")
                    print("==================================")
                    awal()
    elif(keterangann == "2"):
        print("\n")
        input("Tekan Enter Untuk Memilih Menu...")
        menucustomer()
    else:
        exit

def back_menu_admin():
    print("\n")
    input("Tekan Enter Untuk Kembali...")
    menuadmin()

def menuadmin():
    clear_screen()
    print("===============================================================") 
    print("===============================================================") 
    print(">>> Pilih Menu :") 
    menuadmin_tuple = "[1] Melihat Daftar Produk Skincare", "[2] Menambahkan Daftar Produk Skincare", "[3] Mengupdate Daftar Produk Skincare", "[4] Menghapus Daftar Produk Skincare", "[5] Mengurutkan/Menyorting Daftar Produk Skincare", "[6] Mencari Daftar Produk Skincare", "[7] Menghitung Banyak Barang Produk Skincare", "[8] Kembali", "[0] Logout"
    a,b,c,d,e,f,g,h,i = menuadmin_tuple
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)
    print("===============================================================") 
    print("===============================================================") 
    try:
        Menu = str(input("Masukkan Pilihan Anda: "))
        if (Menu == "1"):
            daftar() 
            back_menu_admin()
        elif(Menu == "2"):
            nambah()
        elif(Menu == "3"):
            update()
        elif(Menu == "4"):
            clear_screen()
            print("===========================================================")
            print("| Silahkan pilih ingin menghapus dengan metode yang mana: |")   
            hapus_tuple = "[1] Metode Remove", "[2] Metode Pop", "[3] Metode Clear", "[0] Kembali"   
            j,k,l,m = hapus_tuple 
            print("|",j,"\t\t\t\t\t  |")
            print("|",k,"\t\t\t\t\t  |")
            print("|",l,"\t\t\t\t\t  |")
            print("|",m,"\t\t\t\t\t\t  |")
            print("===========================================================")
            try:
                Menuhapus = str(input("Masukkan pilihan file fungsi yang diinginkan: "))
                if (Menuhapus == "1"):
                    hapus1()
                elif (Menuhapus == "2"):
                    hapus2()
                elif (Menuhapus == "3"):
                    hapus3()
                elif (Menuhapus == "0"):
                    menuadmin()
                else:
                    print("Anda memilih menu yang tidak tersedia")
                    back_menu_admin()
            except(KeyboardInterrupt):
                menuadmin()
        elif(Menu == "5"):
            clear_screen()
            print("========================================================================")
            print("|           Mengurutkan/Menyorting Data Produk Skincare                |")
            print("========================================================================")
            print("| [1] Sorting Nama Produk Metode Insertion Sort                        |")
            print("| [2] Sorting Stok Produk Metode Quick Sort                            |")
            print("| [3] Sorting Harga Produk Metode Quick Sort                           |")
            print("| [4] Sorting No Produk Metode Insertion Sort                          |")
            print("| [0] Kembali                                                          |")
            print("========================================================================")
            sorting = ""
            selected_menu = input("Pilih Menu> ")
            if selected_menu == "1":
                sorting = "NAMA_PRODUK"
            elif selected_menu == "2":
                sorting = "STOK_PRODUK"
            elif selected_menu == "3":
                sorting = "HARGA_PRODUK"
            elif selected_menu == "4":
                sorting = "NO"
            elif selected_menu == "0":
                back_menu_admin()
            else:
                print("========================================================================")
                print("| Error: Anda memilih menu yang salah!                                 |")
                print("========================================================================")
                back_menu_admin()
            clear_screen()
            print("========================================================================")
            print("|                          URUT AKUN PENGGUNA                          |")
            print("========================================================================")
            print("| [1] Secara Ascending                                                 |")
            print("| [2] Secara Descending                                                |")
            print("| [3] Kembali                                                          |")
            print("========================================================================")
            selected_menu = input("Pilih Menu> ")
            order = ""
            if selected_menu == "1":
                order = "Ascending"
            elif selected_menu == "2":
                order = "Descending"
            elif selected_menu == "3":
                back_menu_admin()
            else:
                print("========================================================================")
                print("| Error: Anda memilih menu yang salah!                                 |")
                print("========================================================================")
                back_menu_admin()
            akun = []
            with open(csv_filename, mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    akun.append(row)
            if len(akun) < 1:
                print("========================================================================")
                print("| Error: Tidak ada data pengguna ditemukan!                            |")
                print("========================================================================")
            else:
                datasort = []
                indeks = 0
                for data in akun:
                    if sorting == "NAMA_PRODUK":
                        datasort.append([data["NAMA_PRODUK"], indeks])
                    elif sorting == "STOK_PRODUK":
                        datasort.append([data["STOK_PRODUK"], indeks])
                    elif sorting == "HARGA_PRODUK":
                        datasort.append([data["HARGA_PRODUK"], indeks])
                    elif sorting == "NO":
                        datasort.append([data["NO"], indeks])
                    indeks += 1
                if sorting == "NAMA_PRODUK":
                    insertionSort(datasort, order)
                elif sorting == "STOK_PRODUK":
                    quickSort(datasort, 0, len(datasort)-1, order)
                elif sorting == "HARGA_PRODUK":
                    quickSort(datasort, 0, len(datasort)-1, order)
                elif sorting == "NO":
                    insertionSort(datasort, order)
                old_akun = akun.copy()
                akun.clear()
                for i in range(len(datasort)):
                    akun.append({"NO": old_akun[datasort[i][1]]["NO"], "NAMA_PRODUK": old_akun[datasort[i][1]]["NAMA_PRODUK"], "STOK_PRODUK": old_akun[datasort[i][1]]["STOK_PRODUK"], "HARGA_PRODUK": old_akun[datasort[i][1]]["HARGA_PRODUK"]})
                
                with open(csv_filename, mode="w") as csv_file:
                    fieldnames = ['NO', 'NAMA_PRODUK', 'STOK_PRODUK', 'HARGA_PRODUK']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in akun:
                        writer.writerow({'NO': new_data['NO'], 'NAMA_PRODUK': new_data['NAMA_PRODUK'], 'STOK_PRODUK': new_data['STOK_PRODUK'], 'HARGA_PRODUK': new_data['HARGA_PRODUK']})         
                print("========================================================================")
                print("| Sukses: Data Pengguna berhasil diurutkan                             |")
                print("========================================================================")
            back_menu_admin()
        elif(Menu == "6"):
            clear_screen()
            print("========================================================================")
            print("|                   Mencari Data Produk Skincare                       |")
            print("========================================================================")
            print("| [1] Searching Nama Produk Metode Linear Search                       |")
            print("| [0] Kembali                                                          |")
            print("========================================================================")
            searching = ""
            Menuurut = str(input("Masukkan pilihan yang diinginkan: "))
            if Menuurut == "1":
                produks = []
                with open(csv_filename, mode="r") as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        produks.append(row)
                print("******************************************************************************") 
                print("NO \tNama Produk \t\t Stok Produk \t Harga Produk")
                print("******************************************************************************") 
                for data in produks:
                    print(f"{data['NO']} \t {data['NAMA_PRODUK']} \t {data['STOK_PRODUK']} \t\t {data['HARGA_PRODUK']}")
                
                search = input("Data yang ingin dicari> ")
                
                result = linearSearch(produks, len(produks), search)
                print(result)
                back_menu_admin()

            elif Menuurut == "0":
                back_menu_admin()

            else:
                menuadmin()


        elif(Menu == "7"):
            hitung()
        elif(Menu == "8"):
            keterangan()
        elif(Menu == "0"):
            awal()
        else:
            print("Pilihan salah!")
            input("\nTekan Enter Untuk Memilih Menu Yang Lain")
            menuadmin()
    except(KeyboardInterrupt):
        awal()

def daftar():
    clear_screen()
    produks = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            produks.append(row)
    print("******************************************************************************") 
    print("NO \tNama Produk \t\t Stok Produk \t Harga Produk")
    print("******************************************************************************") 
    for data in produks:
        print(f"{data['NO']} \t {data['NAMA_PRODUK']} \t {data['STOK_PRODUK']} \t\t {data['HARGA_PRODUK']}")

def nambah():
    clear_screen()
    produks = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            produks.append(row)
    print("******************************************************************************") 
    print("NO \tNama Produk \t\t Stok Produk \t Harga Produk")
    print("******************************************************************************") 
    for data in produks:
        print(f"{data['NO']} \t {data['NAMA_PRODUK']} \t {data['STOK_PRODUK']} \t\t {data['HARGA_PRODUK']}")

    print("******************************************************************************") 
    print("|                    Menambahkan Daftar Produk Skincare                      |")
    print("******************************************************************************") 

    with open(csv_filename, mode='a') as csv_file:
        fieldnames = ['NO', 'NAMA_PRODUK', 'STOK_PRODUK', 'HARGA_PRODUK']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        EROR = True
        while(EROR):
            try:
                datano      = int(input("Masukkan no produk baru    : "))
                break
            except ValueError:
                print("Inputan Anda Salah Masukkan Angka!!!")

        databaru    = input("Masukkan produk baru       : ")
        EROR = True
        while(EROR):
            try:
                datastbaru  = int(input("Masukkan stok baru         : "))
                break
            except ValueError:
                print("Inputan Anda Salah Masukkan Angka!!!")
        
        EROR = True
        while(EROR):
            try:
                datahgbaru  = int(input("Masukkan harga baru        : "))
                break
            except ValueError:
                print("Inputan Anda Salah Masukkan Angka!!!")
        
        writer.writerow({'NO': datano,'NAMA_PRODUK': databaru, 'STOK_PRODUK': datastbaru, 'HARGA_PRODUK': datahgbaru})    
        print("Berhasil disimpan!")

    back_menu_admin()

def update():
    clear_screen()
    produks = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            produks.append(row)
    print("******************************************************************************") 
    print("NO \tNama Produk \t\t Stok Produk \t Harga Produk")
    print("******************************************************************************") 
    for data in produks:
        print(f"{data['NO']} \t {data['NAMA_PRODUK']} \t {data['STOK_PRODUK']} \t\t {data['HARGA_PRODUK']}")

    print("******************************************************************************") 
    print("|                      Mengupdate Daftar Produk Skincare                     |")
    print("******************************************************************************")
    EROR = True
    while(EROR):
        try:
            nodelete = input("Masukkan No dari produk yang ingin dihapus: ")
            break
        except ValueError:
            print("Inputan Anda Salah Masukkan Angka!!!")
    EROR = True
    while(EROR):
        try:
            no     = int(input("Pilih Nomor Produk          : "))
            datanp = str(input("Masukkan nama produk baru   : "))
            indeks = 0 
            for data in produks:
                if (data['NO'] == no):
                    produks[indeks]['NAMA_PRODUK'] = datanp
                indeks = indeks + 1
            
            EROR = True
            while(EROR):
                try:
                    datast = int(input("Masukkan stok produk baru   : "))
                    indeks = 0 
                    for data in produks:
                        if (data['NO'] == no):
                            produks[indeks]['STOK_PRODUK'] = datast
                        indeks = indeks + 1
                    break
                except ValueError:
                    print("Inputan Anda Salah Masukkan Angka!!!")
            EROR = True
            while(EROR):
                try:
                    datahg = int(input("Masukkan harga produk baru  : "))
                    indeks = 0 
                    for data in produks:
                        if (data['NO'] == no):
                            produks[indeks]['HARGA_PRODUK'] = datahg
                        indeks = indeks + 1
                    break
                except ValueError:
                    print("Inputan Anda Salah Masukkan Angka!!!")
            break
        except ValueError:
            print("Inputan Anda Salah Masukkan Angka!!!")
    
    print("******************************************************************************") 
    indeks = 0 
    for data in produks:
        if (data['NO'] == no):
            produks[indeks]['NAMA_PRODUK'] = datanp
            produks[indeks]['STOK_PRODUK'] = datast
            produks[indeks]['HARGA_PRODUK'] = datahg
        indeks = indeks + 1
    
    # Menulis data baru ke file CSV (tulis ulang)
    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NO', 'NAMA_PRODUK', 'STOK_PRODUK', 'HARGA_PRODUK']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in produks:
            writer.writerow({'NO': new_data['NO'], 'NAMA_PRODUK': new_data['NAMA_PRODUK'], 'STOK_PRODUK': new_data['STOK_PRODUK'], 'HARGA_PRODUK': new_data['HARGA_PRODUK']}) 
    back_menu_admin()

def hapus1():
    clear_screen()
    produks = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            produks.append(row)

    print("******************************************************************************") 
    print("NO \tNama Produk \t\t Stok Produk \t Harga Produk")
    print("******************************************************************************") 
    for data in produks:
        print(f"{data['NO']} \t {data['NAMA_PRODUK']} \t {data['STOK_PRODUK']} \t\t {data['HARGA_PRODUK']}")    
    
    print("******************************************************************************") 
    print("|   Menghapus Daftar, Stok, dan Harga Produk Skincare Dengan Metode Remove   |")
    print("******************************************************************************") 

    EROR = True
    while(EROR):
        try:
            nodelete = int(input("Masukkan No dari produk yang ingin dihapus: "))
            indeks = 0
            for data in produks:
                if (data['NO'] == nodelete):
                    produks.remove(produks[indeks])
                indeks = indeks + 1
            break
        except ValueError:
            print("Inputan Anda Salah Masukkan Angka!!!")


    if(len(produks) > 0):
        with open(csv_filename, mode="w") as csv_file:
            fieldnames = ['NO', 'NAMA_PRODUK', 'STOK_PRODUK', 'HARGA_PRODUK']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in produks:
                writer.writerow({'NO': new_data['NO'], 'NAMA_PRODUK': new_data['NAMA_PRODUK'], 'STOK_PRODUK': new_data['STOK_PRODUK'], 'HARGA_PRODUK': new_data['HARGA_PRODUK']}) 
        print("Data sudah terhapus")
    else:
        print("Data tidak ditemukan")
    back_menu_admin()

def hapus2():
    clear_screen()
    produks = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            produks.append(row)

    print("******************************************************************************") 
    print("NO \tNama Produk \t\t Stok Produk \t Harga Produk")
    print("******************************************************************************") 
    for data in produks:
        print(f"{data['NO']} \t {data['NAMA_PRODUK']} \t {data['STOK_PRODUK']} \t\t {data['HARGA_PRODUK']}")    
    
    print("******************************************************************************") 
    print("|   Menghapus Daftar, Stok, dan Harga Produk Skincare Dengan Metode POP   |")
    print("******************************************************************************") 

    nodelete = input("Masukkan Indeks No dari produk yang ingin dihapus: ")
    indeks = 0
    for data in produks:
        if (data['NO'] == nodelete):
            produks.pop(produks[indeks])
        indeks = indeks + 1

    if(len(produks) > 0):
        with open(csv_filename, mode="w") as csv_file:
            fieldnames = ['NO', 'NAMA_PRODUK', 'STOK_PRODUK', 'HARGA_PRODUK']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in produks:
                writer.writerow({'NO': new_data['NO'], 'NAMA_PRODUK': new_data['NAMA_PRODUK'], 'STOK_PRODUK': new_data['STOK_PRODUK'], 'HARGA_PRODUK': new_data['HARGA_PRODUK']}) 
        print("Data sudah terhapus")
    else:
        print("Data tidak ditemukan")
    back_menu_admin() 

def hapus3():
    clear_screen()
    produks = []
    print("******************************************************************************") 
    print("|   Menghapus Daftar, Stok, dan Harga Produk Skincare Dengan Metode Clear   |")
    print("******************************************************************************") 

    with open(csv_filename, mode="w") as csv_file:
        fieldnames = ['NO', 'NAMA_PRODUK', 'STOK_PRODUK', 'HARGA_PRODUK']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in produks:
            writer.writerow({'NO': new_data['NO'], 'NAMA_PRODUK': new_data['NAMA_PRODUK'], 'STOK_PRODUK': new_data['STOK_PRODUK'], 'HARGA_PRODUK': new_data['HARGA_PRODUK']}) 
    print("All Data sudah terhapus")
    back_menu_admin() 

def insertionSort(array, order):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        if order == "Ascending":
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key
        elif order == "Descending":
            while j >= 0 and key > array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key

def partition(array, low, high, order):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if order == "Ascending":
            if array[j] <= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]
        elif order == "Descending":
            if array[j] >= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high, order):
    if low < high:
        pi = partition(array, low, high, order)
        quickSort(array, low, pi - 1, order)
        quickSort(array, pi + 1, high, order)

def linearSearch(array, n, x):
    for i in range(0, n):
        if array[i]['NAMA_PRODUK'] == x:
            print("Element terdapat di index: ", i)
            return i
    return -1

def hitung():
    clear_screen()
    print("******************************************************************************") 
    print("|               Menghitung Banyak Daftar Produk Skincare                     |")
    print("******************************************************************************") 
    produks = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            produks.append(row)
    print("******************************************************************************") 
    print("NO \tNama Produk \t\t Stok Produk \t Harga Produk")
    print("******************************************************************************") 
    for data in produks:
        print(f"{data['NO']} \t {data['NAMA_PRODUK']} \t {data['STOK_PRODUK']} \t\t {data['HARGA_PRODUK']}")
    print("******************************************************************************") 
    print("\nBanyaknya Produk  : ", len(produks))
    back_menu_admin()

def back_menu_customer():
    print("\n")
    input("Tekan Enter Untuk Kembali...")
    menucustomer()

def menucustomer():
    clear_screen()
    print("===============================================================") 
    print("===============================================================") 
    print(">>> Pilih Menu :") 
    menucustome_tuple = "[1] Melihat Daftar Harga Skincare", "[2] Pembayaran/Kasir", "[3] Kembali", "[0] Logout"
    w, x, y, z = menucustome_tuple
    print(w)
    print(x)
    print(y)
    print(z)
    print("===============================================================") 
    print("===============================================================") 
    Menu = str(input("Masukkan Pilihan Anda: "))
    if (Menu == "1"):
        clear_screen()
        daftar()
        back_menu_customer()
    elif (Menu == "2"):
        clear_screen()
        datapembeli()
    elif (Menu == "3"):
        back_menu_customer()
    elif (Menu == "0"):
        awal()
    else:
        print("Pilihan salah!")
        input("\nTekan Enter Untuk Memilih Menu Yang Lain")
        back_menu_customer()

def datapembeli():
    print("===============================================")
    print("Silahkan isi data Anda sebelum memilih produk: ")
    nama    = str(input("Nama Anda   : "))
    alamat  = str(input("Alamat Anda : "))
    datacustomer.append(nama)
    datacustomer.append(alamat)
    print("===============================================")
    input("Silahkan tekan ENTER untuk memilih produk!!! ")
    clear_screen()
    masukkan()

def masukkan():
    produks = []

    with open(csv_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            produks.append(row)
    print("******************************************************************************") 
    print("NO \tNama Produk \t\t Stok Produk \t Harga Produk")
    print("******************************************************************************") 
    for data in produks:
        print(f"{data['NO']} \t {data['NAMA_PRODUK']} \t {data['STOK_PRODUK']} \t\t {data['HARGA_PRODUK']}")
    
    print("===============================================")
    no = int(input("Pilih Nomor Produk          : "))
    for data in produks:
        if (data['NO'] == str(no)): 
            no -= 1
            print(produks[no]['HARGA_PRODUK'])
    print("===============================================")
    jumlah= int(input("Masukan jumlah Produk yang dibeli  : "))
    print("===============================================")
    Total= jumlah * int(produks[no]['HARGA_PRODUK'])
    print("Yang harus dibayar                 : Rp", Total)
    print("===============================================")
    Bayar=int(input("Pembayaran                         : Rp " ))
    Kembalian= (Bayar-Total)
    print("===============================================")

    clear_screen()
    print("\n===========================================")
    print("======= S T R U K   P E M B E L I A N =====")
    print("===========================================")
    struck_tuple = tuple(datacustomer)
    struck_dict = {'Nama Anda' : struck_tuple[0],'Alamat Anda' : struck_tuple[1]}
    print(" Nama        :",struck_tuple[0])
    print(" Alamat      :",struck_tuple[1])
    print(" Produk      :",produks[no]['NAMA_PRODUK'])
    print(" Tagihan     : Rp",Total)
    print(" Uang        : Rp",Bayar)
    print(" Kembalian   : Rp",Kembalian)
    print("===========================================")
    print("===========================================")
    back_menu_customer()

if __name__ == "__main__":
    while True:
        awal()