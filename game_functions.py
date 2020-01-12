import sys

import pygame

def check_keydown_events(event, ship):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get(): #event loop #pygame.event.get() accesses the events detected by Pygame
        if event.type == pygame.QUIT: #if statements detect and respond to specific event; this exits if you press x
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pss through the loop.
    screen.fill(ai_settings.bg_color) #method fills screen with the argument of color
    ship.blitme()

    # Make the most recently drawn screen visiable.
    pygame.display.flip()