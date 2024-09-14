import random
import json

# Load all cards into variable
with open("cards.json", "r") as file:
    data = json.load(file)

# Generate a random number between lower and upper (inclusive) excluding numbers in an array of nums
def random_number(lower: int = 0, upper: int = 0, exclude: list = []):
    # Return if exclude is empty
    if len(exclude) == 0:
        return random.randint(lower, upper)
    else:
        num = random.randint(lower, upper)
        # Loop until num is a number not in exclude
        while num in exclude:
            print("swapped")
            num = random.randint(lower, upper)
        return [num]

validate = True
while validate:
    intro = input("Welcome to Blackjack! Do you know how to play the game? (yes or no): ")
    if intro == "freaky":
        print("""
            I been a nasty girl, nasty
            `I been a nasty girl, nasty
            I been a nasty girl, nasty
            I been a nasty, nasty, nasty
            Is somebody gonna match my freak?
            Is somebody gonna match my freak?
            Is somebody gonna match my nasty?
            I got stamina, they say I'm a athlete
            Is somebody gonna match my freak?
            Need somebody with a good technique
            Is somebody gonna match my nasty?
            Pillow talking got my throat raspy
            If you keep up with me
            I'll keep on coming back
            If you do it too good
            I'm gonna get attached
            'Cause it feels like heaven when it hurts so bad
            Baby, put it on me
            I like it just like that
            Just like that
            I been a nasty girl, nasty
            I been a nasty girl, nasty (just like that)
            I been a nasty girl, nasty
            I been a nasty, nasty, nasty (I like it just like that)
            I been a nasty girl, nasty
            I been a nasty girl, nasty (just like that)
            I been a nasty girl, nasty
            I been a nasty, nasty, nasty
            Big time, pull up, make a scene
            Party's lame, no vibe, we can leave
            Shotgun, my thighs on the seat
            I ain't got nothing underneath
            Looks like, you 'bout to spend the night
            Looks like, I'm 'bout to change your life
            Wife type, he's staying for the week
            So I might just let him pay the lease
            If you keep up with me
            I'll keep on coming back
            If you do it too good
            I'm gonna get attached
            'Cause it feels like heaven when it hurts so bad
            Baby, put it on me
            I like it just like that
            Just like that
            I been a nasty girl, nasty
            I been a nasty girl, nasty (just like that)
            I been a nasty girl, nasty
            I been a nasty, nasty, nasty (I like it just like that)
            I been a nasty girl, nasty
            I been a nasty girl, nasty (just like that)
            I been a nasty girl, nasty
            I been a nasty, nasty, nasty
            If you keep up with me
            I'll keep on coming back
            If you do it too good
            I'm gonna get attached
            'Cause it feels like heaven when it hurts so bad
            Baby, put it on me
            I like it just like that`
            Just like that
        """)
    elif intro == "yes" or intro == "y":
        validate = False
    elif intro == "no" or intro == "n":
        print("https://www.venetianlasvegas.com/resort/casino/table-games/how-to-play-blackjack.html\n")
    else:
        print("Invalid Input; Please enter yes or no\n")

dealer = [random_number()]