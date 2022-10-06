from alien import Alien
from settings11 import Settings
import pygame

ai_settings = Settings()
screen =  pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
alien = Alien(ai_settings, screen)
alien_width = alien.rect.width
available_space_x = ai_settings.screen_width -  2 * alien_width
number_aliens_x = int(available_space_x / (2 * alien_width))

print(number_aliens_x)
