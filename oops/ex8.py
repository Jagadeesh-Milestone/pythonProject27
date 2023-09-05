#classmethod/instancemethod/staticmethod
class milestone:
    myname='jagadeesh'
    def d1(self,friendname):
        print(friendname,'and',self.myname)

    @staticmethod
    def d2(friendname):
        print(friendname,'and',milestone.myname)

    @classmethod
    def d3(cls,friendname):
        print(friendname,'and',cls.myname)

obj=milestone()
obj.d1('hari')
obj.d2('suresh')
obj.d3('naresh')

