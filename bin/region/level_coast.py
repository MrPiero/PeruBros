from bin.others.musicManager import *
from bin.region.levels import *


class Level_Coast(Level):

    origin_X = 330
    origin_Y = 70

    def __init__(self, player, name):
        Level.__init__(self, player)
        level_name = name

        self.background = pygame.image.load("resources/pictures/" + level_name + ".png").convert()
        self.background.set_colorkey(bin.constants.WHITE)
        #self.add_data(level_name)

        pygame.mixer.init()
        selectSong('coast')