import pygame
from bin.others.sprite_manager import SpriteSheet
from bin.others.musicManager import soundMobDeath as Sound
from bin.constants import SCORES

bck = (255, 0, 255)


class Enemy(pygame.sprite.Sprite):
        walking_frames_l = []
        walking_frames_r = []

        direction = "R"


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
            pos = self.rect.x  # self.level.world_shift
            if self.direction == "R":
                frame = (pos // 30) % len(self.walking_frames_r)
                self.image = self.walking_frames_r[frame]
            else:
                frame = (pos // 30) % len(self.walking_frames_l)
                self.image = self.walking_frames_l[frame]

            self.rect.x += self.change_x

            hit = pygame.sprite.collide_rect(self, self.player)
            if hit:
                if self.rect.y > self.player.rect.y:
                    # print("muere el mob")
                    # Que suene su muerte
                    Sound()
                    self.kill()
                    self.rect.x = -1000
                    self.rect.y = -1000
                    self.player.current_stats['mobs_killed'] += 1
                    self.player.current_stats['score'] += SCORES['MOB']

                else:
                    self.player.kill_player()
                    # print(self.player.current_stats['deaths'])
                    # print(self.player.current_stats['jumps'])
                    # print(self.player.current_stats['score'])
                    # print(self.player.current_stats['time'])

            self.rect.y += self.change_y

            cur_pos = self.rect.x - self.level.world_shift
            if cur_pos < self.boundary_left or cur_pos > self.boundary_right:

                self.change_x *= -1

                # print(self.change_x)

                if self.change_x >= 1:
                    self.direction = "R"
                else:
                    self.direction = "L"

class Paloma(Enemy):
    walking_frames_l = []
    walking_frames_r = []
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("resources/sprites/enemy/animalesM.png")

        for x in range(1, 6):
            image = sprite_sheet.get_image(0 + 70 * x, 70, 70, 70)
            image.set_colorkey(bck)
            self.walking_frames_r.append(image)
            image = sprite_sheet.get_image(0 + 70 * x, 70, 70, 70)
            image = pygame.transform.flip(image, True, False)
            image.set_colorkey(bck)
            self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()


class Alpaca(Enemy):
    walking_frames_l = []
    walking_frames_r = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("resources/sprites/enemy/animalesM.png")

        for x in range(1, 3):
            image = sprite_sheet.get_image(0 + 70 * x, 0, 70, 70)
            image.set_colorkey(bck)
            self.walking_frames_r.append(image)
            image = sprite_sheet.get_image(0 + 70 * x, 0, 70, 70)
            image = pygame.transform.flip(image, True, False)
            image.set_colorkey(bck)
            self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()


class Otorongo(Enemy):
    walking_frames_l = []
    walking_frames_r = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("resources/sprites/enemy/animalesM.png")

        for x in range(1, 8):
            image = sprite_sheet.get_image(0 + 140 * x, 140, 140, 70)
            image.set_colorkey(bck)
            self.walking_frames_r.append(image)
            image = sprite_sheet.get_image(0 + 140 * x, 140, 140, 70)
            image = pygame.transform.flip(image, True, False)
            image.set_colorkey(bck)
            self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()

class Caballo(Enemy):
    walking_frames_l = []
    walking_frames_r = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("resources/sprites/enemy/animalesM.png")

        for x in range(1, 8):
            image = sprite_sheet.get_image(0 + 140 * x, 210, 140, 70)
            image.set_colorkey(bck)
            self.walking_frames_r.append(image)
            image = sprite_sheet.get_image(0 + 140 * x, 210, 140, 70)
            image = pygame.transform.flip(image, True, False)
            image.set_colorkey(bck)
            self.walking_frames_l.append(image)

        self.image = self.walking_frames_r[0]
        self.rect = self.image.get_rect()