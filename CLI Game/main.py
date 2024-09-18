import random
import json
import time

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
        print("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿
⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⡄⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿
⣿⣿⣷⣄⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡧⠇⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣾⣮⣭⣿⡻⣽⣒⠀⣤⣜⣭⠐⢐⣒⠢⢰⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⡟⣾⣿⠂⢈⢿⣷⣞⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣷⣶⣾⡿⠿⣿⠗⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠋⠉⠑⠀⠀⢘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠟⢹⣿⣿⡇⢀⣶⣶⠴⠶⠀⠀⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⠀⠀⠣⠀⠀⠀⠀⠀⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠹⣿⣧⣀⠀⠀⠀⠀⡀⣴⠁⢘⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿
⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⠗⠂⠄⠀⣴⡟⠀⠀⡃⠀⠉⠉⠟⡿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠾⠛⠂⢹⠀⠀⠀⢡⠀⠀⠀⠀⠀⠙⠛⠿⢿
              """)
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
validate = True

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

# Adds all the values and updates respective totals
# Key of value must contain an array with value of card at index 0
def update_totals(without_aces = False):
    global dealer_total
    global player_total
    dealer_total = 0
    player_total = 0
    for card in dealer:
        dealer_total += data[card]['value'][0]
    if not without_aces:
        for card in player:
            player_total += data[card]['value'][0]
    else:
        for card in player:
            if data[card]['name'] != 'Ace':
                player_total += data[card]['value'][0]


# Print options and return use choice
def print_options():
    print("""\nChoose an action (1, 2, 3, 4):
\t1) Choose Ace values
\t2) Check cards
\t3) Hit
\t4) Stand
""")
    return input()

# Check the dealer's cards and the player's cards
def check_cards():
    player_cards_string = ""
    for card in player:
        player_cards_string += "\t" + data[card]['name'] + " of " + data[card]['suit'] + "\n"
    print("\nDealer's Cards:")
    print(f"\t{data[dealer[0]]['name']} of {data[dealer[0]]['suit']}\n\t??\n")

    print("Player's Cards:")
    print(player_cards_string)

# Draws a card for the player
def hit():
    player.append(random_number(0, len(data) - 1, player + dealer))
    print(f"\nPlayer drew a {data[player[-1]]['name']} of {data[player[-1]]['suit']}!\n")
    update_totals(True)
    print(f"Player's total without Aces: {player_total}")
    choose_ace_values()
    update_totals()
    print(f"Player's total: {player_total}")
    if player_total > 21:
        bust(player)

# Ends game and busts the hand over 21
def bust(hand: list):
    if hand == player:
        print("You lose!")
    else:
        print("You win!")
    global validate
    validate = False

# Allow player to update ace values
def choose_ace_values():
    for card in player:
        if data[card]["name"] == "Ace":
            valid = True
            while valid:
                option = input(f"Value of {data[card]['name']} of {data[card]['suit']}: ")
                match option:
                    case "1":
                        data[card]['value'] = [1]
                        valid = False
                    case "11":
                        data[card]['value'] = [11]
                        valid = False
                    case _:
                        print("Invalid input")
    if num_aces(player) == 0:
        print("No aces found!")
    else:
        update_totals()

# End player's turn, dealer deal to at least 17
def stand():
    global player_total
    global dealer_total
    print(f"Player's total: {player_total}")
    print(f"\nDealer's Cards: {data[dealer[0]]['name']} of {data[dealer[0]]['suit']} and {data[dealer[1]]['name']} of {data[dealer[1]]['suit']}")
    if dealer_total > 21:
        bust(dealer)
    elif dealer_total >= 17:
        time.sleep(0.5)
        check_winner()
    else:
        while not (dealer_total >= 17 and dealer_total < 21):
            dealer.append(random_number(0, len(data) - 1, player + dealer))
            update_totals()
            time.sleep(0.5)
            print(f"Dealer drew a(n) {data[dealer[-1]]['name']} of {data[dealer[-1]]['suit']}!")
        check_winner()

# Counts the number of aces in a given hand
def num_aces(hand: list):
    aces = 0
    for card in hand:
        if data[card]['name'] == 'Ace':
            aces += 1
    return aces

# Determine end result of the game
def check_winner():
    if player_total > dealer_total:
        print("Player Wins!")
    elif player_total < dealer_total:
        print("Player Loses!")
    else:
        print("It's a tie!")

print(f"\nDealer's Cards: {data[dealer[0]]['name']} of {data[dealer[0]]['suit']} and ??")
print(f"Player's Cards: {data[player[0]]['name']} of {data[player[0]]['suit']} and {data[player[1]]['name']} of {data[player[1]]['suit']}")

while validate:
    option = print_options()
    match option:
        case "1":
            choose_ace_values()
        case "2":
            check_cards()
        case "3":
            hit()
        case "4":
            stand()
            validate = False
        case _:
            print("Invalid input")