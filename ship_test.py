import pygame

class TShip():

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/trumpy.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect =  screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def blitme(self):
        """ Draw the ship  at is current location."""
        self.screen.blit(self.image, self.rect)
