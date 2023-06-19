#tugas menghitung total bilangan
total = 0
bil = int(input('Masukkan bilangan= '))

print ('Total nilai = ', end = '')

while bil >= 1:
    print(bil, end = ' ')
    if 1 == bil:
        print('=', end = ' ')
    else:
        print('+', end = ' ')
    total = total + bil 
    bil = bil - 1
    
print(total)