#imports
import button
from game import *

import pygame
import pygame_gui
import os
import json

pygame.init()
pygame.font.init()

#window variables
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Card game")

#variables
#VALID_USERS = json.loads(open('valid_users.json').read())
VALID_USERS = ("mitesh", "bob")
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (159, 159, 159)
RED = (255, 0, 0)
LIGHT_BLUE = (24, 123, 205)

#fonts
SCORE_FONT = pygame.font.SysFont("Comic sans MS", 30)
CARDS_FONT = pygame.font.SysFont("Comic sans MS", 30)
PLAYER_FRONT = pygame.font.SysFont("Comic sans MS", 30)

#inputs
PLAYER1_INPUT= pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((WIDTH//2 - 200, HEIGHT//2 -25 -(125//2)), (400, 50)), 
                                                        manager = MANAGER, object_id = "#player1_input")
PLAYER2_INPUT= pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((WIDTH//2 - 200, HEIGHT//2 +50 -(125//2)), (400, 50)), 
                                                        manager = MANAGER, object_id = "#player2_input")



#rectangles
BOARDER = pygame.Rect(WIDTH // 2 -5, 50, 10, HEIGHT)

#button images
roll_button_image = pygame.image.load(os.path.join('Assets', 'roll_button.png'))
roll_button_pos = (WIDTH//2 - (roll_button_image.get_width())//2, 0)
play_button_image = pygame.image.load(os.path.join('Assets', 'play_button.png'))
play_button_pos = WIDTH//2 - (play_button_image.get_width())//2, HEIGHT//2 - (play_button_image.get_height())//2

#buttons
roll_button = button.Button(WIDTH//2 - (roll_button_image.get_width())//2, 0, roll_button_image)
play_button = button.Button(WIDTH//2 - (play_button_image.get_width())//2, HEIGHT//2 - (play_button_image.get_height())//2 +125, play_button_image)

#physics
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



#user validation
def check_validation(player1, player2):
    print("validating...")
    if player1 and player2 in VALID_USERS:
        print("validation passed...")
        return True
    else:
        print("validation failed...")
        return False

#add valid user
def add_user(name):
    with open("valid_users.json", "r") as user:
        users = json.load(user)
    
    users.append(name)
    
    with open("valid_users.json", "w") as user:
        json.dump(name, user)
        print(f"added user: {name}")
    

#runs the game in ui
def run_game(player1, player2, run):
    deck = get_shuffled_deck(create_deck(colors))
    pygame.display.update()
    while len(deck) > 0:
        play = input("Press enter to play (q to quit).").lower()
        if play == "q":
            break
        
        #if roll_button.draw(WIN) == True:
        #    print("clicked...")
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
        pygame.quit()
        exit()



#draws game
def draw_game(player1, player2, run):
    WIN.fill(GREY)
    draw_rects()
    #draw_texts(player1, player2, player1_text, player2_text)
    
    if roll_button.draw(WIN):
        print("clicked")
        run_game(player1, player2, run)
    
    #check_user_input()
    
    
    pygame.display.update()


#creates the login menu
def create_login_menu():
    WIN.fill(LIGHT_BLUE)





#creates the game menu
def draw_window(player1, player2, run):
    run = True
    print("loading game...")
    clock = pygame.time.Clock()
    while run == True:
        print("running game...")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            MANAGER.process_events(event)
        
        draw_game(player1, player2, run)
        
        MANAGER.update(clock.tick(FPS)/1000)
        
        #MANAGER.draw_ui(WIN)
        
        pygame.display.update()
    
    print("exiting...")
    pygame.quit()
    exit()

#draws the login menu
def main_():
    #add_user("mitesh")
    run = True
    print("loading...")
    clock = pygame.time.Clock()
    while run == True:
        #print("running login menu...")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#player1_input":
                player1 = event.text
            
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#player2_input":
                player2 = event.text
            
                #if check_validation(player1, player2) == True:
                #    draw_window(player1, player2, run)
                
                
                
                
            MANAGER.process_events(event)
            #check_user_input()
        
        MANAGER.update(clock.tick(FPS)/1000)
        
        create_login_menu()
        
        if play_button.draw(WIN):
            if check_validation(player1, player2) == True:
                    draw_window(player1, player2, run)
            else:
                print("unable to validate...")
                pygame.quit()
                exit()
        
        
        MANAGER.draw_ui(WIN)
        
        pygame.display.update()

    print("exiting...")
    pygame.quit()
    exit()


if __name__ == '__main__':
    main_()
