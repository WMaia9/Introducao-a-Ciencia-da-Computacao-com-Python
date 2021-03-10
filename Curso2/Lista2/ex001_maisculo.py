def maiusculas(frase):
    b = ""
    for c in frase:
        if c >= 'A' and c <= 'Z':
            b = b + c
    return b 
