number = 4

def factorial(number):

    if number == 1:
        return 1

    return number * factorial(number-1)

result = factorial(number)
print(result)