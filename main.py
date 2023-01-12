#imports
import button
from game import *

import pygame
import os

pygame.init()
pygame.font.init()

#variables
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Dice game")

#colors
WHITE = (255, 255, 255)
GREY = (159, 159, 159)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#fonts
SCORE_FONT = pygame.font.SysFont("Comic sans MS", 30)
CARDS_FONT = pygame.font.SysFont("Comic sans MS", 30)
PLAYER_FRONT = pygame.font.SysFont("Comic sans MS", 30)

#rectangles
BOARDER = pygame.Rect(WIDTH // 2 -5, 50, 10, HEIGHT)

#button images
roll_button_image = pygame.image.load(os.path.join('Assets', 'roll_button.png'))
roll_button_pos = (WIDTH//2 - (roll_button_image.get_width())//2, 0)

#buttons
roll_button = button.Button(WIDTH//2 - (roll_button_image.get_width())//2, 0, roll_button_image)

#
FPS = 60

#draws the rectangles
def draw_rects():
    pygame.draw.rect(WIN, BLACK, BOARDER)

#draws texts
def draw_texts(player1, player2, player1_text, player2_text):
    player1_cards_text = CARDS_FONT.render(f"cards: 0", 1, WHITE) #0 is a place holder for now
    player2_cards_text = CARDS_FONT.render(f"cards: 0", 1, WHITE) #0 is a place holder for now
    #WIN.blit(player1_drawn_text, (0, 50))
    #WIN.blit(player2_drawn_text, (WIDTH-(17*16), 50)) # replace 5 with len(name)
    WIN.blit(player1_cards_text, (0, HEIGHT-50))
    WIN.blit(player2_cards_text, (WIDTH//2 +6, HEIGHT-50))
    WIN.blit(player1_text, (0, 0))
    WIN.blit(player2_text, (WIDTH-(17*16), 0)) # replace 5 with len(name)

#runs the game in ui
def run_game(player1, player2, run):
    deck = get_shuffled_deck(create_deck(colors))
    pygame.display.update()
    while len(deck) > 0:
        play = input("Press enter to play (q to quit).").lower()
        if play == "q":
            break
        game(player1, player2, deck, SCORE_FONT, WHITE, WIN, WIDTH, HEIGHT)
    if len(player1cards) > len(player2cards):
        print(f"The game ended because there are {len(deck)} cards remaining.")
        print(f"{player1} won the game because {player1} had {len(player1cards)} cards whereas {player2} had {len(player2cards)} cards.")
        run = False
        exit()
        pygame.quit()
        
    else:
        print(f"The game ended because there are {len(deck)} cards remaining.")
        print(f"{player2} won the game because {player2} had {len(player2cards)} cards whereas {player1} had {len(player1cards)} cards.")
        run = False
        exit()
        pygame.quit()

#draws the window
def draw_window(player1, player2, run, player1_text, player2_text):
    WIN.fill(GREY)
    draw_rects()
    draw_texts(player1, player2, player1_text, player2_text)
    
    if roll_button.draw(WIN):
        print("clicked")
        run_game(player1, player2, run)
    
    pygame.display.update()

#
def main_():
    player1 = input("Enter the first player's name: ").lower()
    player2 = input("Enter the second player's name: ").lower()
    if player1 == "mitesh" and player2 == "janani":
        run = True
    else:
        run = False
        pygame.quit()
        print("invalid users...")
        exit()
    player1_text = PLAYER_FRONT.render(f"player1: {player1}", 1, WHITE) # name is a place holder for now
    player2_text = PLAYER_FRONT.render(f"player2: {player2}", 1, WHITE) # name is a place holder for now

    clock = pygame.time.Clock()
    while run == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window(player1, player2, run, player1_text, player2_text)
    
    
    
    pygame.quit()


if __name__ == '__main__':
    main_()