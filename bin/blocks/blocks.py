import pygame

from bin.others.spritesheet_functions import SpriteSheet

# Ejemplo: Nombre = (X,Y,W,H)

BLOCK_STONE            = (70, 0, 70, 70)
BLOCK_POWERUP          = (70  , 0, 70, 70)
BLOCK_DEAD             = (70  , 0, 70, 70)

BLOCK_END              = (0 ,0 ,70 ,70 )

LIMA_BLOCK_1 = (70  , 0, 70, 70)

# Lima Blocks
class Block(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_data):

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("../../resources/sprites/blocks/tiles_blocks_v2.png")
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.rect = self.image.get_rect()
