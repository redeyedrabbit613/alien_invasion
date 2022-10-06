class Settingst():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width  = 1600
        self.screen_height = 800
        self.bg_color = (0, 0, 230)

        #Star settings
        self.star_speed_factor = 1
        self.fleet_drop_speed = 10
        #Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
