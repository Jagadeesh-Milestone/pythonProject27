class milestone:
    myname='jagadeesh'

t=milestone()
print(id(t))
m=milestone()
print(id(m))

k=milestone.myname
print(id(k))
l=milestone.myname
print(id(l))