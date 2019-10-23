import sys
from collections import defaultdict

import pygame

import colors
import config as c


class Game:
    def __init__(self,
                 caption,
                 width,
                 height,
                 background_image_filename,
                 frame_rate,):
        self.background_image = pygame.image.load(background_image_filename)
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

    def update(self):
        for obj in self.objects:
            obj.update()

    def draw(self):
        for obj in self.objects:
            obj.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))
            pygame.draw.rect(self.surface, colors.SKY, [0, 0, c.SCREEN_WIDTH, c.ground_level])
            pygame.draw.rect(self.surface, colors.GROUND_COLOR, [0,
                                                                 c.ground_level,
                                                                 c.SCREEN_WIDTH,
                                                                 c.SCREEN_HEIGHT - c.ground_level])
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)
