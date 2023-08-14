#relational operators:
a=10
b=20
print(a<b)#less than
print(a>b)#greater than
print(a<=b)#less than or equals to
print(a>=b)#greater than or equals to
print(a==b)#equals to
print(a!=b)#not equals to

#membership operators:
#these are used to find the occurrence of a value in sequence
x=['hello','bangalore',10,10.2,5+6j]
print('hello' in x)
print(10.2 in x)
print('jagadeesh' in x)

print('hello' not in x)
print(10.2 not in x)
print('jagadeesh' not in x)

s='bangalore'
print('n' in s)
print('z' in s)
print('n' not in s)
print('z' not in s)

#identity operators:
a=100
b=200
print(id(a))
print(id(b))

l=[10,20,30,40]
m=[10,20,30,40]
n=l
print(id(l))
print(id(m))
print(id(n))

print(l is m)
print(m is n)
print(l is n)

print(l is not m)
print(m is not n)
print(l is not n)
print('bitwise operators')
#bitwise operators:
#bitwise and(&)

x=5
y=6
print(x&y)#

print(bin(5))
print(bin(6))
print(bin(4))

#0b101 --5
#0b110 --6
#----------
#0b100 --4
#0b111 --7
print(x|y)
print(bin(7))
