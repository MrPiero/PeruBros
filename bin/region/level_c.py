from bin.others.musicManager import *
from bin.region.levels import *
import bin.constants

class Level_C(Level):

    origin_X = 330
    origin_Y = 70

    def __init__(self, player, name):
        Level.__init__(self, player)
        level_name = name

        self.background = pygame.image.load("resources/pictures/" + level_name + ".png").convert()
        self.background.set_colorkey(bin.constants.WHITE)
        #self.add_data(level_name)

        pygame.mixer.init()
        selectSong(bin.constants.level_type[name])