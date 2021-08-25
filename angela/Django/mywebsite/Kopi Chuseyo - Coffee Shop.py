import os
import time

jenis = []
harga = []
harga_milk=[]
harga_fd =[]
harga_kopi =[]
name = []
nama = ""
pembayaran = ""


milk = {}
fd = {}
kopi = {}

daftarKopi = ["Oppa", "Unnie", "Ahjussi", "Dalgona", "Caramel Latte", "Caramel Macchiato"]
daftarHargaKopi = [19000, 19000, 25000, 25000, 30000, 35000]

daftarMilk = ["Banana Uyu", "White Regal", "Dark Chocolit", "Bobo Brown Boba"]
daftarHargaMilk = [25000, 25000, 25000, 30000]

daftarFreshDrink = ["Sunny Summer", "Classic Tea"]
daftarHargaFreshDrink = [25000, 25000]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def welcome():
    print("=======================================")
    print("              2009106047               ")
    print("    Muhammad Amri Rasyid Ramadhan      ")
    print(" _____________________________________ ")
    print("|                                     |")
    print("|         Selamat Datang di           |")
    print("|       KOPI CHUSEYO SAMARINDA        |")
    print("\_____________________________________/")
    print("\n")

    print("1. Admin")
    print("2. Kasir")
    pil = input("Masuk Ke Menu :    ")

    if (pil == "1" or pil.lower() == "admin"):
        admin()
        pass
    elif (pil == "2" or pil.lower() == "kasir"):
        nama = str(input("\n\nAtas Nama : "))
        name.append(nama)
        menu()


def admin():
    clear_screen()
    print("         ---Menu Admin---          ")
    print("1. Tambahkan Minuman                      ")
    print("2. Hapus Minuman                          ")
    print("3. Upate Harga Minuman                    ")

    pil = input("Pilih Menu :    ")

    if pil == "1" :
        clear_screen()
        print("         ---Tambahkan Minuman---          ")
        print("1. Tambahkan Kopi                         ")
        print("2. Tambahkan Fresh Drink                  ")
        print("3. Tambahkan Milk                         ")
        pil1 = input("Pilih Menu :    ")
        if pil1 == "1":

            tambahMinum = input("Masukkan Nama Kopi :    ")
            tambahHargaMinum = int(input("Masukkan Harga Kopi :    "))
            daftarKopi.append(tambahMinum)
            daftarHargaKopi.append(tambahHargaMinum)
            print("Berhasil!...")
            welcome()

        if pil1 == "2":
            tambahMinum = input("Masukkan Nama Fresh Drink :    ")
            tambahHargaMinum = int(input("Masukkan Harga Fresh Drink :    "))
            daftarFreshDrink.append(tambahMinum)
            daftarHargaFreshDrink.append(tambahHargaMinum)
            print("Berhasil!...")
            welcome()
            
        if pil1 == "3":
            tambahMinum = input("Masukkan Nama Milk :    ")
            tambahHargaMinum = int(input("Masukkan Harga Milk :    "))
            daftarMilk.append(tambahMinum)
            daftarHargaMilk.append(tambahHargaMinum)
            print("Berhasil!...")
            welcome()


    elif pil == "2" :
        clear_screen()
        print("         ---Tambahkan Minuman---          ")
        print("1. Hapus Kopi                             ")
        print("2. Hapus Fresh Drink                      ")
        print("3. Hapus Milk                             ")
        pil2 = input("Pilih Menu :    ")
        if pil2 == "1":
            for i in range(len(daftarKopi)):
                print(f"{i+1}.  {daftarKopi[i]}")
            hapusMinum = int(input("Masukkan ID Kopi :    "))
            del daftarKopi[hapusMinum-1]
            del daftarHargaKopi[hapusMinum-1]
            print("Berhasil!...")
            welcome()

        if pil2 == "2":
            for i in range(len(daftarFreshDrink)):
                print(f"{i+1}. {daftarFreshDrink[i]}")
            hapusMinum = int(input("Masukkan ID Fresh Drink :    "))

            del daftarFreshDrink[hapusMinum-1]
            del daftarHargaFreshDrink[hapusMinum-1]
            print("Berhasil!...")
            welcome()
            
        if pil2 == "3":
            for i in range(len(daftarMilk)):
                print(f"{i+1}. {daftarMilk[i]}")
            hapusMinum = int(input("Masukkan ID Milk :    "))

            del daftarMilk[hapusMinum-1]
            del daftarHargaMilk[hapusMinum-1]
            print("Berhasil!...")
            welcome()

    elif pil == "3":
        clear_screen()
        print("         ---Tambahkan Minuman---          ")
        print("1. Update Kopi                            ")
        print("2. Update Fresh Drink                     ")
        print("3. Update Milk                            ")
        pil3 = input("Pilih Menu :    ")
        if pil3 == "1":
            for i in range(len(daftarKopi)):
                print(f"{i+1}. Kopi {daftarKopi[i]}")

            ubahMinum = int(input("Masukkan ID Kopi :    "))
            print("\nAnda ingin Mengubah Harga Kopi :  ", end="")
            print(daftarKopi[ubahMinum-1])
            print("Harga Sebelumnya :  ", daftarHargaKopi[ubahMinum-1], "\n\n")
            
            ubahHargaMinum = int(input("Masukkan Harga Baru Kopi :    "))
            daftarHargaKopi[ubahMinum-1] = ubahHargaMinum

            print("Berhasil!...")
            welcome()

        if pil3 == "2":
            for i in range(len(daftarFreshDrink)):
                print(f"{i+1}. {daftarFreshDrink[i]}")

            ubahMinum = int(input("Masukkan ID Fresh Drink :    "))
            print("\nAnda ingin Mengubah Harga Fresh Drink :  ", end="")
            print(daftarFreshDrink[ubahMinum-1])
            print("Harga Sebelumnya :  ", daftarHargaFreshDrink[ubahMinum-1], "\n\n")
            
            ubahHargaMinum = int(input("Masukkan Harga Baru Fresh Drink :    "))
            daftarHargaFreshDrink[ubahMinum-1] = ubahHargaMinum

            print("Berhasil!...")
            welcome()

            
        if pil3 == "3":
            for i in range(len(daftarMilk)):
                print(f"{i+1}. {daftarMilk[i]}")

            ubahMinum = int(input("Masukkan ID Milk :    "))
            print("\nAnda ingin Mengubah Harga Milk :  ", end="")
            print(daftarMilk[ubahMinum-1])
            print("Harga Sebelumnya :  ", daftarHargaMilk[ubahMinum-1], "\n\n")
            
            ubahHargaMinum = int(input("Masukkan Harga Baru Milk :    "))
            daftarHargaMilk[ubahMinum-1] = ubahHargaMinum

            print("Berhasil!...")
            welcome()



def menu():
    clear_screen()
    print("         ---Pilih Jenis Minuman---        ")
    print("1. Kopi                                   ")
    print("2. Fresh Drink                            ")
    print("3. Milk                                   ")
    
    pilih = int(input("\nPilih Menu : "))
    
    if pilih == int('1'):
        Coffee()
    elif pilih == int('2'):
        FreshDrink()
    elif pilih == int('3'):
        Milk()
    elif pilih == int('0'):
        exit()
    else:
        print("Pilihan menu tidak ada! harap masukkan dengan benar")
        time.sleep(1)
        menu()             



def Coffee():
    clear_screen()
    jenis.append("Coffee")
    for i in range(len(daftarKopi)):
        print(f"{i+1}. Kopi {daftarKopi[i]}")

    pil = int(input("Pilih Kopi yang anda inginkan : "))
    
    clear_screen()
    print("Atas nama : ", name[0])
    print ("="*25)
    print(f"        Kopi {daftarKopi[pil-1]}        ")
    print(f"     Harga : Rp. {daftarHargaKopi[pil-1]}    ")
    print ("-"*25)
    print("Sukses")
    kopi[len(kopi)+1] = daftarKopi[pil-1]
    harga_kopi.append(daftarHargaKopi[pil-1])
    nanya()
    print("\n")




def FreshDrink():
    clear_screen()
    jenis.append("Fresh Drink")
    
    jenis.append("Coffee")
    for i in range(len(daftarFreshDrink)):
        print(f"{i+1}.  {daftarFreshDrink[i]}")

    pil = int(input("Pilih Fresh Drink yang anda inginkan : "))
    
    clear_screen()
    print("Atas nama : ", name[0])
    print ("="*25)
    print(f"         {daftarFreshDrink[pil-1]}        ")
    print(f"     Harga : Rp. {daftarHargaFreshDrink[pil-1]}    ")
    print ("-"*25)
    print("Sukses")
    fd[len(kopi)+1] = daftarFreshDrink[pil-1]
    harga_fd.append(daftarHargaFreshDrink[pil-1])
    nanya()
    print("\n")


def Milk():
    clear_screen()
    jenis.append("Milk")
    for i in range(len(daftarMilk)):
        print(f"{i+1}. {daftarMilk[i]}")

    pil = int(input("Pilih Milk yang anda inginkan : "))
    
    clear_screen()
    print("Atas nama : ", name[0])
    print ("="*25)
    print(f"        {daftarMilk[pil-1]}        ")
    print(f"     Harga : Rp. {daftarHargaMilk[pil-1]}    ")
    print ("-"*25)
    print("Sukses")
    milk[len(kopi)+1] = daftarMilk[pil-1]
    harga_milk.append(daftarHargaMilk[pil-1])
    nanya()
    print("\n")




def nanya():
    jawab = str(input("Apakah Anda ingin membeli yang lain? y/n : ")) 
    if jawab == str('y'):
        clear_screen()
        menu()
    if jawab == str('n'):
        clear_screen()
        bayar()
        terima_kasih()

# def nanya1():
#     jawab = str(input("Apakah Anda ingin membeli yang lain? y/n : ")) 
#     if jawab == str('y'):
#         clear_screen()
#         menu()
#     if jawab == str('n'):
#         clear_screen()
#         bayar()
#         terima_kasih()

# def nanya2():
#     jawab = str(input("Apakah Anda ingin membeli yang lain? y/n : ")) 
#     if jawab == str('y'):
#         clear_screen()
#         menu()
#     if jawab == str('n'):
#         clear_screen()
#         bayar()
#         terima_kasih()




def terima_kasih():
    print("           ---Terima Kasih!---             ")
    print(" Silahkan Datang Kembali di lain waktu yaa ")
    print("-------------------------------------------")



def back_to_menu():
    input("Tekan Enter untuk kembali...")
    menu()  
    
def bayar():
    clear_screen
    hasil = total(harga_fd, harga_kopi, harga_milk)
    print ("="*47)
    print ("                  KOPI CHUSEYO                  ")
    print ("-"*47)
    print ("| NO |   KETERANGAN   | PEMBELIAN |    TOTAL    ")
    print ("-"*47)
    print ("| 1. | KOPI           | {} CUP      Rp.{}     ".format(len(kopi),sum(harga_kopi)))
    print ("| 2. | FRESH DRINK    | {} CUP      Rp.{}     ".format(len(fd),sum(harga_fd)))
    print ("| 3. | MILK           | {} CUP      Rp.{}     ".format(len(milk),sum(harga_milk)))
    print ("-"*47)
    print ("| +  |            TOTAL           |   Rp.{}  ".format(hasil))
    print ("="*47)
    print ("\n") 
    uangtidakcukup = True
    while(uangtidakcukup):
        try:
            uang = int(input("Masukkan nominal uang anda  :   RP."))
            if uang > hasil:
                print ("Kembalian", uang - hasil)
                uangtidakcukup =  False
            elif uang == hasil:
                print("Uang Anda Pas")
                uangtidakcukup = False
            else:
                print("Uang Anda Tidak Cukup")
        except ValueError:
            print("Input anda salah, Masukkan angka yang benar")
            time.sleep(2)
            bayar()


def total (a, b, c):
    x = sum (a)
    y = sum (b)
    z = sum (c)
    hasil = x + y + z
    return hasil

welcome()