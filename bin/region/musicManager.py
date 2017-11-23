import pygame


def selectSong(level):
    if (level == 'coast'):
        pygame.mixer.music.load("resources/sounds/bck_01.ogg")
        pygame.mixer.music.play()


def stopSong():
    pygame.mixer.music.stop()
