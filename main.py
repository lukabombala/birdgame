import pygame

import colors
import config as c
from birdgame import BirdGame
from objects.bar_object import Bar
from objects.bird_object import Bird
from objects.pipe_object import Pipe

game = BirdGame(c.caption,
                c.SCREEN_WIDTH,
                c.SCREEN_HEIGHT,
                c.background_image_filename,
                c.frame_rate,
                )

bird = Bird(50, 150, 45, 30, colors.BLACK, )
pipe1 = Pipe((c.SCREEN_WIDTH // 2) - 50, 50)
pipe2 = Pipe(c.SCREEN_WIDTH - 50, 50)
bar1 = Bar(0, c.ground_level)
bar2 = Bar(c.SCREEN_WIDTH, c.ground_level)

game.objects.append(bird)
game.objects.append(pipe1)
game.objects.append(pipe2)
game.objects.append(bar1)
game.objects.append(bar2)

bird.speed = (0, 5)
game.keyup_handlers[pygame.K_SPACE].append(bird.keyup_handle)
game.keydown_handlers[pygame.K_SPACE].append(bird.keydown_handle)
game.run()
