import pygame
from objects.game_object import GameObject
import config as c


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
            dy = 5
        elif self.moving_up:
            dy = -30
        elif not self.moving_up:
            if self.bottom >= c.ground_level:
                dy = 0
            else:
                dy = 5
        else:
            return

        self.move(0, dy)
