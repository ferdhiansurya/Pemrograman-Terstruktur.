try:
    from datetime import *
    data = open('d:\chptr11.txt','r')

    data_perpus = data.readlines()

    cari = input('Masukkan Kode Member\t\t: ')


    for i in data_perpus:
    
        pecah = i.replace('\n','')
        pecah = pecah.split('|')
        if cari in pecah:
            member = pecah
            break
    
    
    if cari in member:
        indeks = member.index(cari)
        tglKembali = datetime.date(datetime.now())
        tgl_kembali = datetime.strptime(member[indeks+4], '%Y-%m-%d').date()

        telat = tglKembali - tgl_kembali
        if int(telat.days) < 0:
            telat = '0'
            denda = '0'
        else:
            telat = int(telat.days)
            denda = telat * 2000

        print ('\nData Peminjaman Buku')
        print ('Kode Member\t\t\t:', member[indeks])
        print ('Nama Member\t\t\t:', member[indeks+1])
        print ('Judul Buku\t\t\t:', member[indeks+2])
        print ('Tanggal Mulai Pengembalian\t:', member[indeks+3])
        print ('Tanggal Maks Pengembalian\t:', member[indeks+4])
        print ('tanggal Pengembalian\t\t:', str(tglKembali))
        print ('Terlambat\t\t\t:', str(telat),'hari')
        print ('Denda\t\t\t\t: Rp.', denda)
except NameError:
    print('Member tidak ditemukan')
