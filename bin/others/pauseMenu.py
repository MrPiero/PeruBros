from random import randrange
import datetime
import os
import pygame
from pygame.locals import *

# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *

# Constants and global variables
ABOUT = ['PygameMenu {0}'.format("Perubros v0.0"),
         'Author: {0}'.format("Grupo F"),
         TEXT_NEWLINE,
         'Email: {0}'.format("...")]
COLOR_BLUE = (12, 12, 200)
COLOR_BACKGROUND = [128, 0, 128]
COLOR_WHITE = (255, 255, 255)
FPS = 60
H_SIZE = 600  # Height of window size
HELP = ['Presiona ESC para salir del menu',
        'Presiona ENTER para entrar a una opcion']
W_SIZE = 800  # Width of window size
audio_status = -1

# Init pygame
pygame.init()
#os.environ['SDL_VIDEO_CENTERED'] = '1'

for m in HELP:
    print(m)

# Crear ventana (sera eliminado)
surface = pygame.display.set_mode((W_SIZE, H_SIZE))
#pygame.display.set_caption('Ejemplo de pausa')


# Main timer and game clock
#clock = pygame.time.Clock()
#timer = [0.0]
#dt = 1.0 / FPS
#timer_font = pygame.font.Font(pygameMenu.fonts.FONT_NEVIS, 100)


# Functions
def mainmenu_background():
    """
    Background color of the main menu, on this function user can plot
    images, play sounds, etc.
    """
    #surface.fill((40, 40, 40))


def reset_timer():
    """
    Reset timer
    """
    #timer[0] = 0


def change_color_bg(c, **kwargs):
    """
    Change background color

    :param c: Color tuple
    """
    if c == (-1, -1, -1):  # If random color
        c = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
    if kwargs['write_on_console']:
        print('New background color: ({0},{1},{2})'.format(*c))
    COLOR_BACKGROUND[0] = c[0]
    COLOR_BACKGROUND[1] = c[1]
    COLOR_BACKGROUND[2] = c[2]

def audio_change(audio_status):
    if audio_status == 0:
        audio_status = -1
    else:
        audio_status = 0

# Menu juego
game_menu = pygameMenu.Menu(surface,
                            window_width=W_SIZE,
                            window_height=H_SIZE,
                            font=pygameMenu.fonts.FONT_NEVIS,
                            title='Menu juego',
                            # Adds 5px to title vertical position
                            title_offsety=5,
                            menu_alpha=85,
                            menu_width=600,
                            menu_height=int(H_SIZE / 2),
                            # If this menu closes (press ESC) back to main
                            onclose=PYGAME_MENU_RESET,
                            dopause=False)

# Adds a selector (element that can handle functions)
game_menu.add_selector('Sonido',
                       # Values of selector, call to change_color_bg
                        [('Encendido', audio_change(audio_status)),  # Random color
                         ('Apagado', audio_change(audio_status))],
                       # Action when changing element with left/right
                        onchange=None,
                       # Action when pressing return on a element
                        onreturn=audio_change(audio_status),
                       # Kwargs, optional parametrs to change_color_bg function
                        write_on_console=True)
game_menu.add_option('Volver al Menu', PYGAME_MENU_BACK)


# Help menu
help_menu = pygameMenu.TextMenu(surface,
                                window_width=W_SIZE,
                                window_height=H_SIZE,
                                font=pygameMenu.fonts.FONT_FRANCHISE,
                                title='Ayuda',
                                # Pressing ESC button does nothing on this menu
                                onclose=PYGAME_MENU_DISABLE_CLOSE,
                                menu_color_title=(120, 45, 30),
                                # Background color
                                menu_color=(30, 50, 107),
                                dopause=False)
help_menu.add_option('Regresar al', PYGAME_MENU_BACK)
for m in HELP:
    help_menu.add_line(m)

# About menu
about_menu = pygameMenu.TextMenu(surface,
                                 window_width=W_SIZE,
                                 window_height=H_SIZE,
                                 font=pygameMenu.fonts.FONT_NEVIS,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 title='Acerca de',
                                 # Disable menu close (ESC button)
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 text_fontsize=20,
                                 font_size_title=30,
                                 menu_color_title=COLOR_BLUE,
                                 dopause=False)
about_menu.add_option('Regresar al Menu', PYGAME_MENU_BACK)
for m in ABOUT:
    about_menu.add_line(m)
about_menu.add_line(TEXT_NEWLINE)

# Main menu, pauses execution of the application
menu = pygameMenu.Menu(surface,
                       window_width=W_SIZE,
                       window_height=H_SIZE,
                       font=pygameMenu.fonts.FONT_NEVIS,
                       title='Menu Pausa',
                       title_offsety=5,
                       menu_alpha=90,
                       enabled=False,
                       bgfun=mainmenu_background,
                       onclose=PYGAME_MENU_CLOSE)
menu.add_option(game_menu.get_title(), game_menu)  # Add timer submenu
menu.add_option(help_menu.get_title(), help_menu)  # Add help submenu
menu.add_option(about_menu.get_title(), about_menu)  # Add about submenu
#menu.add_option('Cerrar Menu', PYGAME_MENU_CLOSE)
menu.add_option('Salir del juego', PYGAME_MENU_EXIT)  # Add exit function

# Main loop
while True:

    # Tick
    #clock.tick(60)
    #timer[0] += dt

    # Paint background
    #surface.fill(COLOR_BACKGROUND)

    # Application events
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if menu.is_disabled():
                    menu.enable()

    # Draw timer
    #time_string = str(datetime.timedelta(seconds=int(timer[0])))
    #time_blit = timer_font.render(time_string, 1, COLOR_WHITE)
    #time_blit_size = time_blit.get_size()
    #surface.blit(time_blit, (
    #    W_SIZE / 2 - time_blit_size[0] / 2, H_SIZE / 2 - time_blit_size[1] / 2))

    # Execute main from principal menu if is enabled
    menu.mainloop(events)

    # Flip surface
    pygame.display.flip()