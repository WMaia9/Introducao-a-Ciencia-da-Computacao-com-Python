# Retângulo

x = int(input("Largura: "))
w = int(input("Altura: "))

y = w
while y > 0:
    z = x
    while z > 0:
        if(y == 1 or y == w):
            print("#", end="")
        elif(z == x or z == 1):
            print("#", end = "")
        else:
            print(" ", end ="")
        z -= 1
    print()    
    y -= 1