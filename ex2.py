#normal function we cant use after it dleleted
def d1():
    return "hello world"
d=d1()
print(d)
print(d)
del d
print(d)

#the use of closure is even-though we deleted the main function
#we can use its functionality.
def d2():
    def d3():
        return " hello python"
    return d3()
x=d2()
print(x)

del d2
print(x)
print(x)