def calculateGmean (a, b):
    gmean = (a*b)/(a+b)
    print (gmean)

def isGreater (a, b):
    if (a>b):
     print("frist number is greater")
    else:
     print("second number is greater or equal")
    
a = 2
b = 3
# if (a>b):
#     print("frist number is greater")
# else:
#     print("second number is greater or equal")
isGreater (a,b)
calculateGmean (a, b)

c = 3
d = 5
isGreater (c,d)
calculateGmean (c, d)