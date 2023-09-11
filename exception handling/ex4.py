try:
    l = [10, 20, 30, 40]
    print(l[0])
    print('statement one')
    print(l[2])
    s = {10, 20, 30, 40, 50}
    print(s)
except Exception:
    print('statement two')
else:
    print('statement three')

#if there are any errors exception block will be executed
#if there are no errors else block will be executed
