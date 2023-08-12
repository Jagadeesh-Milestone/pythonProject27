#decorators:
#decorators are the python functions
#we use @ annotations as a decorators
#decorators are used to add some functionality to already existing
#function
#a function without decorator
def d1(fun):
    def d2():
        result=fun+"world"
        return result
    return d2()
def d3():
    return "hello"
d=d1(d3())
print(d)

#a function with decorator:'
def d4(fun):
    def d5():
        result=fun()
        return result+"python"
    return d5
@d4
def d6():
    return "hello"
d=d6()
print(d)