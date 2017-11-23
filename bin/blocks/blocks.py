"""
Module for managing blocks.
"""
import pygame

from bin.others.spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

BLOCK_STONE            = (70, 0, 70, 70)
BLOCK_POWERUP          = (70  , 0, 70, 70)
BLOCK_DEAD             = (70  , 0, 70, 70)

BLOCK_END              = (0 ,0 ,70 ,70 )

LIMA_BLOCK_1 = (70  , 0, 70, 70)

# Lima Blocks


class Block(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("../../resources/sprites/blocks/tiles_blocks_v2.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()
