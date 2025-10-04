x = int(input("Enter the number: "))

match x:
    case 0:
        print ("x is zero")
    case _ if x < 5:
        print ("Lesser than five")
    
    case _ if x == 5:
        print("x is odd number")

    case _:
        print(x)
5
