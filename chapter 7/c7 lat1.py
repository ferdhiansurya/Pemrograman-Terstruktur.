try :
    nama = input('masukkan nama file : ')
    file = open(nama,'r')
    print('isi file', nama, 'adalah :')
    print('')
    print(file.read())
except NameError :
    print('nama tidak ditemukan')
except ValueError :
    print('data yang anda masukkan tidak valid')
except FileNotFoundError :
    print('file tidak ditemukan')
