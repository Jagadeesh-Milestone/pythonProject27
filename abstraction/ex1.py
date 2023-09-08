#abstraction
#hiding the unnecessary information
from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def sides(self):
        print('polygon has many sides')
class square(polygon):
    def sides(self):
        print('a square has four sides')
class triangle(polygon):
    def sides(self):
        print('triangle has three sides')
class pentagon(polygon):
    def sides(self):
        print('pentagon has five sides')
p=pentagon()
p.sides()

t=triangle()
t.sides()

s=square()
s.sides()

p=polygon()
p.sides()