
def factorial(n):
    if n < 0:
        print("Your entered number cannot be minus.")
    elif n == 0 or n == 1:
        print(1)
    else:
        r = 1
        for i in range(1, n+1):
            r = r * i
        print(r)

n = int(input("Enter a number to calculate the factorial: "))
factorial(n)