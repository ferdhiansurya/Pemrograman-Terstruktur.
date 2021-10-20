gaji_A = 10000000
gaji_B = 8500000
gaji_C = 7000000
gaji_D = 5500000
potongan_A = 2.5
potongan_B = 2.0
potongan_C = 1.5
potongan_D = 1.0
A = 1
B = 2
C = 3
D = 4

#inputdata
kode = int(input('MASUKKAN KODE KARYAWAN: '))
nama = str(input('MASUKKAN NAMA KARYAWAN: '))
golongan = (int(input('MASUKKAN GOLONGAN (1-4): ')))
print('============================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('----------------------------')
print('NAMA KARYAWAN :',nama)
print('KODE KARYAWAN :',kode)
potA = (2.5/100)*gaji_A
potB = (2.0/100)*gaji_B
potC = (1.5/100)*gaji_C
potD = (1.0/100)*gaji_D
nom_potA = (gaji_A - ((2.5/100)*gaji_A))
nom_potB = (gaji_B - ((2.0/100)*gaji_B))
nom_potC = (gaji_C - ((1.5/100)*gaji_C))
nom_potD = (gaji_D - ((1.0/100)*gaji_D))
if(golongan < B):
    print('GOLONGAN : A')
    print('----------------------------')
    print('GAJI POKOK : Rp.',gaji_A)
    print('POTONGAN ',potongan_A,'%    : Rp.',potA)
    print('----------------------------  -')
    print('GAJI BERSIH    :',nom_potA)
elif(golongan < C) and (golongan > A):
    print('GOLONGAN : B')
    print('----------------------------')
    print('GAJI POKOK : Rp.',gaji_B)
    print('POTONGAN ',potongan_B,'%    : Rp.',potB)
    print('----------------------------  -')
    print('GAJI BERSIH    :',nom_potB)
elif(golongan > B) and (golongan < D):
    print('GOLONGAN : C')
    print('----------------------------')
    print('GAJI POKOK : Rp.',gaji_C)
    print('POTONGAN ',potongan_C,'%    : Rp.',potC)
    print('----------------------------  -')
    print('GAJI BERSIH    :',nom_potC)
elif(golongan > C):
    print('GOLONGAN : D')
    print('----------------------------')
    print('GAJI POKOK : Rp.',gaji_D)
    print('POTONGAN ',potongan_D,'%    : Rp.',potD)
    print('----------------------------  -')
    print('GAJI BERSIH    :',nom_potD)


    



    
