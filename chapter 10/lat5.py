data = open('bilanganku.txt', 'r')
jmlh = open('jmlhbilangan.txt', 'w')

baca = data.readlines()

for i in range(len(baca)):
    x = baca[i].replace('\n', '')
    y = x.split("|")
    jmlh.write(str(int(y[0])+int(y[1]))+'\n')
    
data.close()
jmlh.close()
