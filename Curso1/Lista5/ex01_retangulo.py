# Retângulo

x = int(input("Largura: "))
y = int(input("Altura: "))

while y > 0:
    z = x
    while z > 0:
        print("#", end="")
        z -= 1
    print()    
    y -= 1