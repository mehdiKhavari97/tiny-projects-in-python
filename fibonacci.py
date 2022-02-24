def fib(n):
    a = 0
    b = 1
    if n <= 0:
        print("Your entered number cannot be less than 1.")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c

n = int(input("Enter the interation: "))
fib(n)