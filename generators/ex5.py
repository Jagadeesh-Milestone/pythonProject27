def d1(n):
    for i in range(n):
        yield i
print(d1)
d=d1(5)
print(next(d))

