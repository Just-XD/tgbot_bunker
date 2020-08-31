#!/usr/bin/env python
# -*- coding: utf-8 -*-

import helper as h
from random import randint, choice

overweight = bmi = exp = age = 0

phob_t = hobby_t = iq_t = char_t = bag_t = info_t = act_t \
    = bmi_t = health_t = prof_t = sa_t = rp_t = 'some text'


# пол и возраст
def get_sa():
    global age, sa_t, bmi, overweight

    sex = ['Мужчина', 'Женщина']
    cf = ['Хочет иметь детей', 'Хочет иметь детей', 'Хочет иметь детей',
          'Хочет иметь детей', 'Хочет иметь детей', 'Не хочет иметь детей']

    age = randint(18, 90)
    manORwoman = choice(sex)
    canORnot = choice(cf)
    why = ''

    if manORwoman == 'Женщина':
        if (age > 49 and manORwoman == 'Женщина'):
            canORnot = 'Не может иметь детей'
            why = '(Из-за возраста)'
        elif (age > 49 and manORwoman == 'Женщина') and (bmi != 0 and bmi > 31) or \
                (overweight != 0 and overweight == 'Анорексия'):
            canORnot = 'Не может иметь детей'
            why = '(Из-за возраста и BMI)'
        elif (bmi != 0 and bmi > 31) or (overweight != 0 and overweight == 'Анорексия'):
            canORnot = 'Не может иметь детей'
            why = '(Из-за BMI)'
    else:
        why = ''

    sa_t = f'Пол и возраст: {manORwoman} - {age} | {canORnot} {why}'


# профессия
def get_prof():
    global prof_t

    rnd_prof = randint(0, len(h.prof) - 1)
    prof_t = f'Профессия: {h.prof[rnd_prof]} | Стаж работы: прежний'


# здоровье
def get_health():
    global health_t

    health_lvl = [' | Тяжесть: Ремиссия', ' | Тяжесть: Минимальная', ' | Тяжесть: Лёгкая',
                  ' | Тяжесть: Средняя', '| Тяжесть: Тяжелая', ' | Тяжесть: Максимальная']

    lvl = choice(health_lvl)
    rnd_health = randint(0, len(h.health))
    if h.health[rnd_health] == 'Полностью здоров':
        lvl = ''
    health_t = f'Состояние здоровья: {h.health[rnd_health]}{lvl} (если применимо)'


# телосложение
def get_bmi():
    global bmi_t, bmi

    overweight = ''
    weight = randint(450, 1400) / 10
    height = randint(15, 21) / 10

    bmi = weight / (height ** 2)
    if bmi < 18:
        overweight = 'Анорексия'
        newCanORnot = 'не может рожать'
    elif bmi < 22:
        overweight = 'Худой'
        newCanORnot = 'может рожать (если бесплодие связано с BMI)'
    elif bmi < 24:
        overweight = 'Нормальный вес'
        newCanORnot = 'может рожать (если бесплодие связано с BMI)'
    elif bmi < 27:
        overweight = 'Полноват'
        newCanORnot = 'может рожать (если бесплодие связано с BMI)'
    elif bmi < 30:
        overweight = 'Избыточный вес'
        newCanORnot = 'может рожать (если бесплодие связано с BMI)'
    elif bmi < 31:
        overweight = 'Лёгкое ожирение'
        newCanORnot = 'не может рожать'
    elif bmi < 33:
        overweight = 'Ожирение средней тяжести'
        newCanORnot = 'не может рожать'
    elif bmi >= 33:
        overweight = 'Сильное ожирение'
        newCanORnot = 'не может рожать'
    bmi_t = f'Телосложение: {overweight} (Вес: {weight} кг | Рост: {height} м)\nТвой персонаж теперь {newCanORnot}'


# фобия
def get_phob():
    global phob_t

    phob_lvl = [' | Тяжесть страха: Почти не заметная', ' | Тяжесть страха: Лёгкая',
                ' | Тяжесть страха: Средняя', ' | Тяжесть страха: Тяжелая',
                ' | Тяжесть страха: Максимальная', ' | Тяжесть страха: Смертельная']

    rnd_phob = randint(0, len(h.phob) - 1)
    rnd_phob_lvl = choice(phob_lvl)

    if h.phob[rnd_phob] == 'Нет фобии':
        rnd_phob_lvl = ' '
    phob_t = f'Фобия: {h.phob[rnd_phob]}{rnd_phob_lvl}'


# хобби
def get_hobby():
    global hobby_t
    rnd_hobby = randint(0, len(h.hobby) - 1)
    hobby_t = f'Хобби: {h.hobby[rnd_hobby]}'


# iq
def get_iq():
    global iq_t
    iq = randint(80, 200)
    iq_t = f'Уровень IQ: {iq} | Влияет на получение новых знаний'


# характер
def get_char():
    global char_t
    rnd_char = randint(0, len(h.char) - 1)
    char_t = f'Характер: {h.char[rnd_char]}'


# багаж
def get_baggage():
    global bag_t
    rnd_bag = randint(0, len(h.baggage) - 1)
    bag_t = f'Багаж: {h.baggage[rnd_bag]}'


# доп инфа
def get_info():
    global info_t
    rnd_info = randint(0, len(h.info) - 1)
    info_t = f'Доп. информация: {h.info[rnd_info]}'


# карта действия
def get_act():
    global act_t
    rnd_act = randint(0, len(h.act) - 1)
    act_t = f'Карта действия: {h.act[rnd_act]}'


# rp
def get_rp():
    global rp_t
    rnd_rp = randint(0, len(h.roleplay) - 1)
    rp_t = f'RP: {h.roleplay[rnd_rp]}'
