#elif:
#it is used to check the multiple conditions at a time:
game="hocky"
if game=='foot ball':
    print('i dont like',game)
elif game=='hockey':
    print('i dont like',game)
elif game=='kabaddi':
    print('i dont like',game)
elif game=='cricket':
    print('i love to play',game)
else:
    print('i like to play cricket only')
name=input('enter your name:')
if name=='hari':
    print('hello hari')
elif name=='jagadeesh':
    print('hi jagadeesh')
elif name=='manoj':
    print('welcome',name)
else:
   print('your name not in list')

#nested if:
x=100
if x<110:
    print('first condition true')
    if x<150:
        print('second condition also true')
        if x>50:
            print('third condition is true')
            if x>200:
                print('fourth condition is true')
            else:
                print('fourth condition is false')
                if x==100:
                    print('fifth condition is true')

