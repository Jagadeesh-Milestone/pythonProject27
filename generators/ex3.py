#we cant use return in generators
def d1():
    yield 100
    return 200
    yield 300
print(d1())
d=d1()
print(next(d))
print(next(d))