def conta_letras(frase, contar="vogais"):
    frase = frase.lower()
    soma = 0
    if contar == "vogais":
        vogais = "aeiou"
        for i in vogais:
            if i in frase:
                soma += frase.count(i)
    elif contar == "consoantes":
        consoante = "qwrtypsdfghjklzxcvbnm"
        for i in consoante:
            if i in frase:
                soma += frase.count(i)
    return soma
