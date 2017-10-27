import pygame




import sys
sys.path.insert(0, '../bin/')
from bin.blocks.blocks import *
import bin.constants
from bin.platforms.platforms import *

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

        self.background = pygame.image.load("resources/pictures/test_background_01.png").convert()
        self.background.set_colorkey(bin.constants.WHITE)
        self.level_limit = -2500


        # Array with type of platform, and x, y location of the platform.
        level = []
        #crear barrera
        for x in range (0,50):
            level.append([BLOCK_STONE, 50, 550-70*x])
            level.append ([BLOCK_STONE, 50-70, 550 - 70 * x])
        #crear bases
        for x in range(0,16):
            level.append([GRASS_BASE_MIDDLE, 120+70*x, 550])


        level += [
                 [BLOCK_DEAD, 260, 340],
                 [BLOCK_POWERUP, 330, 340],
                 [BLOCK_POWERUP, 330, 340-70*2],
                 [BLOCK_DEAD, 400, 340],
                 [GRASS_BASE_RIGHT, 1240, 550],
                 [GRASS_BASE_LEFT, 1800, 550],
                 [GRASS_BASE_MIDDLE, 1870, 550],
                 [GRASS_BASE_MIDDLE, 1940, 550],
                 [GRASS_BASE_MIDDLE, 2010, 550],
                 [GRASS_BASE_MIDDLE, 2080, 550],
                 [GRASS_BASE_MIDDLE, 2150, 550],
                 [GRASS_BASE_MIDDLE, 2220, 550],
                 [GRASS_BASE_MIDDLE, 2290, 550],
                 [GRASS_BASE_MIDDLE, 2360, 550],
                 [GRASS_BASE_MIDDLE, 2430, 550],
                 [GRASS_BASE_MIDDLE, 2500, 550],
                 [GRASS_BASE_MIDDLE, 2570, 550],
                 [GRASS_BASE_MIDDLE, 2640, 550],
                 [GRASS_LEFT, 800, 380],
                 [GRASS_MIDDLE, 870, 380],
                 [GRASS_RIGHT, 940, 380],
                 [GRASS_LEFT, 1120, 280],
                 [GRASS_MIDDLE, 1190, 280],
                 [GRASS_RIGHT, 1260, 280],
                 ]


        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = MovingPlatform(STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


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
        level = [ [STONE_PLATFORM_LEFT, 500, 550],
                  [STONE_PLATFORM_MIDDLE, 570, 550],
                  [STONE_PLATFORM_RIGHT, 640, 550],
                  [GRASS_LEFT, 800, 400],
                  [GRASS_MIDDLE, 870, 400],
                  [GRASS_RIGHT, 940, 400],
                  [GRASS_LEFT, 1000, 500],
                  [GRASS_MIDDLE, 1070, 500],
                  [GRASS_RIGHT, 1140, 500],
                  [STONE_PLATFORM_LEFT, 1120, 280],
                  [STONE_PLATFORM_MIDDLE, 1190, 280],
                  [STONE_PLATFORM_RIGHT, 1260, 280],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = MovingPlatform(STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
