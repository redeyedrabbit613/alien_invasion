import sys

import pygame
def run_game():
        # Initialize game and creat a screen object.
        pygame.init()
        screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        #set the background color.
        bg_color = (000,  100,  130)

        #Start the main loop for the game.
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Redraw the scrren during each pass through the loop.
            screen.fill(bg_color)
            #Make the most recently drawn screen visible.
            pygame.display.flip()

run_game()
