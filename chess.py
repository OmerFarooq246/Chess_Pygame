import pygame
from Board import Board
from Config import Config
import sys

pygame.init()
screen = pygame.display.set_mode((960, 540))
clock = pygame.time.Clock()

#controls
start_color = "#779556"
end_color = "#ebecd0"
focus_color_dark = "#aaafff"
focus_color_light = "#ccc111"
scale = 50
offset_x = 292
offset_y = 50

Config(start_color, end_color, focus_color_dark, focus_color_light, scale, offset_x, offset_y)
board = Board()
board.init_chess_board()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #to uninitialize the init() function of pygame
            sys.exit()  #to terminate the code
        
    # board = Board(start_color, end_color, focus_color_dark, focus_color_light, scale, offset_x, offset_y)
    board.update(screen)

    
    pygame.display.update()
    clock.tick(60)
    