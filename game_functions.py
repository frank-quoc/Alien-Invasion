import sys

import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        new_bullet = Bullet(ai_settings, screen, ship) #instance bullet is created
        bullets.add(new_bullet) #added to group bullets

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get(): #event loop #pygame.event.get() accesses the events detected by Pygame
        if event.type == pygame.QUIT: #if statements detect and respond to specific event; this exits if you press x
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pss through the loop.
    screen.fill(ai_settings.bg_color) #method fills screen with the argument of color
    ship.blitme()
    # Redraw all bullets behding ship and aliens.
    for bullet in bullets.sprites(): #returns a list of all sprites in the group bullets
        bullet.draw_bullet()
    # Make the most recently drawn screen visiable.
    pygame.display.flip()