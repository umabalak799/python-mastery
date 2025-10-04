num = list(map(int,input("Enter the numbers: ").split()))

total = sum(num)
average = total / len(num)

print("Numbers in the list: ", num)
print("Sum = ", total)
print("Average = ", average)

# num = list(map(int,input("Enter the numbers: ").split()))

# smallest = num[0]

# for numbers in num:
#     if numbers < smallest:
#         smallest = numbers

# print("The smallest number is: ", smallest)