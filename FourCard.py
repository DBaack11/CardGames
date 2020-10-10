import random

print("Welcome to Four Card! \n")
valid_num_players = False;

while not valid_num_players:
    num_players = int(input("(Maximum of 8 Players)\nEnter the number of players: "))
    if 1 < num_players <= 8:
        valid_num_players = True
    else:
        print("\nSorry! Must have at least 2 players and no more than 8!")

values = [2, 3, 4, 5, 6, 7, 8, 9, 10,
          "Jack", "Queen", "King", "Ace"]
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
deck = []
players = []
current_turn = False


# can check values and suits using if string in
def create_game():
    for suit in suits:
        for value in values:
            deck.append(f"{value} of {suit}")

    for a in range(num_players):
        individual_player_list = []
        players.append(individual_player_list)


def deal_cards():
    random.shuffle(deck)

    for b in range(4):
        for player in range(len(players)):
            dealt_card = deck.pop()
            players[player].append(dealt_card)


def play_card():
    # series of if statements, check if suit in there or value, check for value and assign
    # action to corresponding person (to the right)
    pass


create_game()
deal_cards()
game_over = False
previous_card = deck.pop()
print(f"Player's Hands: {players}")
print(f"Remaining Deck ({len(deck)} cards): {deck}")
print(f"Previous Card: {previous_card}")

while not game_over:

    for player in range(len(players)):
        played_card = input(f"\nPlayer {player + 1}, your turn to play a card: ")
        # check for valid card input
        play_card(played_card)

        if len(players[player]) == 0:
            print(f"Player {player + 1} wins!")
            game_over = True
            break

        else:
            continue

# for i in range(len(deck)):
#     print(f"{deck[i].value} of {deck[i].suit}")
