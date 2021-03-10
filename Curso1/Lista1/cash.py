x = int(input("Enter whith the number of your credit card: "))

z = 0
l = 0
number = x
count = 0
h = x

while h > 0:
    h = h //10
    count = count + 1

while number >= 100:
    number = number // 10

while x > 0:
    y = (x // 10) 
    z = z + (2 * ((y % 10)) // 10) + (2 * ((y % 10)) % 10)
    k = (x % 10)
    l = l + k
    x = x // 100

l = (z + l) % 10

if (l == 0 and (number//10) == 4 and (count == 16 or count == 13)):
    print("VISA")
elif((l == 0 and (number == 51 or number == 52 or number == 53 or number == 54 or number == 55) and (count == 16))):
        print("MASTERCARD")
elif (l == 0 and (number == 34 or number == 37) and (count == 15)):
          print("AMEX")
else:
    print("INVALID")