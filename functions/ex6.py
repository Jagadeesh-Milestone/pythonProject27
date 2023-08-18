#default arguments:
#we can pass default value to the arguments.If you pass a value
#it will be taken or the default value will be taken:
def d1(country='India'):
    print('I am from',country)
d1('australia')
d1()
d1('england')
d1()

def d2(a,b=100):
    print(a+b)
d2(30,50)
d2(60)