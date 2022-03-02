# passing multiple variables as arguments to a function
# *v means v is a tuple
def sum(*v):
    c =0
    for i in v:
        c = c + i
    return c


print(sum(1, 5, 9, 58, 65))

# passing multiple variables with keys as arguments to a function
def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,":",j)


person("Mehdi", age=24, city="Malmo", phone=738980755)