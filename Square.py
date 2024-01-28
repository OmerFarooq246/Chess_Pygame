import pygame
from Config import Config

class Square:
    def __init__(self, x, y, focused_state):
        self.x = x
        self.y = y
        self.focused = focused_state
        self.width = Config.scale
        self.height = Config.scale

        if (y//Config.scale)%2 == 0:
            self.color = Config.start_color if (x//Config.scale)%2 == 0 else Config.end_color
            self.focus_color = Config.focus_color_light if (x//Config.scale)%2 == 0 else Config.focus_color_dark
        else:
            self.color = Config.end_color if (x//Config.scale)%2 == 0 else Config.start_color
            self.focus_color = Config.focus_color_dark if (x//Config.scale)%2 == 0 else Config.focus_color_light
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, screen):
        # print(self.x, self.y)
        # print("focused:", self.focused)
        if self.focused:
            pygame.draw.rect(screen, self.focus_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
