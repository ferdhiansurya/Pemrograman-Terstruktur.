print("RENTAL MOBIL RODA LIMA")
def jam(jamkeluar,jamkembali):
    return jamkembali-jamkeluar
def menit(jamkeluar,jamkembali):
    return jamkembali-jamkeluar
def keseluruhan(jamkeluar,jamkembali):
    return lamajam*60+lamamenit
#inputdata
print("WAKTU MEMINJAM")
jamkeluar= int(input("JAM: "))
menitkeluar= int(input("MENIT: "))
print("WAKTU MENGEMBALIKAN") 
jamkembali= int(input("JAM: "))
menitkembali= int(input("MENIT: "))
lamajam= jam(jamkeluar,jamkembali)
lamamenit= menit(menitkeluar, menitkembali)
print("LAMA MEMINJAM: ", lamajam, "JAM", lamamenit, "MENIT")
total= keseluruhan(lamajam, lamamenit)
if total<721:
    print("HARGA=Rp. 200.000,-")
elif total:
        total= int((total-720)*166.6666666666667+200000)
        print("HARGA= Rp. ", total)
