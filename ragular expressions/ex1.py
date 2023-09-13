#regular expressions
#it is a sequence of characters that forms a search pattern
#it is used to check if a string contains the specified search
#pattern
#to use regex we have to import module/package named re
import re
text="Hello Python Learners"
x=re.search("^Hello",text)
if x:
    print('there is a match')
else:
    print('no match')

y=re.search('Learners$',text)
if y:
    print('there is a one match ')
else:
    print('there is no match')
