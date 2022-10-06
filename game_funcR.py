import sys
import pygame
from RainDrop import Rain_drop


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to key presses."""
    if event.key == pygame.K_q:
        sys.exit()
    

def check_events(ai_settings, screen, raindrops):
    """Respond to key presses."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        

def update_screen(ai_settings, screen, raindrop):
    """ Update images on the screen and flip to the new screen."""
    #Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    #Making the raindrop appear.
    raindrop.draw(screen)

    #Make the most recently drawn screen visible.
    pygame.display.flip()

def get_number_raindrops_x(ai_settings, raindrop_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * raindrop_width
    number_raindrops_x = int(available_space_x / (2 *  raindrop_width))
    return number_raindrops_x

def get_number_rows(ai_settings, raindrop_height):
    """Determine the number of rows of raindrops that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * raindrop_height))
    number_rows = int(available_space_y / (2 * raindrop_height))
    return number_rows

def create_raindrop(ai_settings, screen, raindrops, raindrop_number, row_number):
    """Create a raindrop and place it in the row."""
    raindrop = Rain_drop(ai_settings, screen)
    raindrop_width = raindrop.rect.width
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    raindrop.rect.x = raindrop.x
    raindrop.rect.y = raindrop.rect.height + 2 * raindrop.rect.height * row_number
    raindrops.add(raindrop)
    
def create_fleet(ai_settings, screen, raindrops):
    """Create a full fleet of raindrops."""
    # Create a raindrop and find the number of raindrops in a row.
    raindrop = Rain_drop(ai_settings, screen)
    number_raindrops_x = get_number_raindrops_x(ai_settings, raindrop.rect.width)
    number_rows = get_number_rows(ai_settings,raindrop.rect.height)

    #Create the fleet of raindrops.
    for row_number in range(number_rows):
        for raindrop_number in range(number_raindrops_x):
            create_raindrop(ai_settings, screen, raindrops, raindrop_number, row_number)

def change_fleet_directions(ai_settings, raindrops):
    """Drop the entire fleet and change the fleet's direction."""
    for raindrop in raindrops.sprites():
        raindrop.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def update_raindrop(ai_settings, screen, raindrops):
    """
    Check if the fleet is at an edge,
        and then update the positions of all raindrops in the fleet.
    """
    raindrops.update()

    #Get rid of raindrops that have disappeared.
    screen_rect = screen.get_rect()
    for raindrop in raindrops.copy():
        if raindrop.rect.top >= screen_rect.bottom:
            raindrops.remove(raindrop)

    #Create new raindrops and add it to the screen.
    if len(raindrops) == 0:
        new_raindrop = Rain_drop(ai_settings, screen)
        number_raindrops_x = get_number_raindrops_x(ai_settings, new_raindrop.rect.width)
        number_rows = get_number_rows(ai_settings,new_raindrop.rect.height)

        #Create the fleet of raindrops.
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops_x):
                create_raindrop(ai_settings, screen, raindrops, raindrop_number, row_number)
        raindrops.add(new_raindrop)
        raindrops.draw(screen)
        


