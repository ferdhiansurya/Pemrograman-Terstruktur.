def faktorial(n):
    a = 1
    while (n > 0):
        a *= n
        n -= 1
    return a

def kombinasi(a,b):
    return faktorial(a) / (faktorial(a - b) * faktorial(b))

def permutasi(a,b):
    return faktorial(a) / faktorial (a - b)

print('C(5,3) =', kombinasi(5,3))
print('P(10,7) =', permutasi(10,7))
    

