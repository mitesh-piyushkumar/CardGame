#imports
from ..classes import button
from..classes import input
from ..db import db


#test = [("mitesh", 0), ("janani", 10)]

#db.multiexec("insert into leaderboard values (?, ?)", test)
#db.commit()


#for row in db.execute("select * from leaderboard"):
#    print(row)

import random
import pygame
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
p1_wins = []
p2_wins = []

#window variables
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Card game")

#variables
VALID_USERS_PATH = "./data/valid_users.txt"

with open(VALID_USERS_PATH) as users:
    valid_users = users.read()
#valid_users_file = open("valid_users.json")
#valid_users = json.loads(valid_users_file.read())
#valid_users = json.loads(open('valid_users.json').read())
#valid_users = ["mitesh", "bob"]
#print(valid_users)

#new_users = ["", ]

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
p1_text_message = "player1: "
player1_input_box = input.InputBox(WIDTH//2 - 200, HEIGHT//2 -25 -(125//2), 400, 50)
p2_text_message = "player2: "
player2_input_box = input.InputBox(WIDTH//2 - 200, HEIGHT//2 +50 -(125//2), 400, 50)
player_input_boxes = [player1_input_box, player2_input_box]

add_user_message = "new user's name: "
add_user_input_box = input.InputBox(WIDTH//2 - 200, HEIGHT//2 -25 -(125//2) - 100, 400, 50)



#rectangles
BOARDER = pygame.Rect(WIDTH // 2 -5, 100, 10, HEIGHT-100)

#button images
roll_button_image = pygame.image.load(os.path.join('Assets', 'roll_button.png'))
roll_button_pos = (WIDTH//2 - (roll_button_image.get_width())//2, 0)
play_button_image = pygame.image.load(os.path.join('Assets', 'play_button.png'))
play_button_pos = WIDTH//2 - (play_button_image.get_width())//2, HEIGHT//2 - (play_button_image.get_height())//2
replay_button_image = pygame.image.load(os.path.join('Assets', 'replay_button.png'))
add_user_button_image = pygame.image.load(os.path.join('Assets', 'add_user_button.png'))
add_user_pos = (WIDTH//2 - (add_user_button_image.get_width() //2), HEIGHT//2 +45)
adduser_button_image = pygame.image.load(os.path.join('Assets', "adduser_button.png"))

#buttons
roll_button = button.Button(WIDTH//2 - (roll_button_image.get_width())//2, 0, roll_button_image)
play_button = button.Button(WIDTH//2 - (play_button_image.get_width())//2, HEIGHT//2 - (play_button_image.get_height())//2 +125, play_button_image)
replay_button = button.Button(WIDTH//2 - (replay_button_image.get_width())//2, HEIGHT//2 - (replay_button_image.get_height())//2 +125, replay_button_image)
add_user_button = button.Button(WIDTH//2 - (add_user_button_image.get_width() //2), HEIGHT//2 +45, add_user_button_image)
adduser_button = button.Button(WIDTH//2 - (adduser_button_image.get_width() //2), HEIGHT//2 - (adduser_button_image.get_height() //2) +125 - 125, adduser_button_image)


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

#checks for extra pixels
def check_for_extra_pixels(player1, player2):
    if len(player1) > len("leaderboard: "):
        extra_pixels = len(player1) *8
    else:
        extra_pixels = 0
    
    if len(player2) > len("leaderboard: "):
        extra_pixels = len(player2) *8
    else:
        extra_pixels = 0
    return extra_pixels

#draws leaderbard
def draw_lb(player1, player2, p1_total_wins, p2_total_wins):

    extra_pixels = check_for_extra_pixels(player1, player2)
    
    lb_rect = pygame.Rect(0, 0, 200 + (extra_pixels), 150)
    lb_text = SCORE_FONT.render("leaderboard: ", 1, WHITE)
    
    p1_lb_text = SCORE_FONT.render(f"{player1}: {p1_total_wins} wins" if p1_total_wins != 1 else f"{player1}: {p1_total_wins} win" , 1, WHITE)
    p2_lb_text = SCORE_FONT.render(f"{player2}: {p2_total_wins} wins" if p2_total_wins != 1 else f"{player2}: {p2_total_wins} win" , 1, WHITE)
    
    pygame.draw.rect(WIN, GREY, lb_rect)
    WIN.blit(lb_text, (0, 0))
    WIN.blit(p1_lb_text, (0, 50))
    WIN.blit(p2_lb_text, (0, 100))

#draws global leaderboard
def draw_glb():
    glb_rect = pygame.Rect(WIDTH -300, 0, 300, HEIGHT)
    glb_text = SCORE_FONT.render("global leaderboard: ", 1, WHITE)
    
    pygame.draw.rect(WIN, GREY, glb_rect)
    WIN.blit(glb_text, (WIDTH -300, 0))



#play again
def play_again(player1, player2, clicked, deck):
    
    draw_window(player1, player2, clicked, deck)
    
    

#stores wins
def store_wins(player1, player2, p1_win, p2_win, winner):
    if winner == player1:
        p1_win += 1
        
        print(f"{player1}: {p1_win}")
        p1_wins.append(p1_win)
        #wins = len(p1_wins)
        #print(f"{player1}: {wins}")
        db.execute("UPDATE leaderboard SET Wins = Wins + ? WHERE PlayerName = ?", p1_win, player1)
        db.commit()
    if winner == player2:
        p2_win += 1
        
        print(f"{player1}: {p2_win}")
        p2_wins.append(p2_win)
        #wins = len(p2_wins)
        #print(f"{player2}: {wins}")
        db.execute("UPDATE leaderboard SET Wins = Wins + ? WHERE PlayerName = ?", p2_win, player2)
        db.commit()
        


#draws winner menu
def draw_winner_menu(winner, player1, player2, deck, p1_total_wins, p2_total_wins):
    
    #p1_win = 1
    #p2_win = 1
    
    #store_p1_wins(player1, winner, p1_win)
    #store_p2_wins(player2, winner, p2_win)
    
    #p1_total_wins = len(p1_wins)
    #p2_total_wins = len(p2_wins)
    
    WIN.fill(RED)
    draw_lb(player1, player2, p1_total_wins, p2_total_wins)
    draw_glb()
    
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
    
    p1_win = 0
    p2_win = 0
    
    store_wins(player1, player2, p1_win, p2_win, winner)
    
    p1_total_wins = len(p1_wins)
    p2_total_wins = len(p2_wins)
    
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
            
            #MANAGER.process_events(event)
        
        
        
        
        #MANAGER.update(clock.tick(FPS)/1000)
        
        
        draw_winner_menu(winner, player1, player2, new_deck, p1_total_wins, p2_total_wins)
        
        
        
        #MANAGER.draw_ui(WIN)
        
        pygame.display.update()
    
    
    print("leaving winner menu...")
    pygame.quit()
    exit()




#user validation
def check_validation(player1, player2):
    print(f"validating {player1} and {player2}...")
    if player1.isalpha() and player2.isalpha():
        if player1 in valid_users and player2 in valid_users:
            print("validation passed...")
            return True
        else:
            print("validation failed...")
            return False

#add valid user
def add_valid_user(name):
    db.execute("insert into leaderboard values (?, ?)", name, 0)
    db.commit()

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
    #print("loading signup menu...")
    WIN.fill(LIGHT_ORANGE)

#creates the signup menu
def load_signup_menu():
    added_user = False
    clock = clock = pygame.time.Clock()
    while added_user == False:
        #print("running signup menu...")
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                added_user = not added_user
            
            add_user_input_box.handle_event(event)
            
            
            
        
        WIN.fill(LIGHT_ORANGE)
        new_user = add_user_input_box.draw(WIN, add_user_message)
        
        if adduser_button.draw(WIN):
            add_valid_user(new_user)
            print("added")
            main_()
            
        
        
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
            
            
        
        draw_game(player1, player2, run, deck)
        
        
        
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
    
    
    pygame.display.update()
    pygame.time.delay(2000)



#draws the login menu
def main_():
    run = True
    signup_menu_open = False
    print("loading...")
    clock = pygame.time.Clock()
    while run == True:
        #print("running login menu...")
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            for box in player_input_boxes:
                box.handle_event(event)
        
        WIN.fill(LIGHT_BLUE)
        
        player1 = player1_input_box.draw(WIN, p1_text_message)
        player2 = player2_input_box.draw(WIN, p2_text_message)

        
        
        #create_login_menu()
        
        #create_signup()
        if add_user_button.draw(WIN):
            print("clicked")
            load_signup_menu()
        
        if play_button.draw(WIN):
            all_players = db.column("SELECT PlayerName FROM leaderboard")
            print(f"all players: {all_players}")
            
            if player1 in all_players and player2 not in all_players:
                valid = "failed"
                load_validation_text(valid)
                print(f"player2: {player2} is not in the database...")
            elif player1 not in all_players and player2 in all_players:
                valid = "failed"
                load_validation_text(valid)
                print(f"player1: {player1} is not in the database...")
            elif player1 not in all_players and player2 not in all_players:
                valid = "failed"
                load_validation_text(valid)
                print("both players arent in the database...")
            else:
                valid = "passed"
                load_validation_text(valid)
                draw_window(player1, player2, run, deck)
            
            
            #if player1 not in all_players and player2 not in all_players:
            #    #if player1 not in all_players:
            #    #    print(f"{player2} is not in the database...")
            #    #else:
            #    #    print(f"{player1} is not in the database...")
            #    
            #    if check_validation(player1, player2) == True:
            #        players = [(player1, 0), (player2, 0)]
            #        valid = "passed"
            #    
            #        db.multiexec("insert into leaderboard values (?, ?)", players)
            #        db.commit()
            #
            #        load_validation_text(valid)
            #        draw_window(player1, player2, run, deck)
            #    
            #    else:
            #        valid = "failed"
            #        load_validation_text(valid)
            #
            #else:
            #    print("both players in the database...")
            #    valid = "passed"
            #    load_validation_text(valid)
            #    draw_window(player1, player2, run, deck)

                
        pygame.display.update()

    print("exiting...")
    pygame.quit()
    exit()


#if __name__ == '__main__':
#    main_()
