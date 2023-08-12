#tuple:
#it is the collection of data and this data may be any type
#tuple allows index calling and index slicing
#tuple allows duplicate values
#tuple is immutable meaning that once we create a tuple we cant
#modify the data.
#tuple is taken in ():
t=(10,20,30,40)
print(t)
print(type(t))

#it allows duplicate values
a=(10,20,10,20,10)
print(a)

#count()
b=(10,20,10,10,10)
print(b.count(10))

#len():
c=(1,2,4,4,56,8)
print(len(c))

#append:
d=(10,20,30,40)
#d.append(100)
#print(d)

#concatenation:
#Adding a tuple to another tuple is called concatenation
e=(10,20,40,50)
f=(100,200,300,400)
print(e+f)
print(e+(100,200))
#we cant concatenate a tuple to list or a list to tuple

#index calling
m=(10,20,30,40)
print(m[0])
print(m.index(20))

x=(10)
print(x)
print(type(x))#integer

y=(10,)
print(y)
print(type(y))#tuple