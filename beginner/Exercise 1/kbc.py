# this is the list of questions
questions = [
    ["Which city is know as the city of dreams", "Mumbai", "Chennai", "Bangalore", "Kolkata", 0],
    
    ["A farmer has 17 goats. All of them but 8 die. How many goats are alive?", "8", "9",
     "25", "35", 0],

    ["What is the Capital of Mumbai", "Bandra", "Dharavi", "Chembur", "CST", 3],

    ["Who is the PM of India", "Modi", "Rahul Gandhi", "Stalin", "Arvind Kejriwal", 0]

]

# this line contains prize amount for each questions
levels = [1000, 2000, 3000, 4000]

# this variable stores how much money does the player has won
money = 0
# loops through each question (So i takes values 0, 1, 2, 3.) lens(questions) gives the total no of questions 
for i in range (0, len(questions)):

    # displays the questions and options
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a. {question[1]}          b. {question[2]}")
    print(f"c. {question[3]}          d. {question[4]}")

    # This line asks the player to enter a number between 1 and 4.
    reply = int(input("Enter your answer(1-4): "))

    # Check the answer
    if (reply - 1) == question[-1]:
        print(f"Correct answer, you have won Rs. {levels[i]}")
        

    else:
        print("Wrong answer")
        break

