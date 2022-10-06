import sys
import pygame
from settings import Settings
from ship_test  import TShip
import game_functionsT as gf
def run_game():
    #Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    shipt =  TShip(screen)
    
    # Start the main loop for the game.

    while True:
        gf.Tcheck_events()        
        gf.update_screen(ai_settings, screen, shipt)
        
run_game()
