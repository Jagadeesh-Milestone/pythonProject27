#multiple errors
try:
    l=[10,20,30,40]
    print(l[0])
    print('statement one')
    print(l[10])
    s={10,20,30,40,50}
    print(s[0])
except Exception:
    print('statement two')



