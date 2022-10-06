import pygame
from pygame.sprite import Sprite

class Rain_drop(Sprite):
    """A class to represent a single rain drop in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the rain drop and set its starting position."""
        super(Rain_drop, self).__init__()
        self.screen =  screen
        self.ai_settings = ai_settings

        #Load the rain drop image and set its rect attribute.
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the raindrop down."""
        self.y += self.ai_settings.rain_speed_factor
        self.rect.y = self.y

    def blitme(self):
        """Draw the alien at its current locatiuon."""
        self.screen.blit(self.image, self.rect)
        
