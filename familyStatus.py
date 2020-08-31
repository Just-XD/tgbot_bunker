#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getPlayerInfo as gpi

status_f1, status_f2 = '', ''
man_woman1 = man_woman2 = age1 = age2 = 0


def onlyMan():
    global status_f1, man_woman1, status_f2, man_woman2, age1, age2

    if age1 > age2:
        if (age1 - age2) in range(0, 17):
            status_f1 = 'Брат'
            status_f2 = 'Брат'
        elif (age1 - age2) in range(18, 36):
            if gpi.f1cf == 'Не хочет иметь детей':
                status_f1 = 'Отчим'
                status_f2 = 'Пасынок'
            else:
                status_f1 = 'Папа'
                status_f2 = 'Сын'
        elif (age1 - age2) in range(37, 72):
            status_f1 = 'Дедушка'
            status_f2 = 'Внук'

    elif age1 < age2:
        if (age2 - age1) in range(0, 17):
            status_f2 = 'Брат'
            status_f1 = 'Брат'
        elif (age2 - age1) in range(18, 36):
            if gpi.f2cf == 'Не хочет иметь детей':
                status_f2 = 'Отчим'
                status_f1 = 'Пасынок'
            else:
                status_f2 = 'Папа'
                status_f1 = 'Сын'

        elif (age2 - age1) in range(37, 72):
            status_f2 = 'Дедушка'
            status_f1 = 'Внук'

    elif age1 == age2:
        status_f1 = 'Брат'
        status_f2 = 'Брат'



def onlyWoman():
    global status_f1, man_woman1, status_f2, man_woman2, age1, age2

    if age1 > age2:
        if (age1 - age2) in range(0, 17):
            status_f1 = 'Сестра'
            status_f2 = 'Сестра'
        elif (age1 - age2) in range(18, 36):
            if gpi.f1cf == 'Не хочет иметь детей':
                status_f1 = 'Мачеха'
                status_f2 = 'Падчерица'
            else:
                status_f1 = 'Мама'
                status_f2 = 'Дочь'
        elif (age1 - age2) in range(37, 72):
            status_f1 = 'Бабушка'
            status_f2 = 'Внучка'

    elif age1 < age2:
        if (age2 - age1) in range(0, 17):
            status_f2 = 'Сестра'
            status_f1 = 'Сестра'
        elif (age2 - age1) in range(18, 36):
            if gpi.f2cf == 'Не хочет иметь детей':
                status_f2 = 'Мачеха'
                status_f1 = 'Падчерица'
            else:
                status_f2 = 'Мама'
                status_f1 = 'Дочь'

        elif (age2 - age1) in range(37, 72):
            status_f2 = 'Бабушка'
            status_f1 = 'Внучка'

    elif age1 == age2:
        status_f1 = 'Сестра'
        status_f2 = 'Сестра'



def manWoman():
    global status_f1, man_woman1, status_f2, man_woman2, age1, age2

    # f1 - man / f2 - woman
    if man_woman1 == 'Мужчина':
        if age1 > age2:
            if (age1 - age2) in range(0, 17):
                status_f1 = 'Брат'
                status_f2 = 'Сестра'
            elif (age1 - age2) in range(18, 36):
                if gpi.f1cf == 'Не хочет иметь детей':
                    status_f1 = "Отчим"
                    status_f2 = "Падчерица"
                else:
                    status_f1 = 'Папа'
                    status_f2 = 'Дочь'

            elif (age1 - age2) in range(37, 72):
                status_f1 = 'Дедушка'
                status_f2 = 'Внучка'

        elif age1 < age2:
            if (age2 - age1) in range(0, 17):
                status_f2 = 'Сестра'
                status_f1 = 'Брат'
            elif (age2 - age1) in range(18, 36):
                if gpi.f2cf == 'Не хочет иметь детей':
                    status_f2 = "Мачеха"
                    status_f1 = "Пасынок"
                else:
                    status_f2 = 'Мама'
                    status_f1 = 'Сын'

            elif (age2 - age1) in range(37, 72):
                status_f2 = 'Бабушка'
                status_f1 = 'Внук'

        elif age1 == age2:
            status_f1 = 'Брат'
            status_f2 = 'Сестра'

    # f1 - woman / f2 - man
    elif man_woman1 == 'Женщина':
        if age1 > age2:
            if (age1 - age2) in range(0, 17):
                status_f1 = 'Сестра'
                status_f2 = 'Брат'
            elif (age1 - age2) in range(18, 36):
                if gpi.f1cf == 'Не хочет иметь детей':
                    status_f1 = "Мачеха"
                    status_f2 = "Пасынок"
                else:
                    status_f1 = 'Мама'
                    status_f2 = 'Сын'

            elif (age1 - age2) in range(37, 72):
                status_f1 = 'Бабушка'
                status_f2 = 'Внук'

        elif age1 < age2:
            if (age2 - age1) in range(0, 17):
                status_f2 = 'Брат'
                status_f1 = 'Сестра'
            elif (age2 - age1) in range(18, 36):
                if gpi.f2cf == 'Не хочет иметь детей':
                    status_f2 = "Отчим"
                    status_f1 = "Падчерица"
                else:
                    status_f2 = 'Папа'
                    status_f1 = 'Дочь'

            elif (age2 - age1) in range(37, 72):
                status_f2 = 'Дедушка'
                status_f1 = 'Внучка'

        elif age1 == age2:
            status_f1 = 'Сестра'
            status_f2 = 'Брат'

