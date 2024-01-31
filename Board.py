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
        self.has_piece = [None]*64 #keeps track of pieces
        self.index = 0
        # self.in_move = False
        self.chess_board = []
        self.selected_piece = None
        self.possible_moves = []
        
    #initialize chess_board and pieces
    def init_chess_board(self):
        for x in range(8):
            x_pos = Config.offset_x + (Config.scale * (x))
            for y in range(8):
                y_pos = Config.offset_y + (Config.scale * (y))
                # self.chess_board.append(Square(x_pos, y_pos, self.focus_sqrs[x*8+y]))
                self.chess_board.append(Square(x_pos, y_pos, False))

                if y == 0: #Adding black pieces
                    if x == 0 or x == 7:
                        self.has_piece[x*8+y] = Rook(1, x, y)
                    if x == 1 or x == 6:
                        self.has_piece[x*8+y] = Knight(1, x, y)
                    if x == 2 or x == 5:
                        self.has_piece[x*8+y] = Bishop(1, x, y)
                    if x == 3:
                        self.has_piece[x*8+y] = Queen(1, x, y)
                    if x == 4:
                        self.has_piece[x*8+y] = King(1, x, y)
                elif y == 1: #Adding black pawns
                    self.has_piece[x*8+y] = Pawn(1, x, y)
                    
                elif y == 6: #Adding white pawns
                    self.has_piece[x*8+y] = Pawn(0, x, y)
                elif y == 7: #Adding white pieces
                    if x == 0 or x == 7:
                        self.has_piece[x*8+y] = Rook(0, x, y)
                    if x == 1 or x == 6:
                        self.has_piece[x*8+y] = Knight(0, x, y)
                    if x == 2 or x == 5:
                        self.has_piece[x*8+y] = Bishop(0, x, y)
                    if x == 3:
                        self.has_piece[x*8+y] = Queen(0, x, y)
                    if x == 4:
                        self.has_piece[x*8+y] = King(0, x, y)

    #finds the square the mouse is in by updating index
    def get_mouse_index(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_box_x = (mouse_pos[0] - Config.offset_x)//Config.scale
        mouse_box_y = (mouse_pos[1] - Config.offset_y)//Config.scale
        self.index = mouse_box_x*8 + mouse_box_y #index of the square in chess_board
        return mouse_box_x, mouse_box_y

    def update_sqrs(self):
        #resets
        for i in range(len(self.chess_board)):
            self.chess_board[i].focused = False
        if self.selected_piece:
            self.chess_board[Config.piece_index].focused = True
    
    def update_chess_board_array(self):
        #updating the chess_board array
        self.has_piece[Config.piece_index] = None
        self.has_piece[self.index] = self.selected_piece
        self.selected_piece = None
        Config.piece_index = None
        self.index = 0

    def handle_mouse_click(self):
        # print("selected_piece:", self.selected_piece)
        if pygame.mouse.get_pressed()[0]:
            square_x, square_y = self.get_mouse_index()
            if self.selected_piece == None and self.index < 64 and self.has_piece[self.index]:
                self.selected_piece = self.has_piece[self.index]
                Config.piece_index = self.index
                self.possible_moves = self.selected_piece.possible_moves(Config.piece_index)
            elif self.selected_piece:
                #seleting a new piece
                if self.index < 64 and self.has_piece[self.index]:
                    self.selected_piece = self.has_piece[self.index]
                    Config.piece_index = self.index
                    self.possible_moves = self.selected_piece.possible_moves(Config.piece_index)
                    # self.update_sqrs()
                elif self.index in self.possible_moves:
                    self.selected_piece.move(square_x, square_y)
                    self.update_chess_board_array()
                    # self.update_sqrs()
                elif self.index not in self.possible_moves:
                    self.selected_piece = None
                    Config.piece_index = None
                    return
            self.update_sqrs()

    def draw(self, screen):
        for square in self.chess_board:
            square.draw(screen)
        for piece in self.has_piece:
            if piece: piece.draw(screen)

    def update(self, screen):
        self.handle_mouse_click()
        self.draw(screen)