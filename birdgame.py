import time

import pygame

import colors
import config as c
from game import Game
from objects.text_object import TextObject


class BirdGame(Game):
    def show_message(self,
                     text,
                     color=colors.WHITE,
                     font_name='Arial',
                     font_size=20,
                     centralized=False):
        message = TextObject(c.SCREEN_WIDTH // 2,
                             c.SCREEN_HEIGHT // 2,
                             lambda: text,
                             color,
                             font_name,
                             font_size)

        self.draw()
        message.draw(self.surface, centralized)
        pygame.display.update()
        time.sleep(c.message_duration)