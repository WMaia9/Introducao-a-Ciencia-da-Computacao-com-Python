def maior_elemento(lista):
    x = -9999
    for i in lista:
        if (x < i):
            x = i
    return x
