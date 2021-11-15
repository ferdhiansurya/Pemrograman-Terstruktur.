hargaBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6800}
print('='*24)
print('TOTAL PEMBAYARAN BUAH')
print('='*24)
hasil = 0
try :
    while True :
        print('')
        buah = input('Buah yang dibeli : ')
        if buah in hargaBuah :
            harga = int(input('Banyaknya buah (KG) : '))
            lagi = input('Beli buah lain? (y/n) : ')
            if lagi in ('Y', 'y'):
                True
            elif lagi in ('N', 'n'):
                print('-'*24)
                total = harga * hargaBuah[buah]
                hasil += total
                print('total nominal : Rp.',hasil)
                break
            else :
                print('Maaf input tidak valid')
                break
                
        else:
            print('='*24)
            print('Maaf input tidak valid')
            break
except ValueError :
    print('Maaf harus angka ya!')
