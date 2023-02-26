tahunLahir=int(input("Masukkan Tahun Lahir: "))

if(tahunLahir-1912)%12==0:
    zodiak="Tikus"
elif(tahunLahir-1913)%12==0:
    zodiak="Kerbau"
elif(tahunLahir-1914)%12==0:
    zodiak="Harimau"
elif(tahunLahir-1915)%12==0:
    zodiak="Kelinci"
elif(tahunLahir-1916)%12==0:
    zodiak="Naga"
elif(tahunLahir-1917)%12==0:
    zodiak="Ular"
elif(tahunLahir-1918)%12==0:
    zodiak="Kuda"
elif(tahunLahir-1919)%12==0:
    zodiak="Kambing"
elif(tahunLahir-1920)%12==0:
    zodiak="Monyet"
elif(tahunLahir-1921)%12==0:
    zodiak="Ayam"
elif(tahunLahir-1922)%12==0:
    zodiak="Anjing"
elif(tahunLahir-1923)%12==0:
    zodiak="Babi"

print("Zodiak: ",zodiak)
