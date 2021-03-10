def incomodam(n, lista = ""):
    if n < 0:
        return lista
    else:
        if n == 0:
            return lista
        else:
            return "incomodam " + incomodam(n -1)

def elefantes(n, i = 1):
    if n < 1:
        return ""
    else:
        if i == 1:
            return "Um elefante incomoda muita gente" + (elefantes(n-1, i+1))
        elif n == 1:
            return "\n" + str(i) + " elefantes " +  incomodam(i) + "muita mais"
        else:
            return   "\n" + str(i) + " elefantes " +  incomodam(i) + "muita mais\n" + str(i) + " elefantes incomodam muita gente" + elefantes(n-1, i+1)
