
mulai='y'
print(type(mulai))
while(mulai=='y'):
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian  ")
    print("4. Pembagian  ")
    operator=float(input("Pilih operasi perhitungan 1/2/3/4: "))
    while(operator<1 or operator>4):
        operator=float(input("Pilih operasi perhitungan 1/2/3/4: "))

    bilangan1=float(input("Masukkan bilangan pertama: "))
    bilangan2=float(input("Masukkan bilangan kedua  : "))
    if(operator==1):
        hasil=bilangan1+bilangan2
    elif(operator==2):
        hasil=bilangan1-bilangan2
    elif(operator==3):
        hasil=bilangan1*bilangan2
    elif(operator==4):
        hasil=bilangan1/bilangan2
    print("hasilnya", hasil)
    mulai=str(input("hitung lagi? (y/t)"))
print("Program Selesai")