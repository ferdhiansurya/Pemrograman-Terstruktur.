def luasSegitiga2(alas, tinggi):
    global luas1
    luas1 = alas * tinggi / 2
    print('luas segitiga dg alas', alas, 'dan tinggi', tinggi,'adalah',luas1)

alas = 10
tinggi = 20
luasSegitiga2(alas, tinggi)

def luasSegitiga3(alas, tinggi):
    global luas2
    luas2 = alas * tinggi / 2
    print('luas segitiga dg alas', alas, 'dan tinggi', tinggi,'adalah',luas2)

alas = 15
tinggi = 45
luasSegitiga3(alas, tinggi)

luasTotal = luas1 + luas2
print('luas total kedua segitiga tersebut adalah', luasTotal)




    
