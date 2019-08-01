# Задание 2
def odometer(N):
    V = 1
    t = 1
    for i in range(len(N)):
        if i % 2 == 0:
            V = N[i]
            #print('V -', V)
        else:
            t = N[i]
            #print('t -', t)
        S = V * t
        #print('S -', S)

    return S

#print(odometer([10,1,20,2,30,3]))
    
