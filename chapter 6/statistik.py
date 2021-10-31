def sum(*myData):
    #init values
    sum = 0
    i = 0
    # menjumlahkan semua data dalam myData
    for data in myData:
        sum += data
        i += 1
    return sum

def average(*myData):
    #init values
    sum = 0
    i = 0

    #menjumlahkan semua data dalam myData
    for data in myData:
        sum += data
        i += 1

    # hitung rata-rata
    rata2 = sum/i
    return rata2

def max(*myData):
  angkaTerbesar = myData[0]

  for nilai in myData:
    if nilai > angkaTerbesar:
      angkaTerbesar = nilai
  return angkaTerbesar

def min(*myData):
  angkaTerkecil = myData[0]

  for nilai in myData:
    if nilai < angkaTerkecil:
      angkaTerkecil = nilai
  return angkaTerkecil




