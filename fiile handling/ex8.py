#pickling:
import pickle
print('pickling the list')
f=open('java.dat','wb')
l=['a','b','c','d']
x=pickle.dump(l,f)
print(x)
f.close()
