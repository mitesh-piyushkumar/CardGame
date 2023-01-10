#imports
import random

#variables
colors = {
    "red" :10,
    "black" :10,
    "yellow" :10
}

#creates the deck of cards
def create_deck(color):
    all_deck = []
    for color, colors in color.items():
        for i in range(colors):
            card = f"{color}{i}"
            all_deck.append(card)
    return all_deck

#shuffles the deck of cards
def get_shuffled_deck(all_deck):
    random.shuffle(all_deck)
    return all_deck

#gets card from the top of the deck
def get_card(all_deck):
    card = all_deck[0]
    all_deck.remove(card)
    return card

#gets the color of the card
def get_card_color(card):
    card_color = card[0:len(card)-1]
    return card_color

#gets the number of the card
def get_card_number(card):
    card_number = card[len(card) - 1 : len(card)]
    return card_number

#gets winning card (if two different cards are drawn)
def get_winning_card(player1, player2, player1_card_color, player2_card_color, player1cards, player2cards, deck):
    if (player1_card_color == "red" and player2_card_color == "black"):
        player1cards.append(player1_card_color)
        player1cards.append(player2_card_color)
        print(f"{player1} won this round.")
        print(f"cards remaining: {len(deck)}")
        return player1cards
    elif (player2_card_color == "red" and player1_card_color == "black"):
        player2cards.append(player1_card_color)
        player2cards.append(player2_card_color)
        print(f"{player2} won this round.")
        print(f"cards remaining: {len(deck)}")
        return player2cards
    elif (player1_card_color == "yellow" and player2_card_color == "red"):
        player1cards.append(player1_card_color)
        player1cards.append(player2_card_color)
        print(f"{player1} won this round.")
        print(f"cards remaining: {len(deck)}")
        return player1cards
    elif (player2_card_color == "yellow" and player1_card_color == "red"):
        player2cards.append(player1_card_color)
        player2cards.append(player2_card_color)
        print(f"{player2} won this round.")
        print(f"cards remaining: {len(deck)}")
        return player2cards
    elif (player1_card_color == "black" and player2_card_color == "yellow"):
        player1cards.append(player1_card_color)
        player1cards.append(player2_card_color)
        print(f"{player1} won this round.")
        print(f"cards remaining: {len(deck)}")
        return player1cards
    elif (player2_card_color == "black" and player1_card_color == "yellow"):
        player2cards.append(player1_card_color)
        player2cards.append(player2_card_color)
        print(f"{player2} won this round.")
        print(f"cards remaining: {len(deck)}")
        return player2cards

#the game
def game(player1, player2, deck, player1cards, player2cards):
    player1_card = get_card(deck)
    player2_card = get_card(deck)
    
    player1_card_color = get_card_color(player1_card)
    player2_card_color = get_card_color(player2_card)
    
    player1_card_number = get_card_number(player1_card)
    player2_card_number = get_card_number(player2_card)
    
    print(f"{player1} draw the card: {player1_card}")
    print(f"{player2} draw the card: {player2_card}")

    if player1_card_color != player2_card_color:
        #print("Drew different cards")
        get_winning_card(player1, player2, player1_card_color, player2_card_color, player1cards, player2cards, deck)
    else:
        if player1_card_number > player2_card_number:
            player1cards.append(player1_card)
            player1cards.append(player2_card)
            print(f"{player1} won this round because both players drew the same color cards but {player1} had the larger number.")
            print(f"cards remaining: {len(deck)}")
        else:
            player2cards.append(player1_card)
            player2cards.append(player2_card)
            print(f"{player2} won this round because both players drew the same color cards but {player2} had the larger number.")
            print(f"cards remaining: {len(deck)}")

#runs the games
def main():
    deck = get_shuffled_deck(create_deck(colors))
    player1 = input("Enter the first player's name: ")
    player2 = input("Enter the second player's name: ")
    player1cards = []
    player2cards = []
    while len(deck) > 0:
        play = input("Press enter to play (q to quit).").lower()
        if play == "q":
            break
        game(player1, player2, deck, player1cards, player2cards)
    if len(player1cards) > len(player2cards):
        print(f"The game ended because there are {len(deck)} cards remaining.")
        print(f"{player1} won the game because {player1} had {len(player1cards)} cards whereas {player2} had {len(player2cards)} cards.")
    else:
        print(f"The game ended because there are {len(deck)} cards remaining.")
        print(f"{player2} won the game because {player2} had {len(player2cards)} cards whereas {player1} had {len(player1cards)} cards.")

main()