import pygame
import sys
sys.path.insert(0, '../bin/')
from bin.enemy.mob import *
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
        mobs = []

        data = uncode('lvl_1_1')
        level += data[0]
        mobs += data[1]

        # Lectura del arreglo level[]
        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
        #lectura del arreglo mobs[]
        for mob in mobs:
            enemy = MovingEnemy(mob[0])
            enemy.rect.x = mob[1]
            enemy.rect.y = mob[2]
            enemy.boundary_left = mob[3]
            enemy.boundary_right = mob[4]
            enemy.change_x = mob[5]
            enemy.player = self.player
            enemy.level = self
            self.platform_list.add(enemy)

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
