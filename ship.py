import pygame

class Ship():
    # Ship class require an instance of 'AlienInvasion' class as input
    def __init__(self, ai_game):
        # initialize ship in screen
        self.screen = ai_game.screen
        # using .get_rect() method to create a object of rectangular
        # this object contains attributs of:
        #   1. width and height
        #   2. position like left right top bottom etc.
        self.screen_rect = ai_game.screen.get_rect()

        #laod ship image
        self.image = pygame.image.load('ship.bmp')
        # acquire image rectangular
        # .get_rect() is a method of Surface
        self.rect = self.image.get_rect()
        # remove ship background by colro
        # beaware, this will also remove other pixa with the same colro
        self.image.set_colorkey((230, 230, 230))

        # place new ship in the bottom of window
        self.rect.midbottom = self.screen_rect.midbottom

        # moving right flag (default as not moving)
        self.moving_right = False
        self.moving_left = False

        # defining default firing mode
        self.firing = False
        # defining firing time gap in seconds
        self.fire_gap = 0.5

        # define moving speed
        self.x = float(self.rect.x)
        self.ship_speed = ai_game.settings.ship_speed

    # define method that updates ship position
    def update(self):
        # whiel moving right flat is true and ship is within right boarder
        if  self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        # whiel moving left flat is true and ship is within left boarder
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.ship_speed
        self.rect.x = self.x
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # place ship mid bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)