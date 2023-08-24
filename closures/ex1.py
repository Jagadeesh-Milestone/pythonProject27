#closures:
#a python closure is the higher order function which satisfies the
#following three conditions:
#a function must be taken inside another function:
#a function must be returned:
#a function must be sended to a variable:
def d1():
    name='jagadeesh'
    def d2():
        return name
    return d2()
d=d1()
print(d)

