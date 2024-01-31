from Piece import Piece

class Pawn(Piece):
    pawn_img_path = [Piece.main_path + "/w_pawn_png_128px.png",
                     Piece.main_path + "/b_pawn_png_128px.png"]
    
    def __init__(self, side, square_x, square_y):
        super().__init__(Pawn.pawn_img_path[side], side, square_x, square_y) #side = 0 means white and 1 means black
    
    # def possible_moves(self, index):
    #     possible_moves = []
    #     # square_x = index//8
    #     square_y = index%8
    #     if self.side == 0:
    #         if square_y == 6 and self.__class__.__name__ == "Pawn":
    #             possible_moves = [index-1, index-2]
    #         else:
    #             possible_moves = [index-1]
    #     elif self.side == 1:
    #         if square_y == 1 and self.__class__.__name__ == "Pawn":
    #             possible_moves = [index+1, index+2]
    #         else:
    #             possible_moves = [index+1]
    #     return possible_moves
