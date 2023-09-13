#search
import re

text="Hello python learners"
x=re.search('\s',text)
print('the first white space character located at',x.start())

text='hello bangalore'
y=re.search('hyderabad',text)
print(y)

z=re.findall('hyderabad',text)
print(z)