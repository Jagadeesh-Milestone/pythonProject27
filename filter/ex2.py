a=['a','b','c','d','e','f']
for i in a:
    if i in ['a','e','i','o','u']:
        print(i,'is a vowel')

def d1(n):
    return n in ['a','e','i','o','u']
x=filter(d1,a)
print(list(x))

y=filter(lambda m:m in ['a','e','i','o','u'],a)
print(tuple(y))
