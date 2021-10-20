minim_nilai = 60
nilai_mtk = 71

#input data
print('STATUS KELULUSAN UJIAN MAHASISWA')

print(input('NAMA MAHASISWA: '))

nilai_bi = (int(input('NILAI BAHASA INDONESIA: ')))
nilai_ipa = (int(input('NILAI ILMU PENGETAHUAN ALAM: ')))
nilai_mat = (int(input('NILAI MATEMATIKA: ')))

if(minim_nilai < nilai_bi) and (minim_nilai < nilai_ipa) and (minim_nilai < nilai_mat) and (nilai_mtk < nilai_mat):
    print('            LULUS         ')
else:
    print('         TIDAK LULUS     ')
