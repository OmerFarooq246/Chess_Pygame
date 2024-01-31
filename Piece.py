import pygame
from Config import Config

class Piece:
    main_path = "./Public/PNGs/No shadow/128h"
    def __init__(self, path, side, square_x, square_y):
        # +8 and +6 are used to center the pieces in the square
        self.x = Config.offset_x + square_x*Config.scale + 8
        self.y = Config.offset_y + square_y*Config.scale + 6
        self.side = side
        
        self.piece_surface = pygame.image.load(path).convert_alpha()
        self.piece_surface = pygame.transform.rotozoom(self.piece_surface, 0, 0.285) #0 degree rotation, 0.285 zoom
        self.piece_rect = self.piece_surface.get_rect(topleft = (self.x, self.y))
    
    def move(self, square_x, square_y):
        print("accessing move function")
        self.piece_rect.x = Config.offset_x + square_x*Config.scale + 8
        self.piece_rect.y = Config.offset_y + square_y*Config.scale + 8

    def possible_moves(self, index):
        possible_moves = []
        # square_x = index//8
        square_y = index%8
        if self.side == 0:
            if square_y == 6 and self.__class__.__name__ == "Pawn":
                possible_moves = [index-1, index-2]
            else:
                possible_moves = [index-1]
        elif self.side == 1:
            if square_y == 1 and self.__class__.__name__ == "Pawn":
                possible_moves = [index+1, index+2]
            else:
                possible_moves = [index+1]
        return possible_moves

    def parent(self):
        print("accessing parent function")

    def draw(self, screen):
        screen.blit(self.piece_surface, self.piece_rect)
