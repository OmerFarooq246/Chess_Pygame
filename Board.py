import pygame
from Square import Square
from Pawn import Pawn
from King import King
from Queen import Queen
from Bishop import Bishop
from Knight import Knight
from Rook import Rook
from Config import Config

class Board:

    def __init__(self):
        self.focus_sqrs = [False]*64 #keeps track of focused squares
        self.has_piece = [False]*64 #keeps track of squares having pieces
        self.index = 0
        self.in_move = False
        self.chess_board = []
        self.pieces = [] #
        
    #initialize chess_board and pieces
    def init_chess_board(self):
        for x in range(8):
            x_pos = Config.offset_x + (Config.scale * (x))
            for y in range(8):
                y_pos = Config.offset_y + (Config.scale * (y))
                self.chess_board.append(Square(x_pos, y_pos, self.focus_sqrs[x*8+y]))

                if y == 0: #Adding black pieces
                    if x == 0 or x == 7:
                        self.pieces.append(Rook(1, x, y))
                        self.has_piece[x*8+y] = True
                    if x == 1 or x == 6:
                        self.pieces.append(Knight(1, x, y))
                        self.has_piece[x*8+y] = True
                    if x == 2 or x == 5:
                        self.pieces.append(Bishop(1, x, y))
                        self.has_piece[x*8+y] = True
                    if x == 3:
                        self.pieces.append(Queen(1, x, y))
                        self.has_piece[x*8+y] = True
                    if x == 4:
                        self.pieces.append(King(1, x, y))
                        self.has_piece[x*8+y] = True
                elif y == 1: #Adding black pawns
                    self.pieces.append(Pawn(1, x, y))
                    self.has_piece[x*8+y] = True
                    
                elif y == 6: #Adding white pawns
                    self.pieces.append(Pawn(0, x, y))
                    self.has_piece[x*8+y] = True
                elif y == 7: #Adding white pieces
                    if x == 0 or x == 7:
                        self.pieces.append(Rook(0, x, y))
                        self.has_piece[x*8+y] = True
                    if x == 1 or x == 6:
                        self.pieces.append(Knight(0, x, y))
                        self.has_piece[x*8+y] = True
                    if x == 2 or x == 5:
                        self.pieces.append(Bishop(0, x, y))
                        self.has_piece[x*8+y] = True
                    if x == 3:
                        self.pieces.append(Queen(0, x, y))
                        self.has_piece[x*8+y] = True
                    if x == 4:
                        self.pieces.append(King(0, x, y))
                        self.has_piece[x*8+y] = True

    #finds the square the mouse is in by updating index
    def get_mouse_info(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_box_x = (mouse_pos[0] - Config.offset_x)//Config.scale
        mouse_box_y = (mouse_pos[1] - Config.offset_y)//Config.scale
        btn_status = pygame.mouse.get_pressed()[0] #0th index gives me left click
        # self.index = mouse_box_x*8 + mouse_box_y #index of the square in chess_board
        if btn_status:
            self.index = mouse_box_x*8 + mouse_box_y #index of the square in chess_board
            if self.index < 64 and self.has_piece[self.index]:
                self.in_move = True
            else:
                self.in_move = False

    # def move_piece(self):
    #     if self.in_move:
            
            
    def update_focus_sqrs(self):
        #resets
        for i in range(len(self.focus_sqrs)):
            self.focus_sqrs[i] = False
            self.chess_board[i].focused = False
        if self.in_move:
            self.focus_sqrs[self.index] = True
            self.chess_board[self.index].focused = True

    def draw(self, screen):
        for square in self.chess_board:
            square.draw(screen)
        for piece in self.pieces:
            piece.draw(screen)

    def update(self, screen):
        self.get_mouse_info()
        self.update_focus_sqrs()
        self.draw(screen)