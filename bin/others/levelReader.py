from bin.platforms.platforms import *
from bin.blocks.blocks import *

f = open('resources/levels/lvl_1_1.pbr')



def barrier():
    barrier = []
    for x in range(0, 10):
        barrier.append([BLOCK_STONE, 50, 550 - 70 * x])
        barrier.append([BLOCK_STONE, 50 - 70, 550 - 70 * x])
    return barrier

def uncode():
    d = {'lim': [LIMA1_BASE_M, LIMA1_BASE_L, LIMA1_BASE_R]}

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
                print(w)
                lims = w.split('-')
                print(lims)
                print('test')
                l0 = int(lims[0])
                l1 = int(lims[1])
                level.append([d[level_type][1], 120+70*int(lims[0]), 550])
                level.append([d[level_type][1], 120 + 70 * int(lims[1]), 550])
                for y in range(l0+1, l1):
                    print(y)

                    level.append([d[level_type][0], 120+70*y, 550])

        x=x+1

        for t in level:
            print(t)

    return level

