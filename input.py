#imports
import pygame

#class inputs
class Inputs():
    def __init__(self, user_ip, text_box):
        self.user_ip = user_ip
        self.text_box = text_box
        self.inputted = False
    
    def check_user_input(self):
        active = False
        pos = pygame.mouse.get_pos()
        
        if self.text_box.collidepoint(pos):
            if pygame.MOUSEBUTTONDOWN:
                active = True
            else:
                active = False
        
        if pygame.KEYDOWN:
            if active == True:
                if pygame.K_BACKSPACE:
                    self.user_ip = self.user_ip[:-1]
                
                else:
                    self.user_ip += pygame.TEXTINPUT
                    self.inputted = True
                
        
        return self.inputted
