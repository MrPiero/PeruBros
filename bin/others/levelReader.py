from bin.platforms.platforms import *
from bin.blocks.blocks import *

def barrier():
    barrier = []
    for x in range(0, 10):
        barrier.append([BLOCK_STONE, 50, 550 - 70 * x])
        barrier.append([BLOCK_STONE, 50 - 70, 550 - 70 * x])
    return barrier

def uncode(level_name):
    f = open('resources/levels/' + level_name + '.pbr')

    d = {'lim': [LIMA1_BASE_M, LIMA1_BASE_L, LIMA1_BASE_R]}
    b = {'lim': [LIMA_BLOCK_1]}

    level = []

    level += barrier()

    f = open('resources/levels/lvl_1_1.pbr')
    l = f.readlines()
    level_type = None
    x = 1

    for words in l:
        print(x)
        print(words)
        if x == 1:
            level_type = words.split()[0]
            print(level_type)
        elif x == 2:
            t = words.split(',')
            for w in t: #lectura de limites de bases
                lims = w.split('-')
                l0 = int(lims[0])
                l1 = int(lims[1])
                level.append([d[level_type][1], 120+70*int(lims[0]), 550])
                level.append([d[level_type][1], 120 + 70 * int(lims[1]), 550])
                for y in range(l0+1, l1):
                    level.append([d[level_type][0], 120+70*y, 550])
        elif x == 3:
            t = words.split(',')
            for w in t: #lectura de bloques
                print(w)
                posxy = w.split('-')
                print(posxy)
                print('test')
                pos_x = int(posxy[0])
                pos_y = int(posxy[1])
                level.append([b[level_type][0],50+70*pos_x, 550-70*pos_y])

        x=x+1

        for t in level:
            print(t)

    return level

