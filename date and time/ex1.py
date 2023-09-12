#date time
import time
x=time.ctime()
print(x)
y=time.localtime()
#weekday full name
a=time.strftime('%A',y)
print(a)
#short form of week day
b=time.strftime('%a',y)
print(b)
#full month name
c=time.strftime('%B',y)
print(c)
#short month name
d=time.strftime('%b',y)
print(d)
#hours 24 hours possible values 00-23
e=time.strftime('%H',y)
print(e)
#day of the year possible values 1-366
f=time.strftime('%j',y)
print(f)
#month of the year possible values 01-12
g=time.strftime('%m',y)
print(g)
#12 hours possible values 00-12
h=time.strftime('%I',y)
print(h)
#am or pm
i=time.strftime('%p',y)
print(i)
#day of the week possible values are 1-7
j=time.strftime('%w',y)
print(j)
#date
k=time.strftime('%x',y)
print(k)
#time
l=time.strftime('%X',y)
print(l)
#short form of year
m=time.strftime('%y',y)
print(m)
#full form of year
n=time.strftime('%Y',y)
print(n)
#time zone
o=time.strftime('%z',y)
print(o)
#date of month
p=time.strftime('%d',y)
print(p)
#week of the year
q=time.strftime('%U',y)
print(q)
#century
r=time.strftime('%C',y)
print(r)