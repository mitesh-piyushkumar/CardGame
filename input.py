#imports
import pygame

pygame.font.init()



#colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (159, 159, 159)
RED = (255, 0, 0)
LIGHT_BLUE = (24, 123, 205)
LIGHT_ORANGE = (255,103,0)

#variables
COLOR_INACTIVE = GREY
COLOR_ACTIVE = BLACK
FONT = pygame.font.SysFont("Comic sans MS", 30)

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, 1, self.color)
        self.clicked = False
    
    def handle_event(self, event):
        #print("running...")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
            else:
                self.clicked = False
            self.color = COLOR_ACTIVE if self.clicked else COLOR_INACTIVE
        
        if event.type == pygame.KEYDOWN and self.clicked:
            if event.key == pygame.K_RETURN:
                self.clicked = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.txt_surface = FONT.render(self.text, True, self.color)
    
    
    def draw(self, surface):
        surface.blit(self.txt_surface, (self.rect.x, self.rect.y))
        pygame.draw.rect(surface, self.color, self.rect, 2)
        return self.text