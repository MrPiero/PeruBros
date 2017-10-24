import time
import constants
#import sys
#sys.path.insert(0, '../../bin/')
from chars.player import Player
from others.methods import *
from others.pauseMenu import *

from region.levels import *

def pause(surface):
    ABOUT = ['PygameMenu {0}'.format ("Perubros v0.0"),
             'Author: {0}'.format ("Grupo F"),
             TEXT_NEWLINE,
             'Email: {0}'.format ("...")]
    COLOR_BLUE = (12, 12, 200)
    COLOR_BACKGROUND = [128, 0, 128]
    COLOR_WHITE = (255, 255, 255)
    FPS = 60
    H_SIZE = 600  # Height of window size
    HELP = ['Presiona ESC para salir del menu',
            'Presiona ENTER para entrar a una opcion']
    W_SIZE = 800  # Width of window size
    audio_status = -1

    for m in HELP:
        print(m)

    game_menu = pygameMenu.Menu (surface,
                                 window_width=W_SIZE,
                                 window_height=H_SIZE,
                                 font=pygameMenu.fonts.FONT_NEVIS,
                                 title='Menu juego',
                                 # Adds 5px to title vertical position
                                 title_offsety=5,
                                 menu_alpha=85,
                                 menu_width=600,
                                 menu_height=int (H_SIZE / 2),
                                 # If this menu closes (press ESC) back to main
                                 onclose=PYGAME_MENU_RESET,
                                 dopause=False)

    # Adds a selector (element that can handle functions)
    game_menu.add_selector ('Sonido',
                            # Values of selector, call to change_color_bg
                            [('Encendido', audio_change (audio_status)),  # Random color
                             ('Apagado', audio_change (audio_status))],
                            # Action when changing element with left/right
                            onchange=None,
                            # Action when pressing return on a element
                            onreturn=audio_change (audio_status),
                            # Kwargs, optional parametrs to change_color_bg function
                            write_on_console=True)
    game_menu.add_option ('Volver al Menu', PYGAME_MENU_BACK)

    # Help menu
    help_menu = pygameMenu.TextMenu (surface,
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
    help_menu.add_option ('Regresar al', PYGAME_MENU_BACK)
    for m in HELP:
        help_menu.add_line (m)

    # About menu
    about_menu = pygameMenu.TextMenu (surface,
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
    about_menu.add_option ('Regresar al Menu', PYGAME_MENU_BACK)
    for m in ABOUT:
        about_menu.add_line (m)
    about_menu.add_line (TEXT_NEWLINE)

    # Main menu, pauses execution of the application
    menu = pygameMenu.Menu (surface,
                            window_width=W_SIZE,
                            window_height=H_SIZE,
                            font=pygameMenu.fonts.FONT_NEVIS,
                            title='Menu Pausa',
                            title_offsety=5,
                            menu_alpha=90,
                            enabled=False,
                            bgfun=mainmenu_background,
                            onclose=PYGAME_MENU_CLOSE)
    menu.add_option (game_menu.get_title (), game_menu)  # Add timer submenu
    menu.add_option (help_menu.get_title (), help_menu)  # Add help submenu
    menu.add_option (about_menu.get_title (), about_menu)  # Add about submenu
    # menu.add_option('Cerrar Menu', PYGAME_MENU_CLOSE)
    menu.add_option ('Salir del juego', PYGAME_MENU_EXIT)  # Add exit function

    # Main loop
    while True:

        # Tick
        # clock.tick(60)
        # timer[0] += dt

        # Paint background
        # surface.fill(COLOR_BACKGROUND)

        # Application events
        events = pygame.event.get ()
        for event in events:
            if event.type == QUIT:
                exit ()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if menu.is_disabled ():
                        menu.enable ()

        # Draw timer
        # time_string = str(datetime.timedelta(seconds=int(timer[0])))
        # time_blit = timer_font.render(time_string, 1, COLOR_WHITE)
        # time_blit_size = time_blit.get_size()
        # surface.blit(time_blit, (
        #    W_SIZE / 2 - time_blit_size[0] / 2, H_SIZE / 2 - time_blit_size[1] / 2))

        # Execute main from principal menu if is enabled
        menu.mainloop (events)

        # Flip surface
        pygame.display.flip ()

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Platformer with sprite sheets")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    #Posicion de origen del jugador
    player.rect.x = 200
    #player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    player.rect.y = 500
    active_sprite_list.add(player)

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

            if event.type == QUIT:
                    exit ()
            elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        if pause(screen).menu.is_disabled ():
                            pause(screen).menu.enable()


        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            #piero estupido
            #time.sleep(5)
            #print("Test_1")
            if current_level_no < len(level_list)-1:
                time.sleep (5)
                print("Test_2")
                dec = nextLevel()
                if dec == "1":
                    current_level_no += 1
                    current_level = level_list[current_level_no]
                    player.level = current_level
                else:
                    pass


        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()
