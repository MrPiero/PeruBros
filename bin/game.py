import bin.region.levels
import bin.others.methods
import bin.constants
from bin.chars.player import Player
from bin.region.level_coast import *
import time
from bin.region.levels import *
# from datetime import datetime, time


def createPlayer(done):
    player = Player()
    if done == 0:
        player.rect.x = 200
        player.rect.y = 500
    elif done == 1:
        # aca debemos ponerlo en su lugar original...
        player.rect.x = 200
        player.rect.y = 500
        pass
    return player


def LevelInit(player):
    level_list = []
    # piero ahi invocas el metodo con la base de datos y reemplazas el valor de current level.
    level_list.append((Level_Coast(player, bin.constants.curr_level)))
    level_list.append((Level_Coast(player, 'lvl_1_2')))  # este de prueba, hardcoded
    return level_list


def changeLv(curr_level_num, level_list, player):
    stopSong()
    curr_level_num += 1
    curr_level = level_list[curr_level_num]
    player.level = curr_level


def event_move_player(event, player):
    if event.type == pygame.QUIT:
        done = -1

    if event.type == pygame.KEYDOWN:
        if player is not None:
            if event.key == pygame.K_LEFT:
                player.go_left()
            if event.key == pygame.K_RIGHT:
                player.go_right()
            if event.key == pygame.K_UP:
                player.jump()

    if event.type == pygame.KEYUP:
        if player is not None:
            if event.key == pygame.K_LEFT and player.eje_x < 0:
                player.stop()
            if event.key == pygame.K_RIGHT and player.eje_x > 0:
                player.stop()


def move_world_axis_x(player, current_level, curr_level_num, level_list):
    if player.status == 1:
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff, 0)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff, 0)

        current_height = player.rect.y
        if current_height >= 530:
            player.kill_player()


def main():
    done = 0
    pygame.init()
    size = [bin.constants.SCREEN_WIDTH, bin.constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PeruBros")

    player = createPlayer(done)
    level_list = LevelInit(player)
    curr_level_num = bin.constants.level_number[bin.constants.curr_level]
    current_level = level_list[curr_level_num]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    active_sprite_list.add(player)
    # estados:
    # -1 = Juego finalizado
    # 0 = Juego en ejecución
    # 1 = Jugador muerto
    # 2 = ???

    clock = pygame.time.Clock()
    cont = 0
    while done != -1:
        print("Done" + str(done))

        if done == 1:
            if cont == 0:
                timer = time.time()
                cont = 1

            sec = time.time()- timer
            if sec >= 3:
                # poner trigger para contar las muertes
                # funcionAgregarMuerteAEstadisticas
                done = -1

        for event in pygame.event.get():
            event_move_player(event, player)

        active_sprite_list.update()
        current_level.update()
        print(str(player))
        if player is not None:
            move_world_axis_x(player, current_level, curr_level_num, level_list)
            curr_pos = player.rect.x + current_level.world_shift
            if player.status == 0:
                player = None
                done = 1

        if player is not None:
            if curr_pos < current_level.level_limit:
                player.rect.x = 120
                if curr_level_num < len(level_list) - 1:
                    print("Test_2")
                    # dec = nextLevel()
                    dec = "1"
                    if dec == "1":
                        changeLv(curr_level_num, level_list, player)
                        curr_level_num += 1
                        # print("CL" + current_level)
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
    return 1


if __name__ == "__main__":
    main()
