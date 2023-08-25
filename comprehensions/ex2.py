#dict without comprehension
d={}
l=[10,20,30,40]
for i in l:
    d[i]=i*5
print(d)

#dict using comprehension:
x={i:i*2 for i in l}
print(x)
