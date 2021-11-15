#chapter 8

#nomor 1
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

#nomor 2
a.insert(3,int(10))
b.insert(2,int(15))

#nomor 3
a.insert(10,int(4))
b.insert(10,int(8))

#nomor 4
x = sorted(a)
y = sorted(b)

#nomor 5
c = a[0:8]
d = b[2:10]

#nomor 6
e = []
for i in range (len(c)):
    jmlh = c[i] + d[i]
    e = e + [jmlh]

#nomor 7
Tuple = tuple(e)

#nomor 8
nilai_min = min(e)
nilai_max = max(e)
jumlah = sum(e)

#nomor 9
myString = 'python adalah bahasa pemrograman yang menyenangkan'

#nomor 10
huruf = set(myString)

#nomor 11
urutan = list(huruf)
sortir = sorted(urutan)

print(a)
print(b)
print(x)
print(y)
print(c)
print(d)
print(e)
print(Tuple)
print(nilai_min)
print(nilai_max)
print(jumlah)
print(huruf)
print(urutan)
print(sortir)







