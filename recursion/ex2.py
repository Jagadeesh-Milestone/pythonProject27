#finding recursion limit
import  sys
print(sys.getrecursionlimit())
x=sys.setrecursionlimit(1200)
print(sys.getrecursionlimit())
i=1
def d2():
    global i
    print('d2 function',i)
    i+=1
    d2()
d2()