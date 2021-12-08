from datetime import *

def diff_date(x):
    waktu = datetime.strptime(x, '%Y-%m-%d').date()
    
    waktuSekarang = datetime.date(datetime.now())
    
    gap =  waktuSekarang - waktu

    return gap
    
print ('Selisih tanggal 2021-12-1 dengan hari ini adalah',diff_date('2021-12-1').days)
