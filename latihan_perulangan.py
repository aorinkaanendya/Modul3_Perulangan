#LATIHAN SISTEM LOGIN
print("======SISTEM LOGIN SEDERHANA======")

login = 0
while True:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if login == 3:
        print("Percobaan login sudah habis. Silakan coba nanti")
    
    if username == "aorinka" and password == "1406":
        print("Selamat datang", username,"!")
        break
    else:
        print("Coba cek kembali username dan password salah")
        login += 1
        
#LATIHAN MENCARI BILANGAN GENAP
bil = int(input("Masukkan bilangan maksimal: "))
i = 0
while i < bil:
    print(i)
    i += 2
    if i == bil:
        break
    
#LATIHAN MENCARI FPB
#mendefinisikan fungsi
def hitung_FPB(x, y):
# memilih bilangan yang paling kecil
    if x > y:
        terkecil = y
    else:
        terkecil = x
    for i in range(1, terkecil+1):
        if((x % i == 0) and (y % i == 0)):
            fpb = i
    return fpb
nilai1 = int(input("Masukan bilangan pertama: "))
nilai2 = int(input("Masukan bilangan kedua: "))
print("Faktor Persekutuan Terbesar =", hitung_FPB(nilai1, nilai2))