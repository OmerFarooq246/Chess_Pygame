import pygame

class Config:
    offset_x = 0
    offset_y = 0
    scale = 0
    start_color = ""
    end_color = ""
    focus_color_dark = ""
    focus_color_light = ""
    font = ""

    def __init__(self, start_color, end_color, focus_color_dark, focus_color_light, scale, offset_x, offset_y, font_path, size):
        Config.offset_x = offset_x
        Config.offset_y = offset_y
        Config.scale = scale
        Config.start_color = start_color
        Config.end_color = end_color
        Config.focus_color_dark = focus_color_dark
        Config.focus_color_light = focus_color_light
        Config.font = pygame.font.Font(font_path, size)