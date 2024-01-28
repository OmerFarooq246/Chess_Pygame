from Piece import Piece

class Pawn(Piece):
    pawn_img_path = [Piece.main_path + "/w_pawn_png_128px.png",
                     Piece.main_path + "/b_pawn_png_128px.png"]
    
    def __init__(self, side, square_x, square_y):
        super().__init__(Pawn.pawn_img_path[side], square_x, square_y) #side = 0 means white and 1 means black
