import pygame
from dino_runner.utils.constants import FONT_STYLE, FONT_STYLE_2 ,COLORS, SCREEN_HEIGHT, SCREEN_WIDTH


class TextUtils:
    def get_score_element(self, points):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render('Points : ' + str(points), True, COLORS['silver'])
        text_rect = text.get_rect()
        text_rect.center = (1000,550)
        return text, text_rect
    
    def get_centered_message(self, message, width = SCREEN_WIDTH //2, height = SCREEN_HEIGHT //2):
        font = pygame.font.Font(FONT_STYLE_2, 50)
        text = font.render(message, True, COLORS['purple'])
        text_rect = text.get_rect()
        text_rect.center = (width, height)
        return text, text_rect