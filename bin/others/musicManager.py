import pygame


def selectSong(level):
    if (level == 'coast'):
        pygame.mixer.music.load("resources/sounds/costa.mp3")
    elif(level == 'sierra'):
        pygame.mixer.music.load("resources/sounds/Sierra.mp3")
    elif(level == 'selva'):
        pygame.mixer.music.load("resources/sounds/Selva.ogg")
    pygame.mixer.music.play()

def soundJump():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("resources/sounds/jump.ogg"))

def soundMobDeath():
    # pygame.mixer.Channel(1).play(pygame.mixer.Sound("resources/sounds/woosh.mp3"))
    pass

def stopSong():
    pygame.mixer.music.stop()
