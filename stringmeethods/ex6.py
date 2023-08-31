#index
a='hello python learners'
print(a.index('p'))
print(a.index('l'))
print(a.rindex('l'))

#translate
d={65:97}
s='Hello Apple'
print(s.translate(d))

#format:
b='my name is {} my address is {}'
c=b.format('milestone','bangalore','hyderabad')
print(c)

d='my name is {1} my address is {0}'
e=d.format('bangalore','jagadeesh')
print(e)

f='my name is {name} my address is {address}'
g=f.format(name='hari',address='hyderabad')
print(g)

h='I have {:,} rupees'
i=h.format(2000000)
print(i)

j='I have {:<5} mangoes'
k=j.format(30)
print(k)

l='I have {:>5} bananas'
m=l.format(50)
print(m)

n='I have {:^5} cherrys'
o=n.format(100)
print(o)

p='the binary format of {0} is {0:b}'
q=p.format(55)
print(q)

r='I have {:d} mangos'
s=r.format(0b111)
print(s)

#reverse:
t="hello world"
print(t[::-1])

for i in reversed(t):
    print(i,end="")

print(tuple(reversed(t)))