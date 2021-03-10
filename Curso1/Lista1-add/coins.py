c_str = input("Entre com a moeda: ")
c = float(c_str)

x = 25; y = 10; z = 5; w = 1

t = c//x
c = c%x

t = t + c// y
c = c % y

t = t + c// z
c = c % z

t = t + c // w

print("A quantidade de moeda é: ", t)