bil = []
banyak = int(input('anda mau memasukkan berapa bilangan? : '))
for i in range (banyak):
    angka = int(input('masukkan bilangan pilihan anda : '))
    bil. append(angka)
    

def kuadrat(bil):
    for i in range(len(bil)):
        bil[i]**=2
    return bil

print(bil)
print(kuadrat(bil))

