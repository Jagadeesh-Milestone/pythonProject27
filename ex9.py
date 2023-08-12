#comprehensions:
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    if i%2==0:
        print('even number',i)
    else:
        print('odd number',i)
#comprehension is used to concise the code when you want to create
#new sequence from already existing sequence
#list comprehension

x=[i for i in l if i%2==0]
print(x)

y=[i for i in l if i%2==1]
print(y)

#dictionary:
d={}
m=[10,20,30,40,50,60]
for i in m:
    d[i]=i*2
print(d)

#dict comprehension
c={i:i*3 for i in m}
print(c)