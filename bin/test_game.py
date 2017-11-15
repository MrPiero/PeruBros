import pygame


import bin.region.levels
import bin.others.methods



import time
import bin.constants
#import sys
#sys.path.insert(0, '../../bin/')
from bin.chars.player import Player
from bin.others.methods import *
#from others.pauseMenu import *

from bin.region.levels import *


def changeLv(current_level_no,level_list,player):
    current_level_no += 1
    current_level = level_list[current_level_no]
    player.level = current_level

def main():
    pygame.init()
    #pygame.font.init()
    #myfont = pygame.font.SysFont ('Arial', 30)
    #textsurface = myfont.render ('Some Text', False, (0, 0, 0))

    # Set the height and width of the screen
    size = [bin.constants.SCREEN_WIDTH, bin.constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)


    pygame.display.set_caption("PeruBros Developer Build")

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
    print ("0")
    pygame.font.init()
    print("1")
    #font = pygame.font.Font(os.path.join('./others/pygameMenu/fonts','8bit.TTF'), 35)
    font_b = pygame.font.SysFont('monospace',35)
    print("judas virgen")
    txt = font_b.render("Holi", True, pygame.Color('white'))
    rect = txt.get_rect()
    #myfont = pygame.font.SysFont ('freesansbold', 30)
    rect.center = ((0,0))
#    display.blit(txt,rect)
    print ("2")
    #textsurface = myfont.render ('Some Text', False, (0, 0, 0))
    print ("3")

    #screen.blit (textsurface, (0, 0))

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
                if event.key == pygame.K_LEFT and player.eje_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.eje_x > 0:
                    player.stop()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:

                    print("Pause :v")
                    # if pause (screen).menu.is_disabled ():
                        #pause (screen).menu.enable ()


        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff, 0)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff, 0)

        # If the player gets near the top side, shift the world right (+y)
        #if player.rect.y <= 120:
        #    diff = 120 - player.rect.y
        #    player.rect.y = 120
        #    current_level.shift_world(0, diff)

        #if player.rect.y >= 480:
        #    diff = player.rect.y - 480
        #    player.rect.y = 480
        #    current_level.shift_world(0, -diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120

            if current_level_no < len(level_list)-1:
                #time.sleep (5)
                print("Test_2")
                #dec = nextLevel()
                dec = "1"
                if dec == "1":
                    #changeLv(current_level_no, level_list, player)
                    current_level_no += 1
                    #print("CL" + current_level)
                    current_level = level_list[current_level_no]
                    player.level = current_level
                else:
                    pass

        current_height = player.rect.y
        print(current_height)
        print("currPOS:" + str(current_position))
        print("currLIM" + str(current_level.level_limit))
        if current_height >= 530:
            player.kill_player()

        if player.status == 0:
            print("Jugador muerto...")
            player = Player()
            changeLv(current_level_no-1, level_list, player)
            player.level = current_level
            # Posicion de origen del jugador
            player.rect.x = current_position - 150
            # player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
            player.rect.y = 500
            active_sprite_list.add(player)
            player.status = 1
            active_sprite_list.update()

            # Update items in the level
            current_level.update()

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


