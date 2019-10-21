from game import Game
from objects.text_object import TextObject
import colors
import config as c
import pygame
import time


class BirdGame(Game):
    def show_message(self,
                     text,
                     color=colors.WHITE,
                     font_name='Arial',
                     font_size=20,
                     centralized=False):
        message = TextObject(c.screen_width // 2,
                             c.screen_height // 2,
                             lambda: text,
                             color,
                             font_name,
                             font_size)

        self.draw()
        message.draw(self.surface, centralized)
        pygame.display.update()
        time.sleep(c.message_duration)
