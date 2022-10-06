import sys
import pygame
from settingsR import Settings
from RainDrop import Rain_drop
import game_funcR as gf
from pygame.sprite import Group

def run_sim():
    #Initialize pygame, setting and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,  ai_settings.screen_height))
    pygame.display.set_caption("Rain Simulation")

    #Make a raindrop.
    raindrop = Rain_drop(ai_settings, screen)
    #Make a group to store raindrops in.
    raindrops = Group()
    #Create the fleet of rain drops.
    gf.create_fleet(ai_settings, screen, raindrops)


    #Start the main loop for the game.
    while True:
        gf.update_raindrop(ai_settings, screen, raindrops)
        gf.update_screen(ai_settings, screen, raindrops)

        
        
        
run_sim()
