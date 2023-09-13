#split:
import re
text="hello python hello java"
x=re.split("\s",text)
print(x)

y=re.split('\s',text,2)
print(y)

#sub
text='Hello python Hello java'
z=re.sub('\s','jagadeesh',text)
print(z)

a=re.sub('\s','hari',text,2)
print(a)