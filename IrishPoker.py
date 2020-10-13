##############################################################################
# This section of code introduces the game, gets number of players, validates
# the input, and creates/initializes the lists for the deck and players

# have names as input and put in list and refer to list
# have loop asking if want to play again

import random

print("Welcome to Irish Poker! \n")
valid_num_players = False

while not valid_num_players:
    num_players = int(input("(Maximum of 12 Players)\nEnter the number of players: "))
    if 1 < num_players <= 8:
        valid_num_players = True
    else:
        print("\nSorry! Must have at least 2 players and no more than 12!")

# IMPLEMENT NAME - assign to list and use counters and variable to appropriately know who is playing each time

values = [2, 3, 4, 5, 6, 7, 8, 9, 10,
          "Jack", "Queen", "King", "Ace"]
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
deck = []
players = []
played_cards = []
round_counter = 0
current_card = None
incorrect_points = [0] * num_players
round_boolean = False
riding_bus = False


##############################################################################
# this section of code creates all of the necessary functions for game play

# can check values and suits using if string in
def create_deck():
    for suit in suits:
        for value in values:
            deck.append(f"{value} of {suit}")


def create_game():
    create_deck()

    for a in range(num_players):
        individual_player_list = []
        players.append(individual_player_list)


def shuffle_deck():
    random.shuffle(deck)


def deal_cards():
    shuffle_deck()
    for b in range(4):
        for player in range(len(players)):
            dealt_card = deck.pop()
            players[player].append(dealt_card)


def reset_deck():
    deck.clear()
    create_deck()
    shuffle_deck()


def return_int_value(card):
    card_num = card[:2]
    card_num.rstrip()
    if card_num == "Ja":
        answer = 11
    elif card_num == "Qu":
        answer = 12
    elif card_num == "Ki":
        answer = 13
    elif card_num == "Ac":
        answer = 1
    else:
        answer = int(card_num)

    return answer


def red_or_black(guess):
    if current_card.find("Diamonds") != -1 or current_card.find("Hearts") != -1:
        answer = "red"
    else:
        answer = "black"

    if guess.lower() == answer:
        return True
    else:
        return False


# NOT WORKING -- FIX LOGIC ERROR
def higher_or_lower(guess):
    current = return_int_value(played_cards[round_counter])
    if riding_bus:
        previous = return_int_value(played_cards[round_counter - 1])
    else:
        previous = return_int_value(played_cards[round_counter - 2])

    if current > previous:
        answer = "higher"
    elif current < previous:
        answer = "lower"
    else:
        answer = "even"

    if answer == "even":
        return False
    elif guess.lower() == answer:
        return True
    else:
        return False


def inside_or_outside(guess):
    current = return_int_value(played_cards[round_counter])
    if riding_bus:
        previous = return_int_value(played_cards[round_counter - 1])
        initial = return_int_value(played_cards[round_counter - 2])
    else:
        previous = return_int_value(played_cards[round_counter - 2])
        initial = return_int_value(played_cards[round_counter - 4])

    low_range = min(previous, initial)
    high_range = max(previous, initial)

    if low_range < current < high_range:
        answer = "inside"
    elif current < low_range or current > high_range:
        answer = "outside"
    else:
        answer = "even"

    if answer == "even":
        return False
    elif guess.lower() == answer:
        return True
    else:
        return False


def guess_suit(guess):
    if current_card.find("Diamonds") != -1:
        answer = "diamonds"
    elif current_card.find("Hearts") != -1:
        answer = "hearts"
    elif current_card.find("Spades") != -1:
        answer = "spades"
    else:
        answer = "clubs"

    if guess.lower() == answer:
        return True
    else:
        return False


def simulate_round(round_type):
    # implement name
    player_num = 1
    global round_counter
    global current_card
    global incorrect_points
    global round_boolean
    round_boolean = False

    for player in players:
        played_cards.append(player.pop())
        current_card = played_cards[round_counter]
        guess = input(f"\nPlayer {player_num}, guess {round_type}: ")

        if round_type == "Red or Black":
            function = red_or_black(guess)
        elif round_type == "Higher or Lower":
            function = higher_or_lower(guess)
        elif round_type == "Inside or Outside":
            function = inside_or_outside(guess)
        elif round_type == "Suit":
            function = guess_suit(guess)

        if function:
            print(f"Correct! \nCard: {current_card}")
            round_boolean = True
        else:
            print(f"Wrong! \nCard: {current_card}")
            incorrect_points[player_num - 1] += 1

        player_num += 1
        round_counter += 1


##############################################################################
# this section of code simulates game play by creating the game, dealing the
# cards, and executes the logic for game play and determining the winner

create_game()
deal_cards()
#print(f"Player's Hands: {players}")

simulate_round("Red or Black")
simulate_round("Higher or Lower")
simulate_round("Inside or Outside")
simulate_round("Suit")


print("\nRIDE THE BUS")
bus_rider = [i for i, x in enumerate(incorrect_points) if x == max(incorrect_points)]
riding_bus = True

# check if have to reset any variables and player list has to get the deck as its hand so it pops off one by one
players = [0]
for rider in bus_rider:
    consecutive_correct = False
    reset_deck()
    players[0] = deck
    #implement name
    # TEMP
    print(f"Player's Deck: {players[0]}")

# DEBUG LOOP, POTENTIALLY NEST ALL IF STATEMENTS
# problem with two people riding the bus, when initial simulate round function is called it acts as if multiple people are going
# and alternates turns but error because player two does not have any items
# figure out how to have code not alternate turns when riding bus or incrementally add players to players
    while not consecutive_correct:
        if len(deck) > 0:
            simulate_round("Red or Black")
            if round_boolean:
                simulate_round("Higher or Lower")
                if round_boolean:
                    simulate_round("Inside or Outside")
                    if round_boolean:
                        simulate_round("Suit")
                        if round_boolean:
                            consecutive_correct = True
                        else:
                            print("Restart the Ride!")
                    else:
                        print("Restart the Ride!")
                else:
                    print("Restart the Ride!")
            else:
                print("Restart the Ride!")
        else:
            reset_deck()

    print("Congratulations! You successfully 'Rode The Bus'! ")
# print(played_cards)
# print(incorrect_points)
# print(bus_rider)

# once round counter is reached, identify most incorrect points and they ride the bus

# RIDE THE BUS, for loop for how many players have to ride the bus, call ride the bus function,
# while not for in a row and cards left in deck, call each phase function, if incorrect restart,
# else once four in a row is true, break game over

# have boolean value for if four in a row right, while loop popping cards off reshuffled deck (reshuffle function)
# functions will be called and if incorrect, restart, else once four in a row is true, break loop and game over

# ADD INPUT VALIDATION WITH LOOPS OR EXCEPTION HANDLING
# For Tkinter, may have to put everything in functions and call in order of necessary actions
