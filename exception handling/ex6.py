#raise an error
number=int(input('enter any number:'))
if number<0:
    raise Exception('number must be positive')
print(number)

print('hello world')