# define a class to register game status
class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stat()
    
    # define method that resets game status
    def reset_stat(self):
        self.ship_left = self.settings.ship_limit