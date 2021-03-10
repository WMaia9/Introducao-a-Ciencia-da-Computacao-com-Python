sequencia = []
i = 1
while (i != 0):
    x = int(input("Digite um número: "))
    sequencia.append(x)
    i = x

tam = len(sequencia) - 1
while tam >= 0:
    if (sequencia [tam]) !=0:
        print(sequencia[tam])
    tam = tam - 1