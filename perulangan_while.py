i = 0
while i <= 7:
    print("Hello World")
    i += 1

#perulangan increment
a = 1
b = 10
while a < b:
    print("Step ke-", a)
    a += 1

#perulangan decrement
a = 5
b = 0
while a > b:
    print("Kuota internet anda tersisa", a, "GB")
    a -= 1

#fungsi break dan continue
#fungsi break untuk menghentikan paksa program 
#continue untuk skip

#contoh continue pada perulangan break
for i in range (1, 10):
    print("Perulangan ke-", i)
    if i == 5:
        print("Berhenti pada perulangan ke-", i)
        break


#contoh continue pada perulangan for
for i in range(0, 5):
    if (i == 3):
        continue
    
    print(i)

#contoh break pada perulangan while
a = 0
while True:
    print("Step ke-", a)
    a += 1
    if a == 7:
        print("Step ke-",a, "dihentikan!")
        break
    
#contoh continue pada perulangan while
angka = ['1','2','3','4','5','6','7','8','9','10']
i = -1
while i < len(angka):
    i += 1
    if i % 2 == 0 and i > 0:
        print('skip')
        continue
    print(angka[i])





