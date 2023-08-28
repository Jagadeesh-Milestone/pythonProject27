#reversing the strings in a list:
l=['apple','banana','mango','cherry']
#l.reverse()
#print(l)

for i in l:
    print(i[::-1])

def d1(n):
    return n[::-1]
x=map(d1,l)
print(list(x))

y=map(lambda m:m[::-1],l)
print(tuple(y))