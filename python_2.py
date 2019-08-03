# Задание 2
def odometer(N):
    V = 0
    S = 0
    t2 = 0
    for i in range(len(N)):
        if i % 2 == 0:
            V = N[i]
            t = N[i + 1] - t2
            t2 = N[i + 1]
            S = S + V * t
    return S
