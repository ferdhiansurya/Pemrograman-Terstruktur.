minim_nilai = 60
nilai_mtk = 71
batas_bwh = 0
batas_ats = 100

#input data
print('STATUS KELULUSAN UJIAN MAHASISWA')

print(input('NAMA MAHASISWA: '))

nilai_bi = (int(input('NILAI BAHASA INDONESIA: ')))
nilai_ipa = (int(input('NILAI ILMU PENGETAHUAN ALAM: ')))
nilai_mat = (int(input('NILAI MATEMATIKA: ')))
if(batas_bwh > nilai_bi) or (batas_ats < nilai_bi) or (batas_bwh > nilai_mat) or (batas_ats < nilai_mat) or (batas_bwh > nilai_ipa) or (batas_ats < nilai_ipa):
    print('            NILAI TIDAK VALID         ')
elif(minim_nilai < nilai_bi) and (minim_nilai < nilai_ipa) and (minim_nilai < nilai_mat) and (nilai_mtk < nilai_mat):
    print('        LULUS        ')
else:
    print('         TIDAK LULUS     ')
