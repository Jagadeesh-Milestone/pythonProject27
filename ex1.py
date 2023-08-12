#closures:
#a closure is a python function which satisfies the following
#three conditions:
#a function must be taken inside another function
#a function must be returned
#a function is sent to a variable:
def d1():
    def d2():
        return "hello world"
    return d2()
d=d1()
print(d)

