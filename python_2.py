# Задание 2
def odometer(N):
    V = 0
    S = 0
    t = 0
    for i in range(len(N)):
        if i % 2 == 0:
            V = V + N[i]
            #print(i + 1, '- итерация, V (Скорость) -', V)
        elif i % 2 != 0 and i != 0:
            t = N[i]
            #print(i + 1, '- итерация, t (Время) -', t)
        #print('')
    S = V * t
    #print('S (Расстояние) -', S)
    return S

#print(odometer([20,2,30,6,10,7]))

    
