#tell():
f=open('hello.txt','r')
s=f.tell()
print(s)
a=f.read(5)
print(a)
b=f.tell()
print(b)
c=f.read()
print(c)
