hargaBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6800}
print('='*24)
print('TOTAL PEMBAYARAN BUAH')
print('='*24)
buah = input('Buah yang dibeli : ')
if buah in hargaBuah :
    harga = int(input('Banyaknya buah (KG) : '))
    print('-'*24)
    total = harga * hargaBuah[buah]
    print('total nominal : Rp.',total)
else:
    print('='*24)
    print('Maaf input tidak valid')
    
