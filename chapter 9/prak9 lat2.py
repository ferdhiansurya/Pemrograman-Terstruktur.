def bintang(n):
    ruang = 2*n-1
    for i in range(n):
        print(('*'*(i*2+1)).center(ruang))
bintang(4)
