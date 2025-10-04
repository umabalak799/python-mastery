import random

print("Welcome to Kaun Banega Crorepati.")
print("Answer the questions correctly to win 1000000")

def playKbc(): #function

    questions = [   #contains all the questions and its options 
        {
            "question": "What is the capital of India",
            "options": ["A. Delhi", "B. Bangalore", "C. Chennai", "D. Mumbai"],
            "answer": "A"

        },{
            "question": "Who is the leader of TVK",
            "options": ["A. Thalapathy", "B. Joesph Vijay", "C. Actor Vijay", "D. All of the above"],
            "answer": "D"
        },{
            "question": "What do Uma like the most in sweets",
            "options": ["A. Gulab Jamun", "B. Jalebi", "C. Ice Cream", "D. Rasgulla"],
            "answer": "C"
        },{
            "question": "Who invented light",
            "options": ["A. Prema", "B. Selvi", "C. Thomas Edison", "D. Venky"],
            "answer": "C"
        }
        
    ]

    money_won = 0 #it sets the starting money of the player to zero
    prize_amount = [0, 100000, 300000, 600000, 1000000] #the list which stores the money for each level

    
    for i, data in enumerate(questions):  #this is a - for loop which will run all the question one by one using enumerate function
        print(f"\nQuestion {i + 1}:")     #prints the 1st ques and then 2nd and so on
        print(data["question"])           #prints the text of the question
        for option in data["options"]:    #loops through all the option
            print(option)                 #prints the options
        
        userAnswer = input("Enter your answer: ").upper()                    #user enter the answer

        if userAnswer == data['answer']:                                     #checks the answer
            print("Correct Answer")                                          #if correct prints this one
            money_won = prize_amount[min(i + 1, len(prize_amount) - 1)]      #Calculate the money won by the user at that round 

            print(f"You have won: {money_won} rupees")                       #prints the money won by the user

        else:
            print(f"Incorrect. The correct answer was {data['answer']}")     #if user eneter the incorrect ans then its prints this code 
            print("Game Over")
            break                                                            #and also it will break the If loop and the code execution will end
    
    else:
        print(f"Congratulations You have answered all the questions correctly")     #this is end of the For loop and this will be executed only if
        print(f"Total Money won: {money_won}"  )                                    #the user answer the all questions correctly
                                                                             
if __name__ == "__main__":                          
    playKbc()

    