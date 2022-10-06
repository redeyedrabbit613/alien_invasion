import sys
import pygame
from Stars import Star
from random import randint

random_number = randint(1,10)

def update_screen(ai_settings, screen, stars):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    #Making the star appear.
    stars.draw(screen)

    #Make the  most recently drawn  screen visible.
    pygame.display.flip()

def get_number_stars_x(ai_settings, star_width):
    """Determine the number of stars that fit in a row."""
    available_space_x = ai_settings.screen_width - (2 * star_width)
    number_stars_x = int(available_space_x / (2 * star_width))
    return number_stars_x

def get_number_rows(ai_settings, star_height):
    """Determine the number of rows of stars that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                             (3 * star_height) - star_height)
    number_rows = int(available_space_y / (2 * star_height))
    return number_rows

def create_star(ai_settings, screen, stars, star_number, row_number):
    """Create an alien and place it in the row."""
    star = Star(ai_settings, screen)
    star_width = star.rect.width
    star.x = star_width + 2 * star_width * star_number
    star.rect.x = star.x
    star.rect.y = star.rect.height + 2 * star.rect.height * row_number
    stars.add(star)

def create_fleet(ai_settings, screen, stars):
    """Create a full fleet of stars."""
    #Create a star and find the number of stars in a row.
    #Spacing between each star is equal to one star width.
    star = Star(ai_settings, screen)
    number_stars_x = get_number_stars_x(ai_settings, star.rect.width)
    number_rows = get_number_rows(ai_settings, star.rect.height)

    #Create the first row of stars
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(ai_settings, screen, stars, star_number,  row_number)
