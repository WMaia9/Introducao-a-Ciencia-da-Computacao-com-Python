def busca(lista, elemento):
    for valor in range(len(lista)):
        if lista[valor] == elemento:
            return valor

    return False