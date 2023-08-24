#use of closure:
#normal function
def d1():
    print('hello world')
d1()
d1()
del d1
#d1()

#closure function
#even you deleted the actual function we can use its functionality:
def d2():
    def d3():
        return 'hello milestone'
    return d3()
d=d2()
print(d)
del d2
print(d)
print(d)