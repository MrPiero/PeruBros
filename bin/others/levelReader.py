from bin.platforms.platforms import *
from bin.blocks.blocks import *
from bin.blocks.lima_block import *


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
    pb = {'lim': [PLAT1_L, PLAT1_M, PLAT1_R]}
    edificio_base = {'a': [BLOCK_B1_BOTL, BLOCK_B1_BOTM, BLOCK_B1_BOTR],
                     'b': [BLOCK_B2_BOTL, BLOCK_B2_BOTM, BLOCK_B2_BOTR],
                     'g': [BLOCK_B3_BOTL, BLOCK_B3_BOTM, BLOCK_B3_BOTR]}
    edificio_medio = {'a': [BLOCK_B1_MIDL, BLOCK_B1_MIDM, BLOCK_B1_MIDR],
                      'b': [BLOCK_B2_MIDL, BLOCK_B2_MIDM, BLOCK_B2_MIDR],
                      'g': [BLOCK_B3_MIDL, BLOCK_B3_MIDM, BLOCK_B3_MIDR]}
    edificio_techo = {'a': [BLOCK_B1_TOPL, BLOCK_B1_TOPM, BLOCK_B1_TOPR],
                      'b': [BLOCK_B2_TOPL, BLOCK_B2_TOPM, BLOCK_B2_TOPR],
                      'g': [BLOCK_B3_TOPL, BLOCK_B3_TOPM, BLOCK_B3_TOPR]}

    level = []

    level += barrier()
    l = f.readlines()
    level_type = None
    x = 1

    for words in l:

        t = words.split(',')
        if x == 1:
            level_type = words.split()[0]
        elif x == 2:
            limit = int(words.split()[0])
            level += [[BLOCK_END, limit, 490]]
        elif x == 3:
            for w in t:  # lectura de limites de bases
                lims = w.split('-')
                l0 = int(lims[0])
                l1 = int(lims[1])
                level.append([d[level_type][1], 120 + 70 * int(lims[0]), 550])
                level.append([d[level_type][1], 120 + 70 * int(lims[1]), 550])
                for y in range(l0 + 1, l1):
                    level.append([d[level_type][0], 120 + 70 * y, 550])
        elif x == 4:
            for w in t:  # lectura de bloques
                posxy = w.split('-')
                pos_x = int(posxy[0])
                pos_y = int(posxy[1])
                level.append([b[level_type][0], 50 + 70 * pos_x, 550 - 70 * pos_y])
        elif x == 5:
            for w in t:  # lectura de plataformas
                posxyl = w.split('-')
                pos_x = int(posxyl[0])
                pos_y = int(posxyl[1])
                length = int(posxyl[2])
                level.append([pb[level_type][0], 50 + 70 * pos_x, 550 - 70 * pos_y])
                level.append([pb[level_type][2], 50 + 70 * (pos_x + length - 1), 550 - 70 * pos_y])
                for y in range(0, length - 2):
                    level.append([pb[level_type][1], 50 + 70 * (pos_x + length - 2), 550 - 70 * pos_y])
        elif x == 6:
            for w in t:
                posxylh = w.split('-')
                type_b = posxylh[0]
                pos_x = int(posxylh[1])
                pos_y = int(posxylh[2])
                length = int(posxylh[3])
                heigth = int(posxylh[4])
                level.append([edificio_base[type_b][0], 50 + 70 * pos_x, 550 - 70 * pos_y])
                level.append([edificio_base[type_b][2], 50 + 70 * (pos_x + length - 1), 550 - 70 * pos_y])
                level.append([edificio_techo[type_b][0], 50 + 70 * pos_x, 550 - 70 * (pos_y + heigth - 1)])
                level.append(
                    [edificio_techo[type_b][2], 50 + 70 * (pos_x + length - 1), 550 - 70 * (pos_y + heigth - 1)])
                for eje_x in range(0, length - 2):
                    level.append([edificio_base[type_b][1], 50 + 70 * (eje_x + pos_x + 1), 550 - 70 * pos_y])
                    level.append(
                        [edificio_techo[type_b][1], 50 + 70 * (eje_x + pos_x + 1), 550 - 70 * (pos_y + heigth - 1)])

                for eje_y in range(0, heigth - 2):
                    level.append([edificio_medio[type_b][0], 50 + 70 * pos_x, 550 - 70 * (eje_y + pos_y + 1)])
                    level.append(
                        [edificio_medio[type_b][2], 50 + 70 * (pos_x + length - 1), 550 - 70 * (eje_y + pos_y + 1)])

                for eje_x in range(0, length - 2):
                    for eje_y in range(0, heigth - 2):
                        print(eje_x + pos_x + length)
                        level.append(
                            [edificio_medio[type_b][1], 50 + 70 * (eje_x + pos_x + 1), 550 - 70 * (eje_y + pos_y + 1)])

        x = x + 1

    return level
