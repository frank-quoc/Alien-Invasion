import sys

import pygame

def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get(): #event loop #pygame.event.get() accesses the events detected by Pygame
        if event.type == pygame.QUIT: #if statements detect and respond to specific event; this exits if you press x
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pss through the loop.
    screen.fill(ai_settings.bg_color) #method fills screen with the argument of color
    ship.blitme()

    # Make the most recently drawn screen visiable.
    pygame.display.flip()