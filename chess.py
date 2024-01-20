import pygame
import sys

class Board:
    def __init__(self, start_color, end_color, scale, offset_x, offset_y):
        # self.x = x
        # self.y = y

        #initialize chess_board
        self.chess_board = []
        for x in range(8):
            x_pos = offset_x + (scale * (x))
            for y in range(8):
                y_pos = offset_y + (scale * (y))
                self.chess_board.append(Squre(x_pos, y_pos, scale, scale, start_color, end_color, scale))
            
    def draw(self, screen):
        print("chess_board: ", len(self.chess_board))
        for square in self.chess_board:
            square.draw(screen)
        

class Squre:
    def __init__(self, x, y, width, height, start_color, end_color, scale):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        if (y//scale)%2 == 0:
            self.color = start_color if (x//scale)%2 == 0 else end_color
            self.focus_color = start_color if (x//scale)%2 == 0 else end_color
        else:
            self.color = end_color if (x//scale)%2 == 0 else start_color
            self.focus_color = end_color if (x//scale)%2 == 0 else start_color

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, screen):
        print(self.x, self.y)
        pygame.draw.rect(screen, self.color, self.rect)


pygame.init()
screen = pygame.display.set_mode((960, 540))
clock = pygame.time.Clock()

#controls
start_color = "#779556"
end_color = "#ebecd0"
scale = 50
offset_x = 292
offset_y = 50

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #to uninitialize the init() function of pygame
            sys.exit()  #to terminate the code
        
    board = Board(start_color, end_color, scale, offset_x, offset_y)
    board.draw(screen)

    
    pygame.display.update()
    clock.tick(60)
    