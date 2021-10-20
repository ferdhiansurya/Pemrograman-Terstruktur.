gaji_A = 10000000
gaji_B = 8500000
gaji_C = 7000000
gaji_D = 5500000
potongan_A = 2.5
potongan_B = 2.0
potongan_C = 1.5
potongan_D = 1.0
tnjgn_istri_suami = 10
tnjgn_anak = 5
A = 1
B = 2
C = 3
D = 4
M = 11
J = 12

#inputdata
kode = int(input('MASUKKAN KODE KARYAWAN: '))
nama = str(input('MASUKKAN NAMA KARYAWAN: '))
golongan = (int(input('MASUKKAN GOLONGAN (1-4): ')))
mnkh = int(input('MASUKKAN STATUS (11 = menikah / 12 = jomblo): '))
if(mnkh < J):
    jmlh_anak = int(input('MASUKKAN JUMLAH ANAK: '))
elif(J > mnkh):
    print('')

print('============================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('----------------------------')
print('NAMA KARYAWAN :',nama)
print('KODE KARYAWAN :',kode)
if(M < mnkh):
    print('STATUS : JOMBLO')
elif(J > mnkh):
    print('STATUS : MENIKAH')
    print('JUMLAH ANAK :',jmlh_anak)

nom_potA = (gaji_A - ((2.5/100)*gaji_A))
nom_potB = (gaji_B - ((2.0/100)*gaji_B))
nom_potC = (gaji_C - ((1.5/100)*gaji_C))
nom_potD = (gaji_D - ((1.0/100)*gaji_D))
tunjang_suis = (tnjgn_istri_suami/100)
tunjang_anak = (tnjgn_anak/100)

if(golongan < B):
    print('GOLONGAN : A')
    print('----------------------------')
    print('GAJI POKOK : Rp.',gaji_A)
    tot_suis = print('TUNJANGAN ISTRI/SUAMI : Rp.',tunjang_suis*gaji_A)
    tot_anak = print('TUNJANGAN ANAK : Rp.',(tunjang_anak*gaji_A)*jmlh_anak)
    print('----------------------------  +')
    total = gaji_A + (tunjang_suis*gaji_A) + (tunjang_anak*gaji_A)*jmlh_anak
    print('GAJI KOTOR : Rp.',(total))
    print('POTONGAN ',potongan_A,'%    : Rp.',(2.5/100)*total)
    print('----------------------------  -')
    print('GAJI BERSIH    :',total - ((2.5/100)*total))
elif(golongan < C) and (golongan > A):
    print('GOLONGAN : B')
    print('----------------------------')
    print('GAJI POKOK : Rp.',gaji_B)
    tot_suis = print('TUNJANGAN ISTRI/SUAMI : Rp.',tunjang_suis*gaji_B)
    tot_anak = print('TUNJANGAN ANAK : Rp.',(tunjang_anak*gaji_B)*jmlh_anak)
    print('----------------------------  +')
    total_B = gaji_B + (tunjang_suis*gaji_B) + (tunjang_anak*gaji_B)*jmlh_anak
    print('GAJI KOTOR : Rp.',(total_B))
    print('POTONGAN ',potongan_B,'%    : Rp.',(2.0/100)*total_B)
    print('----------------------------  -')
    print('GAJI BERSIH    :',total_B - ((2.0/100)*total_B))
elif(golongan > B) and (golongan < D):
    print('GOLONGAN : C')
    print('----------------------------')
    print('GAJI POKOK : Rp.',gaji_C)
    tot_suis = print('TUNJANGAN ISTRI/SUAMI : Rp.',tunjang_suis*gaji_C)
    tot_anak = print('TUNJANGAN ANAK : Rp.',(tunjang_anak*gaji_C)*jmlh_anak)
    print('----------------------------  +')
    total_C = gaji_C + (tunjang_suis*gaji_C) + (tunjang_anak*gaji_C)*jmlh_anak
    print('GAJI KOTOR : Rp.',(total_C))
    print('POTONGAN ',potongan_C,'%    : Rp.',(1.5/100)*total_C)
    print('----------------------------  -')
    print('GAJI BERSIH    :',total_C - ((1.5/100)*total_C))
elif(golongan > C):
    print('GOLONGAN : D')
    print('----------------------------')
    print('GAJI POKOK : Rp.',gaji_D)
    tot_suis = print('TUNJANGAN ISTRI/SUAMI : Rp.',tunjang_suis*gaji_D)
    tot_anak = print('TUNJANGAN ANAK : Rp.',(tunjang_anak*gaji_D)*jmlh_anak)
    print('----------------------------  +')
    total_D = gaji_D+ (tunjang_suis*gaji_D) + (tunjang_anak*gaji_D)*jmlh_anak
    print('GAJI KOTOR : Rp.',(total_D))
    print('POTONGAN ',potongan_D,'%    : Rp.',((1.0/100)*total_D))
    print('----------------------------  -')
    print('GAJI BERSIH    :',total_D - ((1.0/100)*total_D))

    
