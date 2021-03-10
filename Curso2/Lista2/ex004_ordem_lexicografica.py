def  primeiro_lex(lista):
    d = lista[0]
    for i in range(len(lista)):
        if lista[i] < d :
            d = lista[i]
    return d