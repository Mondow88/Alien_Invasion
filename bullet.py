import pygame
from pygame.sprite import Sprite

# create a sub class from Parent class Sprite
class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.game = ai_game

        # create Rectangular instance as bullet
        # initial position 0,0 is top left position
        self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
        # bullet intial position is from ship midtopo position
        self.rect.midtop = ai_game.ship.rect.midtop

        # create progress y position
        self.y = float(self.rect.y)

    # define method that updates bullet position
    def update(self):
        # update bullet progress y position
        self.y -= self.settings.bullet_speed
        # update bullet actual y position
        self.rect.y = self.y
        # if bullet moves out of screen, remove bullet
        if self.rect.bottom < 0:
            self.game.bullets.remove(self)

    # define method that draws a bullet
    def draw_bullet(self):
        # draw bullet via drawing regtangular
        pygame.draw.rect(self.screen, self.color, self.rect)
