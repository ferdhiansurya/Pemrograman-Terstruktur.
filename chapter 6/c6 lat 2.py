def starFormation1(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end='')
        print()

def starFormation2(n):
    for i in reversed(range(n)):
        for j in range(i+1):
            print('*',end='')
        print()

def starFormation3(n):
    starFormation1(n//2)
    starFormation2(n//2 + 1)

starFormation3(7)


