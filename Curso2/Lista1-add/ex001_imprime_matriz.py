def imprime_matriz(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            if (coluna == len(matriz[0]) - 1):
                print(matriz[linha][coluna])
            else:
                print(matriz[linha][coluna], end = " ")
    return
