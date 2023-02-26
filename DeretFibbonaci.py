batas=int(input("Masukkan Batas: "))
arr=[]
for indeks in range(0,2):
    arr.append(indeks)
    print(arr[indeks], end=" ")

for indeks in range(2, batas):
    arr.append(arr[indeks-1]+arr[indeks-2])
    print(arr[indeks], end=" ")