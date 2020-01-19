import pygame # module for functionality to make game
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    """Initialize pygame, settings, and screen object."""
    pygame.init() #initializes the background settings for Pygame
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) #draws out game's graphical elements
    pygame.display.set_caption("Alien Invasion")

    # Make a ship, groups of bulets, an a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group() #makes instance of Group(list) and store in variable bullets, this has to be outside while loop
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True: #game is controlled by this while loop and contains event loops
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()