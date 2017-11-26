from bin.enemy.mob import *
import bin.constants
from bin.others.levelReader import *
from bin.others.methods import *


class Level:
    platform_list = None
    paloma_list = None
    alpaca_list = None
    otorongo_list = None
    caballo_list = None
    capibara_list = None
    cuy_list = None
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.paloma_list = pygame.sprite.Group()
        self.alpaca_list = pygame.sprite.Group()
        self.otorongo_list = pygame.sprite.Group()
        self.caballo_list = pygame.sprite.Group()
        self.capibara_list = pygame.sprite.Group()
        self.cuy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self):
        self.platform_list.update()
        self.paloma_list.update()
        self.alpaca_list.update()
        self.otorongo_list.update()
        self.caballo_list.update()
        self.cuy_list.update()
        self.capibara_list.update()

    def draw(self, screen):
        screen.fill(bin.constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        self.platform_list.draw(screen)
        self.alpaca_list.draw(screen)
        self.paloma_list.draw(screen)
        self.otorongo_list.draw(screen)
        self.caballo_list.draw(screen)
        self.capibara_list.draw(screen)
        self.cuy_list.draw(screen)

    def shift_world(self, shift_x, shift_y):
        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for platform in self.platform_list:
            platform.rect.y += shift_y

        for enemy in self.paloma_list:
            enemy.rect.x += shift_x

        for enemy in self.paloma_list:
            enemy.rect.y += shift_y

        for enemy in self.alpaca_list:
            enemy.rect.x += shift_x

        for enemy in self.alpaca_list:
            enemy.rect.y += shift_y

        for enemy in self.otorongo_list:
            enemy.rect.x += shift_x

        for enemy in self.otorongo_list:
            enemy.rect.y += shift_y

        for enemy in self.caballo_list:
            enemy.rect.x += shift_x

        for enemy in self.caballo_list:
            enemy.rect.y += shift_y

        for enemy in self.capibara_list:
            enemy.rect.x += shift_x

        for enemy in self.capibara_list:
            enemy.rect.y += shift_y

        for enemy in self.cuy_list:
            enemy.rect.x += shift_x

        for enemy in self.cuy_list:
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
            if(mob[0]=="PALOMA"):
                enemy = Paloma()
            elif(mob[0]=="ALPACA"):
                enemy = Alpaca()
            elif(mob[0]=="OTORONGO"):
                enemy = Otorongo()
            elif (mob[0] == "CABALLO"):
                enemy = Caballo()
            elif(mob[0]=="CAPIBARA"):
                enemy = Capibara()
            elif (mob[0] == "CUY"):
                enemy = Cuy()

            enemy.rect.x = mob[1]
            enemy.rect.y = mob[2]
            enemy.boundary_left = mob[3]
            enemy.boundary_right = mob[4]
            enemy.change_x = mob[5]
            enemy.player = self.player
            enemy.level = self
            if(mob[0]=="PALOMA"):
                self.paloma_list.add(enemy)
            elif(mob[0]=="ALPACA"):
                self.alpaca_list.add(enemy)
            elif(mob[0]=="OTORONGO"):
                self.otorongo_list.add(enemy)
            elif (mob[0] == "CABALLO"):
                self.caballo_list.add(enemy)
            elif (mob[0] == "CAPIBARA"):
                self.capibara_list.add(enemy)
            elif (mob[0] == "CUY"):
                self.cuy_list.add(enemy)
            #self.enemy_list.add(enemy)
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
