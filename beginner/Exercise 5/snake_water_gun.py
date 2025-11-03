import random                                                                                              #picks the random choice

def get_player_choice():                                                                                   #this function is for player
    while True:
        player_choice = input("Enter your choice: snake(s), water(w), gun(g)= ").strip().lower()
        if player_choice in ['s', 'snake']:
            return 'snake'
        elif player_choice in ['w', 'water']:
            return 'water'
        elif player_choice in ['g', 'gun']:
            return 'gun'
        else:
            print("invalid input. Try again")
choice = get_player_choice()
print("You chose:", choice)

import random
def get_computer_choice():
    choices = ['snake', 'water', 'gun']
    random.choice(['snake', 'water', 'gun'])
    coumputer_choice = random.choice(choices)
    return coumputer_choice
for i in range(3):
    print(get_computer_choice())

#step 4
def decide_winner (player, computer):
    if player == computer:
        return "tie"
        
    elif player == "snake":
        if computer == "water":
            return "player"
        if computer == "gun":
            return "computer"
            
    elif player == "water":
        if computer == "gun":
            return "player"
        if computer == "snake":
            return "computer"
            
    elif player == "gun":
        if computer == "snake":
            return "player"
        if computer == "water":
            return "computer"

#step 5 
def print_round_result(player, computer, winner):
    print(f"\n You chose {player.title()}, Computer chose {computer.title()}.")
    
    if winner == "player":
        print("You won this round")
    elif winner == "computer":
        print ("Computer won this round")
    else:
        print("It's a tie")

#step 6
def play_round():
    player = get_player_choice()
    computer = get_computer_choice()
    winner = decide_winner(player, computer)
    print_round_result(player, computer, winner)
    return winner

result = play_round()
print("Winner returned: ", result)

#step 7
def main():
    while True:
        print("\n Welcome to the nske, water and gun game")
        player_score = 0
        computer_score = 0
        ties = 0
        
        rounds = int(input("How many rounds you want  to play?"))
        
        for i in range(rounds):
            print(f"\n ---Round {i + 1} --- ")
            result =   play_round()

            if result == "player":
             player_score += 1
            
            elif result == "computer":
             computer_score += 1
            
            else:
             ties += 1

            print(f"Score: You {player_score} | Computer {computer_score} | Ties {ties}")

        print("\nFinal results")
        print(f"Score: You {player_score} | Computer {computer_score} | Ties {ties}")

        if player_score > computer_score:
            print("You win the game")
        elif computer_score > player_score:
            print("Computer win this game")
        else:
            print("Its a tie")

        
    
