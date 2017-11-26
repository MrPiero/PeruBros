from bin.enemy.mob import *
import bin.constants
from bin.others.levelReader import *
from bin.others.methods import *


class Level:
    platform_list = None
    enemy_list = None
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        screen.fill(bin.constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x, shift_y):
        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for platform in self.platform_list:
            platform.rect.y += shift_y

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.y += shift_y

    def add_data(self, levelName, screen):
        data = uncode(levelName)

        level = []
        mobs = []
        moving_platforms = []

        level += data[0]
        mobs += data[1]
        moving_platforms += data[2]

        total_elements = len(level) + len(mobs) + len(moving_platforms)
        #print("Numero de objetos: " + str(total_elements))
        cont = 0
        # Lectura del arreglo level[]
        for platform in level:
            cont = cont + 1
            block = Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
            loading_bar(cont, total_elements, screen)
        # lectura del arreglo mobs[]
        for mob in mobs:
            cont = cont + 1
            enemy = MovingEnemy(mob[0])
            enemy.rect.x = mob[1]
            enemy.rect.y = mob[2]
            enemy.boundary_left = mob[3]
            enemy.boundary_right = mob[4]
            enemy.change_x = mob[5]
            enemy.player = self.player
            enemy.level = self
            self.enemy_list.add(enemy)
            loading_bar(cont, total_elements, screen)
        for movplat in moving_platforms:
            cont = cont + 1
            mp = MovingPlatform(movplat[0])
            mp.rect.x = movplat[1]
            mp.rect.y = movplat[2]
            mp.boundary_left = movplat[3]
            mp.boundary_right = movplat[4]
            mp.change_x = movplat[5]
            mp.player = self.player
            mp.level = self
            self.platform_list.add(mp)
            loading_bar(cont, total_elements, screen)
        self.level_limit = 1000 - data[3]
