#tugas menghitung hasil pangkat
nilai = int(input('Masukkan bilangan = '))
pangkat = int(input('Masukkan pencacah = '))

hasil = nilai
for i in range(pangkat - 1):
    hasil *= nilai

print('Hasil pangkat bilangan =', hasil)