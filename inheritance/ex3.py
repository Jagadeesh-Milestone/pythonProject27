#multiple inheritance:
class grandparent:
    def d1(self):
        print('grandparent property')
class parent:
    def d2(self):
        print('parent property')
class child(parent,grandparent):
    def d3(self):
        print('child property')
c=child()
c.d1()
c.d2()
c.d3()

