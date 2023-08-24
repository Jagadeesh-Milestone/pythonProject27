#decorators:
#these are the higher order functions
#these are used to add extra functionality to already existing function
#we use @ symbol as a decorator:
def d1(func):
    def d2():
        result=func
        return result+'world'
    return d2()
def d3():
    return 'hello'
d=d1(d3())
print(d)
#using @ annotation
def d1(func):
    def d2():
        result=func()
        return result+'world'
    return d2()
@d1
def d3():
    return 'hello'
d=d3
print(d)


