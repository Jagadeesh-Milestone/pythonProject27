#file handling
#writing into a file
f=open('hello.txt','w')
s=input('enter a text:')
f.write(s)
print('new file created')
f.close()
