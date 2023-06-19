#tugas menghitung KPK

# mendefinisikan fungsi
def hitung_FPB(x, y):
# memilih bilangan yang paling kecil
    if x > y:
        terkecil = y
    else:
        terkecil = x
    for i in range(1, terkecil +1):
        if((x % i == 0) and (y % i == 0)):
            fpb = i
    return fpb


def KPK (x, y):
    KPK = int(x *y / hitung_FPB(x,y))
    return KPK

nilai1 = int(input("Masukan bilangan pertama: "))
nilai2 = int(input("Masukan bilangan kedua: "))
print("KPK = ", KPK(nilai1, nilai2))