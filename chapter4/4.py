jar_AkeB = 125
jar_BkeC = 256
kec_AkeB = 62
kec_BkeC = 70

jamber = 6
menber = 00

menis = 45/60

wak_AkeB = round(jar_AkeB / kec_AkeB)
wak_BkeC = round(jar_BkeC / kec_BkeC)

totwaktu = wak_AkeB + wak_BkeC + menis
totwaktu = round(totwaktu, 2)

totjam = totwaktu // 1
jamsampai = totjam + jamber

totmen = totwaktu % 1
totmen = round(totmen * 60, 1)
mensam = round(totmen + menber, 1)

print('waktu yang dibutuhkan untuk sampai dari kota A ke B adalah', wak_AkeB, 'jam')
print('waktu yang dibutuhkan untuk sampai dari kota B ke C adalah', wak_BkeC, 'jam')
print('total waktu perjalanan dan istirahat adalah', totwaktu, 'jam')
print('atau', round(totjam), "jam", totmen, 'menit')
print('apabila pak amir berangkat pukul', jamber, 'lebih', menber, 'menit')
print('maka pak amir akan smapai di tempat tujuan pukul', round(jamsampai), 'lebih', mensam, 'menit' )
