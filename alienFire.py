import pygame

class FireBullet:

    def __init__(self, screen):
        bullet = pygame.image.load("bullet.png")   # load image
        self.bullet = bullet
        bulletXcord = 0
        self.bulletXcord = bulletXcord
        bulletYcord = 525
        self.bulletYcord = bulletYcord

        self.screen = screen

        bullet_state = False        #check bullet is fired or not
        self.bullet_state = bullet_state

    def fire(self, x, y):
        self.screen.blit(self.bullet, (x + 16, y+10))
        self.bullet_state = True                #shows bullet is fired and on the way

    def check(self,  score):
        if self.bulletYcord <=0:
            self.bulletYcord = 525
            self.bullet_state = False       #if bullet reach top
            if score >= 25:
                score -= 25
                return score
            else:
                return 0
        else: return  score

    def collision(self, enemyXcord, enemyYcord):
        distance = ((enemyXcord - self.bulletXcord)**2 + (enemyYcord - self.bulletYcord)**2)**(1/2)
        if distance < 28:
            return True
        return False
