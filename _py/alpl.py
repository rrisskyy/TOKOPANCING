# baris = int(input("Input baris matriks:"))
# kolom =  int(input("Input kolom matriks:"))
# A = []

# for i in range (baris):
#     for j in range(kolom):
#         A.append(int(input(f"Masukkan angka baris ke ke-{i} kolom ke-{j}:    ")))


# print(A)

import sys, os
import numpy as np
import matplotlib.pyplot as plt
import pprint
import scipy
import scipy.linalg  



os.system('color 0f')

temp = []

def clr():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

def underScore():
    return "\n_______________________________________________________________________"

def printMatrix(a, n):
    for i in range(n):
        print("\t", end="")
        for j in range(n):
            print(round(a[i][j], 2), "\t", end="")
        print()
    print("\n")




def printMatrixResult(a, n):
    for i in range(n):
        print("\t", end="")
        for j in range(n+1):
            print(round(a[i][j], 2), "\t", end="")
            if (j == n-1):
                print("|", end=" ")
        print()
    print("\n")




def gauss(a, n):
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Mengandung Pembagian Terhadap Nol!')

        for j in range(i+1, n):
            ratio = a[j][i] / a[i][i]        
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
    # Back Substitution
    x[n-1] = a[n-1][n] / a[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j] * x[j]
        x[i] = x[i] / a[i][i]
    return x


        

def GaussJordan(a, n):
    flag = 0
    for i in range(n):
        if (a[i][i] == 0):
            c = 1;
            while ((i + c) < n and a[i + c][i] == 0):
                c+=1;            
            if ((i + c) == n):
                flag = 1;
                break
            j=i
            for k in range(n+1):
                a[j][k], a[j+c][k] = a[j+c][k], a[j][k]
  
        for j in range(n):
              
            if (i != j) :    
                pro = a[j][i] / a[i][i];
                for k in range(n+1):                 
                    a[j][k] = a[j][k] - (a[i][k]) * pro             
    return flag




def PrintResult(a, n, flag):
    if (flag == 2):     
     print("    Infinite Solutions Exists")
    elif (flag == 3):
      print("   No Solution Exists")
    else:
        print("Maka Vector (x) :   \n")
        for i in range(n):     
            x[i] = a[i][n] / a[i][i]
            print("\t", round(x[i], 2))    
        return x 
  



def CheckConsistency(a, n, flag):      
    flag = 3
    for i in range(n-1):
        sum = 0
        for j in range(n):      
            sum = sum + a[i][j]
            if (sum == a[i][j]):
                flag = 2
    return flag




while(True):
    clr()
    print("\n//＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\\\\")
    print("||                                                                                      ||")
    print("||                                                                                      ||")
    print("||       1.  Metode Eliminasi Gauss                                                     ||")        # ✔
    print("||                                                                                      ||")      
    print("||       2.  Metode Eliminasi Gauss-Jordan                                              ||")        # ✔
    print("||                                                                                      ||")     
    print("||       3.  Metode Matriks Balikan                                                     ||")        # ✔
    print("||                                                                                      ||")      
    print("||       4.  Metode Dekomposisi LU                                                      ||")        # ✔
    print("||                                                                                      ||")      
    print("||       0.  Keluar                                                                     ||")      
    print("||                                                                                      ||")      
    print("||                                                                                      ||")      
    print("\\\\＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝//\n")
    pil = input("Pilih Menu >>  ")

    
    clr()
    if (pil == '1' or pil == '2' or pil == '3' or pil == '4'):
        if pil == "1":
            print("\nMetode Eliminasi Gauss")
        elif pil == "2": 
            print("\nMetode Gauss-Jordan")
        elif pil == "3":
            print("\nMetode Matriks Balikan")
        elif pil == "4":
            print("\nMetode Dekomposisi LU")
        n = 0
        print("\n\n+                                                                +")
        print("|  a11     a12     a13     ...     a1n  |  |  x1  |       |  b1  |")
        print("|  a21     a22     a23     ...     a2n  |  |  x2  |   ＝  |  b2  |")
        print("|   :       :       :       :       :   |  |  :   |       |   :  |")
        print("|  am1     am2     am3     ...     amn  |  |  x3  |       |  bm  |")
        print("+                                                                +")
        n = int(input('\n\n Berapa Variabel ?    : '))

        A = np.zeros((n, n))
        a = np.zeros((n, n))
        invA = np.zeros((n, n))
        x = np.zeros((n))
        b = []

        

        print("\n\n\nMulai Menghitung ...")
        print(underScore())
        print(f"Silahkan Masukkan Elemen Matriks A({n} x {n})")
        print("Masukkan Elemen dan pisah dengan Tab, dan Tekan Enter Untuk Baris Baru!\n\nContoh Inputan:\n")
        print(">>>\ta11\ta12\ta13\t...\ta1n")
        print(">>>\ta21\ta22\ta23\t...\ta2n ")
        print(">>>\t :\t :\t :\t :\t :")
        print(">>>\tam1\tam2\tam3\t...\tamn \n\n")
        print("Input (A): \n")
        for i in range(n):
            print(">>>\t", end="")
            addList = filter(None, input().split("\t"))
            addList = list(map(float, addList))  
            temp.append(addList)
        A = temp.copy()
        temp.clear()
        print(underScore())


        print("Silahkan Masukkan Elemen Vektor B")
        print("Masukkan Elemen dan pisah dengan Tab, dan Tekan Enter Untuk Baris Baru!\n\nContoh Inputan:\n")
        print(">>>\tb1\tb2\tb3\t...\tbn\n\n")
        print("Input (b): \n")
        print(">>>\t", end="")

        addList = filter(None, input().split("\t"))
        addList = list(map(float, addList)) 
        temp.append(addList) 
        b = temp.copy()
        temp.clear()
        print(underScore())
        
        for i in range(n):
            for j in range (n):
                a[i][j] = A[i][j]
            A[i].append(b[0][i])




# gauss
# =====================================================================================================================



    if (pil == '1'):
        print("\n\n\nMatriks (A) Anda :   \n")
        printMatrix(A, n)
        print("Vector (b) Anda :   \n")
        for i in range(n):
            print("\t", round(b[0][i], 2))
    
        x = gauss(A, n)
        
        print("\n\nAugumented Matrix Akhir Adalah : \n")
        printMatrixResult(A, n);
        print()

        print('\n\nMaka Vector (x) :  \n')
        for i in range(n):
            print("\t", round(x[i], 2))          

        print('\n\nSolusi Yang Dicari Adalah :  \n\n')
        for i in range(n):
            print('x%d = %0.2f' %(i+1,round(x[i], 2)), end = '\t')
        print("\n\n\n")

        input("Tekan Enter untuk Kembali ...")




# gauss-jordan
# =====================================================================================================================




    elif (pil == '2'):
        print("\n\n\nMatriks (A) Anda :   \n")
        printMatrix(A, n)
        print("Vector (b) Anda :   \n")
        for i in range(n):
            print("\t", b[0][i])

        flag = GaussJordan(A, n)
            
        if (flag == 1):     
            flag = CheckConsistency(A, n, flag);    

        print("\n\nAugumented Matrix Akhir Adalah : \n")
        printMatrixResult(A, n);
            
        x = PrintResult(A, n, flag);

        print('\n\nSolusi Yang Dicari Adalah :  \n\n')
        for i in range(n):
            print('x%d = %0.2f' %(i+1,x[i]), end = '\t')
        print("\n\n\n")
        input("Tekan Enter untuk Kembali ...")



# matriks-balikan
# =====================================================================================================================



    elif (pil == '3'):
        print("\n\n\nMatriks (A) Anda :   \n")
        printMatrix(A, n)
        print("Vector (b) Anda :   \n")
        for i in range(n):
            print("\t", b[0][i])

        print("\n\nInverse Matrix A : \n")
        invA = np.linalg.inv(a)
        printMatrix(invA, n)

        # Kali
        invASqueeze = np.squeeze(np.asarray(invA))
        bSqueeze = np.squeeze(np.asarray(b))
        print("\nPerkalian antara Inverse Matrix A dan Vector (B) Akan Menghasilkan Vector (x) ..\n")
        print('\n\nMaka Vector (x) :  \n')
        result = np.dot(invASqueeze, bSqueeze)
        for i in result:
            print("\t", round(i, 2))
        print("\n\n\n")
        input("Tekan Enter untuk Kembali ...")


    

# dekomposisiLU
# =====================================================================================================================

    elif (pil == '4'):
        P, L, U = scipy.linalg.lu(a)
        
        UList = U.tolist()
        LList = L.tolist()        
        

        print ("Matrix A:\n")
        printMatrix(a, n)  
        
        print("Vector b :   \n")
        for i in range(n):
            print("\t", round(b[0][i], 2))

            
        print ("P :\n")
        printMatrix(P, n)  

        print ("Lower :\n")
        printMatrix(L, n)

        print ("Upper:\n")
        printMatrix(U, n)

        lu, piv = scipy.linalg.lu_factor(a)
        x = scipy.linalg.lu_solve((lu, piv), b[0])

        
        print('\nMaka Vector (x) :  \n')
        for i in range(n):
            print("\t", round(x[i], 2))    
        print("\n\n\n\n")
        input("Tekan Enter untuk Kembali ...")

        
    

# EXIT
# =====================================================================================================================
    elif (pil == '0'):
        print("\n\nTerima Kasih Telah Menggunakan Program Kami (●'◡'●) \n\n\n\n")
        break
    
    print("\n"*55)

    






# # Hilangkan Komentar jika ingin melihat grafik 
# # Gambar Penyelesaiaan Linear
# # 2variabel matplotlib
# # =====================================================================================================================
    
#     if (n == 2): 
#         A_arr = np.array([a])
#         b_arr = np.array(b)
#         c = np.linalg.solve(A_arr,b_arr)
        

#         plt.xlim((-20,20))
#         plt.ylim((-20,20))

#         plt.plot([-20, 20], [0, 0], color='C0')
#         plt.plot([0, 0], [-20, 20], color='C0')



#         x = np.linspace(-20, 20)
#         if (A_arr[0][0][0] > 0):
#             y = (b_arr[0][0] - A_arr[0][0][0] * x) / A_arr[0][0][1]
#         elif (A_arr[0][0][0] < 0):
#             y = (b_arr[0][0] + A_arr[0][0][0] * x) / A_arr[0][0][1]
#         plt.plot(x, y, color='C2')



#         if (A_arr[0][1][0] > 0):
#             y = (b_arr[0][1] - A_arr[0][1][0] * x) / A_arr[0][1][1]
#         if (A_arr[0][1][0] < 0):
#             y = (b_arr[0][1] + A_arr[0][1][0] * x) / A_arr[0][1][1]
#         plt.plot(x, y, color='C2')



#         plt.scatter(c[0][0], c[0][1], marker='x', color='black')
#         plt.annotate('({:0.3f}, {:0.3f})'.format(c[0][0], c[0][1]), c[0]+0.5)
#         plt.title('Quadrant plot')
#         plt.show()
