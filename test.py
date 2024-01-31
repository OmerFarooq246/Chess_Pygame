a = [1,2,3,4,5]
print(a)
if 7 not in a:
    print(True)



    # #sets the in_move attrinute if clicked on a square containing a piece
    # def set_in_move(self):
    #     print("in_move 1:", self.in_move)
    #     if self.in_move == False and pygame.mouse.get_pressed()[0]:  #0th index gives me left click
    #         self.get_mouse_index()
    #         if self.index < 64 and self.has_piece[self.index]:
    #             self.in_move = True
    #             print("in_move 1:", self.in_move)
    
    # def remove_in_move(self):
    #     print("in_move 2:", self.in_move)
    #     if self.in_move == True and pygame.mouse.get_pressed()[0]:
    #         if self.in_move == True:
    #             possible_moves = self.has_piece[self.index].possible_moves(self.index)
    #             # print("possible_moves:", possible_moves)
    #             self.get_mouse_index() #gives new index
    #             if self.index not in possible_moves:
    #                 self.in_move = False
    #                 print("in_move 2:", self.in_move)

    # def move_piece(self):
    #     if self.in_move:
    #         btn_status = pygame.mouse.get_pressed()[0]
    #         if btn_status:
    #             square_x, square_y = self.get_mouse_index()
    #             if square_x < 64 and square_y < 64:
    #                 self.has_piece[Config.piece_index].move(square_x, square_y)

    print(-12//6)