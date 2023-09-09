#writelines
f=open('list.txt','w')
l=['python','java','html','javascript']
f.writelines(l)
print('one file created')
f.close()