#__init__ method:
class milestone:
    def __init__(self,name):
        self.name=name
    def d1(self):
        print('hi',self.name)
    def d2(self):
        print('hello',self.name)
    def d3(self):
        print('welcome',self.name)
obj1=milestone('hari')
obj1.d1()

obj2=milestone('jagadeesh')
obj2.d2()

obj3=milestone('suresh')
obj3.d3()