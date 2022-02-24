
a = 10
b = 16

def something():
    # gloabl a >> it is a way of access to global a out of the function
    a = 9
    x = globals()['a']
    print("ID x: ", id(x))
    print("ID a in fun: ", id(a))
    print("a in fun: ", a)
    print("x in fun: ", x)

something()
print("ID a out of fun: ", id(a))
print("a out of fun: ", a)

