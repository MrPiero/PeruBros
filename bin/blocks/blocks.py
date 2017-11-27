import pygame

from bin.others.sprite_manager import SpriteSheet

# Ejemplo: Nombre = (X,Y,W,H)

BLOCK_STONE            = (70, 0, 70, 70)
BLOCK_POWERUP          = (70  , 0, 70, 70)
BLOCK_DEAD             = (70  , 0, 70, 70)

BLOCK_END              = (0 ,0 ,70 ,70 )

LIMA_BLOCK_1 = (70  , 0, 70, 70)
SELVA_BLOCK_1 = (69  , 420, 70, 70)

SELVA_ARBOL_T =  (560,210,70,70)
SELVA_ARBOL_HL = (491,141,70,70)
SELVA_ARBOL_HM = (561,141,70,70)
SELVA_ARBOL_HR = (631-1,141,70,70)

bck = (27, 25, 27)
# Lima Blocks
class Block(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_data):

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("../../resources/sprites/blocks/Tiles.png")
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.image.set_colorkey(bck)
        self.rect = self.image.get_rect()
