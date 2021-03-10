def ordenada(lista):
    ordem = lista[0]
    for valores in lista:
        if valores < ordem:
            return False
        else:
            ordem = valores
    return True