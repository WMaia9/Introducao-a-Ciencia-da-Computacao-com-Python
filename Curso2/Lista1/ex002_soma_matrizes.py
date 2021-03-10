def soma_matrizes(m1, m2):
    soma = []
    if ((len(m1), len(m1[0])) != (len(m2), len(m2[0]))):
        return False
    else:
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                soma = m1[i][j] + m2[i][j]
    return soma