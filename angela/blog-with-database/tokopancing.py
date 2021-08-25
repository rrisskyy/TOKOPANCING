import os
def clr():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')


clr()
print("\n\n\t  SELAMAT DATANG DI TOKO PANCING")
print("//=====================================================\\\\")
print("||   1. Pembayaran                                     ||")      # ✔
print("||   2. Lihat Daftar Barang                            ||")      # ✔
print("||   3. Lihat Barang Yang Masih Tersedia               ||")      # ✔
print("||   4. Lihat Barang Yang Kehabisan STOK               ||")      # ✔
print("||   5. Tambahkan Barang                               ||")      # ✔
print("||   6. Ubah Harga Barang                              ||")      # ✔
print("||   7. Hapus Barang                                   ||")      # ✔
print("||   8. Cari Barang                                    ||")      
print("||   9. Urutkan Barang                                 ||")         
print("||   0. Exit                                           ||")      
print("\\\\=====================================================//\n")
pil = input("Pilih Menu >>  ")

