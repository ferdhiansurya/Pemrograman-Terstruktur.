def dataStat(x):
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    return(a,b,c)

bil = []
banyak = int(input('kamu mau memasukkan berapa bilangan? : '))
for i in range (banyak):
    bulat = int(input('silakan masukkan angkamu : '))
    bil. append(bulat)

print('nilai rata-rata, nilai tertinggi, dan nilai terendah berturut turut adalah', dataStat(bil))
