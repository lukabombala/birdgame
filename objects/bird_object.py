import pygame

import config as c
from objects.game_object import GameObject


class Bird(GameObject):
    def __init__(self, x, y, w, h, color, special_effect=None):
        GameObject.__init__(self, x, y, w, h)
        self.color = color
        self.special_effect = special_effect
        self.moving_up = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def keydown_handle(self, key):
        if key == pygame.K_SPACE:
            self.moving_up = True

    def keyup_handle(self, key):
        if key == pygame.K_SPACE:
            self.moving_up = False

    def update(self):
        if self.top <= 0:
            dy = c.fall_speed
        elif self.moving_up:
            dy = -28
        elif not self.moving_up:
            if (self.bottom + c.fall_speed) >= c.ground_level:
                dy = c.ground_level - self.bottom
            else:
                dy = c.fall_speed
        else:
            return

        self.move(0, dy)
