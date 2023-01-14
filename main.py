#imports
import button
#from game import get_shuffled_deck, create_deck, colors, game, player1cards, player2cards

import random
import pygame
import pygame_gui
import os
import json

pygame.init()
pygame.font.init()

#game variables
GAME_SPEED = 2000 # 1 second = 5000 milliseconds
CARDS_PER_COLOR = 2 # ENSURE IT IS AN EVEN NUMBER!

colors = {
    "red" :CARDS_PER_COLOR,
    "black" :CARDS_PER_COLOR,
    "yellow" :CARDS_PER_COLOR
}

player1cards = []
player2cards = []

#window variables
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Card game")

#variables
#VALID_USERS = json.loads(open('valid_users.json').read())
VALID_USERS = ["mitesh", "bob"]
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))
VALID_USERS.append("janani")
print(VALID_USERS)

new_users = []

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (159, 159, 159)
RED = (255, 0, 0)
LIGHT_BLUE = (24, 123, 205)
LIGHT_ORANGE = (255,103,0)

#fonts
WINNER_FONT = pygame.font.SysFont("Comic sans MS", 50)
SIGN_UP_FONT = pygame.font.SysFont("Comic sans MS", 20)
SCORE_FONT = pygame.font.SysFont("Comic sans MS", 30)
CARDS_FONT = pygame.font.SysFont("Comic sans MS", 30)
PLAYER_FRONT = pygame.font.SysFont("Comic sans MS", 30)

#inputs
#PLAYER1_INPUT= pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((WIDTH//2 - 200, HEIGHT//2 -25 -(125//2)), (400, 50)), 
#                                                        manager = MANAGER, object_id = "#player1_input")
#PLAYER2_INPUT= pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((WIDTH//2 - 200, HEIGHT//2 +50 -(125//2)), (400, 50)), 
#                                                        manager = MANAGER, object_id = "#player2_input")
#ADD_USER_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((WIDTH//2 - 200, HEIGHT//2 -25 -(125//2) + 100), (400, 50)), 
#                                                        manager = MANAGER, object_id = "#add_user_input")


#rectangles
BOARDER = pygame.Rect(WIDTH // 2 -5, 100, 10, HEIGHT)

#button images
roll_button_image = pygame.image.load(os.path.join('Assets', 'roll_button.png'))
roll_button_pos = (WIDTH//2 - (roll_button_image.get_width())//2, 0)
play_button_image = pygame.image.load(os.path.join('Assets', 'play_button.png'))
play_button_pos = WIDTH//2 - (play_button_image.get_width())//2, HEIGHT//2 - (play_button_image.get_height())//2
replay_button_image = pygame.image.load(os.path.join('Assets', 'replay_button.png'))
add_user_button_image = pygame.image.load(os.path.join('Assets', 'add_user_button.png'))
add_user_pos = (WIDTH//2 - (add_user_button_image.get_width() //2), HEIGHT//2 +45)

#buttons
roll_button = button.Button(WIDTH//2 - (roll_button_image.get_width())//2, 0, roll_button_image)
play_button = button.Button(WIDTH//2 - (play_button_image.get_width())//2, HEIGHT//2 - (play_button_image.get_height())//2 +125, play_button_image)
replay_button = button.Button(WIDTH//2 - (replay_button_image.get_width())//2, HEIGHT//2 - (replay_button_image.get_height())//2 +125, replay_button_image)
add_user_button = button.Button(WIDTH//2 - (add_user_button_image.get_width() //2), HEIGHT//2 +45, add_user_button_image)


#physics
FPS = 60


"""
THE GAME LOGIC
"""


#creates the deck of cards
def create_deck(color):
    all_deck = []
    for color, colors in color.items():
        for i in range(colors):
            card = f"{color}{i}"
            all_deck.append(card)
        #print("all_deck")
    return all_deck

#shuffles the deck of cards
def get_shuffled_deck(all_deck):
    random.shuffle(all_deck)
    return all_deck

#gets card from the top of the deck
def get_card(all_deck):
    card = all_deck[0]
    all_deck.remove(card)
    print(f"removed card: {card}")
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
        
        draw_winner_text(player1, player1, player2)
        
        print(f"{player1} won this round.")
        print(f"cards remaining: {len(deck)}")
        print(f"{player1} has {len(player1cards)} cards.")
        print(f"{player2} has {len(player2cards)} cards.")
        return player1cards
    elif (player2_card_color == "red" and player1_card_color == "black"):
        player2cards.append(player1_card_color)
        player2cards.append(player2_card_color)
        
        draw_winner_text(player2, player1, player2)
        
        print(f"{player2} won this round.")
        print(f"cards remaining: {len(deck)}")
        print(f"{player1} has {len(player1cards)} cards.")
        print(f"{player2} has {len(player2cards)} cards.")
        return player2cards
    elif (player1_card_color == "yellow" and player2_card_color == "red"):
        player1cards.append(player1_card_color)
        player1cards.append(player2_card_color)
        
        draw_winner_text(player1, player1, player2)
        
        print(f"{player1} won this round.")
        print(f"cards remaining: {len(deck)}")
        print(f"{player1} has {len(player1cards)} cards.")
        print(f"{player2} has {len(player2cards)} cards.")
        return player1cards
    elif (player2_card_color == "yellow" and player1_card_color == "red"):
        player2cards.append(player1_card_color)
        player2cards.append(player2_card_color)
        
        draw_winner_text(player2, player1, player2)
        
        print(f"{player2} won this round.")
        print(f"cards remaining: {len(deck)}")
        print(f"{player1} has {len(player1cards)} cards.")
        print(f"{player2} has {len(player2cards)} cards.")
        return player2cards
    elif (player1_card_color == "black" and player2_card_color == "yellow"):
        player1cards.append(player1_card_color)
        player1cards.append(player2_card_color)
        
        draw_winner_text(player1, player1, player2)
        
        print(f"{player1} won this round.")
        print(f"cards remaining: {len(deck)}")
        print(f"{player1} has {len(player1cards)} cards.")
        print(f"{player2} has {len(player2cards)} cards.")
        return player1cards
    elif (player2_card_color == "black" and player1_card_color == "yellow"):
        player2cards.append(player1_card_color)
        player2cards.append(player2_card_color)
        
        draw_winner_text(player2, player1, player2)
        
        print(f"{player2} won this round.")
        print(f"cards remaining: {len(deck)}")
        print(f"{player1} has {len(player1cards)} cards.")
        print(f"{player2} has {len(player2cards)} cards.")
        return player2cards
    
    pygame.display.update()
    pygame.time.delay(GAME_SPEED)

#the game
def game(player1, player2, SCORE_FONT, WHITE, WIN, WIDTH, HEIGHT, deck, BOARDER):
    print("check1")
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
            
            draw_winner_text(player1, player1, player2)
            
            print(f"{player1} won this round because both players drew the same color cards but {player1} had the larger number.")
            print(f"{player1} has {len(player1cards)} cards.")
            print(f"{player2} has {len(player2cards)} cards.")
            print(f"cards remaining: {len(deck)}")
        else:
            player2cards.append(player1_card)
            player2cards.append(player2_card)
            
            draw_winner_text(player2, player1, player2)
            
            print(f"{player2} won this round because both players drew the same color cards but {player2} had the larger number.")
            print(f"{player1} has {len(player1cards)} cards.")
            print(f"{player2} has {len(player2cards)} cards.")
            print(f"cards remaining: {len(deck)}")
    
    
    
    player1_drawn_text = SCORE_FONT.render(f"Card drawn: {player1_card}", 1, WHITE) #card is a place holder for now
    player2_drawn_text = SCORE_FONT.render(f"Card drawn: {player2_card}", 1, WHITE) #card is a place holder for now
    
    
    
    
    
    WIN.blit(player1_drawn_text, (0, 50))
    WIN.blit(player2_drawn_text, (WIDTH-(17*16), 50))
    
    
    pygame.display.update()
    pygame.time.delay(GAME_SPEED)


deck = get_shuffled_deck(create_deck(colors))

"""
THE GUI LOGIC
"""


#draws the rectangles
def draw_rects():
    pygame.draw.rect(WIN, BLACK, BOARDER)

#draws texts
def draw_texts(player1, player2, deck):
    player1_text = SCORE_FONT.render(f"player1: {player1}", 1, WHITE)
    player2_text = SCORE_FONT.render(f"player2: {player2}", 1, WHITE)
    
    player1_cards_text = CARDS_FONT.render(f"cards: {len(player1cards)}", 1, WHITE)
    player2_cards_text = CARDS_FONT.render(f"cards: {len(player2cards)}", 1, WHITE)
    
    cards_remaining_text = CARDS_FONT.render(f"cards remaining: {len(deck)}", 1, WHITE)

    WIN.blit(player1_cards_text, (0, HEIGHT-50))
    WIN.blit(player2_cards_text, (WIDTH//2 +6, HEIGHT-50))
    WIN.blit(player1_text, (0, 0))
    WIN.blit(player2_text, (WIDTH-(17*16), 0))
    WIN.blit(cards_remaining_text, (WIDTH//2 - (cards_remaining_text.get_width()//2), 50))

#draws winner text
def draw_winner_text(winner, player1, player2):
    round_winner_text = SCORE_FONT.render(f"{winner} won this round.", 1, WHITE)
    player1_winner_text_pos = WIDTH//4 -5 - (round_winner_text.get_width()//2), HEIGHT//2 - (round_winner_text.get_height()//2)
    player2_winner_text_pos = WIDTH//2 + (WIDTH//2 +5)//2 - (round_winner_text.get_width()//2), HEIGHT//2 + (round_winner_text.get_height()//2)
    
    if winner == player1:
        WIN.blit(round_winner_text, (player1_winner_text_pos))
    else:
        WIN.blit(round_winner_text, (player2_winner_text_pos))

#draws winner message
def draw_winner(winner):
    winner_message = WINNER_FONT.render(f"{winner} won the game!!!", 1, WHITE)
    WIN.blit(winner_message, (WIDTH//2 - (winner_message.get_width() //2), HEIGHT//2 - (winner_message.get_height() //2)))
    
    if replay_button.draw(WIN):
        play_again = True
        return play_again

    pygame.display.update()


#play again
def play_again(player1, player2, clicked, deck):
    
    draw_window(player1, player2, clicked, deck)
    
    

#draws winner menu
def draw_winner_menu(winner, player1, player2, deck):
    WIN.fill(RED)
    
    if draw_winner(winner):
        print("clicked")
        clicked = True
        print("loading game again...")
        play_again(player1, player2, clicked, deck)
        #run_game(player1, player2, True, deck)
        
    
    
    pygame.display.update()

#loads winner menu
def load_winner_menu(winner, player1, player2, deck):
    player1cards.clear()
    player2cards.clear()
    
    new_deck = get_shuffled_deck(create_deck(colors))
    print(new_deck)
    run = True
    play_again = False
    print("winner menu...")
    clock = pygame.time.Clock()
    while play_again != True and run == True:
        #print("running winner menu...")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            MANAGER.process_events(event)
        
        
        
        
        MANAGER.update(clock.tick(FPS)/1000)
        
        
        draw_winner_menu(winner, player1, player2, new_deck)
        
        #MANAGER.draw_ui(WIN)
        
        pygame.display.update()
    
    
    print("leaving winner menu...")
    pygame.quit()
    exit()




#user validation
def check_validation(player1, player2):
    print(f"validating {player1} and {player2}...")
    if player1 in VALID_USERS and player2 in VALID_USERS:
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
def run_game(player1, player2, clicked, deck):
    print("running game...")
    
    if clicked == True:
        print(len(deck))
        game(player1, player2, SCORE_FONT, WHITE, WIN, WIDTH, HEIGHT, deck, BOARDER)
    
    if len(deck) == 0:
        print("game ended...")
        create_deck(colors)
        if len(player1cards) > len(player2cards):
            load_winner_menu(player1, player1, player2, deck)
            print(f"The game ended because there are {len(deck)} cards remaining.")
            print(f"{player1} won the game because {player1} had {len(player1cards)} cards whereas {player2} had {len(player2cards)} cards.")
            run = False
            exit()
            pygame.quit()
        
        else:
            load_winner_menu(player2, player1, player2, deck)
            print(f"The game ended because there are {len(deck)} cards remaining.")
            print(f"{player2} won the game because {player2} had {len(player2cards)} cards whereas {player1} had {len(player1cards)} cards.")
            run = False
            pygame.quit()
            exit()





#draws game
def draw_game(player1, player2, run, deck):
    WIN.fill(GREY)
    draw_rects()
    draw_texts(player1, player2, deck)
    
    if roll_button.draw(WIN):
        print("clicked")
        clicked = True
        run_game(player1, player2, clicked, deck)
    
    #check_user_input()
    
    
    pygame.display.update()


#draws the signup menu
def draw_signup_menu():
    print("loading signup menu...")
    WIN.fill(LIGHT_ORANGE)
    
    #MANAGER.draw_ui(WIN)


#creates the signup menu
def load_signup_menu():
    run = True
    clock = clock = pygame.time.Clock()
    while run == True:
        #print("running signup menu...")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#add_user_input":
                new_user = event.text
                print(new_user)
            
            
            MANAGER.process_events(event)
        
        draw_signup_menu()
        
        
        #draw_signup_menu()
        MANAGER.update(clock.tick(FPS)/1000)
        
        MANAGER.draw_ui(WIN)
        
        pygame.display.update()
    
    print("exiting...")
    pygame.quit()
    exit()



#creates the game menu
def draw_window(player1, player2, run, deck):
    run = True
    print("loading game...")
    clock = pygame.time.Clock()
    while run == True:
        #print("running game...")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            MANAGER.process_events(event)
        
        draw_game(player1, player2, run, deck)
        
        MANAGER.update(clock.tick(FPS)/1000)
        
        #MANAGER.draw_ui(WIN)
        
        pygame.display.update()
    
    print("exiting...")
    pygame.quit()
    exit()

#loads signup menu
def load_validation_text(valid):
    passed_message = SIGN_UP_FONT.render(f"Validation passed, loading game...", 1, RED)
    failed_message = SIGN_UP_FONT.render(f"Validation failed. Please enter a valid user or add a new user.", 1, RED)
    
    if valid == "passed":
        WIN.blit(passed_message, (WIDTH//2 - (passed_message.get_width() //2), HEIGHT//2 + (HEIGHT//4) +50))
    else:
        WIN.blit(failed_message, (WIDTH//2 - (failed_message.get_width() //2), HEIGHT//2 + (HEIGHT//4) +50))
    
    MANAGER.draw_ui(WIN)
    pygame.display.update()
    pygame.time.delay(5000)

#draw inputs
def draw_inputs(run, signup_menu_open):
    if run == True and signup_menu_open == False:
        PLAYER1_INPUT= pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((WIDTH//2 - 200, 
                HEIGHT//2 -25 -(125//2)), (400, 50)), manager = MANAGER, object_id = "#player1_input")
        PLAYER2_INPUT= pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((WIDTH//2 - 200, 
                HEIGHT//2 +50 -(125//2)), (400, 50)), manager = MANAGER, object_id = "#player2_input")
    

#draws the login menu
def main_():
    WIN.fill(LIGHT_BLUE)
    run = True
    signup_menu_open = False
    draw_inputs(run, signup_menu_open)
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
        
        #create_login_menu()
        
        #create_signup()
        #if add_user_button.draw(WIN):
        #    create_signup_menu()
        #    print("clicked")
        
        
        if play_button.draw(WIN):
            if check_validation(player1, player2) == True:
                valid = "passed"
                load_validation_text(valid)
                draw_window(player1, player2, run, deck)
            else:
                valid = "failed"
                load_validation_text(valid)
        
        if add_user_button.draw(WIN):
                signup_menu_open = True
                print("clicked")
                new_user = ADD_USER_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect = pygame.Rect((WIDTH//2 - 200, HEIGHT//2 -25 -(125//2) + 100), (400, 50)), 
                                                    manager = MANAGER, object_id = "#add_user_input")
                load_signup_menu()
                print("hello ")
                
        
        
        
        
        MANAGER.draw_ui(WIN)
        
        pygame.display.update()

    print("exiting...")
    pygame.quit()
    exit()


if __name__ == '__main__':
    main_()
