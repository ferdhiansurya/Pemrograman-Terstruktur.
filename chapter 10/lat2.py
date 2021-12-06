#Program input data mahasiswa

file = open('D:\datamhs.txt', 'a')

while True:
    nim = input('Masukkan data NIM: ')
    nama = input('Masukkan data nama: ')
    alamat = input('Masukkan data alamat: ')

    myString = nim+"|"+nama+'|'+alamat+'\n'

    file.write(myString)

    print()
    jawab = input("Mau input data lagi (y/n) ? ")
    print()
    if jawab in ('N','n'):
        break

file.close()
