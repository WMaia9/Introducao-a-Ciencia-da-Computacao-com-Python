import math

def soma_hipotenusas(x):
    cont = 0
    while (x > 0):
        cont += é_hipotenusa(x)
        x -= 1
    return cont

def é_hipotenusa(x):
    a = 1
    while(a < x):
        b = 1
        while(b < a):
            z = math.sqrt(a**2 + b**2)
            if (z % x == 0):
                return x
            b += 1
        a += 1
    return 0
