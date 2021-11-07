print('-'*24)
print('PROGRAM HITUNG RATA-RATA')
print('-'*24)

bilangan = 0
banyak = 0
while True:
    try:
        bil = int(input('Ayo masukkan bilangan bulat pilihanmu: '))
        bilangan += bil
        banyak += 1
        cek = input('Lagi (y/n)?: ')
        if cek == 'y' or cek == 'Y':
            True
        elif cek == 'n' or cek == 'N':
            hasil = bilangan / banyak
            print('Rata-rata = ',hasil)
            break
        else:
            print('Pilihan tidak tersedia')
            break
                
    except ValueError:
            print('Itu bukan bilangan bulat kawan')
            continue
        
        
