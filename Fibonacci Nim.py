# This program is a simple fabonacci nim game
# Start with random coins
# The one who takes the last coin wins
# Authors: john samy roshdy
# ID: 20210108
# Version: 1.0

# random number of cions
import random
turn = 0
number_of_coins=random.randint(2,1000)
previous_move = None

def player_input(player_name,max_coins):
    print(f"You can take up to {max_coins} coins")
    player_take = int(input(f"{player_name}: "))
#check if the player take number of coins > number of coins he can taken
    while player_take > max_coins:
        print("Wrong choice, please try again.")
        player_take = int(input(f"{player_name}: "))

    return player_take

def player_take(max_coins):
        global turn, previous_move,number_of_coins
        print("Remaining coins: ",number_of_coins)
        player = turn % 2 + 1                  #switch player
        move = player_input(f'Player {player}',max_coins)
        number_of_coins-=move
# check wins
        if number_of_coins==0:
            print(f'Player {player} wins')
            return True

        turn += 1
        previous_move = move
        return False

player_take(number_of_coins - 1)

while True:

    if player_take(min(number_of_coins, previous_move * 2)):
        break

print("Game over! ")









