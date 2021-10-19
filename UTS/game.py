import random
import os

nyawa = 3
skor = 0
soal_ke = 1
level_1 = 1
level_2 = 2
level_3 = 3
keluar = 4

print('===GAME BURIK UNINSTALL AJA===')
print('ANDA MEMILIKI 3 NYAWA DAN SKOR 0, JIKA ANDA BENAR SKOR BERTAMBAH 2 DAN JIKA SALAH NYAWA BERKURANG 1 DAN SKOR BERKURANG 2')
print('SILAKAN PILIH LEVEL!!!')
print('1. LEVEL 1/PENJUMLAHAN')
print('2. LEVEL 2/PENJUMLAHAN')
print('3. LEVEL 3/PENJUMLAHAN')
print('4. EXIT')
level = int(input('MASUKKAN LEVEL :'))
print('=================')
if(level == level_1):
    while True :
        os.system('cls')
        print('soal :',soal_ke)
        print('skor :',skor)
        print('nyawa :',nyawa)
        print('=================')
        print('HITUNGLAH HASIL DIBAWAH INI JIKA ANDA MAMPU')
        a = random.randint (-100,100)
        b = random.randint (-100,100)
        c = a + b
        str(print(a ,'+', b))
        jawab = int(input('= '))
        if (jawab == c):
            print('WAH ANDA BOLEH JUGA')
            print('=====================')
            skor += 1
        else:
            print('YAELAH LU GITU AJA GABISA, JAWABAN YANG BENAR ITU =', c)
            skor -= 1
            nyawa -= 1
            if(nyawa == 0):
                print('===GAME OVER===')
                break
        input('KLIK ENTER UNTUK LANJUT >>')
        print('=====================')
        soal_ke += 1
        
elif(level == level_2):
    while True :
        os.system('cls')
        print('soal :',soal_ke)
        print('skor :',skor)
        print('nyawa :',nyawa)
        print('=================')
        print('HITUNGLAH HASIL DIBAWAH INI JIKA ANDA MAMPU')
        a = random.randint (-100,100)
        b = random.randint (-100,100)
        c = a - b
        str(print(a ,'-', b))
        jawab = int(input('= '))
        if (jawab == c):
            print('WAH ANDA BOLEH JUGA')
            print('=====================')
            skor += 1
        else:
            print('YAELAH LU GITU AJA GABISA, JAWABAN YANG BENAR ITU =', c)
            skor -= 1
            nyawa -= 1
            if(nyawa == 0):
                print('===GAME OVER===')
                break
        input('KLIK ENTER UNTUK LANJUT >>')
        print('=====================')
        soal_ke += 1

elif(level == level_3):
    while True :
        os.system('cls')
        print('soal :',soal_ke)
        print('skor :',skor)
        print('nyawa :',nyawa)
        print('=================')
        print('HITUNGLAH HASIL DIBAWAH INI JIKA ANDA MAMPU')
        a = random.randint (-100,100)
        b = random.randint (-100,100)
        c = a * b
        str(print(a ,'*', b))
        jawab = int(input('= '))
        if (jawab == c):
            print('WAH ANDA BOLEH JUGA')
            print('=====================')
            skor += 1
        else:
            print('YAELAH LU GITU AJA GABISA, JAWABAN YANG BENAR ITU =', c)
            skor -= 1
            nyawa -= 1
            if(nyawa == 0):
                print('===GAME OVER===')
                break
        input('KLIK ENTER UNTUK LANJUT >>')
        print('=====================')
        soal_ke += 1

elif(level == keluar):
    exit()

else:
    print('LEVEL YANG KAMU PILIH BELUM TERSEDIA')
    exit()

