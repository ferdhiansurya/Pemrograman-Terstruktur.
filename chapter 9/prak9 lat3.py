def bintang(n):
    ruang = 2*n-1
    if n%2 == 0:
        for i in range(n//2):
            print(('*'*(i*2+1)).center(ruang))
        for i in reversed(range(n//2)):
            print(('*'*(i*2+1)).center(ruang))
    else:
        for i in range(n//2):
            print(('*'*(i*2+1)).center(ruang))
        for i in reversed(range(n//2+1)):
            print(('*'*(i*2+1)).center(ruang))
bintang(7)
