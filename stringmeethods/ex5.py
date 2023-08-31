#\n newline
a='hello \npython \nlearners'
print(a)

#\t tab
b='hello\tpython\t\t\tlearners'
print(b)

#isprintable
c='hello98789*&&*'
print(c.isprintable())
d='hello\t98789\n*&&*'
print(d.isprintable())

#ljust
e='hello'
f=e.ljust(20)
print(f,'python learners')
g=e.rjust(20)
print(g,'java learners')

#partition
h='hello python learnears'
print(h.partition('p'))
print(h.rpartition('l'))

