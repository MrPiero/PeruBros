import pygame




import sys
sys.path.insert(0, '../bin/')
from bin.blocks.blocks import *
from bin.enemy.mob import *
from bin.blocks.lima_block import *
import bin.constants
#from bin.platforms.platforms import *
from bin.others.levelReader import *

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None

    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(bin.constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x, shift_y):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for platform in self.platform_list:
            platform.rect.y += shift_y

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.y += shift_y

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
    origin_X = 330
    origin_Y = 70

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("resources/pictures/bck_lima.png").convert()
        self.background.set_colorkey(bin.constants.WHITE)
        self.level_limit = -4000


        # Array with type of platform, and x, y location of the platform.
        level = []

        level+= uncode('lvl_1_1')

        #Crear un edificio (Amarillo de ejemplo)
        level.append([BLOCK_B1_BOTL, 1800, 480])
        level.append([BLOCK_B1_BOTR, 2010+70, 480])
        level.append([BLOCK_B1_MIDL, 1800, 410])
        level.append([BLOCK_B1_MIDR, 2010 + 70, 410])
        level.append([BLOCK_B1_MIDL, 1800, 340])
        level.append([BLOCK_B1_MIDR, 2010 + 70, 340])
        level.append([BLOCK_B1_TOPL, 1800, 270])
        level.append([BLOCK_B1_TOPR, 2010 + 70, 270])
        for x in range(0,3):
            level += [
                [BLOCK_B1_BOTM, 1870 + 70 * x, 480],
                [BLOCK_B1_MIDM, 1870 + 70 * x, 410],
                [BLOCK_B1_MIDM, 1870 + 70 * x, 340],
                [BLOCK_B1_TOPM, 1870 + 70 * x, 270]
            ]

        #Crear Segundo edificio
        level.append([BLOCK_B2_BOTL, 2500, 480])
        level.append([BLOCK_B2_MIDL, 2500, 410])
        level.append([BLOCK_B2_TOPL, 2500, 340])
        level.append([BLOCK_B2_BOTR, 2920, 480])
        level.append([BLOCK_B2_MIDR, 2920, 410])
        level.append([BLOCK_B2_TOPR, 2920, 340])
        for x in range (0,5):
            level += [
                [BLOCK_B2_BOTM, 2570 + x*70, 480],
                [BLOCK_B2_MIDM, 2570 + x * 70, 410],
                [BLOCK_B2_TOPM, 2570 + x * 70, 340]
            ]
        #Crear tercer edificio
        level.append([BLOCK_B3_BOTL, 2990, 480])
        level.append([BLOCK_B3_BOTR, 3270, 480])
        level.append([BLOCK_B3_MIDL, 2990, 410])
        level.append([BLOCK_B3_MIDR, 3270, 410])
        level.append([BLOCK_B3_MIDL, 2990, 340])
        level.append([BLOCK_B3_MIDR, 3270, 340])
        level.append([BLOCK_B3_TOPL, 2990, 270])
        level.append([BLOCK_B3_TOPR, 3270, 270])
        for x in range(0, 3):
            level += [
                [BLOCK_B3_BOTM, 3060 + 70 * x, 480],
                [BLOCK_B3_MIDM, 3060 + 70 * x, 410],
                [BLOCK_B3_MIDM, 3060 + 70 * x, 340],
                [BLOCK_B3_TOPM, 3060 + 70 * x, 270]
            ]

        level += [
                 [LIMA1_BASE_R, 1240, 550],
                 [LIMA1_BASE_L, 1800, 550],
                 [LIMA1_BASE_M, 1870, 550],
                 [LIMA1_BASE_M, 1940, 550],
                 [LIMA1_BASE_M, 2010, 550],
                 [LIMA1_BASE_M, 2080, 550],
                 [LIMA1_BASE_M, 2150, 550],
                 [LIMA1_BASE_M, 2220, 550],
                 #[GRASS_BASE_MIDDLE, 2290, 550],
                 #[GRASS_BASE_MIDDLE, 2360, 550],
                 #[GRASS_BASE_MIDDLE, 2430, 550],
                 [LIMA1_BASE_M, 2500, 550],
                 [LIMA1_BASE_M, 2570, 550],
                 [LIMA1_BASE_M, 2640, 550],
                 [PLAT1_L , 800, 380],
                 [PLAT1_M, 870, 380],
                 [PLAT1_R, 940, 380],
                 [PLAT1_L, 1120, 280],
                 [PLAT1_M, 1190, 280],
                 [PLAT1_R, 1260, 280],
                 [BLOCK_END, 5000, 490]
                 ]


        # Poner la plataforma del arreglo level[]
        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        #Añadir plataforma maldita
        #killer_plat = KillerPlatform(BLOCK_DEAD)
        #killer_plat.rect.x = 470
        #killer_plat.rect.y = 500
        #killer_plat.boundary_top = 470
        #killer_plat.boundary_bottom = 520
        #killer_plat.change_y = 1
        #killer_plat.player = self.player
        #killer_plat.level = self
        #self.platform_list.add(killer_plat)

        #Añadir enemigo?
        enemy_test = MovingEnemy("PALOMA")
        enemy_test.rect.x = 500
        enemy_test.rect.y = 550-70
        enemy_test.boundary_left = 200
        enemy_test.boundary_right = 500
        enemy_test.change_x = 1
        enemy_test.player = self.player
        enemy_test.level = self
        self.platform_list.add(enemy_test)

        # Añadir enemigo?
        enemy_test2 = MovingEnemy("PALOMA")
        enemy_test2.rect.x = 2700
        enemy_test2.rect.y = 270
        enemy_test2.boundary_left = 2500
        enemy_test2.boundary_right = 2920
        enemy_test2.change_x = 2
        enemy_test2.player = self.player
        enemy_test2.level = self
        self.platform_list.add(enemy_test2)


        # Add a custom moving platform
        block = MovingPlatform(PLAT1_FLY_M )
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block2 = MovingPlatform(PLAT1_FLY_M )
        block2.rect.x = 1350-200
        block2.rect.y = 280+200
        block2.boundary_left = 1350-200
        block2.boundary_right = 1600-200
        block2.change_x = 1
        block2.player = self.player
        block2.level = self
        self.platform_list.add(block2)


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("resources/pictures/test_background_02.png").convert()
        self.background.set_colorkey(bin.constants.WHITE)
        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [ [LIMA1_BASE_M, 0, 550],
                  [LIMA1_BASE_M, 70, 550],
                  [LIMA1_BASE_M, 140, 550],
                  [LIMA1_BASE_M, 210, 400],
                  [LIMA1_BASE_M, -70, 400],
                  [LIMA1_BASE_M, -140, 400],
                  [LIMA1_BASE_M, 240, 500],
                  [LIMA1_BASE_M, 300, 500],
                  [LIMA1_BASE_M, 370, 500],
                  [LIMA1_BASE_M, 1120, 280],
                  [LIMA1_BASE_M, 1190, 280],
                  [LIMA1_BASE_M, 1260, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = MovingEnemy(PLAT1_FLY_M)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
