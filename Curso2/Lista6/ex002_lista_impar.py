def encontra_impares(lista, impar=[]):
    
    if lista == []:
        return impar
    else:
        if lista[0] % 2 == 0:
            return encontra_impares(lista[1:])
        else:
            impar.append(lista[0])
            return encontra_impares(lista[1:])