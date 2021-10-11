print("KONSUMSI BBM MOBIL PAK BUDI")
def liter(jarakAkeC, jarak1literBBM):
    return jarakAkeC/jarak1literBBM
#inputdata
print("BBM YANG DIPERLUKAN")
jarakAkeC= int(input("JARAK(KM): "))
print("1 LITER BBM")
jarak1literBBM= int(input("JARAK 1 LITER BBM(KM): "))
print("JARAK A KE C", jarakAkeC, "KM","DENGAN JARAK 1 LITER BBM", jarak1literBBM, "KM")
total= jarakAkeC/jarak1literBBM
print("BENSIN YANG DIPERLUKAN", total, "LITER")
print("SEKIAN TERIMAKASIH")
