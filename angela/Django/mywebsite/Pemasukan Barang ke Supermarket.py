import os
import time

data_nama = ["admin"]
data_pw = ["admin"]
login = 0
b = 3


barang = ["Soun Naga","Spaghetti","Ligo Havermout","Honic Makaroni","Honic Maizenaku","Kecap Anggur"]
stok = [20,40,100,90,150,20]
harga = [7800,15000,29000,8500,5000,22000]
pesanan = []
kembali = []
data1 = {"Nama Supermarket":"Borma Parahyangan",
        "Alamat Supermarket":"Padalarang",
        "Staff":"Aep Saefulloh",
        "Nomor hp":"085624613983",
        }
data2 = {"Nama Supermarket":"Borma Manglayang",
        "Alamat Supermarket":"Cibiru",
        "Staff":"Asep Sutisna",
        "Nomor hp":"0822120292621",
                }
data3 = {"Nama Supermarket":"Borma Jatinangor",
        "Alamat Supermarket":"Jatinangor",
        "Staff":"Endang ",
        "Nomor hp":"081396467660",
                }



while login == 0:
    nama = input("Silahkan masukkan ID : ")
    pw = input("Silahkan masukkan password : ")
    for i in range(len(data_nama)):
        if nama == data_nama[i] and pw == data_pw[i]:
            login = 1
        else:
            login = 0
    if login == 1:
        break
    else:
        b -= 1
        print("Anda Salah")

    if b == 0:
        print("Sudah 3x, Sistem Otomatis Berhenti")
        exit()

def clear_screen():
    os.system('cls')

def back_pilihan():
    print("\n")
    input("Tekan Enter Untuk Kembali...")
    menu()

def menu():
    clear_screen()
    print("============================================")
    print("=           DATA SUPLY BARANG              =")
    print("============U.D Aneka Favorites=============")
    print("============================================")
    print("= [1] Daftar, Stok, Harga Barang           =")
    print("= [2] Menambah Daftar, Stok, Harga Barang  =")
    print("= [3] Meupdate Daftar, Stok, Harga Barang  =")
    print("= [4] Menghapus Daftar, Stok, Harga Barang =")
    print("= [5] Mencari Harga Maximal dan Minimal    =")
    print("= [6] Menghitung Banyak Barang             =")
    print("= [7] Mengurutkan Daftar Barang            =")
    print("= [8] Membalikkan Daftar Barang            =")
    print("= [9] Data Barang Keluar                   =")
    print("= [10] Data Barang Return                  =")
    print("= [22] Kasir pembelian eceran              =")
    print("= [11] Data Informasi Supermarket          =")
    print("= [0] EXIT                                 =")
    print("============================================")
    pilihmenu = str(input("Silahkan pilih menu yang tersedia >> "))
    if(pilihmenu == "1"):
        daftar()
    elif(pilihmenu == "2"):
        add()
    elif(pilihmenu == "3"):
        update()
    elif(pilihmenu == "4"):
        delete()
    elif(pilihmenu == "5"):
        maxmin()
    elif(pilihmenu == "6"):
        banyak_barang()
    elif(pilihmenu == "7"):
        sorting()
    elif(pilihmenu == "8"):
        reverse_barang()
    elif(pilihmenu == "9"):
        data_keluar()
    elif(pilihmenu == "10"):
        data_return()
    elif(pilihmenu == "22"):
        kasir_eceran()
    elif(pilihmenu == "11"):
        info_super()
    elif(pilihmenu == "0"):
        print("Terimakasih sudah menggunakan Aplikasi ini..")
        print("\n")
        time.sleep(5)
        exit()
    else:
        print("Pilihan anda tidak ada di menu...")
        back_pilihan()

def daftar():
    print("===============================================")
    print("===Nama Barang\t\t===Stok Barang\t\t===Harga Barang===")
    for i in range(len(barang)):
        print ("[" , (i+1) , "]", barang[i], "\t:\t ", stok[i], "\t:\t Rp." , harga[i])
    back_pilihan()

def add():
    clear_screen()
    print("===========================================")
    print("=        Menambahkan dengan cara apa?     =")
    print("= [1] Menambahkan di akhir (append)       =")
    print("= [2] Menyisipkan (insert)                =")
    print("= [0] Kembali ke menu utama               =")
    print("===========================================")
    pilihcara = int(input("Pilih cara yang akan digunakan : "))
    if(pilihcara == 1):
        app()
    elif(pilihcara == 2):
        ins()
    elif(pilihcara == 0):
        back_pilihan()
    else:
        print("Pilihan anda tidak ada di menu..")
        input("Tekan ENTER untuk kembali!")
        add()
    
def app():
    print("===Nama Barang\t\t===Stok Barang\t\t===Harga Barang===")
    for i in range(len(barang)):
        print ("[" , (i+1) , "]", barang[i], "\t:\t ", stok[i], "\t:\t Rp." , harga[i])
    tambah = str(input("Masukkan Barang : "))
    price = int(input("Masukkan harga barang : "))
    persediaan = int(input("Masukkan stok barang : "))
    barang.append(tambah)
    harga.append(price)
    stok.append(persediaan)
    print(barang)
    print(harga)
    print(stok)
    pilihan=str(input("Apakah ingin melanjutkan menambah barang? y/n >> "))
    if(pilihan == "y"):
        app()
    elif(pilihan == "n"):
        add()

def ins():
    print("===Nama Barang\t\t===Stok Barang\t\t===Harga Barang===")
    for i in range(len(barang)):
        print ("[" , (i+1) , "]", barang[i], "\t:\t ", stok[i], "\t:\t Rp." , harga[i])
    instambah = str(input("Masukkan Barang : "))
    sisip = int(input("Mau disisipkan di urutan ke berapa ? > "))
    barang.insert(sisip, instambah)
    print(barang)
    stins = int(input("Masukkan jumlah stok : "))
    sisip3 = int(input("Masukkan sesuai dengan sisipan barang! > "))
    stok.insert(sisip3,stins)
    print(stok)
    priceins = int(input("Masukkan Harga Barang : "))
    sisip2 = int(input("Masukkan Sesuai dengan sisipan pada barang! > "))
    harga.insert(sisip2,priceins)
    print(harga)
    pilihan=str(input("Apakah ingin melanjutkan menambah barang? y/n >> "))
    if(pilihan == "y"):
        app()
    elif(pilihan == "n"):
        add()
        
def update():
    clear_screen()
    print("===Nama Barang\t\t===Stok Barang\t\t===Harga Barang===")
    for i in range(len(barang)):
        print ("[" , (i+1) , "]", barang[i], "\t:\t ", stok[i], "\t:\t Rp." , harga[i])
    index1 = int(input("Masukkan indeksnya : "))
    angka1 = str(input("Masukkan barang yang akan diubah : "))
    barang[index1] = angka1
    print("Nama-nama barang : ", barang)
    print("Barang telah berhasil diupdate!")
    index2 = int(input("Masukkan indeksnya : "))
    angka2 = int(input("Masukkan harga yang akan diubah : "))
    harga[index2] = angka2
    print(harga)
    print("Harga telah berhasil diupdate!")
    index3 = int(input("Masukkan indeksnya : "))
    angka3 = int(input("Masukkan stok yang akan diubah : "))
    stok[index3] = angka3
    print(stok)
    print("Stok telah berhasil diupdate!")
    pilihan=str(input("Apakah ingin melanjutkan menambah barang? y/n >> "))
    if(pilihan == "y"):
        update()
    elif(pilihan == "n"):
        menu()

def delete():
    clear_screen()
    print("===============================================================")
    print("=                  Menghapus dengan cara apa?                 =")
    print("= [1] Menghapus dengan mengetik nama barang (remove)          =")
    print("= [2] Menghapus dengan index yang dituju (pop)                =")
    print("= [3] Menghapus semua (clear)                                 =")
    print("= [0] Kembali ke menu utama                                   =")
    print("===============================================================")
    pilihcara = int(input("Pilih cara yang akan digunakan : "))
    if(pilihcara == 1):
        rmv()
    elif(pilihcara == 2):
        pp()
    elif(pilihcara == 3):
        cl()
    elif(pilihcara == 0):
        back_pilihan()
    else:
        print("Pilihan anda tidak ada di menu..")
        input("Tekan ENTER untuk kembali!")
        add()

def rmv():
    print("===Nama Barang\t\t===Stok Barang\t\t===Harga Barang===")
    for i in range(len(barang)):
        print ("[" , (i+1) , "]", barang[i], "\t:\t ", stok[i], "\t:\t Rp." , harga[i])
    rembarang = str(input("Masukkan Nama barang yang akan di hapus : "))
    barang.remove(rembarang)
    print("Barang telah berhasil dihapus!")
    remharga = int(input("Masukkan Harga barang yang akan di hapus : "))
    harga.remove(remharga)
    print("Harga barang telah berhasil dihapus!")
    remstok = int(input("Masukkan Stok barang yang akan di hapus : "))
    stok.remove(remstok)
    print("Stok barang telah berhasil dihapus!")
    pilihan=str(input("Apakah ingin melanjutkan menambah barang? y/n >> "))
    if(pilihan == "y"):
        rmv()
    elif(pilihan == "n"):
        delete()
        
def pp():
    print("===Nama Barang\t\t===Stok Barang\t\t===Harga Barang===")
    for i in range(len(barang)):
        print ("[" , (i+1) , "]", barang[i], "\t:\t ", stok[i], "\t:\t Rp." , harga[i])
    inbarang = int(input("Masukkan indeks Nama barang yang akan di hapus : "))
    barang.pop(inbarang)
    print("Barang telah berhasil dihapus!")
    inharga = int(input("Masukkan indeks Harga barang yang akan di hapus : "))
    harga.pop(inharga)
    print("Harga barang telah berhasil dihapus!")
    instok = int(input("Masukkan indeks Stok barang yang akan di hapus : "))
    stok.pop(instok)
    print("Stok barang telah berhasil dihapus!")
    pilihan=str(input("Apakah ingin melanjutkan menambah barang? y/n >> "))
    if(pilihan == "y"):
        pp()
    elif(pilihan == "n"):
        delete()

def cl():
    print("===Nama Barang\t\t===Stok Barang\t\t===Harga Barang===")
    for i in range(len(barang)):
        print ("[" , (i+1) , "]", barang[i], "\t:\t ", stok[i], "\t:\t Rp." , harga[i])
    barang.clear()
    harga.clear()
    stok.clear()
    print("Barang, Harga dan Stok telah di hapus semua!")
    pilihan=str(input("Apakah ingin melanjutkan menambah barang? y/n >> "))
    if(pilihan == "y"):
        cl()
    elif(pilihan == "n"):
        delete()
        
def maxmin():
    print("===Nama Barang\t\t===Stok Barang\t\t===Harga Barang===")
    for i in range(len(barang)):
        print ("[" , (i+1) , "]", barang[i], "\t:\t ", stok[i], "\t:\t Rp." , harga[i])
    maximal = max(harga)
    minimal = min(harga)
    print("Nilai Maximal pada harga : ", maximal)
    print("Nilai Minimal pada harga : ", minimal)
    maximal1 = max(stok)
    minimal1 = min(stok)
    print("Nilai Maximal pada stok : ", maximal1)
    print("Nilai Minimal pada stok : ", minimal1)
    pilihan=str(input("Apakah ingin melanjutkan menambah barang? y/n >> "))
    if(pilihan == "y"):
        maxmin()
    elif(pilihan == "n"):
        menu()

def banyak_barang():
    print("===Nama Barang\t\t===Stok Barang\t\t===Harga Barang===")
    for i in range(len(barang)):
        print ("[" , (i+1) , "]", barang[i], "\t:\t ", stok[i], "\t:\t Rp." , harga[i])
    print("\nBanyaknya Produk (Barang) : ")
    print(len(barang))
    back_pilihan()
    
def sorting():
    clear_screen()
    print("===============================================================")
    print("=                  Mensorting dengan cara apa?                =")
    print("= [1] Cara Ascending                                          =")
    print("= [2] Cara Descending                                         =")
    print("= [0] Kembali ke menu utama                                   =")
    print("===============================================================")
    pilihcara = int(input("Pilih cara yang akan digunakan : "))
    if(pilihcara == 1):
        size = len(barang)
        shellSort(barang, size)
        print('Sorted Array in Ascending Order:')
        print(barang)
        shellSort(barang,size)
        
    elif(pilihcara == 2):
        desc()
    elif(pilihcara == 0):
        menu()

def shellSort(array, n):
    
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2
        

def desc():
    barang.sort(reverse=True)
    print("Barang terurut secara Ascending : ", barang)
    harga.sort(reverse=True)
    print("Harga terurut secara Ascending : ", harga)
    stok.sort(reverse=True)
    print("Stok terurut secara Ascending : ", stok)
    pilihan=str(input("Apakah ingin melanjutkan menambah barang? y/n >> "))
    if(pilihan == "y"):
        asc()
    elif(pilihan == "n"):
        sorting()

def reverse_barang():
    print("= [1] Membalikkan Data Barang =")
    print("= [2] Membalikkan Data Harga =")
    print("= [3] Membalikkan Data Stok =")
    pilgan = int(input("Masukkan Data apa yang akan di balikkan : "))
    if(pilgan == 1):
        barang.reverse()
        print(barang)
        print("Barang telah di Reverse!")
        pilihan0=str(input("Apakah ingin melanjutkan menambah barang? y/n >> "))
        if(pilihan0 == "y"):
            reverse_barang()
        elif(pilihan0 == "n"):
            menu()
    elif(pilgan == 2):
        harga.reverse()
        print(harga)
        print("Harga telah di Reverse!")
        pilihan1=str(input("Apakah ingin melanjutkan menambah barang? y/n >> "))
        if(pilihan1 == "y"):
            reverse_barang()
        elif(pilihan1 == "n"):
            menu()
    elif(pilgan == 3):
        stok.reverse()
        print(stok)
        print("Stok telah di Reverse!")
        pilihan2=str(input("Apakah ingin melanjutkan menambah barang? y/n >> "))
        if(pilihan2 == "y"):
            reverse_barang()
        elif(pilihan2 == "n"):
            menu()
    else:
        print("Maaf tidak tersedia dimenu")
        back_pilihan()
    
def data_keluar():
    total = 0
    print("=             Data Penjualanan             =")
    print("********************************************")
    namatoko = str(input("Masukkan Nama Toko : "))
    alamattoko = str(input("Masukkan Alamat Toko : "))
    tanggal = str(input("Masukkan tanggal pengiriman barang : "))
    for i in range(len(barang)):
        pesan = int(input("Pesan berapa " + barang[i] + "\t:\t"))
        pesanan.append(pesan)
        print("Total: ", harga[i], " x ", pesan, " = Rp. ", pesan * harga[i])
        total += harga[i] * pesan
        print("Tagihan: Rp.", total)
    print("\n")
    print("=======================================================")
    print("=                      S T R U K                      =")
    print("=======================================================")
    print("Toko : ", namatoko)
    print("Alamat : ", alamattoko)
    print("Tanggal pengiriman : ", tanggal)
    print("Produk yang dibeli : ",barang)
    print("Jumlah yang dibeli : ",pesanan)
    print("Total Tagihan : Rp.", total)
    pilihan=str(input("Apakah ingin mengulang? y/n >> "))
    if(pilihan == "y"):
        data_keluar()
    else:
        print("Terima kasih, anda kembali ke menu..")
        menu()

def data_return():
    total1 = 0
    print("=                Data Return               =")
    print("********************************************")
    namatoko = str(input("Masukkan Nama Toko : "))
    alamattoko = str(input("Masukkan Alamat Toko : "))
    tanggal = str(input("Masukkan tanggal pengiriman barang : "))
    tanggal1 = str(input("Masukkan tanggal return barang : "))
    for i in range(len(barang)):
        kem = int(input("Jumlah return barang " + barang[i] + "\t:\t"))
        kembali.append(kem)
        print("Total: ", harga[i], " x ", kem, " = Rp. ", kem * harga[i])
        total1 += harga[i] * kem
        print("Total barang yang di return : Rp.", total1)
    print("\n")
    print("=======================================================")
    print("=                    CATATAN RETURN                   =")
    print("=======================================================")
    print("Toko : ", namatoko)
    print("Alamat : ", alamattoko)
    print("Tanggal pengiriman : ", tanggal)
    print("Tanggal return : ", tanggal1)
    print("Produk yang di return : ",barang)
    print("Jumlah yang di return : ",kembali)
    print("Total Return : Rp.", total1)
    pilihan=str(input("Apakah ingin mengulang? y/n >> "))
    if(pilihan == "y"):
        data_return()
    else:
        print("Terima kasih, anda kembali ke menu..")
        menu()



def kasir_eceran():
    for i in range(len(barang)):
        print ("[" , (i+1) , "]", barang[i], "\t:\t ", stok[i], "\t:\t Rp." , harga[i])
    print("===============================================")
    nama = str (input("Masukkan Nama Produk              : "))
    print("===============================================")
    hargaa= int(input("Masukkan harga barang             :"))
    jumlah= int(input("Masukan jumlah Produk yang dibeli  : "))
    print("===============================================")
    Total= totalan(jumlah, hargaa)
    print("Yang harus dibayar                 : Rp", Total)
    print("===============================================")
    Bayar=int(input("Pembayaran                         : Rp " ))
    Kembalian= (Bayar-Total)
    print("===============================================")

    clear_screen()
    print("\n===========================================")
    print("======= S T R U K   P E M B E L I A N =====")
    print("\n===========================================")
    print(" Produk      :",nama)
    print(" Tagihan     : Rp",Total)
    print(" Uang        : Rp",Bayar)
    print(" Kembalian   : Rp",Kembalian)
    print("===========================================")
    print("===========================================")
    back_pilihan()
    
def totalan(harbag, jumlah):
    total = harbag * jumlah
    return total

def info_super():
    clear_screen()
    print("\n=============================================")
    print("==============INFORMASI PASAR================")
    print("= [1] Data Supermarket                      =")
    print("= [2] Menambahkan Data Supermarket          =")
    print("= [3] Mengupdate Data Supermarket           =")
    print("= [4] Menghapus Data Supermarket            =")
    print("= [0] Kembali ke Menu Utama                 =")
    pilihinfo = int(input("Pilih menu yang tersedia >> "))
    if(pilihinfo == 1):
        print("==================== DATA SUPERMARKET ====================")
        print("= [1] DATA 1 =")
        for key, value in data1.items():
            print(key, " = ", value)
        print("\n")
        
        print("= [2] DATA 2 =")
        for key, value in data2.items():
            print(key, " = ", value)
        print("\n")
        
        print("= [3] DATA 3 =")
        for key, value in data3.items():
            print(key, " = ", value)
        print("\n")
        input("Tekan ENTER untuk kembali...")
        info_super()
    
    elif(pilihinfo == 2):
        print("================= MENAMBAH DATA SUPERMARKET ==================")
        print("= [1] Data Supermarket 1                                     =")
        print("= [2] Data Supermarket 2                                     =")
        print("= [3] Data Supermarket 3                                     =")
        pilihinfo0 = int(input("Masukkan menu yang dipilih >> "))
        if(pilihinfo0 == 1):
            data1['Second Staff'] = str(input("Masukkan Nama Staff Cadangan >> "))
            data1['Nomor Hp Second Staff']=str(input("Masukkan No hp Staff Cadangan >> "))
            print("Berhasil ditambahkan!")
            input("Tekan Enter untuk kembali!")
            info_super()
        elif(pilihinfo0 == 2):
            data2['Second Staff'] = str(input("Masukkan Nama Staff Cadangan >> "))
            data2['Nomor Hp Second Staff']=str(input("Masukkan No hp Staff Cadangan >> "))
            print("Berhasil ditambahkan!")
            input("Tekan Enter untuk kembali!")
            info_super()
        elif(pilihinfo0 == 3):
            data3['Second Staff'] = str(input("Masukkan Nama Staff Cadangan >> "))
            data3['Nomor Hp Second Staff']=str(input("Masukkan No hp Staff Cadangan >> "))
            print("Berhasil ditambahkan!")
            input("Tekan Enter untuk kembali!")
            info_super()
        else:
            back_pilihan()
    elif(pilihinfo == 3):
        print("================ MENGUPDATE DATA SUPERMARKET =================")
        print("= [1] Data Supermarket 1                                     =")
        print("= [2] Data Supermarket 2                                     =")
        print("= [3] Data Supermarket 3                                     =")
        pilihinfo1 = int(input("Masukkan menu yang dipilih >> "))
        if(pilihinfo1 == 1):
            datasp1()
        elif(pilihinfo1 == 2):
            datasp2()
        elif(pilihinfo1 == 3):
            datasp3()
        else:
            back_pilihan()
    elif(pilihinfo == 4):
        print("================= MENGHAPUS DATA SUPERMARKET =================")
        print("= [1] Data Supermarket 1                                     =")
        print("= [2] Data Supermarket 2                                     =")
        print("= [3] Data Supermarket 3                                     =")
        pilihinfo2 = int(input("Masukkan menu yang dipilih >> "))
        if(pilihinfo2 == 1):
            print("================= METODE HAPUS =================")
            print("= [1] POP                                      =")
            print("= [2] CLEAR                                    =")
            pilihlagi = int(input("Pilih metode >> "))
            if(pilihlagi == 1):
                hapusdata1 = str(input("Masukkan KEY yang akan di hapus > "))
                data1.pop(hapusdata1)
                print("Berhasil di hapus!!")
                input("\nTekan Enter untuk kembali...........")
                info_super()
            elif(pilihlagi == 2):
                data1.clear()
                print("Berhasil di hapus!!")
                input("\nTekan Enter untuk kembali.........")
                info_super()
        elif(pilihinfo2 == 2):
            print("================= METODE HAPUS =================")
            print("= [1] POP                                      =")
            print("= [2] CLEAR                                    =")
            pilihlagi1 = int(input("Pilih metode >> "))
            if(pilihlagi1 == 1):
                hapusdata2 = str(input("Masukkan KEY yang akan di hapus > "))
                data2.pop(hapusdata2)
                print("Berhasil di hapus!!!")
                input("\nTekan Enter untuk kembali...........")
                info_super()
            elif(pilihlagi1 == 2):
                data2.clear()
                print("Berhasil di hapus!!")
                input("\nTekan Enter untuk kembali..........")
                info_super()
        elif(pilihinfo2 == 3 ):
            print("================= METODE HAPUS =================")
            print("= [1] POP                                      =")
            print("= [2] CLEAR                                    =")
            pilihlagi2 = int(input("Pilih metode >> "))
            if(pilihlagi2 == 1):
                hapusdata3 = str(input("Masukkan KEY yang akan di hapus > "))
                data3.pop(hapusdata3)
                print("Berhasil di hapus!!!!!")
                input("\nTekan Enter untuk kembali...........")
                info_super()
            elif(pilihlagi2 == 2):
                data3.clear()
                print("Berhasil di hapus!!")
                input("\nTekan Enter untuk kembali..........")
                info_super()
        else:
            back_pilihan()
    elif(pilihinfo == 0):
        back_pilihan()

def datasp1():
    data1['Nama Supermarket']=str(input("Masukkan Nama Supermarket : "))
    data1['Alamat Supermarket']=str(input("Masukkan Alamat Supermarket : "))
    data1['Staff']=str(input("Masukkan Nama Staff Supermarket : "))
    data1['Nomor hp']=str(input("Masukkan Nomor hp Staff : "))
    print("Berhasil diupdate!")
    print(data1)
    input("Tekan Enter untuk kembali..")
    info_super()

def datasp2():
    data2['Nama Supermarket']=str(input("Masukkan Nama Supermarket : "))
    data2['Alamat Supermarket']=str(input("Masukkan Alamat Supermarket : "))
    data2['Staff']=str(input("Masukkan Nama Staff Supermarket : "))
    data2['Nomor hp']=str(input("Masukkan Nomor hp Staff : "))
    print("Berhasil diupdate!")
    print(data2)
    input("Tekan Enter untuk kembali..")
    info_super()

def datasp3():
    data3['Nama Supermarket']=str(input("Masukkan Nama Supermarket : "))
    data3['Alamat Supermarket']=str(input("Masukkan Alamat Supermarket : "))
    data3['Staff']=str(input("Masukkan Nama Staff Supermarket : "))
    data3['Nomor hp']=str(input("Masukkan Nomor hp Staff : "))
    print("Berhasil diupdate!")
    print(data3)
    input("Tekan Enter untuk kembali..")
    info_super()

menu()