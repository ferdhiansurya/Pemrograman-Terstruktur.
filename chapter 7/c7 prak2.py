# membuka dan mau membaca file d:/data.txt
try :
    file = open('c:/data.txt', 'r')
except FileNotFoundError :
    print('file tidak ditemukan')

# baca baris pertama dari file
# simpan ke dalam variabel bil1 sbg integer
try :
    bil1 = int(file.readline())
except NameError :
    print('nama tidak ditemukan')
    
# baca baris pertama dari file
# simpan ke dalam variabel bil2 sbg integer
try :
    bil2 = int(file.readline())
except NameError :
    print('nama tidak ditemukan')

# hitung dan tampilkan hasil bagi
try :
    hasil = bil1/bil2
    print(bil1, 'dibagi', bil2, 'sama dengan', hasil)
except ZeroDivisionError :
    print('tidak boleh pembagian dengan nol')
except NameError :
    print('nama tidak ditemukan')
