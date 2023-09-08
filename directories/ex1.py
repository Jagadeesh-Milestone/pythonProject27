#directories
import os
#get current working directory
a=os.getcwd()
print(a)

#create new directory
#b=os.mkdir('java')
#print(b)

#create a sub folder:
#c=os.mkdir('java/java')
#print(c)

#rename a folder:
#d=os.rename('java','bangalore')
#print(d)

#delete a sub folder
#e=os.rmdir('bangalore/java')
#print(e)

#delete folder
f=os.rmdir('bangalore')
print(f)

