def jumlah(bilangan1, bilangan2):
    return bilangan1+bilangan2
def kurang(bilangan1, bilangan2):
    return bilangan1-bilangan2
def kali(bilangan1, bilangan2):
    return bilangan1*bilangan2
def bagi(bilangan1, bilangan2):
    return bilangan1*bilangan2

print('''
1. Penjumlahan  [+]
2. Pengurangan  [-]
3. Perkalian    [*]
4. Pembagian    [:]
        ''')
operator=int(input('Pilih operator perhitungan 1/2/3/4: '))
while (operator<1 or operator>4):
    operator=int(input('Pilih operator perhitungan 1/2/3/4: '))
bilangan1=float(input('Masukkan Bilangan 1: '))
bilangan2=float(input('Masukkan Bilangan 2: '))

if operator==1:
    print('Hasil: ', jumlah(bilangan1, bilangan2))
elif operator==2:
    print('Hasil: ',kurang(bilangan1, bilangan2))
elif operator==3:
    print('Hasil: ',kali(bilangan1, bilangan2))
elif operator==4:
    print('Hasil: ',bagi(bilangan1, bilangan2))