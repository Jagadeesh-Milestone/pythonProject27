#changing recursion limit:
import sys
print(sys.getrecursionlimit())
x=sys.setrecursionlimit(1200)
print(sys.getrecursionlimit())
i=1
def d1():
    global i
    print("hello milestone",i)
    i+=1
    d1()
d1()
