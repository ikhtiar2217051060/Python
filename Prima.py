bilangan=int(input("Masukkan sebuah bilangan: "))
status=True
for faktor in range(2, bilangan):
    if(bilangan%faktor==0):
        status=False
        break

if(status==True):
    print(bilangan, "merupakan bilangan prima\n")
else:
    print(bilangan, "bukan bilangan prima\n")