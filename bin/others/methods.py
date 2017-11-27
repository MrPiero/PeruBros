#import spritesheet_functions
import pygame
import bin.constants
#from bin.game import get_screen


def select_char():
    # Metodo que consigue el pj de la base de datos
    loc = "resources/sprites/chars/char_test3d.png"
    return loc

def loading_screen(screen):
    bck = pygame.image.load("resources/pictures/loading_temp.png").convert()
    screen.fill(bin.constants.WHITE)
    screen.blit(bck, (0, 0))
    pygame.display.flip()


def loading_bar(cont, total, screen):
    value = (cont/total)*100
    value = int(value/5)
    bar = pygame.Surface((15*value,43))
    bar.fill(bin.constants.RED)
    screen.blit(bar, (356,465))
    pygame.display.flip()

