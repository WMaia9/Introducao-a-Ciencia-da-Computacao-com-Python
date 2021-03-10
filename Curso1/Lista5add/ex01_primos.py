def n_primos(x):
    y = 0
    while x >= 2:
        divisores = 0
        i = 1
        while i <= x:
            if x % i == 0:
                divisores += 1
            i = i + 1
        if divisores == 2:
            y = y+1
        x = x - 1
    return y
