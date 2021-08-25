from tkinter import *
from PyQt5 import QtWidgets, uic
import sys



root = Tk()
root.geometry("1000x800")
root.title(" TOKO PANCING ")
  


barang = ["Rocket", "Bamboo", "Mirai Nikki", "Golden"]
harga = [80000, 70000, 75000, 130000]


# def asc(num): 
#     n = len(num)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if num[j] > num[j+1] :
#                 num[j], num[j+1] = num[j+1], num[j]
#     print(num)
#     print("\nOK\n\n\n")
#     input("Klik Apapun untuk kembali ke Menu...")
#     return num



def underScore (i, barang, harga):
    a = "[" + str(i+1) + "]" +  barang
    a = a.replace(" ", "_")
    minus = 32 - len(str(harga))  - len(a)
    for j in range(minus) :
        a += "_"
    result = a, "Rp.", harga
    return result
    

def daftarBarang() :
    daftarBarangWindow = Toplevel(root)
    daftarBarangWindow.geometry("400x700")
    daftarBarangWindow.title("Daftar Barang")
    for i in range(len(barang)) : 
        # items = "[", i+1, "]",  barang[i], "________________Rp." , harga[i]
        items = underScore(i, barang[i], harga[i])

        label = Label(daftarBarangWindow, text = items)
        label.pack()
        label.place(x=5,y= 5+(i*30))
        label.config(font =("Arial", 13))
    






# TEXT   
def brand():
    return Label(text = "SELAMAT DATANG !\n", justify=CENTER)


def menu() : 
    return Label( text = "Fitur : \n1. Pembayaran" + 
    "\n2. Lihat Daftar Barang" + 
    "\n3. Lihat Barang Yang Masih Tersedia" +
    "\n4. Lihat Barang Yang Kehabisan STOK" +
    "\n5. Tambahkan Barang" +
    "\n6. Ubah Harga Barang" +
    "\n7. Hapus Barang" +
    "\n8. Cari Barang" +       
    "\n9. Urutkan Barang\n", justify=LEFT )

    

brand = brand()
brand.pack()  
brand.config(font =("Arial", 18))



menu = menu()
menu.place(x=0 ,y=50)
menu.config(font =("Arial", 13))



# BUTTON
pembayaran = Button(root, height = 2,
                 width = 25, 
                 text ="Pembayaran")
daftarBarang = Button(root, height = 2,
                 width = 25, 
                 text ="Daftar Barang",
                 command = daftarBarang) 
barangTersedia = Button(root, height = 2,
                 width = 25, 
                 text ="Barang Tersedia")
barangKosong = Button(root, height = 2,
                 width = 25, 
                 text ="Barang Tidak Tersedia")
tambahBarang = Button(root, height = 2,
                 width = 25, 
                 text ="Tambah Barang")
updateHarga = Button(root, height = 2,
                 width = 25, 
                 text ="Update Harga Barang")
hapusBarang = Button(root, height = 2,
                 width = 25, 
                 text ="Hapus Barang")
urutkanBarang = Button(root, height = 2,
                 width = 25, 
                 text ="Urutkan Barang")



pembayaran.place(x=0, y=300)
daftarBarang.place(x=0, y=370)
barangTersedia.place(x=0, y=440)
barangKosong.place(x=200, y=440)
tambahBarang.place(x=0, y=510)
updateHarga.place(x=200, y=510)
hapusBarang.place(x=400, y=510)
urutkanBarang.place(x=600, y=510)



# INPUT
inputtxt = Text(root, height = 1,
                 width = 25, bg = "white")
Display = Button(root, height = 1,
                 width = 4, 
                 text ="Cari !")



inputtxt.pack()
Display.pack()
mainloop()