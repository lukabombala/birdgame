from birdgame import BirdGame
from objects.bird_object import Bird
from objects.pipe_object import Pipe
from objects.bar_object import Bar

import config as c
import colors
import pygame

game = BirdGame(c.caption,
                c.screen_width,
                c.screen_height,
                c.background_image_filename,
                c.frame_rate,
                )

bird = Bird(50, 150, 45, 30, colors.BLACK, )
pipe1 = Pipe((c.screen_width // 2)-50, 50, colors.PIPE_GREEN)
pipe2 = Pipe(c.screen_width-40,50, colors.PIPE_GREEN)
bar = Bar(0, c.ground_level, c.screen_width, 20, colors.BLACK)

game.objects.append(bird)
game.objects.append(pipe1)
game.objects.append(pipe2)
game.objects.append(bar)

bird.speed = (0, 5)
game.keyup_handlers[pygame.K_SPACE].append(bird.keyup_handle)
game.keydown_handlers[pygame.K_SPACE].append(bird.keydown_handle)
game.run()
