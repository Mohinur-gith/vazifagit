import math as mt
n = int(input(' n = '))
i = 1
a = int(input('a = '))
k = a
while i < n:
    i += 1
    b = int(input('a = '))
    k *= b
    while True:
        if a > b:
            a = a - b
        elif a < b:
            b = b - a
        else:
            break
    k /= a
    a = k
print(" ekuk ", k)
