import random as rnd

import pygame

import config as c
from objects.game_object import GameObject


class Pipe:
    def __init__(self, x, special_effect=None):
        self.lower_pipeImg = pygame.image.load(c.pipe_image_filename)
        self.upper_pipeImg = pygame.transform.rotate(self.lower_pipeImg, 180)
        self.pipe_height = c.ground_level
        self.gap_height = round(c.pipe_gap * self.pipe_height)
        self.gap_y = Pipe.find_gap_y(self)
        self.pipe_width = self.lower_pipeImg.get_width()
        self.upper_pipe = GameObject(x, 0,
                                     self.pipe_width,
                                     self.gap_y, )
        self.lower_pipe = GameObject(x,
                                     self.upper_pipe.height + self.gap_height,
                                     self.pipe_width,
                                     self.pipe_height - (self.gap_height + self.upper_pipe.height), )
        self.special_effect = special_effect
        self.copied = False
        self.copied_x = 0
        self.pipe_copy = None

    def draw(self, surface):
        surface.blit(self.upper_pipeImg,
                     (self.upper_pipe.left, self.upper_pipe.top),
                     self.get_img_rect(self.upper_pipe.bounds))
        surface.blit(self.lower_pipeImg,
                     (self.lower_pipe.left, self.upper_pipe.bottom + self.gap_height),
                     self.get_img_rect(self.lower_pipe.bounds, upper=False))

        if self.copied:
            surface.blit(self.upper_pipeImg,
                         (self.pipe_copy[0].left, self.pipe_copy[0].top),
                         self.get_img_rect(self.pipe_copy[0]))
            surface.blit(self.lower_pipeImg,
                         (self.pipe_copy[1].left, self.pipe_copy[1].top),
                         self.get_img_rect(self.pipe_copy[1], upper=False))

    def find_gap_y(self):
        return abs(rnd.randint(round(0.2 * self.pipe_height),
                               round((0.8 * self.pipe_height) - self.gap_height)))

    def update(self):
        self.move(-c.bird_speed, 0)
        if self.upper_pipe.left <= 0:
            self.pipe_copy = self.copy_pipe()
            self.update_gap()
            self.move(c.SCREEN_WIDTH, 0)
        if self.upper_pipe.right >= c.SCREEN_WIDTH:
            self.copied = True
            self.copied_x -= c.bird_speed
            self.pipe_copy[0][0], self.pipe_copy[1][0] = self.copied_x, self.copied_x
        else:
            self.copied = False
            self.copied_x = 0

    def move(self, dx, dy):
        self.upper_pipe.bounds = self.upper_pipe.bounds.move(dx, dy)
        self.lower_pipe.bounds = self.lower_pipe.bounds.move(dx, dy)

    def copy_pipe(self):
        upper_bounds = pygame.Rect([self.copied_x, self.upper_pipe.top, self.upper_pipe.width, self.upper_pipe.height])
        lower_bounds = pygame.Rect([self.copied_x, self.lower_pipe.top, self.lower_pipe.width, self.lower_pipe.height])
        return upper_bounds, lower_bounds

    def update_gap(self):
        self.gap_y = Pipe.find_gap_y(self)
        self.upper_pipe = GameObject(0, 0,
                                     self.pipe_width,
                                     self.gap_y, )
        self.lower_pipe = GameObject(0,
                                     self.upper_pipe.height + self.gap_height,
                                     self.pipe_width,
                                     self.pipe_height - (self.gap_height + self.upper_pipe.height), )

    def get_img_rect(self, rect_obj, upper=True):
        if upper:
            height = self.upper_pipeImg.get_height()
            width = self.upper_pipeImg.get_width()
            return pygame.Rect(0, height - rect_obj.height, width, rect_obj.height)
        else:
            width = self.upper_pipeImg.get_width()
            return pygame.Rect(0, 0, width, rect_obj.height)
