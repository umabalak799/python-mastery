firstOne = input("Enter the first word: ")
secondOne = input("Enter the second word: ")

set1 = set(firstOne)
set2 = set(secondOne)

common = set1 & set2
print("Print the commmon letters of the first and second word: ", common)