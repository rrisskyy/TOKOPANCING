
import os
import time



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# judulgame rilis pengembang penerbit platform
# Python program for implementation of Bubble Sort



game = [
    ['Maquette', '2 Maret 2021', 'Graceful Decay', 'Anapurna Interactive', 'PS4, PS5, Windows'], 
    ['Harvest Moon: One World', '1 April 2021', 'APPCI', 'Natsume', 'PS4, Xbox One, Nintendo Switch'],
    ['It Takes Two', '27 Maret 2021', 'Hazelight', 'EA',  'Xbox One, PS4, Xbox Series X/S, PS5, Windows']
    ]




# judulGame = ['Maquette','Harvest Moon: One World','It Takes Two','Resident Evil Village','Deathloop']
# rilis = ['2 Maret 2021', '2 Maret 2021', '27 Maret 2021', '7 Mei 2021', '21 Mei 2021']
# pengembang = ['Graceful Decay','APPCI','Hazelight','Capcom','Arkane Studios']
# penerbit = ['Anapurna Interactive','Natsume','EA','Capcom','Bethesda Softworks']
# platform = ['PS4, PS5, Windows', 'PS4, Xbox One, Nintendo Switch', 'Xbox One, PS4, Xbox Series X/S, PS5, Windows', 
# 'Xbox One, PS4, Xbox Series X/S, PS5, Windows', 'Windows, PS5']




gameSteam = {

    1: {
        'Judul Game': 'ARK: Survival Evolved',
        'Harga': 'dari Rp209.999 jadi Rp42.000'
    },
    2: {
        'Judul Game': 'Battlefield V',
        'Harga': 'dari Rp849.000 jadi Rp339.600'
    },
    3: {
        'Judul Game': 'Cities: Ckylines',
        'Harga': 'dari  Rp199.999 jadi Rp49.999'
    }, 
    4: {
        'Judul Game': 'Human: Fall Flat',
        'Harga': 'dari Rp115.999 jadi Rp46.399'
    },
    5: {
        'Judul Game': 'Naruto to Boruto: Shinobi Striker',
        'Harga': 'dari Rp559.000 jadi Rp88.000'
    }

} 




gameEpic = {
    
    1: {
        'Judul Game': 'Halcyon 6',
        'Harga': 'GRATIS'
    },
    2: {
        'Judul Game': 'Rayman Origins',
        'Harga': 'dari Rp58.174 jadi Rp17.350'
    },
    3: {
        'Judul Game': 'Anno 1800',
        'Harga': 'dari Rp830.914 jadi Rp415.384'
    },
    4: {
        'Judul Game': 'Shadowhand',
        'Harga': 'dari Rp87.334 jadi Rp69.838'
    },
    5: {
        'Judul Game': 'Spacebase Startopia',
        'Harga': 'dari Rp276.874 jadi Rp249.172'
    }

} 






gamePlaystation = {

    1: {
        'Judul Game': 'Assassin’s creed Valhalla',
        'Harga': 'dari Rp749.000 jadi Rp524.300',
    },
    2: {
        'Judul Game': 'Call of Duty: Modern Warfare',
        'Harga': 'dari Rp812.000 jadi Rp609.000'
    },
    3: {
        'Judul Game': 'Ghost of Tsushima',
        'Harga': 'dari Rp829.000 jadi Rp497.400'
    },
    4: {
        'Judul Game': 'JUMP FORCE',
        'Harga': 'dari Rp680.000 jadi Rp204.000'
    },
    5: {
        'Judul Game': 'Red Dead Redemption 2',
        'Harga': 'dari Rp740.000 jadi Rp370.000'
    }
    
} 






def melihat_data():
    clear_screen()
    print('\n')
    if len(game) <= 0:
        print ('Belum Ada data')
        show_menu()
    else:
        for i in range(len(game)):
            print(f'[{i + 1}]')
            print(f'Judul Game: {game[i][0]}')
            print(f'Rilis     : {game[i][1]}')
            print(f'Pengembang: {game[i][2]}')
            print(f'Penerbit  : {game[i][3]}')
            print(f'Platform  : {game[i][4]}')
            print('\n')
        




def menambah_data():
    clear_screen()

    game_baru = input('Judul game : ')
    rilis_game = input('Rilis: ')
    nama_pengembang = input('Pengembang: ')
    nama_penerbit = input('Penerbit: ')
    jenis_platform = input('Platform: ')

    game.append((game_baru, rilis_game, nama_pengembang, nama_penerbit, jenis_platform))
    result = "Berhasil!"
    return result


def menghapus_data():
    clear_screen()
    print ('\n')
    melihat_data()
    
    x = int(input('Inputkan angka game: '))
    if(x > len(game)):
        print ('ID salah')
        back_to_menu()
    else:
        del game[x-1]
    back_to_menu()
        




def ascBubbleSort(arr, pil):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j][pil] > arr[j+1][pil] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

def descBubbleSort(arr, pil):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j][pil] > arr[j+1][pil] :
				arr[j], arr[j+1] = arr[j+1], arr[j]




def ascSelectionSort(val, pil):
    clear_screen()
    print('')
    for x in range(len(val)-1,0,-1):
       Max=0
       for y in range(1,x+1):
           if val[y][pil] > val[Max][pil]:
               Max = y
 
       temp = val[x]
       val[x] = val[Max]
       val[Max] = temp

def descSelectionSort(val, pil):
    clear_screen()
    print('')
    for x in range(len(val)-1,0,-1):
       Max=0
       for y in range(1,x+1):
           if val[y][pil] < val[Max][pil]:
               Max = y
 
       temp = val[x]
       val[x] = val[Max]
       val[Max] = temp





'''
     for x in range(1,len(love)):
 
     valueaktif = love[x]
     posisi = x
 
     while posisi>0 and love[posisi-1]>valueaktif:
         love[posisi]=love[posisi-1]
         posisi = posisi-1
 
     love[posisi]=valueaktif
 '''

   
    



'''
def SelectionSort(val):
    clear_screen()
    for isi in range(len(val)-1,0,-1):
       Max=0
       for lokasi in range(1,isi+1):
           if val[lokasi]>val[Max]:
               Max = lokasi
 
       temp = val[isi]
       val[isi] = val[Max]
       val[Max] = temp
 
    SelectionSort(judulGame)
    print(judulGame)
    back_to_menu()        
'''



def mengubah_data():
    clear_screen()
    print('\n')
    melihat_data()
    
    x = int(input('Inputkan angka game: '))
    if(x > len(game)):
        print ('ID salah')
        back_to_menu()
    else:
        clear_screen()
        print(f'[1] Judul game : ', game[x-1][0])
        print(f'[2] Rilis : ', game[x-1][1])
        print(f'[3] Pengembang : ', game[x-1][2])
        print(f'[4] Penerbit : ', game[x-1][3])
        print(f'[5] Platform : ', game[x-1][4])


        print("\n\n\nPilih Data yang ingin anda Ubah!!\n")
        pil = int(input("Pilih Menu :    "))
        dataBaru = input("Masukkan Data :    ")
        game[x-1][pil-1] = dataBaru
        print("Berhasil!!")
    back_to_menu()




def steam():
    for x in range(len(gameSteam)):
        print('')
        print(f'[{x+1}]')
        
        print("Judul Game :  " + gameSteam[x+1]["Judul Game"])
        print("Harga      :  " + gameSteam[x+1]["Harga"])
    back_to_menu()


def epic_store():
    for x in range(len(gameEpic)):
        print('')
        print(f'[{x+1}]')
        
        print("Judul Game :  " + gameEpic[x+1]["Judul Game"])
        print("Harga      :  " + gameEpic[x+1]["Harga"])
    back_to_menu()



def playstation_store():
    for x in range(len(gamePlaystation)):
        print('')
        print(f'[{x+1}]')
        
        print("Judul Game :  " + gamePlaystation[x+1]["Judul Game"])
        print("Harga      :  " + gamePlaystation[x+1]["Harga"])
    back_to_menu()



def show_menu():
    clear_screen()
    print('')
    print('_'*44)
    print('-------------|Sistem Data Game|-------------')
    print('_'*44)
    print('[1] Melihat Data Game')
    print('[2] Menambah Data Game')
    print('[3] Menghapus Data Game')
    print('[4] Mengubah Data Game')
    print('[5] Diskon Game')
    print('[6] Sorting')
    print('[0] Keluar')
    selected_menu = input('Pilih menu> ')


    if(selected_menu == '1'):
        melihat_data()
        back_to_menu()
    elif(selected_menu == '2'):
        result = menambah_data()
        print(result)
        back_to_menu()
    elif(selected_menu == '3'):
        menghapus_data()
    elif(selected_menu == '4'):
        mengubah_data()
    elif(selected_menu == '5'):
        clear_screen()
        print('')
        print("---------- (Diskon Game) ----------")
        print("[1] Steam")
        print("[2] Epic Games Store")
        print("[3] Playstation Store")
        print("[4] Back")
        print("[0] Exit")
        selected_menu = input("Pilih menu> ")
        if(selected_menu == "1"):
            steam()
        elif(selected_menu == "2"):
            epic_store()
        elif(selected_menu == "3"):
            playstation_store()
        elif(selected_menu == "4"):
            show_menu()
        elif(selected_menu == "0"):
            close_app()
        else:
            print("Kamu memilih menu yang salah!")
            back_to_menu()

    elif(selected_menu == '6'):
        clear_screen()
        print('')
        print("---------- (Urutkan Data Berdasarkan) ----------")
        print("[1] Judul Game")
        print("[2] Rilis")
        print("[3] Pengembang")
        print("[4] Penerbit")
        print("[5] Platform")
        print("[6] Back")
        print("[0] Exit")
        
        selected_menu = input("Pilih menu> ")
        # selected_menu = 1
        
        clear_screen()
        print('')
        print("[1] Ascending")
        print("[2] Descending")
        print("[3] Back")
        print("[0] Exit")

        selected_menu1 = input("Pilih menu> ")
        # selected_menu1 = 2


        if(selected_menu1 == "1"):
            ascBubbleSort(game, int(selected_menu)-1)
            melihat_data()
            back_to_menu()

        elif(selected_menu1 == "2"):
            descSelectionSort(game, int(selected_menu)-1)   
            melihat_data()
            # for i in range(len(game)):
            #     print(game[i])
            back_to_menu()
        
        elif(selected_menu1 == "3"):
            show_menu()
        elif(selected_menu1 == "0"):
            close_app()
    elif(selected_menu1 == '0'):
        close_app()
    else:
        print('Kamu memilih menu yang salah!')
        back_to_menu()


def back_to_menu():
    print('\n')
    input('Tekan Enter untuk kembali...')
    show_menu()


def close_app():
    clear_screen()
    print('')
    print('='*44)
    print('\t\tSelamat Berkunjung Kembali :)')
    print('='*44)
    time.sleep(3)
    exit()


show_menu()

