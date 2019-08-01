# Задание 2
def odometer(N):
    V = 1
    t = 1
    itog = 0
    for i in range(len(N)):
        if i % 2 == 0:
            V = N[i]
            #print('V -', V)
        elif i % 2 != 0 and i != 0:
            t = N[i] - 1
            #print('t -', t)
        S = V * t
        itog += S 
        #print('S -', S)

    return itog

#print(odometer([10, 1, 20, 2, 30, 3]))
    
