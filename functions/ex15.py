#functions as an arguments:
def d1(a,b):
    return  'hello world',a,b
def d2(c):
    return  'hello milestone',c
def d3():
    return 'hello python'
d=d1(d3(),d3())
print(d)

m=d1(d2(d3()),d2(d3()))
print(m)