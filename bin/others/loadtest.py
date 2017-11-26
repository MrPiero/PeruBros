import pygame
import bin.constants



def main():
    pygame.init()
    size = [bin.constants.SCREEN_WIDTH, bin.constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PeruBros")
    print("A")
    bck = pygame.image.load("resources/pictures/loading_temp.png").convert()
    screen.fill(bin.constants.WHITE)
    screen.blit(bck, (0, 0))
    pygame.display.flip()
    print("t")