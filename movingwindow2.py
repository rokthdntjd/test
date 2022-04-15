import pygame
from screeninfo import get_monitors
import os
import time



# Set the size of the pygame window
window_width = 600
window_height = 400
window_size = (window_width, window_height)

# Get the bounds of the users monitors, and select the first one
monitors = get_monitors() # Get the resolution of all of the users monitors
screen_width = monitors[0].width # Get width of first monitor found
screen_height = monitors[0].height # Get height of first monitor found

# Set the x and y coordinates of the pygame window in relation to the monitor's resolution 
# (I wanted my pygame window to be located in the bottom-right of the monitor)
pos_x = screen_width - window_width # Calculate the x-location
pos_y = screen_height - window_height # Calculate the y-location
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y) # Set pygame window location

pygame.init() # Initialize the pygame window

screen = pygame.display.set_mode((window_width, window_height)) # Set the location of the pygame window
pygame.display.set_caption("moving window lol")



print(window_width, window_height)
print(window_size)

print(monitors)
print(screen_width, screen_height)

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
       os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x-100, pos_y)
       screen = pygame.display.set_mode((window_width, window_height))

    if keys[pygame.K_RIGHT]:
            run = False

    if keys[pygame.K_UP]:
            run = False

    if keys[pygame.K_DOWN]:
            run = False

    pygame.display.update()


pygame.quit()