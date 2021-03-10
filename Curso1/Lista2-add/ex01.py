import math

x1 = float(input("Entre com o valor de x1: "))
y1 = float(input("Entre com o valor de y1: "))
x2 = float(input("Entre com o valor de x2: "))
y2 = float(input("Entre com o valor de xy: "))

d = math.sqrt((x1 - y1)**2 + (x2 - y2)**2)

if(d >= 10):
    print("longe")
else:
    print("perto")