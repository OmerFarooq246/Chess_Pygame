from Config import Config
import pygame

class ResetBtn:
    def __init__(self):
        self.width = 120
        self.height = 45
        self.center = (300, 520)
        
        self.rest_txt_surface = Config.font.render("RESET", True, Config.end_color) #True for antialias
        self.rest_txt_rect = self.rest_txt_surface.get_rect(center = self.center)

        self.back_surface = pygame.Surface((self.width, self.height))
        self.back_surface.fill(Config.start_color)
        self.back_rect = self.back_surface.get_rect(center = self.center)
    
    # #returns topleft_x, topleft_y, width, height
    # def give_info(self):
    #     topleft_x = self.center[0] - self.x
    #     topleft_y = self.center[0] - self.y
    #     return topleft_x, topleft_y, self.width, self.height
    
    def reset_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            #conditions for clicked inside horizontally
            if mouse_pos[0] > (self.center[0] - self.width//2) and mouse_pos[0] < (self.center[0] + self.width//2):
                #conditions for clicked inside vertically
                if mouse_pos[1] > (self.center[1] - self.height//2) and mouse_pos[1] < (self.center[1] + self.height//2):
                    print("in")
                    return True
                else:
                    return False