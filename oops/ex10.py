#__init__ method:
#class milestone:
   # def __init__(self,name):
     #   self.name=name
    #def d1(self):
       # print('hi',self.name)
    #def d2(self):
       # print('hello',self.name)
   # def d3(self):
       # print('welcome',self.name)
#obj1=milestone('hari')
#obj1.d1()

#obj2=milestone('jagadeesh')
#obj2.d2()

#obj3=milestone('suresh')
#obj3.d3()

#a class must have only one init method:
class bangalore:
    def __init__(self):
        self.name='jagadeesh'
        print(self.name)
    def __int__(self):
        self.address='bangalore'
        print(self.address)
b=bangalore()
print(b.name)
print(b.address)
