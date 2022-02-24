#printing the first divisible number by 5 in a list

nums = [26, 59, 37, 12, 15, 46, 75, 85]

for num in nums:
    if num % 5 == 0:
        print("First divisible number : ", num)
        break
else:
    print("There is no divisible number by 5 in this list.")