#encapsulation
#wrapping up of attributes and methods into a single entity
class parent:
    def __init__(self):
        self._a=100#protected variable a
class child(parent):
    def __init__(self):
        parent.__init__(self)
        print('a value in parent class',self._a)

        self._a=200
        print('a value in child class',self._a)
c=child()
print(c._a)
b=parent()
print(b._a)


