import random
import json
import time
from flask import Flask, request, jsonify
from flask_cors import CORS

# Hands and totals of the dealer and the player
dealer = []
dealer_total = 0
dealer_paths = []
dealer_aces = []
player = []
player_total = 0
player_paths = []
player_aces = []
values = []
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
    global player, dealer, player_total, dealer_total, dealer_paths, player_paths, winner, action, player_aces, values
    dealer = []
    dealer_total = 0
    dealer_paths = []
    player = []
    player_total = 0
    player_paths = []
    player_aces = []
    values = []
    winner = ""
    action = ""
    for i in range(0, 2):
        num = random_number(0, len(data) - 1, dealer + player)
        dealer.append(num)
        dealer_paths.append(data[num]['path'])
        if data[dealer[i]]["name"] == "Ace":
            dealer_total += data[dealer[i]]["value"][random_number(0, 1)]
        else:
            dealer_total += data[dealer[i]]["value"][0]
        num = random_number(0, len(data) - 1, dealer + player)
        player.append(num)
        player_paths.append(data[num]['path'])
        player_total += data[player[i]]["value"][0]

# Adds all the values and updates respective totals
# Key of value must contain an array with value of card at index 0
def update_totals():
    global dealer_total, player_total
    dealer_total = 0
    player_total = 0
    for card in dealer:
        dealer_total += data[card]['value'][0]
    for card in player:
        player_total += data[card]['value'][0]

# Draws a card for the player
def hit():
    global player, player_paths
    num = random_number(0, len(data) - 1, player + dealer)
    player.append(num)
    player_paths.append(data[num]['path'])
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

# Resets the ace values
def init_aces():
    global player_aces
    player_aces = []
    for card in player:
        if data[card]["name"] == "Ace":
            player_aces.append(card)
            values.append(1)

# Allow player to update ace values
def choose_ace_values():
    global player_aces, values
    for count in range(0, len(player_aces)):
        data[player_aces[count]]['value'] = [values[count]]
        update_totals()

# End player's turn, dealer deal to at least 17
def stand():
    global player_total, dealer_total, dealer, winner, dealer_paths
    while dealer_total < 17:
        num = random_number(0, len(data) - 1, player + dealer)
        dealer.append(num)
        dealer_paths.append(data[num]['path'])
        update_totals()
        get_data()
        time.sleep(0.5)
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
            

# Counts the number of aces in a given hand
def num_aces(hand: list):
    aces = 0
    for card in hand:
        if data[card]['name'] == 'Ace':
            aces += 1
    return aces

# Executes a function based off the action received
def execute_action():
    match action:
        case "initial":
            initial_deal()
            init_aces()
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
    global action, player, dealer, player_total, dealer_total, player_aces, values
    # Recieve data from client
    data_r = request.json
    action = data_r['data']['action']
    if data_r['data']['aces'] != []:
        values = data_r['data']['aces']['values']
        player_aces = data_r['data']['aces']['cards']
    execute_action()
    return jsonify({"message": "Data received successfully"})


def get_data():
    return jsonify(
        {
            "dealer": {
                "hand": dealer,
                "paths": dealer_paths,
                "aces": dealer_aces,
                "total": dealer_total,
            },
            "player": {
                "hand": player,
                "paths": player_paths,
                "aces": player_aces,
                "total": player_total,
            },
            "aces": {
                "cards": player_aces,
                "values": values
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