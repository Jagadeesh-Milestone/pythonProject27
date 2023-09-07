#polymorphism in oops
class bird:
    def fly(self):
        print('some birds can fly some birds cannot fly')
class eagle(bird):
    def fly(self):
        print('eagle can fly at heights')
class parrot(bird):
    def fly(self):
        print('parrot can fly but not at heights')
class ostrich(bird):
    def fly(self):
        print('ostrich cannot fly')
b=bird()
b.fly()
o=ostrich()
o.fly()   #9502711782
b.fly()

p=parrot()
p.fly()
b.fly()

e=eagle()
e.fly()
b.fly()