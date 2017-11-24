import pygame
from bin.others.sprite_manager import SpriteSheet

bck = (255,0,255)

class Enemy(pygame.sprite.Sprite):
        walking_frames_l = []
        walking_frames_r = []

        direction = "R"


        def __init__(self, mob_type):
            """ Platform constructor. Assumes constructed with user passing in
                an array of 5 numbers like what's defined at the top of this
                code. """
            pygame.sprite.Sprite.__init__(self)

            #sprite_sheet = SpriteSheet("resources/sprites/blocks/tiles_blocks_v2.png")
            # Grab the image for this platform
            #self.image = sprite_sheet.get_image(sprite_sheet_data[0],
            #                                    sprite_sheet_data[1],
            #                                    sprite_sheet_data[2],
            #                                    sprite_sheet_data[3])

            #self.rect = self.image.get_rect()
            sprite_sheet = SpriteSheet("resources/sprites/enemy/mobs.png")
            if mob_type == "PALOMA":
                for x in range (1,6):
                    image = sprite_sheet.get_image(0+70*x, 70, 70, 70)
                    image.set_colorkey(bck)
                    self.walking_frames_r.append(image)
                    #rev
                    image = sprite_sheet.get_image(0+70*x, 70, 70, 70)
                    image = pygame.transform.flip(image, True, False)
                    image.set_colorkey(bck)
                    self.walking_frames_l.append(image)

            # Set the image the player starts with
            self.image = self.walking_frames_r[0]

            # Set a referance to the image rect.
            self.rect = self.image.get_rect()

        def is_collided_with(self, sprite):
            return self.rect.colliderect(sprite.rect)

        def touching(self, sprite1, sprite2):
            collided = pygame.sprite.collide_mask(self, sprite1)
            print(">>>>>>>>>>>>>>>>>>>Toco.")
            return collided


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
            #print("***********************************")
            pos = self.rect.x #+ self.level.world_shift
            if self.direction == "R":
                frame = (pos // 30) % len(self.walking_frames_r)
                self.image = self.walking_frames_r[frame]
            else:
                frame = (pos // 30) % len(self.walking_frames_l)
                self.image = self.walking_frames_l[frame]

            # Move left/right
            self.rect.x += self.change_x

            # See if we hit the player
            hit = pygame.sprite.collide_rect(self, self.player)
            #print(hit)
            if hit:
            #    print(hit)
                self.player.kill_player()
            #    print("T1")

            # Move up/down
            self.rect.y += self.change_y

            # Check and see if we the player
            #hit = pygame.sprite.collide_rect(self, self.player)
            #if hit:
            #    self.player.kill_player()
            #    #matar jugador

            #if self.is_collided_with(self.player):
            #    self.player.kill_player()
            #    print("T2")

            #if self.touching(self, self.player):
            #    print(">lel")
            #else:
            #    print("><")


            # Check the boundaries and see if we need to reverse
            # direction.
            #if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            #    self.change_y *= -1

            cur_pos = self.rect.x - self.level.world_shift
            if cur_pos < self.boundary_left or cur_pos > self.boundary_right:

                self.change_x *= -1

                print(self.change_x)

                if self.change_x >= 1:
                    self.direction = "R"
                else:
                    self.direction = "L"
