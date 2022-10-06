import pygame
from pygame.sprite import Sprite
from random import randint

random_number = randint(-10,10)

class Star(Sprite):
    """ A class to  represent a single star in  the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the star image and set its rect attribute.
        self.image = pygame.image.load('images/star_1.bmp')
        self.rect = self.image.get_rect()

        #Star each new star near the top left of the screen.
        self.rect.x += random_number
        self.rect.y += random_number
        
        #Store the star's exact position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.star_speed_factor *
                       self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
