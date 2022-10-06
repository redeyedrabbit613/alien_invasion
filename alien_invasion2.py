import sys
import pygame

from settings2 import Settings
from ship2 import Ship
import game_functions2 as gf

def run_game():
    #Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Draw the ship
    ship = Ship(ai_settings, screen)

    #Start the main loop for the game.
    while True:
        #Watch for keyboard and mouse events
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
