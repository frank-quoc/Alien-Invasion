import pygame # module for functionality to make game
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """Initilize pygame, settings, and screen object."""
    pygame.init() #initializes the background settings for Pygame
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) #draws out game's graphical elements
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group() #makes instance of Group(list) and store in variable bullets, this has to be outside while loop

    # Start the main loop for the game
    while True: #game is controlled by this while loop and contains event loops
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update() #update calls for each sprite in the group
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()