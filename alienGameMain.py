import pygame
from alienTitleAndIcon import setTitleAndIcon
from alienPlayerImageLoadAndSet import player
from alienPlayerImageLoadAndSet import enemy
from alienFire import FireBullet
import random
from alienscore import scoring
from alianType import choose_player


# Intialize the pygame                 #1(32)
pygame.init()               # always needed line to use pygame

playerImg, background = choose_player()


# score                 #25
score_points = 0
font = pygame.font.Font("freesansbold.ttf", 26)
textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score : " + str(score_points), True, (0, 0, 255))
    screen.blit(score, (x, y))


# game over
over = pygame.font.Font("freesansbold.ttf", 70)


def game_over():
    game_over = over.render("Game Over", True, (255, 255, 0))
    screen.blit(game_over, (200, 250))


# Create the screen                    #2(58)
screen = pygame.display.set_mode((800, 600))        # tuple passed as screen size (width, hight)  #from top left(0, 0)

# Title and Icon                       #7(63)
setTitleAndIcon()

# crate spaceship                       #10(132)
player = player(screen, playerImg)

# create enemy                        #16(102)
enemy1 = enemy(screen)
enemy2 = enemy(screen)
enemy3 = enemy(screen)
enemy4 = enemy(screen)
enemy5 = enemy(screen)
enemy6 = enemy(screen)
enemy7 = enemy(screen)
enemy8 = enemy(screen)
all_enemy = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8]

# create bullet                         #20(78)
bullet1 = FireBullet(screen)
#bullet2 = FireBullet(screen)
#bullet3 = FireBullet(screen)
#all_bullet = [bullet1, bullet2, bullet3]

# main loop variable                   #3
running = True

while running:                         # 4 main game loop(infinite till close pressed)

    # filling screen with color (backgroung color)      #8(137)
    screen.fill(background)  # this take a tuple (R, G, B) from 0 to 255.

    for event in pygame.event.get():        # 5          #pygame.event.get() #check and get all key presses

        if event.type == pygame.QUIT:     # 6   check if close button pressed as event type pygame.QUIT     #goto line 35
            scoring(score_points)
            running = False

        if event.type == pygame.KEYDOWN:    # 12    check if any key pressed from keyboard(83)
            if event.key == pygame.K_LEFT:
                player.move = -0.35
            if event.key == pygame.K_RIGHT:
                player.move = 0.35

            if event.key == pygame.K_SPACE:     #21     check if spece presed   (90)
                if not bullet1.bullet_state:    #check if bullet is not on the way
                    bullet1.bulletXcord = player.playerXcord
                    bullet1.fire(bullet1.bulletXcord, bullet1.bulletYcord)

        if event.type == pygame.KEYUP:    # 13    check if any key up from keyboard (126)
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player.move = 0

    #   check if bullet tuched    #23(113)
    score_points = bullet1.check(score_points)

    # check if bullet fired than make it move                       #22
    if bullet1.bullet_state:
        bullet1.fire(bullet1.bulletXcord, bullet1.bulletYcord)
        bullet1.bulletYcord -= 0.5

    for enemy in all_enemy:
        # move the enemy1
        enemy.enemyXcord += enemy.move  # 18

        # if enemy hit window(change direction)
        enemy.checkEnemyCord()  # 19(52)

        # display enemy                    #17
        enemy.displayEnemy()

        # collision or not
        collision = bullet1.collision(enemy.enemyXcord, enemy.enemyYcord)
        if collision:
            bullet1.bulletYcord = 525
            bullet1.bullet_state = False
            temp = enemy.move
            if temp < 0: temp = -temp
            score_points += (50 + 10*temp)    # scoring
            # reset enemy               #24
            enemy.enemyXcord = random.randint(0, 736)
            enemy.enemyYcord = random.randint(50, 200)
            if enemy.move > 0:
                enemy.move += 0.05
            else:
                enemy.move -= 0.05
        if enemy.enemyYcord > 450:
            for all in all_enemy:
                all.enemyYcord = 1500
            game_over()
            break

    # move the player by adding or removing move from x cord   #14
    player.playerXcord += player.move

    # if ship came out     from window     #15(41)
    player.checkShipCord()


    # display playerShip              #11(72)
    player.displayPlayer()

    #
    show_score(textX, textY)

    # updating display each time(running shooting,  color changing)     #9(38)
    pygame.display.update()   # always needed line