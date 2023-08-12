#dictionary:
#a dictionary is a collection of keys and value pairs
#it is mutable
#it allows duplicate values
#it dont allow duplicate keys
d={}
print(d)
print(type(d))

#dictionary
a={'username':'jagadeesh','contact':6305134256,'address':'bangalore'}
print(a)
print(type(a))

#keys,values,items
print(a.keys())
print(a.values())
print(a.items())

#add:
a['age']=25
print(a)

#update:
a['contact']=9089880898
print(a)

#duplicate values allowed
b={'name':'hari','address':'hari'}
print(b)

#duplicate keys not allowed:
c={'name':'hari','name':'jagadeesh'}
print(c)

#delete():
b={'name':'hari','address':'hari'}

del b['name']
print(b)

#delete dict
b={'name':'hari','address':'hari'}
#del b
#print(b)

#accessing elements:
b={'name':'hari','address':'hari'}
print(b['address'])
x=b['name']
print(x)
y=b.get('address')
print(y)

#len():
b={'name':'hari','address':'hari'}
print(len(b))

#constructing a dictionary:
c=dict(name='jagadeesh',address='bangalore',contact=898990089)
print(c)

#pop()
c.pop('name')
print(c)

#popitem()
c.popitem()
print(c)