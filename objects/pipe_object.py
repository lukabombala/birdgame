import pygame
import config as c
from objects.game_object import GameObject
import random as rnd
import colors


class Pipe:
    def __init__(self, x, w, color, special_effect=None):
        self.pipe_height = c.ground_level
        self.gap_height = round(c.pipe_gap * self.pipe_height)
        self.pipe_width = w
        self.color = color
        self.gap_y = Pipe.find_gap_y(self)
        self.upper_pipe = GameObject(x, 0,
                                     self.pipe_width,
                                     self.gap_y, )
        self.lower_pipe = GameObject(x,
                                     self.upper_pipe.height + self.gap_height,
                                     self.pipe_width,
                                     self.pipe_height - (self.gap_height + self.upper_pipe.height), )
        self.special_effect = special_effect
        self.copied = False
        self.copied_x = c.screen_width

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.upper_pipe.bounds)
        pygame.draw.rect(surface, self.color, self.lower_pipe.bounds)
        if self.copied:
            pygame.draw.rect(surface, self.color, self.copy_pipe()[0])
            pygame.draw.rect(surface, self.color, self.copy_pipe()[1])

    def find_gap_y(self):
        return abs(rnd.randint(round(0.2 * self.pipe_height),
                               round((0.8 * self.pipe_height) - self.gap_height)))

    def update(self):
        self.move(-c.bird_speed, 0)
        if -50 < self.upper_pipe.left <= 0:
            self.copied = True
            self.copied_x -= c.bird_speed
        elif self.upper_pipe.right <= 0:
            self.update_gap()
            self.move(c.screen_width, 0)
            self.copied = False
            self.copied_x = c.screen_width

    def move(self, dx, dy):
        self.upper_pipe.bounds = self.upper_pipe.bounds.move(dx, dy)
        self.lower_pipe.bounds = self.lower_pipe.bounds.move(dx, dy)

    def copy_pipe(self):
        upper_pipe_bounds = [self.copied_x, self.upper_pipe.top, self.upper_pipe.width, self.upper_pipe.height]
        lower_pipe_bounds = [self.copied_x, self.lower_pipe.top, self.lower_pipe.width, self.lower_pipe.height]
        return upper_pipe_bounds, lower_pipe_bounds

    def update_gap(self):
        pass
