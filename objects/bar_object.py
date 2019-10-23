import pygame
import config as c
from objects.game_object import GameObject


class Bar(GameObject):
    def __init__(self, x, y, special_effect=None):
        self.img = pygame.image.load(c.bar_image_filename)
        GameObject.__init__(self, x, y, self.img.get_width(), self.img.get_height())

        self.special_effect = special_effect

    def draw(self, surface):
        surface.blit(self.img, self.bounds)

    def update(self):
        if self.right <= 0:
            self.move(2 * c.SCREEN_WIDTH - 5, 0)
        else:
            self.move(-c.bird_speed, 0)
