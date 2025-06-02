import random

#function to simulate the roll of the dice, it returns numbers from 1 to 6
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

# value = roll()
# print(value) #testing the number

while True:
    players = input("Enter the number of players (2-4): ") #useres enter number of the players

    if players.isdigit():
        players = int(players) #converts strings into integer
        if 2 <= players <=4:
            break #if number of players different from 1 or 4 exit the loop
        else:
            print("It must be between 2 - 4 players")

    else:
        print('Invalid, try again')

max_score = 50
players_scores = [0 for _ in range(players)] #list can change size based on the number of players so every pplayer starts with score == 0

while max(players_scores) < max_score: #to check which player would win the game, main loop of the game

    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, " turn has just started!\n")
        print("Your total score is:", players_scores[player_idx], "\n")
        current_score = 0

        while True:
               should_roll = input("Would you like to roll (y)? ")
               if should_roll.lower() != "y":
                   break

               value = roll()
               if value == 1:
                   print("You rolled a 1! Turn done!")
                   current_score = 0
                   break
               else:
                   current_score += value
                   print("You rolled a: ", value)

               print("Your current score is: ", current_score)

    players_scores[player_idx] += current_score
    print("Your total score is:",players_scores[player_idx])

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player number", winning_idx + 1, " is the winner with a score of: ", max_score)