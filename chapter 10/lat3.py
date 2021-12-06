data = open('D:\datamhs.txt', 'r')

x = data.readlines()

hasil = []
for i in range(len(x)):
    baca = {}
    fix = x[i].replace('\n', '')
    fix2 = fix.split("|")
    baca['nim']=fix2[0]
    baca['nama']=fix2[1]
    baca['alamat']=fix2[2]
    hasil+=[baca]

print('dataMhs='+str(hasil))
data.close()
