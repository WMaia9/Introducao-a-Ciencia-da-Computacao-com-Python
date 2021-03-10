n = int(input("Digite um número inteiro: "))
a = 0
while (n > 0):
    a += n % 10
    n //= 10

print(a)
