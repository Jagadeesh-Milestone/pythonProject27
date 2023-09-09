#while
f=open('python.txt','w')
s='bangalore'
while s=='bangalore':
    s=input('enter a text:')
    f.write(s)
    print('one file created')
f.close()
