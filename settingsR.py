class Settings():
    """A class to store all settings for Rain Drop Sim."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color  = (0, 0, 230)

        #Rain drop settings
        self.rain_speed_factor  = 1
        self.fleet_drop_speed = 10
        #Fleet_direction of 1 represent right; -1 represents left.
        self.fleet_direction = 1
