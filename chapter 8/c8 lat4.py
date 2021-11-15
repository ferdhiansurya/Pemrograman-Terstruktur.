sayur = ['bayam', 'kangkung', 'wortel', 'selada']
print(sayur)
def menu ():
    print('='*24)
    print('Menu :')
    print('A = Tambah data sayur')
    print('B = Hapus data sayur')
    print('C = Tampilkan data sayur')
    a = input('Pilihan anda : ')
    if (a == 'a') or (a == 'A'):
        tambahan = input('Mau menambahkan sayur apa? : ')
        sayur. append(tambahan)
        print('='*24)
        print('Daftar sayur terbaru')
        print('='*24)
        print(sayur)
        b = input('Ada lagi? y/n : ')
        if (b == 'y') or (b == 'Y'):
            menu()
        elif(b == 'n') or (b == 'N'):
            print('OK makasih ya')
            
    elif (a == 'b') or (a == 'B'):
        try :
            hapus = input('Mau menghapus sayur apa? : ')
            sayur. remove(hapus)
            print('='*24)
            print('Daftar sayur terbaru')
            print('='*24)
            print(sayur)
        except ValueError :
            print('Data tidak ditemukan')
            menu()
        b = input('Ada lagi? y/n : ')
        if (b == 'y') or (b == 'Y'):
            menu()
        elif(b == 'n') or (b == 'N'):
            print('OK makasih ya')
            
    elif (a == 'c') or (a == 'C'):
        print('='*24)
        print('Daftar sayur terbaru')
        print('='*24)
        print(sayur)
        b = input('Kembali ke menu? y/n : ')
        if (b == 'y') or (b == 'Y'):
            menu()
        elif(b == 'n') or (b == 'N'):
            print('OK makasih ya')
    else :
        print('Pilih yang bener napa')
        menu()
menu()
