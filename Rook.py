from Piece import Piece

class Rook(Piece):
    pawn_img_path = [Piece.main_path + "/w_rook_png_128px.png",
                     Piece.main_path + "/b_rook_png_128px.png"]
    
    def __init__(self, side, square_x, square_y):
        super().__init__(Rook.pawn_img_path[side], side, square_x, square_y)