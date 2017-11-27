import pygame

from bin.others.sprite_manager import SpriteSheet

BLOCK_B1_TOPL            = (280, 0, 70, 70)
BLOCK_B1_TOPM            = (350, 0, 70, 70)
BLOCK_B1_TOPR            = (420, 0, 70, 70)

BLOCK_B1_MIDL            = (280, 73, 70, 70)
BLOCK_B1_MIDM            = (350, 73, 70, 70)
BLOCK_B1_MIDR            = (420, 73, 70, 70)

BLOCK_B1_BOTL            = (280, 146, 70, 70)
BLOCK_B1_BOTM            = (350, 146, 70, 70)
BLOCK_B1_BOTR            = (420, 146, 70, 70)


BLOCK_B2_TOPL            = (280, 0+210, 70, 70)
BLOCK_B2_TOPM            = (350, 0+210, 70, 70)
BLOCK_B2_TOPR            = (420, 0+210, 70, 70)

BLOCK_B2_MIDL            = (280, 73+210, 70, 70)
BLOCK_B2_MIDM            = (350, 73+210, 70, 70)
BLOCK_B2_MIDR            = (420, 73+210, 70, 70)

BLOCK_B2_BOTL            = (280, 146+210, 70, 70)
BLOCK_B2_BOTM            = (350, 146+210, 70, 70)
BLOCK_B2_BOTR            = (420, 146+210, 70, 70)

BLOCK_B3_TOPL            = (280, 0+420, 70, 70)
BLOCK_B3_TOPM            = (350, 0+420, 70, 70)
BLOCK_B3_TOPR            = (420, 0+420, 70, 70)

BLOCK_B3_MIDL            = (280, 73+420, 70, 70)
BLOCK_B3_MIDM            = (350, 73+420, 70, 70)
BLOCK_B3_MIDR            = (420, 73+420, 70, 70)

BLOCK_B3_BOTL            = (280, 146+420, 70, 70)
BLOCK_B3_BOTM            = (350, 146+420, 70, 70)
BLOCK_B3_BOTR            = (420, 146+420, 70, 70)
# Lima Blocks
bck = (255, 0, 255)

class LimaBlock(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):

        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("../../resources/sprites/blocks/tiles_blocks_v2.png")
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.set_colorkey(bck)
        self.rect = self.image.get_rect()
