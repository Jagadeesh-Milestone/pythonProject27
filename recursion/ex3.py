#factorial of a number:
def factorial(number):
    result=1
    while number>1:
        result=result*number
        number=number-1
    return result
d=factorial(5)
print('factorial is',d)