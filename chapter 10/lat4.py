data = open('D:\ktrmahasiswa.txt', 'r')

baca = data.readlines()

hasil = []
for i in range(len(baca)):
    baca2 = {}
    fix= baca[i].replace('\n', '')
    fix2= fix.split("|")
    baca2['nim']=fix2[0]
    baca2['nama']=fix2[1]
    baca2['alamat']=fix2[2]
    hasil+=[baca2]

while True:
    kunci = input('Masukkan input yang mau dicari: ')

    for i in range(len(hasil)):
        if kunci in hasil[i]['nim']:
            print()
            print('Data mahasiswa')
            print('NIM   :'+str(hasil[i]['nim']))
            print('nama  :'+str(hasil[i]['nama']))
            print('Alamat:'+str(hasil[i]['alamat']))

    if kunci not in hasil[0]['nim']:
        if kunci not in hasil[1]['nim']:
            if kunci not in hasil[2]['nim']:
                print("\"Data mahasiswa tidak ditemukan\"")

    print()
    ulang = input('Ingin mengulang (y/n) ? ')
    print()
    if ulang in ('N', 'n'):
        print('Terimakasih telah mencoba!!!')
        break
    
data.close()
