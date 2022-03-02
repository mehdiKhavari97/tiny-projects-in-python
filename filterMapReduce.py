from functools import reduce

nums = [1, 56, 89, 45, 12, 6, 75, 40, 8, 9]

evens = list(filter(lambda n : n%2==0, nums))
print("Evens: " ,evens)

increase = list(map(lambda n : n+2, evens))
print("Increase by 2: ", increase)

sum = reduce(lambda a,b: a+b,evens)
print("Sum: ", sum)