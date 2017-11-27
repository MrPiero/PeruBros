import bin.region.levels
import bin.others.methods
import bin.constants
from bin.chars.player import Player
from bin.region.level_c import *
import time
from bin.region.levels import *
from bin.others.sprite_manager import *
from bin.others.methods import loading_screen as load


def createPlayer(done):
    player = Player()
    if done == 0:
        player.rect.x = 200
        player.rect.y = 500
    elif done == 1:
        player.rect.x = 200
        player.rect.y = 500
    return player


def LevelInit(player, screen, progress):
    print(progress)
    level_list = []
    lv = Level_C(player, bin.constants.level_n[progress])
    lv.add_data(bin.constants.level_n[progress], screen)
    level_list.append((lv))
    return level_list


def event_move_player(event, player):
    if event.type == pygame.QUIT:
        done = -1

    if event.type == pygame.KEYDOWN and player is not None:
        if event.key == pygame.K_LEFT:
            player.go_left()
        if event.key == pygame.K_RIGHT:
            player.go_right()
        if event.key == pygame.K_UP:
            player.jump()

    if event.type == pygame.KEYUP and player is not None:
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


def main(progress):
    end_status = 0
    done = 0
    pygame.init()
    size = [bin.constants.SCREEN_WIDTH, bin.constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PeruBros")
    load(screen)
    player = createPlayer(done)
    level_list = LevelInit(player, screen, progress)
    curr_level_num = bin.constants.level_number[bin.constants.curr_level]
    current_level = level_list[0]
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
    timer_t = time.time()
    stats = {}

    while done != -1:
        total_time = time.time() - timer_t
        if done == 1:
            if cont == 0:
                timer = time.time()
                cont = 1

            sec = time.time()- timer
            if sec >= 3:
                done = -1

        for event in pygame.event.get():
            event_move_player(event, player)
        active_sprite_list.update()
        current_level.update()
        if player is not None:
            move_world_axis_x(player, current_level, curr_level_num, level_list)
            curr_pos = player.rect.x + current_level.world_shift
            if player.status == 0:
                stats = player.current_stats
                stats['time'] = total_time
                player = None
                done = 1

        if player is not None and curr_pos < current_level.level_limit:
            done = -1
            stopSong()
            player.current_stats['score'] += bin.constants.SCORES['LV_CLEAR']
            stats = player.current_stats
            stats['time'] = total_time
            player = None
            end_status = 1
            current_level.update()

        current_level.draw(screen)
        active_sprite_list.draw(screen)
        clock.tick(60)
        pygame.display.flip()
    #print(stats['deaths'])
    print(stats['score'])
    pygame.quit()
    print(end_status)
    return [end_status,stats]


if __name__ == "__main__":
    main()
