try:
    a=10
    b=5
    c=0
    print(a/b)
    print('statement one')
    print(a/c)
except ZeroDivisionError:
    print('statement two')