#find the no of digits in a given number:
number=int(input('please enter any number:'))
count=0
while number!=0:
    number//=10
    count+=1
print('the no of digits are',count)

