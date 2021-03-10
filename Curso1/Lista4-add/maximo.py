def maximo(x,y,z):
    if (x > y and x > z):
        resultado = x
    elif (y > z and y > x):
        resultado = y
    else:
        resultado = z
    return resultado
