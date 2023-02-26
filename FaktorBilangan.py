bilangan=int(input("masukkan sebuah bilangan: "))

for faktor in range(1, bilangan+1):
    if bilangan%faktor==0:
        print(faktor,end=" ")