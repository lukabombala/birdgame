import pygame

from objects.game_object import GameObject


class Bar(GameObject):
    def __init__(self, x, y, w, color, special_effect=None):
        GameObject.__init__(self, x, y, w, h=0)
        self.color = color
        self.special_effect = special_effect

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

