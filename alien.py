import pygame
from pygame.sprite import Sprite
from random import choice
from random import randint

class Alien(Sprite):
    def __init__(self, ai_game):
        # inherit a Sprite class
        super().__init__()
        # load screen from game
        self.screen = ai_game.screen
        # load settings from game
        self.settings = ai_game.settings
        # load alien image
        self.image = pygame.image.load('alien.bmp')
        # acquire alien rect from image
        self.rect = self.image.get_rect()
        # remove ship background by colro
        # beaware, this will also remove other pixa with the same colro
        self.image.set_colorkey((230, 230, 230))
        # calculate initial alien position
        # initial position is generated randomly in x axle
        self.rect.x = randint(0, self.screen.get_rect().width - self.rect.width)
        # initial y axle posotion is 1 alien height above screen
        # so that alien can apper into screen
        self.rect.y = 0-self.rect.height

        # define progress x position and y position as float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # randomize initial direction
        self.x_direction =  choice([-1,1])
   
    # define method that updates alien position
    def update(self):
        # update alien x position
        screen_rect = self.screen.get_rect()
        # predict position at current speed and direction
        predict_left = self.x + self.settings.alien_speed_x * self.x_direction
        predict_right = predict_left + self.rect.width
        # if predicted position reached screen edge
        if (predict_right >= screen_rect.right) or (predict_left <= 0):
            # change direction before update progress x position
            self.x_direction *= -1
            # update progress x posision
            self.x += self.settings.alien_speed_x * self.x_direction
        # if predicted position is within screen
        else:
            # update progress x posoition to predicted x position
            self.x = predict_left
        # update alien actual x position
        self.rect.x = self.x

        # update alien progress y position
        self.y += self.settings.alien_speed_y
        # update alien actual y position
        self.rect.y = self.y