x = int(input("Digite um número inteiro: "))

c = 10

if (x == 0):
    print("não")
else:  
    while (x > 0):
        a = x % 10
        if (a == c):
            print("sim")
            break
        else :
            c = a
            x = x // 10
            if (x == 0):
                print("não")