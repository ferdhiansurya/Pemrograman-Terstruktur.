hargaBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6800}
while True:
    print('='*24)
    print('Silakan pilih menu dibawah')
    print('='*24)
    print('A. Tambah data buah')
    print('B. Beli buah')
    print('C. Cukup')
    print('D. Hapus buah')
    a = input('Pilihan anda : ')
    if a in ('A', 'a'):
        tambah = input('Masukkan nama buah : ')
        if tambah in hargaBuah :
            print('Buah sudah ada')
            True
        else :
            perKilo = int(input('Harga satu Kilo : '))
            hargaBuah[tambah] = perKilo
            print('Data buah :')
            for i,j in hargaBuah. items():
                print('-',i,'(Harga Rp.'+str(j)+')')    
            print('')
            True

    elif a in ('B', 'b'):
        print('='*24)
        print('TOTAL PEMBAYARAN BUAH')
        print('='*24)
        print(hargaBuah)
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
    elif a in ('C', 'c'):
        break
    elif a in ('D', 'd'):
        hilang = input('Masukkan buah yang ingin dihilangkan : ')
        if hilang in hargaBuah:
            del hargaBuah[hilang]
            print(hargaBuah)
            True
        else:
            print('Buah tidak ada')
            
    else :
        print('Mohon isi dengan benar')
        break




