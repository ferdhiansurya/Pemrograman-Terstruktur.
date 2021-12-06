buat = open('D:\kodingku01.txt', 'r')

baca = buat.readlines()

baca2 = []
for i in range(len(baca)):
    fix = baca[i].replace('\n', '')
    baca2 += [fix]

ganjil = []
genap = []
for i in range(len(baca2)):
    if (int(baca2[i])%2 == 0):
        genap += [baca2[i]]
    if (int(baca2[i])%2 != 0):
        ganjil += [baca2[i]]

print('Banyaknya bil genap :', len(genap))
print('Banyaknya bil ganjil:', len(ganjil))
buat.close()
