#flow controls:
#these are used to control the flow of a program:
#if
#else
#elif
#nested if

#loops
#while loop
#for loop

#if:
#if returns true if the given statement is true:
a=10
if a>5:
    print('hello world')

name="jagadeesh"
if name=='jagadeesh':
    print('if block executed')

#number=int(input('enter any number'))
#if number==7878:
  #  print('number is correct')

#else:
#if the if condition is false else will be executed:

a=10
if a<5:
    print('if block executed')
else:
    print('else block executed')

name='hari'
if name=='harii':
    print('name is correct')
else:
    print('name is wrong')

#name=input('enter any name:')
#if name=='jagadeesh':
    #print('correct name')
#else:
   # print('wrong name')

#and:
name='jagadeesh'
password=9090
if name=='jagadeesh' and password==9090:
    print('access granted')
else:
    print('access denied')

#name=input('enter your username:')
#password=int(input('enter your password:'))

#if name=='jagadeesh' and password==890890:
  #  print('hello',name,'login successful')

#else:
   #  print('hello',name,'login failed')

#or
username='jagadeesh'
password=123123
if username=='jagadeesh' or password==123123:
    print('login success')
else:
    print('login failed')



