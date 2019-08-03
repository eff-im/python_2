# Задание 2
def odometer(N):
    S = 0
    for i in range(len(N)):
        if i % 2 == 0 and i != 0:
            S = S + (N[i] * N[i + 1])
            #print(S)
    S = S + (N[0] * N[1])
    #print('S (Расстояние) -', S)
    return S

#print(odometer([20,2,30,6,10,7]))

    
