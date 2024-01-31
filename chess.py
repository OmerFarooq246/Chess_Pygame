import pygame
from Board import Board
from ResetBtn import ResetBtn
from Config import Config
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

#controls
start_color = "#779556"
end_color = "#ebecd0"
focus_color_dark = "#aaafff"
focus_color_light = "#ccc111"
scale = 50
offset_x = 100
offset_y = 65
font_path = "./Fonts/Poppins-Bold.ttf"
font_size = 35

Config(start_color, end_color, focus_color_dark, focus_color_light, scale, offset_x, offset_y, font_path, font_size)
board = Board()
board.init_chess_board()
reset_btn = ResetBtn()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #to uninitialize the init() function of pygame
            sys.exit()  #to terminate the code

    screen.fill("black")
    reset_clicked = reset_btn.reset_clicked()
    board.update(screen, reset_clicked)
    #for printing/updating text
    screen.blit(reset_btn.back_surface, reset_btn.back_rect)
    screen.blit(reset_btn.rest_txt_surface, reset_btn.rest_txt_rect)
    pygame.display.update()
    clock.tick(60)
    