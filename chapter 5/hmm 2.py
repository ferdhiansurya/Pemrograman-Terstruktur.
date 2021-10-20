#kotak bintang ajaib
kolom=5
baris=5
i=0
k = 5
while((i+k) <= baris):
    k -= 1
    j = 0 
    while(j < (kolom-k)):
        print('* ',end='')
        j += 1
    print('')
    i += 1
    if(i > 4):
        break
