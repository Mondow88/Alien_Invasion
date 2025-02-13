import pygame
from random import uniform
class Settings:
    def __init__(self):
        # screen settings
        # -------------------------------
        # default screen resolution
        self.screen_res = (1200,800)
        # default screen background color
        self.bg_color = (200,200,230)
        # -------------------------------

        # bullet settings
        # -------------------------------
        # bullet speed
        self.bullet_speed = 20.0
        # bullet width
        self.bullet_width = 2
        # bullet height
        self.bullet_height = 10
        # bullet color
        self.bullet_color = (255,48,48)
        # max bullet allowed in screen
        self.bullets_allowed = 10
        # -------------------------------

        # player ship settings
        # -------------------------------
        # player ship speed
        self.ship_speed = 6.0
        # -------------------------------

        # alien settings
        # -------------------------------
        # alien speed in x
        self.alien_speed_x = uniform(1.0, 2.5)
        # alien speed in y
        self.alien_speed_y = 1.5
        # fleet drop speed
        self.fleet_drop_speed = 1.0
        # alien fleet direction
        self.fleet_direction = 1
        # ship alowed hits
        self.ship_limit = 3
        # maximum aliens allowed on screen
        self.aliens_allowed = 5
        # alien respawn time gap
        self.minimum_respawn_gap = 1.5
        # -------------------------------