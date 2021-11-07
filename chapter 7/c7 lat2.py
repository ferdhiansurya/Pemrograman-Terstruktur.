try:
    nama = input('Masukkan nama file: ')
    file = open(nama,'r')
    
    while True: 
        file = open(nama,'a')
        data = input('Data yang mau ditambahkan: ')
        file.write(data)
        file.close()
        cek = input('Mau lagi (y/n)?: ')
        if cek == 'y' or cek == 'Y':
            True
        elif cek == 'n' or cek == 'N':
            file = open(nama,'r')
            print('Isi File ',nama)
            print()
            print(file.read())
            break
        else:
            print('Pilihan tidak tersedia')
            break
        
except FileNotFoundError:
    print('File tidak ditemukan / salah penulisan')
