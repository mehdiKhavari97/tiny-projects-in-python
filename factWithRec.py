
def fact(n):
    if n < 0:
        print("Your entered number cannot be minus.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

n = int(input("Enter a number to calculate the factorial: "))
print(fact(n))