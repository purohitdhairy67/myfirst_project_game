import pygame
import random


class player:
    def __init__(self, screen, playerImg):
        # player image load set location       #1
        playerImg = pygame.image.load(playerImg)  # load image
        self.playerImg = playerImg

        playerXcord = 355       # x_cord
        self.playerXcord = playerXcord
        playerYcord = 525       # y_cord
        self.playerYcord = playerYcord
        move = 0                # update x cord
        self.move = move

        self.screen = screen

    # display image on screen              #2(11)
    def displayPlayer(self):
        self.screen.blit(self.playerImg, (self.playerXcord, self.playerYcord))      # takes image and tuple (x,y)

    def checkShipCord(self):
        # if ship came out from window     #3(15)
        if self.playerXcord <= 0:
            self.playerXcord = 0
        elif self.playerXcord >= 736:
            self.playerXcord = 736


class enemy:
    def __init__(self, screen):
        # player image load set location       #1(16)
        enemyImg = pygame.image.load("op.png")  # load image
        self.enemyImg = enemyImg

        enemyXcord = random.randint(0, 736)       # x_cord
        self.enemyXcord = enemyXcord
        enemyYcord = random.randint(50, 250)      # y_cord
        self.enemyYcord = enemyYcord
        move = 0.3                # update x cord to move
        self.move = move

        self.screen = screen

    # display image on screen              #2(17)
    def displayEnemy(self):
        self.screen.blit(self.enemyImg, (self.enemyXcord, self.enemyYcord))      # takes image and tuple (x,y)

    def checkEnemyCord(self):
        # if enemy  hit   the window than move some downwards     #3(15)
        if self.enemyXcord <= 0:
            self.enemyXcord = 0
            self.move = -self.move
            self.enemyYcord += 9
        elif self.enemyXcord >= 736:
            self.enemyXcord = 736
            self.move = -self.move
            self.enemyYcord += 9
