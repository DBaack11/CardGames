# Add input validation with loops or exception handling

##############################################################################
# This section of code introduces the game, gets number of players, validates
# the input, and creates/initializes the lists for the deck and players
import random

print("Welcome to Irish Poker! \n")
valid_num_players = False

while not valid_num_players:
    num_players = int(input("(Maximum of 8 Players)\nEnter the number of players: "))
    if 1 < num_players <= 8:
        valid_num_players = True
    else:
        print("\nSorry! Must have at least 2 players and no more than 12!")

values = [2, 3, 4, 5, 6, 7, 8, 9, 10,
          "Jack", "Queen", "King", "Ace"]
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
deck = []
players = []
current_turn = False


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


# try returning at bottom and setting int to answer // DEBUG
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


played_cards = []
round_counter = 0


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


##############################################################################
# this section of code simulates game play by creating the game, dealing the
# cards, and executes the logic for game play and determining the winner

create_game()
deal_cards()
game_over = False
print(f"Player's Hands: {players}")
# print(f"Remaining Deck ({len(deck)} cards): {deck}")


# OR do first card then second card then third card, assigning value of input, use input validation

incorrect_points = []

# while round_counter != (num_players * 4):
#   round_counter = num_players * 4

# for each player, check red or black, increment round counter, add incorrect points
player_num = 1
for player in players:
    # first_card = player.pop()
    played_cards.append(player.pop())
    current_card = played_cards[round_counter]
    red_or_black_guess = input(f"\nPlayer {player_num}, guess Red or Black: ")
    if red_or_black(red_or_black_guess):
        print(f"Correct! \nCard: {current_card}")
    else:
        print(f"Wrong! \nCard: {current_card}")
        # add incorrect points to list
    player_num += 1
    round_counter += 1

    # for each player, check higher or lower, increment round counter, add incorrect points
player_num = 1
for player in players:

    played_cards.append(player.pop())
    current_card = played_cards[round_counter]
    higher_or_lower_guess = input(f"\nPlayer {player_num}, guess Higher or Lower: ")
    if higher_or_lower(higher_or_lower_guess):
        print(f"Correct! \nCard: {current_card}")
    else:
        print(f"Wrong! \nCard: {current_card}")
    player_num += 1
    round_counter += 1

    # for each player, check inside or outside, increment round counter, add incorrect points
player_num = 1
for player in players:
    played_cards.append(player.pop())
    current_card = played_cards[round_counter]
    inside_or_outside_guess = input(f"\nPlayer {player_num}, guess Inside or Outside: ")
    if inside_or_outside(inside_or_outside_guess):
        print(f"Correct! \nCard: {current_card}")
    else:
        print(f"Wrong! \nCard: {current_card}")
    player_num += 1
    round_counter += 1

    # for each player, check suit, increment round counter, add incorrect points
player_num = 1
for player in players:
    played_cards.append(player.pop())
    current_card = played_cards[round_counter]
    suit_guess = input(f"\nPlayer {player_num}, guess the suit: ")
    if guess_suit(suit_guess):
        print(f"Correct! \nCard: {current_card}")
    else:
        print(f"Wrong! \nCard: {current_card}")
        # add incorrect points
    player_num += 1
    round_counter += 1

print(played_cards)

# once round counter is reached, identify most incorrect points and they ride the bus

# RIDE THE BUS, for loop for how many players have to ride the bus, call ride the bus function,
# while not for in a row and cards left in deck, call each phase function, if incorrect restart,
# else once four in a row is true, break game over

# have boolean value for if four in a row right, while loop popping cards off reshuffled deck (reshuffle function)
# functions will be called and if incorrect, restart, else once four in a row is true, break loop and game over

# ADD INPUT VALIDATION
