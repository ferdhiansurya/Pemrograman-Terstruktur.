data = open('sandi.txt', 'r')
hasil = open('sandiku2.txt', 'a')

fileKu = data.read()

mySet = set(fileKu)

mySet.remove(' ')

List = list(mySet)

List.sort()

n = 2

file = fileKu.replace(List[0], chr(ord(List[0])-n))

i = 1
while True:
    file = file.replace(List[i], chr(ord(List[i])-n))
    i+=1

    if(i==10):
        break

file = file.replace(chr(63), chr(89))
file = file.replace(chr(64), chr(90))

hasil.write(file)

data.close()
hasil.close()
