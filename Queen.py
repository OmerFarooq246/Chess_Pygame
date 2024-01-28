from Piece import Piece

class Queen(Piece):
    pawn_img_path = [Piece.main_path + "/w_queen_png_128px.png",
                     Piece.main_path + "/b_queen_png_128px.png"]
    
    def __init__(self, side, square_x, square_y):
        super().__init__(Queen.pawn_img_path[side], square_x, square_y)
