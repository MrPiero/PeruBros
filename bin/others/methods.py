#import spritesheet_functions
import pygame

def nextLevel():
    dec = input("<<1>> = Next level\n<<2>> Cancel")
    return dec

def select_char():
    # Metodo que consigue el pj de la base de datos
    loc = "resources/sprites/chars/char_test3d.png"
    #sprite_sheet = SpriteSheet()
    return loc

def loading_screen():
    bck = pygame.image.load("resources/pictures/loading_temp.png").convert()
    #screen.blit(bck, (0,0))
