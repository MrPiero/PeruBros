import bin.region.levels
import bin.others.methods
import bin.constants
from bin.chars.player import Player
from bin.region.level_coast import *

from bin.region.levels import *

def createPlayer():
    player = Player()
    return player

def LevelInit(player):
    level_list = []
    # piero ahi invocas el metodo con la base de datos y reemplazas el valor de current level.
    level_list.append((Level_Coast(player, bin.constants.current_level)))

    return level_list


def main():
    pygame.init()
    size = [bin.constants.SCREEN_WIDTH, bin.constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PeruBros")

    player = createPlayer()
    level_list = LevelInit(player)
    curr_level_num = bin.constants.level_number[bin.constants.current_level]
    current_level = level_list[curr_level_num]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    # Posicion de origen del jugador
    player.rect.x = 200
    player.rect.y = 500
    active_sprite_list.add(player)
    #estados:
    # 0 = Juego en ejecución
    # -1 = Juego finalizado
    # 2 = ???
    done = 0
    clock = pygame.time.Clock()

    while done != -1:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if player != None:
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                    if event.key == pygame.K_UP:
                        player.jump()

            if event.type == pygame.KEYUP:
                if player != None:
                    if event.key == pygame.K_LEFT and player.eje_x < 0:
                        player.stop()
                    if event.key == pygame.K_RIGHT and player.eje_x > 0:
                        player.stop()

        active_sprite_list.update()
        current_level.update()
        if player != None:
            if player.status == 1:
                if player.rect.x >= 500:
                    diff = player.rect.x - 500
                    player.rect.x = 500
                    current_level.shift_world(-diff, 0)
                if player.rect.x <= 120:
                    diff = 120 - player.rect.x
                    player.rect.x = 120
                    current_level.shift_world(diff, 0)
                current_position = player.rect.x + current_level.world_shift
                current_height = player.rect.y
                if current_height >= 530:
                    player.kill_player()
            if player.status == 0:
                print("Jugador muerto...")
                player = None
                    # player = Player()
                    # changeLv(current_level_no-1, level_list, player)
                    # player.level = current_level
                    # Posicion de origen del jugador
                    # player.rect.x = 300
                    # player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
                    # player.rect.y = 500
                    # active_sprite_list.add(player)
                    # player.status = 1
                    # active_sprite_list.update()


        if current_position < current_level.level_limit:
            player.rect.x = 120
            if curr_level_num < len(level_list)-1:
                #time.sleep (5)
                print("Test_2")
                #dec = nextLevel()
                dec = "1"
                if dec == "1":
                    #changeLv(current_level_no, level_list, player)
                    curr_level_num += 1
                    #print("CL" + current_level)
                    current_level = level_list[curr_level_num]
                    player.level = current_level
                else:
                    pass
            current_level.update()
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        clock.tick(60)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()