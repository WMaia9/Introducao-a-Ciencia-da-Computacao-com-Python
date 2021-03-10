import math

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

delta = ((b**2) - (4*a*c))

if (delta < 0):
    print("esta equação não possui raízes reais")
else:
    if (delta == 0):
        raiz = - b / (2 * a)
        print("a raiz desta equação é", raiz)

    else:
        raiz1 = (- b + math.sqrt(delta)) / (2 * a)
        raiz2 = (- b - math.sqrt(delta)) / (2 * a)
        print("as raízes da equação são", raiz2, "e", raiz1)