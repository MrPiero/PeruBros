import pygame


def selectSong(level):
    if (level == 'coast'):
        pygame.mixer.music.load("resources/sounds/costa.mp3")
        pygame.mixer.music.play()


def soundJump():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("resources/sounds/jump.ogg"))

def soundMobDeath():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("resources/sounds/woosh.ogg"))

def stopSong():
    pygame.mixer.music.stop()
