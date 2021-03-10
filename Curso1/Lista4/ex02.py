def maior_primo(p):
    n = 0
    while p > 0:
        i = 1
        divisores = 0
        n = 1 + n
        while i <= n:
            if n % i == 0:
                divisores += 1
            i += 1

        if divisores == 2:
            a = n
        p = p - 1
    return a