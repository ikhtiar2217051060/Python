lower = 2
batas=int(input("Masukkan Batas: "))

print("Deret bilangan prima antara", lower, "dan", batas, "adalah:")

for num in range(lower, batas+1):
    # bilangan prima harus lebih besar dari 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                # bukan bilangan prima
                break
        else:
            print(num,end=" ")
