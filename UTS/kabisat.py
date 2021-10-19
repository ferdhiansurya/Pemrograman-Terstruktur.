
print('===PENENTUAN TAHUN KABISAT===')
tahun = int(input('MASUKKAN TAHUN : '))
if(tahun%400 == 0):
    print('TAHUN',tahun,'MERUPAKAN TAHUN KABISAT')
elif((tahun%400 > 0) and (tahun%4 == 0)) and tahun%100 > 0:
    print('TAHUN',tahun,'MERUPAKAN TAHUN KABISAT')
elif(tahun%400 > 0) or (tahun%100 == 0):
    print('TAHUN',tahun,'BUKAN MERUPAKAN TAHUN KABISAT')
elif((tahun%400 > 0) or (tahun%100 > 0)) and (tahun%4 > 0):
    print('TAHUN',tahun,'BUKAN MERUPAKAN TAHUN KABISAT')

