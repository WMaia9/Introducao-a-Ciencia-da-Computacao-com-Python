def fizzbuzz(x):
    y = x % 3
    z = x % 5 

    if (y == 0 and z != 0):
        return "Fizz"

    elif (y != 0 and z == 0):
        return "Buzz"
    elif (y == 0 and z == 0):
        return "FizzBuzz"

    else:
        return x