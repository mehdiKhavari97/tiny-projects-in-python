"""
Method 1
Using a third variable
"""
print("Swap by third variable...")
a = 6
b = 5
print("a before swap: ", a)
print("b before swap: ", b)

#Swap
t = a
a = b
b = t
print("Swap...")
print("a after swap: ", a)
print("b after swap: ", b)
print("\n")


"""
Method 2
Using math
"""
a = 6
b = 5
print("Swap by math functions...")
print("a before swap: ", a)
print("b before swap: ", b)

#Swap
a = a + b
b = a - b
a = a - b
print("Swap...")
print("a after swap: ", a)
print("b after swap: ", b)
print("\n")


"""
Method 3
Using XOR
"""
a = 6
b = 5
print("Swap by XOR...")
print("a before swap: ", a)
print("b before swap: ", b)

#Swap
a = a ^ b
b = a ^ b
a = a ^ b
print("Swap...")
print("a after swap: ", a)
print("b after swap: ", b)
print("\n")


"""
Method 4 (the best)
Using python
"""
a = 6
b = 5
print("Swap by python...")
print("a before swap: ", a)
print("b before swap: ", b)

#Swap
a, b = b, a
print("Swap...")
print("a after swap: ", a)
print("b after swap: ", b)