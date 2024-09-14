import random
import json

# Load all cards into variable
with open('cards.json', 'r') as file:
    data = json.load(file)

# Generate a random number between lower and upper (inclusive) excluding numbers in an array of nums
def random_number(lower: int = 0, upper: int = 0, exclude: list = []):
    # Return if exclude is empty
    if len(exclude) == 0:
        return random.randint(lower, upper)
    elif len(exclude) == 52:
        return -1
    else:
        num = random.randint(lower, upper)
        # Loop until num is a number not in exclude
        while num in exclude:
            num = random.randint(lower, upper)
        return num
    

# Intro
validate = True
while validate:
    intro = input('Welcome to Blackjack! Do you know how to play the game? (yes or no): ')
    if intro == 'freaky':
        print('freaky mode')
    elif intro == 'yes' or intro == 'y':
        validate = False
    elif intro == 'no' or intro == 'n':
        print('https://www.venetianlasvegas.com/resort/casino/table-games/how-to-play-blackjack.html\n')
    else:
        print('Invalid Input; Please enter yes or no\n')

# Hands and totals of the dealer and the player
dealer = []
dealer_total = 0
player = []
player_total = 0

# Deal 2 cards to the player and the dealer
for i in range(0, 2):
    num = random_number(0, len(data) - 1, dealer + player)
    dealer.append(num)
    if data[dealer[i]]["name"] == "Ace":
        dealer_total += data[dealer[i]]["value"][random_number(0, 1)]
    else:
        dealer_total += data[dealer[i]]["value"][0]
    num = random_number(0, len(data) - 1, dealer + player)
    player.append(num)
    player_total += data[player[i]]["value"][0]

def print_options():
    print("""
        Choose an action (1, 2, 3, 5):
        1) Choose Ace values
        2) Check your cards
        3) Hit
        4) Stand
        """)
    return input()


print(f"\nDealer's Cards: {data[dealer[0]]['name']} of {data[dealer[0]]['suit']} and ??")
print(f"Player's Cards: {data[player[0]]['name']} of {data[player[0]]['suit']} and {data[player[1]]['name']} of {data[player[1]]['suit']}")

validate = True
while validate:
    if print_options() == "4":
        validate = False