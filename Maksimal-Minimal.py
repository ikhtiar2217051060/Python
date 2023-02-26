jumlah=int(input("Masukkan jumlah List: "))
arr=[]
maksimal=-9999
minimal=9999
for indeks in range(0, jumlah):
    arr.append(int(input("Masukkan List ke-"+str(indeks+1)+": ")))
for indeks in range(0, jumlah):
    if(arr[indeks]>maksimal):
        maksimal=arr[indeks]
    if(arr[indeks]<minimal):
        minimal=arr[indeks]

print("Nilai Maksimal: ", maksimal)
print("Nilai Minimal : ", minimal)
