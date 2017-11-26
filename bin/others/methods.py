#import spritesheet_functions
import pygame
import bin.constants
#from bin.game import get_screen

def nextLevel():
    dec = input("<<1>> = Next level\n<<2>> Cancel")
    return dec

def select_char():
    # Metodo que consigue el pj de la base de datos
    loc = "resources/sprites/chars/char_test3d.png"
    #sprite_sheet = SpriteSheet()
    return loc

def loading_screen(screen):
    #bck = pygame.image.load("resources/pictures/loading_temp.png").convert()
    bck = pygame.image.load("resources/pictures/loading_temp.png").convert()
    screen.fill(bin.constants.WHITE)
    screen.blit(bck, (0, 0))
    pygame.display.flip()
    #screen.blit(bck, (0,0))

def loading_bar(cont, total, screen):
    value = (cont/total)*100
    value = int(value/5)
    #screen = get_screen()
    bar = pygame.Surface((15*value,43))
    bar.fill(bin.constants.RED)
    #rekt = bar.get_rect()

    screen.blit(bar, (356,465))
    pygame.display.flip()

