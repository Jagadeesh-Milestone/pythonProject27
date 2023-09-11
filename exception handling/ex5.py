try:
    l = [10, 20, 30, 40]
    print(l[0])
    print('statement one')
    print(l[12])
    s = {10, 20, 30, 40, 50}
    print(s)
except Exception:
    print('exception block')
else:
    print('else block')
finally:
    print('finally block')
#finally block will be executed even there are errors or no errors
