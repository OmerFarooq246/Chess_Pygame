from Piece import Piece

class King(Piece):
    pawn_img_path = [Piece.main_path + "/w_king_png_128px.png",
                     Piece.main_path + "/b_king_png_128px.png"]
    
    def __init__(self, side, square_x, square_y):
        super().__init__(King.pawn_img_path[side], side, square_x, square_y)