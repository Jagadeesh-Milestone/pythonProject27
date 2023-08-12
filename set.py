#set :
#set is a collection of data and this data may be any type
#it is having unordered elements
#it is mutable
#it dont allow index calling and index slicing
#it is taken in {}
#it dont allow duplicates
s={10,10.5,"hello",True}
print(s)
print(type(s))

#it dont allow duplicates
a={10,20,30,10,20,10}
print(a)

#it dont allow index calling
b={1,2,3,4}
#print(b[0])
#print(b.index(2))

#len():
c={10,20,1,2,3,10,20}
print(len(c))

#count():
d={10,20,30,10,20,10}
#print(d.count(10))

#add():
e={10,20,30,40}
e.add("hello")
print(e)

#pop():
f={10,20,1,2,3,10,20}
f.pop()
print(f)

#remove():
g={10,20,30,40}
g.remove(20)
print(g)

#discard():
h={100,200,300}
h.discard(200)
print(h)

#difference b/w remove and discard
i={100,200,300,400,500}
#i.remove(1000)
#print(i)

i.discard(1000)
print(i)

#subset():
j={10,20,30}
k={10,20,30,40,50}
l={10,20,40,100}
print(j.issubset(k))
print(l.issubset(k))

#superset():
m={10,20,30}
n={1,2,3,4}
o={1,2,3,4}
print(m.issuperset(n))
print(o.issuperset(n))

#difference():
p={10,20,30,50}
q={10,20,40}
print(p.difference(q))

#union():
r={1,2,3,4}
s={5,6,7}
print(r.union(s))

#intersection():
t={10,20,30,40}
u={10,20,100,200}
print(t.intersection(u))

#clear:
d={100,200,300}
d.clear()
print(d)

#copy():
u={10,20,30}
v=u.copy()
print(v)

#update():
w={100,200,300}
w.update([10])
print(w)
