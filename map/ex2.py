#map
x=[10,20,30,40,50,60]
y=[2,3,4,5,6]
#print(x*y)
#for i in x:
    #print(i*y)

#using function:
def d2(a,b):
    return a*b
m=map(d2,x,y)
print(list(m))

#using lambda:
x=map(lambda a,b:a*b,x,y)
print(tuple(x))
