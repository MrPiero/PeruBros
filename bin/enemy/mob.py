import pygame

import sys


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        # Set the size, look, initial position, etc. of an enemy here...
        pass

    def update(self):
        # Define how the enemy moves on each frame here...
        """ Move the platform.
                    If the player is in the way, it will shove the player
                    out of the way. This does NOT handle what happens if a
                    platform shoves a player into another object. Make sure
                    moving platforms have clearance to push the player around
                    or add code to handle what happens if they don't. """

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # Matar jugador
            pass

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # Matar jugador
            pass

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
