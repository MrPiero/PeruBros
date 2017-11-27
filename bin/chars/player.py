import pygame
import bin.constants
from bin.platforms.platforms import MovingPlatform
from bin.others.sprite_manager import SpriteSheet
from bin.others.methods import *
from bin.others.musicManager import soundJump as SoundJump

bck = (255,0,255)

class Player(pygame.sprite.Sprite):
    #velocidad
    eje_x = 0
    eje_y = 0
    direction = "R"

    #arreglos de imagenes del personaje
    camina_L = []
    camina_R = []

    level = None
    lives = 3
    status = 1

    # Por matar monstruos da 100 puntos, por terminar un nivel da 5000.
    _current_stats = {'score': 0,
                     'mobs_killed': 0,
                     'deaths': 0,
                     'jumps': 0,
                     'time' : 0,
                      'death_type' : 0}
    # type 0: no murio
    # type 1: por enemigo
    # type 2: por caida...

    @property
    def current_stats(self):
        return self._current_stats

    @current_stats.setter
    def current_stats(self, val):
        self._current_stats = val

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet(select_char())
        # Cargar imagenes
        image = sprite_sheet.get_image(0, 20, 66, 90-20)
        image.set_colorkey(bck)
        self.camina_R.append(image)
        image = sprite_sheet.get_image(66, 20, 66, 90-20)
        image.set_colorkey(bck)
        self.camina_R.append(image)
        image = sprite_sheet.get_image(132, 20, 67, 90-20)
        image.set_colorkey(bck)
        self.camina_R.append(image)
        image = sprite_sheet.get_image(0, 93+20, 66, 90-20)
        image.set_colorkey(bck)
        self.camina_R.append(image)
        image = sprite_sheet.get_image(66, 93+20, 66, 90-20)
        image.set_colorkey(bck)
        self.camina_R.append(image)
        image = sprite_sheet.get_image(132, 93+20, 72, 90-20)
        image.set_colorkey(bck)
        self.camina_R.append(image)
        image = sprite_sheet.get_image(0, 186+20, 70, 90-20)
        image.set_colorkey(bck)
        self.camina_R.append(image)
        #rev
        image = sprite_sheet.get_image(0, 0+20, 66, 90-20)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(bck)
        self.camina_L.append(image)
        image = sprite_sheet.get_image(66, 0+20, 66, 90-20)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(bck)
        self.camina_L.append(image)
        image = sprite_sheet.get_image(132, 0+20, 67, 90-20)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(bck)
        self.camina_L.append(image)
        image = sprite_sheet.get_image(0, 93+20, 66, 90-20)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(bck)
        self.camina_L.append(image)
        image = sprite_sheet.get_image(66, 93+20, 66, 90-20)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(bck)
        self.camina_L.append(image)
        image = sprite_sheet.get_image(132, 93+20, 72, 90-20)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(bck)
        self.camina_L.append(image)
        image = sprite_sheet.get_image(0, 186+20, 70, 90-20)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(bck)
        self.camina_L.append(image)

        # Imagen inicial
        self.image = self.camina_R[0]
        self.rect = self.image.get_rect()

    def update(self):
        # movimiento del jugador
        # Gravedad
        self.calc_grav()

        # izq/der
        self.rect.x += self.eje_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.camina_R)
            self.image = self.camina_R[frame]
        else:
            frame = (pos // 30) % len(self.camina_L)
            self.image = self.camina_L[frame]

        # Colisiones
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.eje_x > 0:
                self.rect.right = block.rect.left
            elif self.eje_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.eje_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.eje_y > 0:
                self.rect.bottom = block.rect.top
            elif self.eje_y < 0:
                self.rect.top = block.rect.bottom

            self.eje_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        if self.eje_y == 0:
            self.eje_y = 1
        else:
            self.eje_y += .70

        if self.rect.y >= bin.constants.SCREEN_HEIGHT - self.rect.height and self.eje_y >= 0:
            self.eje_y = 0
            self.rect.y = bin.constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        # Sonido de salto
        SoundJump()

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        self.current_stats['jumps'] += 1

        if len(platform_hit_list) > 0 or self.rect.bottom >= bin.constants.SCREEN_HEIGHT:
            #altura salto
            self.eje_y = -18

    def go_left(self):
        self.eje_x = -6
        self.direction = "L"

    def go_right(self):
        self.eje_x = 6
        self.direction = "R"

    def stop(self):
        self.eje_x = 0

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def kill_player(self):
        print("Player is killed.")
        self.current_stats['deaths'] += 1
        self.status = 0
        self.kill()
        self.rect.x = -10000
        self.rect.y = -10000
