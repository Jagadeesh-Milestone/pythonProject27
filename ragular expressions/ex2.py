#function        description
#findall  --   it returns a list containing all the matches
#search  --  it returns match object if there is a match anywhere
             #in the string
#split   --it returns a list where the string has been split at
           #each match
#sub     --it replaces one or more matches with a string

#findall
import re
text="Hello Python Learners"
x=re.findall("[a-m]",text)
print(x)

text="my age is 25 my contact is 898989877"
y=re.findall("\d",text)
print(y)

text="Hello Java learners"
z=re.findall("\s",text)
print(z)