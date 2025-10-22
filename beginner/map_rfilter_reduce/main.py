#map function
def cube(x):
    return x * x * x

l = [1, 2, 3, 4, 5]
newList = list(map(cube, l))
print(newList)

#filter Function
def filter_func(b):
    return b > 4

newList1 = list(filter(filter_func, l))
print(newList1)

#reduce function
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x,y: x + y, numbers)
print (sum)