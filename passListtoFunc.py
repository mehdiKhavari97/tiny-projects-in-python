
def displayLonger5(lst):
    for i in lst:
        if len(i) > 5:
            print(i)


names = []
for i in range(10):
    names.append(input("Enter a name: "))

displayLonger5(names)