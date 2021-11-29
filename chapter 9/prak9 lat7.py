
maha = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('='*75)
print("NIM    NAMA MAHASISWA           TGL LAHIR       TEMPAT LAHIR")
print('-'*75)

for i in maha:
    data = i.split(':')
    nim = data[0]
    nama = data[1]
    tglLahir = data[2]
    tglSplit = tglLahir.split('-')
    tgl = tglSplit[2]
    bln = tglSplit[1]
    thn = tglSplit[0]
    tmpLahir = data[3]
    
    print(nim.ljust(6),
          nama.ljust(24),
          tgl,'/',bln,'/',thn.ljust(5),
          tmpLahir)
