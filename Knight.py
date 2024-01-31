from Piece import Piece

class Knight(Piece):
    pawn_img_path = [Piece.main_path + "/w_knight_png_128px.png",
                     Piece.main_path + "/b_knight_png_128px.png"]
    
    def __init__(self, side, square_x, square_y):
        super().__init__(Knight.pawn_img_path[side], side, square_x, square_y)