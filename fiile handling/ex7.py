#seek
f=open('hello.txt','r')
print(f.tell())
print(f.read(10))
f.seek(10)
print(f.read())

