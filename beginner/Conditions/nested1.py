num = int(input("Enter the number: "))

if (num == 0):
    print("Okay")
elif (num > 0):
    if (num <= 10):
        print("nice")
    elif (num > 10 and num < 20):
        print ("perfect")
    else:
        print ("not good")
else:
    print("not fine")