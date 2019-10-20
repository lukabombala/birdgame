from birdgame import BirdGame
from objects.bird_object import Bird
import config as c
import colors
import pygame

game = BirdGame(c.caption,
                c.screen_width,
                c.screen_height,
                c.background_image_filename,
                c.frame_rate,
                )

bird = Bird(50, 150, 60, 30, colors.BLACK, )
game.objects.append(bird)
bird.speed = (0, 5)
game.keyup_handlers[pygame.K_SPACE].append(bird.keyup_handle)
game.keydown_handlers[pygame.K_SPACE].append(bird.keydown_handle)
game.run()
