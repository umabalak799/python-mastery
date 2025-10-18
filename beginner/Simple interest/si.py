def calculate_si(principal, rate, time):                                              #creating function
    simpleInterest = (principal*rate*time) / 100                                      #formula
    return simpleInterest                                                             #returns SI
try:                                                                                  #used to run a code that might cause an error
    principal = float(input("Enter the principal amount: "))                          #enter the principal amnt, rate of int, no of of years or time
    rate = float(input("Enter the interest rate: "))
    time = float(input("Enter the time in years: "))
    calculateSimpleInterest = calculate_si(principal, rate, time)                     #Calculates the SI

    print(f"\n The simple interest is: {calculateSimpleInterest}")                    #prints the calculated SI

except ValueError:                                                                    #if the try block code gives any error then this  
    print("Inavlid input")                                                            #except code will be executed and it prunt this statement
     



