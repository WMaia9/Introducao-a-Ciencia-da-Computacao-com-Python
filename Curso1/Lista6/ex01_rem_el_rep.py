def remove_repetidos(lista):
    x = []
    for i in lista:
        if (i not in x):
            x.append(i)
    x.sort()
    return x