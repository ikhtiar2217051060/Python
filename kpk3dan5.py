kpk3=[]
kpk5=[]
kpk3dan5=[]

for angka in range (1, 101):
    if angka%3==0:
        kpk3.append(angka)
    if angka%5==0:
        kpk5.append(angka)
    if angka%3==0 and angka%5==0:
        kpk3dan5.append(angka)

for indeks in range(0, len(kpk3)):
    print(kpk3[indeks], end=" ")
print("\n")
for indeks in range(0, len(kpk5)):
    print(kpk5[indeks], end=" ")
print("\n")
for indeks in range(0, len(kpk3dan5)):
    print(kpk3dan5[indeks], end=" ")