import numpy as np

m = int(input("Masukkan baris: "))
n = int(input("Masukkan kolom: "))
temp = []
for i in range(m):
    for j in range(n):
        addList = float(input(f"Masukkan Elemen ke baris ke-{i} kolom ke-{j}"))
        temp.append(addList)
A = temp.copy()
print(A)