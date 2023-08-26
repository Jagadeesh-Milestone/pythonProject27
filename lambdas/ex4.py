#nested lambda :
a=lambda x:(lambda y=30:x+y)
b=a(200)
print(b())