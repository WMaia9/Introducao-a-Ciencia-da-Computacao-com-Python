def menor_nome(nomes):
    a = []
    b = []
    d = "zzzzzzzzz"
    for c in nomes:
        a = c.lower().strip()
        a = a.capitalize()
        b.append(a)
    for i in range(len(b)):
        if len(b[i]) < len(d) :
            d = b[i]
    return d
