import pygame
import sys

class Piece():
    main_path = "./Public/PNGs/No shadow/128h"
    def __init__(self, path, square_x, square_y):
        self.x = Board.offset_x + square_x*Board.scale + 8
        self.y = Board.offset_y + square_y*Board.scale + 6
        
        self.piece_surface = pygame.image.load(path).convert_alpha()
        self.piece_surface = pygame.transform.rotozoom(self.piece_surface, 0, 0.285)
        self.piece_rect = self.piece_surface.get_rect(topleft = (self.x, self.y))
    
    def draw(self, screen):
        screen.blit(self.piece_surface, self.piece_rect)


class Pawn(Piece):
    pawn_img_path = [Piece.main_path + "/w_pawn_png_128px.png",
                     Piece.main_path + "/b_pawn_png_128px.png"]
    
    def __init__(self, side, square_x, square_y):
        super().__init__(Pawn.pawn_img_path[side], square_x, square_y) #side = 0 means white and 1 means black

class King(Piece):
    pawn_img_path = [Piece.main_path + "/w_king_png_128px.png",
                     Piece.main_path + "/b_king_png_128px.png"]
    
    def __init__(self, side, square_x, square_y):
        super().__init__(King.pawn_img_path[side], square_x, square_y)

class Queen(Piece):
    pawn_img_path = [Piece.main_path + "/w_queen_png_128px.png",
                     Piece.main_path + "/b_queen_png_128px.png"]
    
    def __init__(self, side, square_x, square_y):
        super().__init__(Queen.pawn_img_path[side], square_x, square_y)

class Bishop(Piece):
    pawn_img_path = [Piece.main_path + "/w_bishop_png_128px.png",
                     Piece.main_path + "/b_bishop_png_128px.png"]
    
    def __init__(self, side, square_x, square_y):
        super().__init__(Bishop.pawn_img_path[side], square_x, square_y)

class Knight(Piece):
    pawn_img_path = [Piece.main_path + "/w_knight_png_128px.png",
                     Piece.main_path + "/b_knight_png_128px.png"]
    
    def __init__(self, side, square_x, square_y):
        super().__init__(Knight.pawn_img_path[side], square_x, square_y)

class Rook(Piece):
    pawn_img_path = [Piece.main_path + "/w_rook_png_128px.png",
                     Piece.main_path + "/b_rook_png_128px.png"]
    
    def __init__(self, side, square_x, square_y):
        super().__init__(Rook.pawn_img_path[side], square_x, square_y)


class Board:
    offset_x = 0
    offset_y = 0
    scale = 0
    start_color = ""
    end_color = ""

    def __init__(self, start_color, end_color, scale, offset_x, offset_y):
        Board.offset_x = offset_x
        Board.offset_y = offset_y
        Board.scale = scale
        Board.start_color = start_color
        Board.end_color = end_color

        self.chess_board = []
        self.pieces = []
        self.init_chess_board()
        
    #initialize chess_board and pieces
    def init_chess_board(self):
        for x in range(8):
            x_pos = offset_x + (scale * (x))
            for y in range(8):
                y_pos = offset_y + (scale * (y))
                self.chess_board.append(Squre(x_pos, y_pos))

                if y == 0: #Adding black pieces
                    if x == 0 or x == 7:
                        self.pieces.append(Rook(1, x, y))
                    if x == 1 or x == 6:
                        self.pieces.append(Knight(1, x, y))
                    if x == 2 or x == 5:
                        self.pieces.append(Bishop(1, x, y))
                    if x == 3:
                        self.pieces.append(Queen(1, x, y))
                    if x == 4:
                        self.pieces.append(King(1, x, y))
                elif y == 1: #Adding black pawns
                    self.pieces.append(Pawn(1, x, y))
                    
                elif y == 6: #Adding white pawns
                    self.pieces.append(Pawn(0, x, y))
                elif y == 7: #Adding white pieces
                    if x == 0 or x == 7:
                        self.pieces.append(Rook(0, x, y))
                    if x == 1 or x == 6:
                        self.pieces.append(Knight(0, x, y))
                    if x == 2 or x == 5:
                        self.pieces.append(Bishop(0, x, y))
                    if x == 3:
                        self.pieces.append(Queen(0, x, y))
                    if x == 4:
                        self.pieces.append(King(0, x, y))

    def draw(self, screen):
        print("chess_board: ", len(self.chess_board))
        for square in self.chess_board:
            square.draw(screen)
        
        for piece in self.pieces:
            piece.draw(screen)


class Squre:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = Board.scale
        self.height = Board.scale

        if (y//Board.scale)%2 == 0:
            self.color = Board.start_color if (x//Board.scale)%2 == 0 else Board.end_color
            self.focus_color = Board.start_color if (x//Board.scale)%2 == 0 else Board.end_color
        else:
            self.color = Board.end_color if (x//Board.scale)%2 == 0 else Board.start_color
            self.focus_color = Board.end_color if (x//Board.scale)%2 == 0 else Board.start_color

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
    