
#write a program to calculate the ebill:
#msg--welcome to BESCOM
#user input for units:
#units 0-100 --ebill free
#units 101-200 --ebill 3/unit
#units 200-300 --ebill 5/unit
#units >300 --ebill 7/unit

#write a program to find whether the entered number is even or odd
#take input from the user
#input/2 --0 --input is even number
#input/2 --1 --input is odd number

#ebill:
#print("Welcome to BESCOM")
#units=int(input('enter no of units consumed:'))
#if units>0 and units<=100:
   # print('ebill is free no need to pay any amount')
#elif units>100 and units<150:
  #  print('ebill is:Rs',units*2)
    #print('pay ',units*2,'by using gpay or phonepe')
#elif units>150 and units<200:
    #print('ebill is:',units*4)
    #print('pay by using gpay or phonepe')
#else:
    #print('ebill is:',units*5)
    #print('pay by using gpay or phonepe')

#even number or odd number:
#num=int(input('enter any number:'))
#if num%2==0:
  #  print(num,'is an even number')
#else:
  #  print(num,'is an odd number')

#l=[1,2,3,4,5,6,7,8,9,10]
#for i in l:
  #  if i%2==1:
      #  print(i,'is an odd number')
    #else:
      #  print(i,'is an even number')

#palindrome:
x=input('enter any value:')
y=reversed(x)
if list(x)==list(y):
    print(x,'is a palindrome')
else:
    print(x,'is not a palindrome')