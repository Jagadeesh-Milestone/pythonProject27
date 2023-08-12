#iterators
#int is not an iterable
#x=10
#for i in x:
  #  print(i)

#float is not iterable
#x=10.20
#for i in x:
  #  print(i)

#complex is not iterable
#x=5+6j
#for i in x:
    #print(i)

#string is an iterable
x="hello world"
for i in x:
    print(i)
#list is iterable:
x=[10,20,40,60]
for i in x:
    print(i)
#tuple is iterable:
y=(10,20,40,30)
for i in y:
    print(i)
#set is iterable
z={10,20,30}
for i in z:
    print(i)
#dictionary
dict={'name':'jagadeesh','password':2344}
for i in dict:
    print(i)
for i in dict.values():
    print(i)
#range:
for i in range(10):
    print(i)
#in the above examples list,tuple,dictionary,set,range,string
#all are iterables
#the values assigned to iterables are called iterators
#the process which we are doing is called iteration
