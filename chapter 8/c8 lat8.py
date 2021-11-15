hargaBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6800}
def rerata(hargaBuah):
    jumlah = sum(hargaBuah.values())
    bagi = len(hargaBuah.keys())
    hasil = jumlah/bagi
    return hasil
    print(bagi)
print(rerata(hargaBuah))
