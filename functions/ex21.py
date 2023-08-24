#non local keyword
def d1():
    name='jagadeesh'
    def d2():
        nonlocal name
        name='ganesh'
        return name
    print(d2())
    print(name)
d1()