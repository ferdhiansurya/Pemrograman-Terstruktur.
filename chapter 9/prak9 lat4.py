
import random
def shuffleString(x, y):
    kata_acak = []
    i = 0
    while i < y:
        result = ''.join(random.sample(x,len(x)))
        if result not in kata_acak:
            kata_acak.append(result)
            i+=1
            
    print (kata_acak)

shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)
