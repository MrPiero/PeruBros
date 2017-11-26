"""
Global constants
"""
from os import path
# Colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (215, 43, 43)
BLUE = (0, 0, 255)
SLATEGREY = (112, 128, 144, 128)

# Screen dimensions
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600

# URL for requests
GAME_FOLDER = path.dirname(__file__)
URL = "http://www.soft2.wecan.com.pe/laravel/public//usuario/listar"
URL_SAVES_USER = "http://www.soft2.wecan.com.pe/laravel/public//personaje/api/"
URL_PROGRESS_SAVE = "http://www.soft2.wecan.com.pe/laravel/public//personaje/api/progreso/"
URL_SAVE_PROGRESS_CHAR = "ulr aca"

# Paths for resources

LOGO_PATH = "resources/logos/perubrologo.png"
FONT_PATH = 'resources/squarefont/Square.ttf'
GAME_MENU_WALLPAPER = "resources/others/GAME_MENU_WALLPAPER.jpg"

# Nombres de Niveles

REGIONS = ("COSTA", "SIERRA", "SELVA")
LEVELS = {"COSTA": ("CUNA DEL SOL", "CAPITAL", "LINEAS MISTERIOSAS"),
          "SIERRA": ("PARAISOS PERDIDOS", "ALTOS HOGARES", "CIUDAD CELESTIAL"),
          "SELVA": ("RIOS CAUDALOSOS", "EL GRAN BOSQUE", "SELVA PROFUNDA")}

# PATH RESOURCES/OTHERS

level_number = {'lvl_1_1' : 0, 'lvl_1_2' : 1}

curr_level = 'lvl_1_1'
level_name = [['lvl_1_1','lvl_1_2'],[],[]]
RESOURCES_OTHERS = "./resources/others/"

SCORES = {'MOB' : 100,
          'LV_CLEAR' : 5000}
