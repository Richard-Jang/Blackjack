import json

# New card in cards.json
def create_card(name, suit, color, value):
	card = {
		"name": name,
		"suit": suit,
		"color": color,
		"value": value,
	}
	return card

# Define suits and a data placeholder
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
data = []

# Iterate over every suit and every card
for suit in suits:
	for number in range(1, 14):
		# Create variable for each characteristic of the card
		name = ""
		value = []
		color = ""

		# Update value and name
		match number:
			case 1:
				name = "Ace"
				value.append(1)
				value.append(11)
			case 11:
				name = "Jack"
				value.append(10)
			case 12:
				name = "Queen"
				value.append(10)
			case 13:
				name = "King"
				value.append(10)
			case _:
				name = str(number)
				value.append(number)
		
		# Update suit and color
		if suit == "clubs" or suit == "spades":
			color = "black"
		else:
			color = "red"
		
		# Add each dictionary (card) to array
		data.append(create_card(name, suit, color, value))

# Write the data to cards.json in JSON format
with open("cards.json", "w") as file:
    json.dump(data, file, indent = 4)