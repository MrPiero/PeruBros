"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame

import sys
sys.path.insert(0, '../../bin/')
import bin.constants

from bin.platforms.platforms import MovingPlatform
from bin.others.spritesheet_functions import SpriteSheet
from bin.others.methods import *

bck = (255,0,255)

class Player(pygame.sprite.Sprite):
    #velocidad
    eje_x = 0
    eje_y = 0

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []

    # What direction is the player facing?
    direction = "R"

    # List of sprites we can bump against
    level = None

    # -- Methods
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #(self, x, y, width, height):
        #pic = pygame.image.load("../../resources/sprites/chars/char_test5.png").convert_alpha()
        #sprite_sheet = SpriteSheet("../../resources/sprites/chars/char_test3d.png")
        sprite_sheet = SpriteSheet(select_char())
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 20, 66, 90-20)
        image.set_colorkey(bck)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 20, 66, 90-20)
        image.set_colorkey(bck)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 20, 67, 90-20)
        image.set_colorkey(bck)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 93+20, 66, 90-20)
        image.set_colorkey(bck)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 93+20, 66, 90-20)
        image.set_colorkey(bck)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 93+20, 72, 90-20)
        image.set_colorkey(bck)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 186+20, 70, 90-20)
        image.set_colorkey(bck)
        self.walking_frames_r.append(image)
        #rev
        image = sprite_sheet.get_image(0, 0+20, 66, 90-20)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(bck)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 0+20, 66, 90-20)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(bck)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 0+20, 67, 90-20)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(bck)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 93+20, 66, 90-20)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(bck)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 93+20, 66, 90-20)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(bck)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 93+20, 72, 90-20)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(bck)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 186+20, 70, 90-20)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey(bck)
        self.walking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        # movimiento del jugador
        # Gravedad
        self.calc_grav()

        # izq/der
        self.rect.x += self.eje_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.eje_x > 0:
                self.rect.right = block.rect.left
            elif self.eje_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.eje_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.eje_y > 0:
                self.rect.bottom = block.rect.top
            elif self.eje_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.eje_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.eje_y == 0:
            self.eje_y = 1
        else:
            self.eje_y += .70

        # See if we are on the ground.
        if self.rect.y >= bin.constants.SCREEN_HEIGHT - self.rect.height and self.eje_y >= 0:
            self.eje_y = 0
            self.rect.y = bin.constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= bin.constants.SCREEN_HEIGHT:
            #altura salto
            self.eje_y = -18

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.eje_x = -6
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.eje_x = 6
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.eje_x = 0
