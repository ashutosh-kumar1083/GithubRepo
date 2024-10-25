import random

def roll():
    min_value = 1
    max_value = 6

    roll_dice = random.randint(min_value, max_value)
    return roll_dice

while True:
    players = input("Enter the number of players: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number of players should be between 2-4!")
    else:
        print("Invalid input. Try again")

print("The number of players is: ", players)

max_score = 15
players_scores = [0 for i in range(players)]

#Test comment added

while max(players_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number",player_idx+1,"'s turn has just started\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y): ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print ("You rolled a 1. Turn Done!")
                current_score = 0
                break
            else:
                current_score += value
                print ("You rolled a: ", value)

            print ("Your current score is: ", current_score)

        players_scores[player_idx] += current_score
        print("Your total score is: ", players_scores[player_idx])
print("End!")