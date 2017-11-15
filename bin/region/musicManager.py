import pygame

def selectSong(level):
    if(level == 0):
        pygame.mixer.music.load("resources/sounds/bck_01.ogg")
        pygame.mixer.music.play()