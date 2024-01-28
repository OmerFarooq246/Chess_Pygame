import pygame
from Config import Config

class Piece:
    main_path = "./Public/PNGs/No shadow/128h"
    def __init__(self, path, square_x, square_y):
        # +8 and +6 are used to center the pieces in the square
        self.x = Config.offset_x + square_x*Config.scale + 8
        self.y = Config.offset_y + square_y*Config.scale + 6
        
        self.piece_surface = pygame.image.load(path).convert_alpha()
        self.piece_surface = pygame.transform.rotozoom(self.piece_surface, 0, 0.285)
        self.piece_rect = self.piece_surface.get_rect(topleft = (self.x, self.y))
    
    def draw(self, screen):
        screen.blit(self.piece_surface, self.piece_rect)
