#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint, choice
import helper as h
import familyStatus as f

player = f1cf = f2cf = f1 = f2 = 0
name = canORnot = family = ''


def mainFunction():
    global man_woman1, man_woman2, age1, age2, fam1, fam2, f1, f2, family, about_player, player, canORnot, \
        f1cf, f2cf, writeF1, writeF2, name

    h.openF()
    counter = 1

    # family
    family = 'У тебя нет родственников за столом'

    while f1 == f2:
        f1 = randint(1, int(player))
        f2 = randint(1, int(player))

    # MAKE FILES FOR ALL PLAYERS

    while counter <= player:

        # BMI
        overweight = ''
        weight = randint(450, 1400) / 10
        height = randint(15, 21) / 10

        bmi = weight / (height ** 2)
        if bmi < 18:
            overweight = 'Анорексия'
        elif bmi < 22:
            overweight = 'Худой'
        elif bmi < 24:
            overweight = 'Нормальный вес'
        elif bmi < 27:
            overweight = 'Полноват'
        elif bmi < 30:
            overweight = 'Избыточный вес'
        elif bmi < 31:
            overweight = 'Лёгкое ожирение'
        elif bmi < 33:
            overweight = 'Ожирение средней тяжести'
        elif bmi >= 33:
            overweight = 'Сильное ожирение'

        # player parameters randomisation
        rnd_rp = randint(0, (len(h.roleplay) - 1))
        rnd_prof = randint(0, (len(h.prof) - 1))
        rnd_phob = randint(0, (len(h.phob) - 1))
        rnd_char = randint(0, (len(h.char) - 1))
        rnd_hobby = randint(0, (len(h.hobby) - 1))
        rnd_health = randint(0, (len(h.health) - 1))
        rnd_baggage = randint(0, (len(h.baggage) - 1))
        rnd_info = randint(0, (len(h.info) - 1))
        rnd_phob_lvl = randint(0, (len(h.phob_lvl) - 1))
        rnd_act = rnd_act2 = None
        while rnd_act == rnd_act2:
            rnd_act = randint(0, (len(h.act) - 1))
            rnd_act2 = randint(0, (len(h.act) - 1))

        # phobia lvl
        lvl = choice(h.health_lvl)
        if h.health[rnd_health] == 'Полностью здоров':
            lvl = ''

        # sex / cf
        manORwoman = choice(h.sex)
        canORnot = choice(h.cf)
        why = ''

        if manORwoman == 'Мужчина':
            rnd_name = randint(0, (len(h.mnames) - 1))
            name = h.mnames[rnd_name]
        elif manORwoman == 'Женщина':
            rnd_name = randint(0, (len(h.wnames) - 1))
            name = h.wnames[rnd_name]

        # work exp / age
        age = randint(18, 90)
        exp = 0

        if age <= 25:
            exp = randint(0, 3)
        elif age > 25:
            exp = randint(4, 8)
        elif age > 50:
            exp = randint(9, 20)

        y = '(в годах)'
        if exp == 0:
            exp = 'Нет'
            y = ''

        # make family
        if counter != 0:
            if counter == f1:
                f1cf = canORnot
                f.man_woman1 = manORwoman
                f.age1 = age
                family = f'Игрок под номером {f2} твой родственник'
            elif counter == f2:
                f2cf = canORnot
                f.man_woman2 = manORwoman
                f.age2 = age
                family = f'Игрок под номером {f1} твой родственник'

        # women 49+ / man or woman (31 < bmi < 18)
        if manORwoman == 'Женщина':
            # проверка на чайлд фри
            if canORnot != 'Не хочет иметь детей':
                if (age > 49 and manORwoman == 'Женщина'):
                    canORnot = 'Не может рожать'
                    why = '(Из-за возраста)'
                elif (age > 49 and manORwoman == 'Женщина') and (bmi != 0 and bmi > 31) or \
                        (overweight != 0 and overweight == 'Анорексия'):
                    canORnot = 'Не может рожать'
                    why = '(Из-за возраста и BMI)'
                elif manORwoman == 'Женщина' and (
                        (bmi != 0 and bmi > 31) or (overweight != 0 and overweight == 'Анорексия')):
                    canORnot = 'Не может рожать'
                    why = '(Из-за BMI)'
                elif manORwoman == 'Мужчина' and (
                        (bmi != 0 and bmi > 31) or (overweight != 0 and overweight == 'Анорексия')):
                    canORnot = 'Не может иметь детей'
                    why = '(Из-за BMI)'
        else:
            why = ''

        # iq level
        iq = randint(80, 200)

        # write files
        with open('prm/' + str(counter) + '.txt', 'w', encoding='utf-8') as file:
            file.write(
                f"""➢ РП роль (не обязательно): {h.roleplay[rnd_rp]}

➢ Основные характеристики:
1. Биометрия: 
        ↳ Имя: {name}
        ↳ Пол и возраст: {manORwoman} - {age}
        ↳ Деторождение: {canORnot} {why}
2. Профессия: {h.prof[rnd_prof]} | Стаж работы: {exp} {y}
3. Состояние здоровья: {h.health[rnd_health]}{lvl} (если применимо)
4. Телосложение: {overweight} (Вес: {weight} кг | Рост: {height} м)
5. Фобия: {h.phob[rnd_phob]} | Тяжесть страха: {h.phob_lvl[rnd_phob_lvl]}
6. Уровень IQ: {iq} | Влияет на получение новых знаний
7. Хобби: {h.hobby[rnd_hobby]}
8. Характер: {h.char[rnd_char]}
9. Багаж: {h.baggage[rnd_baggage]}
10. Доп. информация: {h.info[rnd_info]}

➢ Карты действия:
1. {h.act[rnd_act]}
2. {h.act[rnd_act2]}

➢ Семья: {family}""")

        def popRnd():
            h.roleplay.pop(rnd_rp)
            h.prof.pop(rnd_prof)
            h.phob.pop(rnd_phob)
            h.char.pop(rnd_char)
            h.hobby.pop(rnd_hobby)
            h.health.pop(rnd_health)
            h.baggage.pop(rnd_baggage)
            h.info.pop(rnd_info)

            if rnd_act > rnd_act2:
                h.act.pop(rnd_act)
                h.act.pop(rnd_act2)
            elif rnd_act2 > rnd_act:
                h.act.pop(rnd_act2)
                h.act.pop(rnd_act)

        popRnd()

        family = 'У тебя нет родственников за столом'
        counter += 1

    writeFS()
    h.closeF()


# write family status

def writeFS():
    global f1, f2

    writeF1 = f1
    writeF2 = f2
    f1 = f2 = 0

    # find man and woman
    if f.man_woman1 == 'Мужчина' and f.man_woman2 == 'Мужчина':
        f.onlyMan()
    elif f.man_woman1 == 'Женщина' and f.man_woman2 == 'Женщина':
        f.onlyWoman()
    elif (f.man_woman1 == 'Мужчина' and f.man_woman2 == 'Женщина') or \
            (f.man_woman1 == 'Женщина' and f.man_woman2 == 'Мужчина'):
        f.manWoman()

        # write family status
    with open('prm/' + str(writeF1) + '.txt', 'a', encoding='utf-8') as file:
        file.write(f' | {f.status_f2}')

    with open('prm/' + str(writeF2) + '.txt', 'a', encoding='utf-8') as file:
        file.write(f' | {f.status_f1}')
