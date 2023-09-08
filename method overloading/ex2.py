#method over loading:
#python does not support method overloading
class milestone:
    def d1(self,a,b):
        self.a=a
        self.b=b
        print(self.a)
        print(self.b)
    def d1(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(self.a)
        print(self.b)
        print(self.c)
obj=milestone()
obj.d1(20,30,40)
