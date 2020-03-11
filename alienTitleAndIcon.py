import pygame


# Title and Icon                       #1
def setTitleAndIcon():

    pygame.display.set_caption("Space Invaders")            # title
    icon = pygame.image.load("spaceshipIcon.png")               # load image for icon
    pygame.display.set_icon(icon)                           # set icon top left side near the title
