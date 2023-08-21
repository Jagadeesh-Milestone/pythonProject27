#nested functions:
def d1():
    print('hello world')
    def d2():
        print('hello python')
    d2()
d1()

#d1 is the outer function
#d2 is the inner function