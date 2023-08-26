#comoprehensions:
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    if i%2==0:
        print('even number',i)
    else:
        print('odd number',i)

#using comprehension:
x=[i for i in l if i%2==1]
print(x)
y=[i for i in l if i%2==0]
print(y)