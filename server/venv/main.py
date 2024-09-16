import random
import json
import time
from flask import Flask, request, jsonify
from flask_cors import CORS

# Hands and totals of the dealer and the player
dealer = []
dealer_total = 0
player = []
player_total = 0
action = ""
winner = ""

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

# Deal 2 cards to the player and the dealer
def initial_deal():
    global player, dealer, player_total, dealer_total
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
    global dealer_total, player_total
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

# Draws a card for the player
def hit():
    player.append(random_number(0, len(data) - 1, player + dealer))
    update_totals(True)
    choose_ace_values()
    update_totals()
    if player_total > 21:
        bust(player)

# Ends game and busts the hand over 21
def bust(hand: list):
    global winner
    if hand == player:
        winner = "dealer"
    else:
        winner = "player"
    get_data()

# Allow player to update ace values
def choose_ace_values():
    for card in player:
        if data[card]["name"] == "Ace":
            valid = True
            while valid:
                option = "1"
                match option:
                    case "1":
                        data[card]['value'] = [1]
                        valid = False
                    case "11":
                        data[card]['value'] = [11]
                        valid = False
        update_totals()

# End player's turn, dealer deal to at least 17
def stand():
    global player_total, dealer_total, dealer, winner
    if dealer_total > 21:
        bust(dealer)
    elif dealer_total >= 17:
        if dealer_total > player_total:
            bust(player)
        elif player_total > dealer_total:
            bust(dealer)
        else:
            winner = "tie"
            get_data()
    else:
        while not (dealer_total >= 17 and dealer_total < 21):
            dealer.append(random_number(0, len(data) - 1, player + dealer))
            update_totals()
            print(dealer_total, dealer)
            get_data()

# Counts the number of aces in a given hand
def num_aces(hand: list):
    aces = 0
    for card in hand:
        if data[card]['name'] == 'Ace':
            aces += 1
    return aces

def execute_action():
    match action:
        case "":
            initial_deal()
            update_totals()
        case "hit":
            hit()
        case "stand":
            stand()
        case "aces":
            choose_ace_values()

# COMMUNICATION BETWEEN CLIENT AND SERVER
# COMMUNICATION BETWEEN CLIENT AND SERVER
# COMMUNICATION BETWEEN CLIENT AND SERVER
app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route("/api/data", methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        return receive_data()
    elif request.method == 'GET':
        return get_data()

def receive_data():
    global action, player, dealer, player_total, dealer_total
    # Recieve data from client
    data_r = request.json
    action = data_r['data']['action']
    execute_action()
    return jsonify({"message": "Data received successfully"})


def get_data():
    # print("sent " + str(player_total) + winner)
    return jsonify(
        {
            "dealer": {
                "hand": dealer,
                "total": dealer_total,
            },
            "player": {
                "hand": player,
                "total": player_total
            },
            "action": "",
            "winner": winner,
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=8080)
# DO NOT MODIFY
# DO NOT MODIFY
# DO NOT MODIFY