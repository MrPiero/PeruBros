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
URL_SAVE_PROGRESS_CHAR = "http://www.soft2.wecan.com.pe/laravel/public//personaje/api/saveprogress"
URL_SAVE_SCORE_CHAR = "http://www.soft2.wecan.com.pe/laravel/public//personaje/api/savepuntaje"

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

level_number = {'lvl_1_1' : 0, 'lvl_1_2' : 1, "lvl_1_3" : 2,
                'lvl_2_1' : 3, 'lvl_2_2' : 4, "lvl_2_3" : 5,
                'lvl_3_1': 6, 'lvl_3_2': 7, "lvl_3_3": 8}
level_type = {'lvl_1_1' : 'coast',
              'lvl_1_2' : 'coast',
              'lvl_1_3' : 'coast',
              'lvl_2_1': 'sierra',
              'lvl_2_2': 'sierra',
              'lvl_2_3': 'sierra',
              'lvl_3_1' : 'selva',
              'lvl_3_2' : 'selva',
              'lvl_3_3' : 'selva'
              }

level_n = {(1,1): 'lvl_1_1',(1,2): 'lvl_1_2',(1,3): 'lvl_1_3',
              (2, 1): 'lvl_2_1', (2, 2): 'lvl_2_2', (2, 3): 'lvl_2_3',
              (3, 1): 'lvl_3_1', (3, 2): 'lvl_3_2', (3, 3): 'lvl_3_3'}

curr_level = 'lvl_1_1'
level_name = [['lvl_1_1','lvl_1_2'],[],[]]
RESOURCES_OTHERS = "./resources/others/"

SCORES = {'MOB' : 100,
          'LV_CLEAR' : 5000}
