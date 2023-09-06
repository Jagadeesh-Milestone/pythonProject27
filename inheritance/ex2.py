#multi level inheritance:
class grandparent:
    def d1(self):
        print('i am a grandparent property')
class parent(grandparent):
    def d2(self):
        print('i am a parent property')
class child(parent):
    def d3(self):
        print('i am a child property')
c=child()
c.d3()
c.d2()
c.d1()
p=parent()
p.d2()
p.d1()
g=grandparent()
g.d1()
