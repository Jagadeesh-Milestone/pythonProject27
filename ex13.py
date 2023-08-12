#sequences:
#list:
#a list is a collection of data and this data may be any type:
#list allows index calling and index slicing
#list allows duplicate values
#list is mutable meaning that once we create a list we can change
#the data
#list is taken in []
l=[10,10.2,5+6j,True,"bangalore"]
print(l)
print(type(l))

#list allows duplicate values
a=[10,20,30,10,20,10]
print(a)

#len():
#it is used to find the no of values in a list
b=[10,20,30,40,50]
print(len(b))

#count():
#it is used to find the no of appearances of an element
c=[10,20,30,10,20,10]
print(c.count(10))
print(c.count(100))

#append():
#it is used to add an element at the end of a list:
d=[100,200,300,400]
d.append(500)
print(d)

#pop():
#it is used to delete an element from the list:
e=[10,20,30,40]
e.pop()
print(e)
e.pop(1)
print(e)

#index():
#the index position of first element is 0,second element is 1..
f=[10,20,30,40]
print(f.index(10))
print(f.index(20))
#print(f.index(100))
print(f[0])
print(f[1])
#print(f[10])

#negative indexing:
#the negative index of last element is -1,..
g=[10,20,30,30]
print(g[-1])
print(g[-2])
#print(g[-5])

#copy():
#it is used to copy the list elements:
h=[100,200,300,400]
i=h.copy()
print(i)

#extend():
#it is used to add multiple elements at the end of a list:
j=[10,20,30,90]
j.extend([100,200,300])
print(j)

#insert():
#it is used to insert an element at particular position:
k=[10,20,40,50]
k.insert(2,30)
print(k)

#remove():
#it is used to remove an element from the list:
l=[10,20,30,40]
l.remove(20)
print(l)

#reverse():
#it is used to reverse the list elements:
m=[10,20,30,40]
m.reverse()
print(m)

#clear():
#it is used to clear the list elements
n=[100,200,300]
n.clear()
print(n)

#sort():
#it is used to print the list elements in ascending or descending order
o=[10,50,20,40,30,70]
o.sort(reverse=False)
print(o)

o.sort(reverse=True)
print(o)

