x = 1820
y = 100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

import pygame
pygame.init()
screen = pygame.display.set_mode((100,100))
pygame.display.set_caption("first game")

# wait for a while to show the window.
import time
time.sleep(2)

run = True
