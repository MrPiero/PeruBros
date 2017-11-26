import pygame
from bin.others.sprite_manager import SpriteSheet

PLAT1_L            = (70, 80, 70, 60)
PLAT1_R           = (210, 80, 70, 60)
PLAT1_M          = (140, 80, 70, 60)
PLAT1_FLY_L   = (70, 140, 70, 20)
PLAT1_FLY_M = (210, 140, 70, 20)
PLAT1_FLY_R  = (140, 140, 70, 20)


LIMA1_BASE_L       = (70, 140, 70, 70)
LIMA1_BASE_R      = (210, 140, 70, 70)
LIMA1_BASE_M     = (140, 140, 70, 70)

####

PLAT2_L            = (70, 220, 70, 60)
PLAT2_R           = (210, 220, 70, 60)
PLAT2_M          = (140, 220, 70, 60)
PLAT2_FLY_L   = (70, 280, 70, 20)
PLAT2_FLY_M = (210, 280, 70, 20)
PLAT2_FLY_R  = (140, 280, 70, 20)


LIMA2_BASE_L       = (70, 280, 70, 70)
LIMA2_BASE_R      = (210, 280, 70, 70)
LIMA2_BASE_M     = (140, 280, 70, 70)
bck = (255, 0, 255)


class Platform(pygame.sprite.Sprite):

    def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("resources/sprites/blocks/backtotalRosa.png")
        #print("Loading...")
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.image.set_colorkey(bck)
        self.rect = self.image.get_rect()


class MovingPlatform(Platform):

    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):
        self.rect.x += self.change_x

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right

        self.rect.y += self.change_y

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1

    class MovingPlatform(Platform):
        change_x = 0
        change_y = 0

        boundary_top = 0
        boundary_bottom = 0
        boundary_left = 0
        boundary_right = 0

        level = None
        player = None

        def update(self):
            self.rect.x += self.change_x
            hit = pygame.sprite.collide_rect(self, self.player)
            if hit:
                if self.change_x < 0:
                    self.player.rect.right = self.rect.left
                else:
                    self.player.rect.left = self.rect.right
            self.rect.y += self.change_y

            hit = pygame.sprite.collide_rect(self, self.player)
            if hit:
                if self.change_y < 0:
                    self.player.rect.bottom = self.rect.top
                else:
                    self.player.rect.top = self.rect.bottom

            if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
                self.change_y *= -1

            cur_pos = self.rect.x - self.level.world_shift
            if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
                self.change_x *= -1
class KillerPlatform(Platform):
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            self.player.kill_player()

        hit = pygame.sprite.collide_rect(self, self.player)

        if hit:
            self.player.kill_player()

        if self.player.is_collided_with(self):
            self.player.kill_player()



        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        self.rect.y += self.change_y

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1

def is_collided_with(self, sprite):
    return self.rect.colliderect(sprite.rect)

