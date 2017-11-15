import pygame
from bin.others.spritesheet_functions import SpriteSheet
import sys

GRASS_LEFT            = (576, 720, 70, 70)
GRASS_RIGHT           = (576, 576, 70, 70)
GRASS_MIDDLE          = (504, 576, 70, 70)
STONE_PLATFORM_LEFT   = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT  = (792, 648, 70, 40)

GRASS_BASE_LEFT       = (504, 648, 70, 70)
GRASS_BASE_RIGHT      = (504, 504, 70, 70)
GRASS_BASE_MIDDLE     = (504, 576, 70, 70)
BLOCK_DEAD             = (0  , 432, 70, 70)

class Enemy(pygame.sprite.Sprite):
        """ Platform the user can jump on """

        def __init__(self, sprite_sheet_data):
            """ Platform constructor. Assumes constructed with user passing in
                an array of 5 numbers like what's defined at the top of this
                code. """
            pygame.sprite.Sprite.__init__(self)

            sprite_sheet = SpriteSheet("resources/sprites/blocks/tiles_blocks_v2.png")
            # Grab the image for this platform
            self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                                sprite_sheet_data[1],
                                                sprite_sheet_data[2],
                                                sprite_sheet_data[3])

            self.rect = self.image.get_rect()

class MovingEnemy(Enemy):
        """ This is a fancier platform that can actually move. """
        change_x = 0
        change_y = 0

        boundary_top = 0
        boundary_bottom = 0
        boundary_left = 0
        boundary_right = 0

        level = None
        player = None

        def update(self):
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
                self.player.kill_player()

            # Move up/down
            self.rect.y += self.change_y

            # Check and see if we the player
            hit = pygame.sprite.collide_rect(self, self.player)
            if hit:
                self.player.kill_player()
                #matar jugador

            # Check the boundaries and see if we need to reverse
            # direction.
            if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
                self.change_y *= -1

            cur_pos = self.rect.x - self.level.world_shift
            if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
                self.change_x *= -1
