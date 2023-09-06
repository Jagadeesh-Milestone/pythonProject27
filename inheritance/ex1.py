#single inheritance:
class parent:
    def d1(self):
        print('i am a parent property')
class child(parent):
    def d2(self):
        print('i am a child property')
c=child()
c.d2()
c.d1()
p=parent()
p.d1()

