import sys
import pygame
from settings import Settings
from ship import Ship
from format_io import Y_N_input
from bullet import Bullet
from alien import Alien
from time import sleep
from time import time
from game_stats import GameStats
from random import randint

class AlienInvasion:
    def __init__(self):
        # pygame.init() is mandatory to use pygame lib
        # 1. it initialize mutiple module of Pygame lib
        # 2. it checks system resource: graphic, sound etc
        # 3. it initialize display window
        # 4. it initialize handling of user imput (event)
        pygame.init()

        # set window resolution by using a tuple of pixas
        self.clock = pygame.time.Clock()

        # create instance of settings
        self.settings = Settings()

        # .display.set_mode() return an instance of Surface class
        # initializing Surface window
        # requesting player input of weather play in fullscreen
        player_screen_choice = Y_N_input("Play game in full screen?")
        if player_screen_choice == 'Y':
            # return a Surface instance in fullscreen
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            # update screen resolution of instance 
            self.settings.screen_res = (self.screen.get_rect().width, self.screen.get_rect().height)
        elif player_screen_choice == 'N':
            # return a Surface instance in default resolution
            self.screen = pygame.display.set_mode(self.settings.screen_res)

        # use default background color in settings
        self.bg_color = self.settings.bg_color

        # set caption of window
        pygame.display.set_caption("Alien Invasion")

        # create Sprite instances
        # each instance is collections of same class instances
        # create group of bulltes
        self.bullets = pygame.sprite.Group()

        # create group of aliens
        self.aliens = pygame.sprite.Group()

        # # create fleet, using method defined below
        # self._create_fleet()

        # create an instance of player ship
        self.ship = Ship(self)

        # create an instance to store game status
        self.stats = GameStats(self)

        # game active flag, initialized as True
        self.game_active = True


    # def game running
    def run_game(self):
        # initialize the last time an alien is created
        last_time_alien_created = time()
        # use - fire_gap as initial last fire time
        # so that 1st round can always be shot
        last_fire_time = time() - self.ship.fire_gap
        while True:
            # monitoring keyboard and mouse input
            self._check_vents()

            # update game elements while game_active flag being True
            if self.game_active:
                # update ship position
                self.ship.update()
                # update bullet position
                # fire bullet
                last_fire_time = self._fire_bullet(last_fire_time)
                self._update_bullets()
                print(f"bullets left: {len(self.bullets)}")
                # create aliens
                last_time_alien_created = self._create_alien(last_time_alien_created)
                # update alien position
                self._update_aliens()
                
            # update screen
            self._update_screen()

            # define refresh rate
            self.clock.tick(60)

    # define method that monitors palyer input
    def _check_vents(self):
        # check all event in event group
        for event in pygame.event.get():
            # system quite
            if event.type == pygame.QUIT:
                sys.exit()
            # check whether any key pressed down
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # check whether any key released up
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # keydown events monitoring method
    def _check_keydown_events(self, event):
        # set moving right on right keydown
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # set moving left on left keydown
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # quit game on q keydown
        elif event.key == pygame.K_q:
            sys.exit()
        # set firing flag on space keydown
        elif event.key == pygame.K_SPACE:
            self.ship.firing = True


    # keyup events monitoring method
    def _check_keyup_events(self, event):
        # reset moving right on right keyup
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        # reset moving right on left keyup
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        # reset firing flag on space keyup
        elif event.key == pygame.K_SPACE:
            self.ship.firing = False

    # define fire bullets method
    def _fire_bullet(self, last_time):
        # only fire bullets while bullets on screen is less than maximum allowed
        # firing condition check
        # check firing control - pressed down space
        firing_control_check = self.ship.firing
        # check maximum bullets in group
        # be noted, bullets collide aliens or passed screen top should be removed
        bullets_number_check =  (len(self.bullets) < self.settings.bullets_allowed)
        # check firing gap
        firing_gap = time() - last_time
        firing_gap_check = firing_gap > self.ship.fire_gap
        # fire bullet when all firing condition checked
        if firing_gap_check and firing_control_check and bullets_number_check:
            # initialize new bullet instance
            new_bullet = Bullet(self)
            # add new instance to group instance
            self.bullets.add(new_bullet)
            # update current time as last time a bullet is fired
            return time()
        else:
            # if firing condition not checked
            # maintain last time
            return last_time

    # define method that updates screen:
    def _update_screen(self):
        # set back ground color
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            # draw ship
        self.ship.blitme()
        # draw alienship
        self.aliens.draw(self.screen)
        # refresh window display
        pygame.display.flip()

    # define method that updates bullet
    def _update_bullets(self):
        # update bullet position
        # be noted, here used group.method, not instance.method
        # different from origianl code:
        # removing bullet out of screen has been define in bullet.update()
        # thus a traversal check of bullets position is not required
        self.bullets.update()
        self._check_bullet_alien_collisions()

    # defeine method that create alien ships
    # method return time that a new alien is created
    def _create_alien(self, last_time):
        # calculate how log is passed since last time an alien ship is created
        delta_time = time() - last_time
        # check delta time is more than minimum time gap
        delta_time_flag = delta_time > self.settings.minimum_respawn_gap
        # check alien number is within maximum allowed number
        alien_number_flag = len(self.aliens) < self.settings.aliens_allowed
        # create alien when two flags above is True
        if delta_time_flag and alien_number_flag:
            # creata an Alien instance
            new_alien = Alien(self)
            # intialize new alien respawn position
            # ---------------------------
            # acquire alien diameter
            alien_width, alien_height = new_alien.rect.width, new_alien.rect.height
            # calculate random respawn horizontal position
            respawn_x = randint(0, self.settings.screen_res[0]-alien_width)
            new_alien.rect.x = respawn_x
            # define vertical respawn position:
            #     0-alien height
            # so that alien ship can appear bit by bit vetically
            respawn_y = 0-alien_height
            new_alien.rect.y = respawn_y
            # ---------------------------
            # add new alien to alien group
            self.aliens.add(new_alien)
            # return current time that a new alien being created
            return time()
        else:
            # return last time a alien being created
            return last_time

    # define method that update alien position
    def _update_aliens(self):
        # define alien moving direction in x
        for alien in self.aliens.sprites().copy():
            alien.update()
        # if alien x + speed is within border, update position
        # check collision between aliens and own ship
        # define ship hit condition
            hit_ship_flag = pygame.sprite.spritecollideany(self.ship, self.aliens)
            # define alien moving out of screen bottom flag
            if alien.rect.bottom >= self.settings.screen_res[1] + alien.rect.height:
                reach_bottom_flag = True
                print(f'Aliens left: {len(self.aliens)}')
            else:
                reach_bottom_flag = False
            # define action when ship is hit or alien reach bottom
            if hit_ship_flag or reach_bottom_flag:
                self._ship_hit(alien)

    # define method that checks bullet alien collision
    def _check_bullet_alien_collisions(self):
            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    # define ship behavior when alien hits ship or reach screen bottom
    def _ship_hit(self, alien):
        # when ship has life left
        if self.stats.ship_left > 0:
            # ship life minus 1
            self.stats.ship_left -= 1
            # # change background color while hit
            # self.bg_color = [255, 99, 71,]
            # self._update_screen()
            # pause shortly
            sleep(0.15)
            # when hit, remove alien
            self.aliens.remove(alien)
            # # change back background color after hit
            # self.bg_color = [230, 230, 230,]
        # when shp life exhausted
        else:
            # reset game active flag
            self.game_active = False
            print('Game Fail')

# if below is used to ensure game running only when the main script is running
# below code cannot be used while imported.
if __name__ == '__main__':
    # create instance of game
    ai = AlienInvasion()
    # run game
    ai.run_game()