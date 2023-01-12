#imports
import random
import pygame

#variables
colors = {
    "red" :10,
    "black" :10,
    "yellow" :10
}

player1cards = []
player2cards = []

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
        print(f"{player1} has {len(player1cards)} cards.")
        print(f"{player2} has {len(player2cards)} cards.")
        return player1cards
    elif (player2_card_color == "red" and player1_card_color == "black"):
        player2cards.append(player1_card_color)
        player2cards.append(player2_card_color)
        print(f"{player2} won this round.")
        print(f"cards remaining: {len(deck)}")
        print(f"{player1} has {len(player1cards)} cards.")
        print(f"{player2} has {len(player2cards)} cards.")
        return player2cards
    elif (player1_card_color == "yellow" and player2_card_color == "red"):
        player1cards.append(player1_card_color)
        player1cards.append(player2_card_color)
        print(f"{player1} won this round.")
        print(f"cards remaining: {len(deck)}")
        print(f"{player1} has {len(player1cards)} cards.")
        print(f"{player2} has {len(player2cards)} cards.")
        return player1cards
    elif (player2_card_color == "yellow" and player1_card_color == "red"):
        player2cards.append(player1_card_color)
        player2cards.append(player2_card_color)
        print(f"{player2} won this round.")
        print(f"cards remaining: {len(deck)}")
        print(f"{player1} has {len(player1cards)} cards.")
        print(f"{player2} has {len(player2cards)} cards.")
        return player2cards
    elif (player1_card_color == "black" and player2_card_color == "yellow"):
        player1cards.append(player1_card_color)
        player1cards.append(player2_card_color)
        print(f"{player1} won this round.")
        print(f"cards remaining: {len(deck)}")
        print(f"{player1} has {len(player1cards)} cards.")
        print(f"{player2} has {len(player2cards)} cards.")
        return player1cards
    elif (player2_card_color == "black" and player1_card_color == "yellow"):
        player2cards.append(player1_card_color)
        player2cards.append(player2_card_color)
        print(f"{player2} won this round.")
        print(f"cards remaining: {len(deck)}")
        print(f"{player1} has {len(player1cards)} cards.")
        print(f"{player2} has {len(player2cards)} cards.")
        return player2cards

#the game
def game(player1, player2, deck, SCORE_FONT, WHITE, WIN, WIDTH, HEIGHT):
    player1_card = get_card(deck)
    player2_card = get_card(deck)
    
    player1_card_color = get_card_color(player1_card)
    player2_card_color = get_card_color(player2_card)
    
    player1_card_number = get_card_number(player1_card)
    player2_card_number = get_card_number(player2_card)
    
    print(f"{player1} draw the card: {player1_card}")
    print(f"{player2} draw the card: {player2_card}")
    player1_drawn_text = SCORE_FONT.render(f"Card drawn: {player1_card}", 1, WHITE) #card is a place holder for now
    player2_drawn_text = SCORE_FONT.render(f"Card drawn: {player2_card}", 1, WHITE) #card is a place holder for now
    WIN.blit(player1_drawn_text, (0, 50))
    WIN.blit(player2_drawn_text, (WIDTH-(17*16), 50))
    
    if player1_card_color != player2_card_color:
        #print("Drew different cards")
        get_winning_card(player1, player2, player1_card_color, player2_card_color, player1cards, player2cards, deck)
    else:
        if player1_card_number > player2_card_number:
            player1cards.append(player1_card)
            player1cards.append(player2_card)
            print(f"{player1} won this round because both players drew the same color cards but {player1} had the larger number.")
            print(f"{player1} has {len(player1cards)} cards.")
            print(f"{player2} has {len(player2cards)} cards.")
            print(f"cards remaining: {len(deck)}")
        else:
            player2cards.append(player1_card)
            player2cards.append(player2_card)
            print(f"{player2} won this round because both players drew the same color cards but {player2} had the larger number.")
            print(f"{player1} has {len(player1cards)} cards.")
            print(f"{player2} has {len(player2cards)} cards.")
            print(f"cards remaining: {len(deck)}")
    pygame.display.update() 