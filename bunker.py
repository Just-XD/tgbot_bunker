#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint, choice
import helper as h
import getPlayerInfo as g

bpS_file = open('src/bp_short.TXT', encoding='utf-8')
bpS = bpS_file.readlines()
bpS = [line.rstrip() for line in bpS]

bpL_file = open('src/bp_long.TXT', encoding='utf-8')
bpL = bpL_file.readlines()
bpL = [line.rstrip() for line in bpL]

small_bp_file = open('src/small_bp.txt', encoding='utf-8')
small_bp = small_bp_file.readlines()
small_bp = [line.rstrip() for line in small_bp]

bunker = []
mest = disaster = size = 0
bed = None


def mainFunction():
    bunker_addons()
    write_addons()

    bpS_file.close()
    bpL_file.close()
    small_bp_file.close()


# GENERATE BUNKER ADDONS
def bunker_addons():
    s = i = j = 0
    global bed, size, mest
    size = randint(50, 400)

    if int(g.player) == 7:
        mest = 4
    elif int(g.player) == 9:
        mest = 5
    elif int(g.player) == 11:
        mest = 6
    else:
        mest = int(g.player) // 2

    # bunker addons (if size <= 100)
    if size <= 100:
        while s <= len(small_bp) - 1:
            if randint(1, 3) == 1:
                bunker.append(small_bp[s] + '\n')
            s += 1
    else:
        # short addons
        while j <= len(bpS) - 1:
            if randint(1, 4) == 1:
                bunker.append(bpS[j] + '\n')
            j += 1

        # long addons
        while i <= len(bpL) - 1:
            if randint(1, 5) == 1:
                bunker.append(bpL[i] + '\n')
            i += 1

    if size <= 150:  # bed
        bed = 'Спальные мешки для всех находящихся в бункере'
    else:
        bed = 'Полноценные спальные места для всех находящихся в бункере'


# WRITE INFO ABOUT DISASTER AND BUNKER
about_bunker = 0


def write_addons():
    global about_bunker, bed, size, bunker, disaster, mest

    h.rndDisaster()

    t = choice(h.time)
    disaster = choice(h.disasters)

    if disaster == h.disasters[0]:
        size = randint(100, 150)
        t = 'Вся жизнь'
    else:
        pass

    about_bunker = f"""
Размер бункера: {size} кв/м
Время пребывания в бункере: {t}
Мест в бункере: {mest}
В бункере есть:
➢ {'➢ '.join(bunker)}➢ Еды и воды хватит на все время прибывания в бункере
➢ {bed}
➢ {randint(2, 4)} детских кроватки.
"""

    with open('prm/info.txt', 'w', encoding='utf-8') as file:
        file.write(disaster + '\n' + about_bunker)

    bunker.clear()

