#*args
#if you dont know how many values you are passing then just put
#a * before the argument name:

def d1(*students):
    print(students)
    print('tallest student is',students[1])
d1('hari','manoj','suresh')