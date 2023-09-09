#unpickling
import pickle
print('unpickling the list')
f=open('java.dat','rb')
s=pickle.load(f)
print(s)
f.close()