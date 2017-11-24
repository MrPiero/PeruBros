import pygame
from bin.others.sprite_manager import SpriteSheet

bck = (255, 0, 255)


class Enemy(pygame.sprite.Sprite):
        walking_frames_l = []
        walking_frames_r = []

        direction = "R"

        def __init__(self, mob_type):
            pygame.sprite.Sprite.__init__(self)

            sprite_sheet = SpriteSheet("resources/sprites/enemy/mobs.png")
            if mob_type == "PALOMA":
                for x in range (1,6):
                    image = sprite_sheet.get_image(0+70*x, 70, 70, 70)
                    image.set_colorkey(bck)
                    self.walking_frames_r.append(image)
                    image = sprite_sheet.get_image(0+70*x, 70, 70, 70)
                    image = pygame.transform.flip(image, True, False)
                    image.set_colorkey(bck)
                    self.walking_frames_l.append(image)

            self.image = self.walking_frames_r[0]
            self.rect = self.image.get_rect()

class MovingEnemy(Enemy):
        change_x = 0
        change_y = 0

        boundary_top = 0
        boundary_bottom = 0
        boundary_left = 0
        boundary_right = 0

        past_dir = 0

        direction = "R"

        level = None
        player = None

        def update(self):
            pos = self.rect.x # self.level.world_shift
            if self.direction == "R":
                frame = (pos // 30) % len(self.walking_frames_r)
                self.image = self.walking_frames_r[frame]
            else:
                frame = (pos // 30) % len(self.walking_frames_l)
                self.image = self.walking_frames_l[frame]

            self.rect.x += self.change_x

            hit = pygame.sprite.collide_rect(self, self.player)
            if hit:
                self.player.kill_player()

            self.rect.y += self.change_y

            cur_pos = self.rect.x - self.level.world_shift
            if cur_pos < self.boundary_left or cur_pos > self.boundary_right:

                self.change_x *= -1

                print(self.change_x)

                if self.change_x >= 1:
                    self.direction = "R"
                else:
                    self.direction = "L"
