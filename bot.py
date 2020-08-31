#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from telebot import types
from random import randint
from time import sleep
from os import remove

import getNewPrm as np
import getPlayerInfo as gpi
import helper as h
import bunker as b

TOKEN = '1321552674:AAGE1WPNYZswJDifGdtJjakG2dPp9UJh2tE'
bot = telebot.TeleBot(TOKEN)


# ОТВЕТ БОТА НА КОМАНДУ
@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.send_message(message.chat.id, """Чтобы начать игру нажми 'Начать игру'""", reply_markup=FIRST_KEYBOARD())
    except Exception:
        sleep(1)
        bot.send_message(message.chat.id, 'Повторите попытку')


# ОТВЕТ БОТА НА НАЖАТИЯ КЛАВИАТУРЫ
@bot.message_handler(content_types='[text]')
def bot_answer(message):
    global disaster
    try:
        chat_id = message.chat.id

        """ ОТВЕТ БОТА НА СОБЫТИЯ - FIRST_KEYBOARD """

        if message.text == 'Начать игру':
            bot.send_message(chat_id, 'Выберите количество играков', reply_markup=get_player())

        if message.text == 'Новые характеристики':
            bot.send_message(chat_id, 'Нажмите на нужную характеристику', reply_markup=newPRM_KEYBOARD())

        if message.text == 'Как играть?':
            text = ' '.join(h.rules)
            bot.send_message(chat_id, text)

        """ ОТВЕТ БОТА НА СОБЫТИЯ - newPRM_KEYBOARD """

        # sex & age
        if message.text == button_title[0]:
            np.get_sa()
            text = np.sa_t
            bot.send_message(chat_id, text, reply_markup=FIRST_KEYBOARD())

        # prof
        if message.text == button_title[1]:
            np.get_prof()
            text = np.prof_t
            bot.send_message(chat_id, text, reply_markup=FIRST_KEYBOARD())

        # health
        if message.text == button_title[2]:
            np.get_health()
            text = np.health_t
            bot.send_message(chat_id, text, reply_markup=FIRST_KEYBOARD())

        # bmi
        if message.text == button_title[3]:
            np.get_bmi()
            text = np.bmi_t
            bot.send_message(chat_id, text, reply_markup=FIRST_KEYBOARD())

        # phob
        if message.text == button_title[4]:
            np.get_phob()
            text = np.phob_t
            bot.send_message(chat_id, text, reply_markup=FIRST_KEYBOARD())

        # hobby
        if message.text == button_title[5]:
            np.get_hobby()
            text = np.hobby_t
            bot.send_message(chat_id, text, reply_markup=FIRST_KEYBOARD())

        # iq
        if message.text == button_title[6]:
            np.get_iq()
            text = np.iq_t
            bot.send_message(chat_id, text, reply_markup=FIRST_KEYBOARD())

        # char
        if message.text == button_title[7]:
            np.get_char()
            text = np.char_t
            bot.send_message(chat_id, text, reply_markup=FIRST_KEYBOARD())

        # baggage
        if message.text == button_title[8]:
            np.get_baggage()
            text = np.bag_t
            bot.send_message(chat_id, text, reply_markup=FIRST_KEYBOARD())

        # info
        if message.text == button_title[9]:
            np.get_info()
            text = np.info_t
            bot.send_message(chat_id, text, reply_markup=FIRST_KEYBOARD())

        # act
        if message.text == button_title[10]:
            np.get_act()
            text = np.act_t
            bot.send_message(chat_id, text, reply_markup=FIRST_KEYBOARD())

        # disaster
        if message.text == button_title[11]:
            disaster = randint(0, (len(h.disasters) - 1))
            bot.send_message(chat_id, h.disasters[disaster], reply_markup=FIRST_KEYBOARD())

        # rp
        if message.text == button_title[12]:
            np.get_rp()
            text = np.rp_t
            bot.send_message(chat_id, text, reply_markup=FIRST_KEYBOARD())

    except Exception:
        sleep(1)
        bot.send_message(message.chat.id, 'Начните игру и повторите попытку', reply_markup=FIRST_KEYBOARD())


""" СОЗДАНИЕ КЛАВИАТУР """


def FIRST_KEYBOARD():
    try:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
        btnStart = types.KeyboardButton('Начать игру')
        btnRules = types.KeyboardButton('Как играть?')
        btnNewParam = types.KeyboardButton('Новые характеристики')

        markup.row(btnStart, btnRules)
        markup.row(btnNewParam)

        return markup
    except Exception:
        sleep(1)


button_title = ['Пол и возраст', 'Профессия', 'Здоровье', 'Телосложение', 'Фобия', 'Хобби', 'IQ', 'Характер', 'Багаж',
                'Доп. инфа', 'Карта действия', 'Новая катастрофа', 'RP']
btn = ['btn0', 'btn1', 'btn2', 'btn3', 'btn4', 'btn5', 'btn6', 'btn7', 'btn8', 'btn9', 'btn10', 'btn11', 'btn12']


def newPRM_KEYBOARD():
    try:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
        i = 0

        while i < len(btn):
            btn[i] = button_title[i]
            i += 1

        markup.row(btn[0], btn[1], btn[2], btn[3])
        markup.row(btn[4], btn[5], btn[6], btn[7], btn[8], btn[12])
        markup.row(btn[9], btn[10], btn[11])

        return markup
    except Exception:
        sleep(1)


def get_player():
    try:
        markup = types.InlineKeyboardMarkup()

        local_buttons = ['btn6', 'btn7', 'btn8', 'btn9', 'btn10', 'btn11', 'btn12']
        local_values = ['6', '7', '8', '9', '10', '11', '12']
        i = 0

        while i < len(local_values):
            btn = types.InlineKeyboardButton(local_values[i], callback_data=local_values[i])
            local_buttons[i] = btn
            i += 1

        markup.row(local_buttons[0], local_buttons[1], local_buttons[2], local_buttons[3])
        markup.row(local_buttons[4], local_buttons[5], local_buttons[6])

        return markup
    except Exception:
        sleep(1)


""" КАТАСТРОФА / БУНКЕР / ПАРАМЕТРЫ ИГРАКОВ """


# SEND INFO ABOUT DISASTER/BUNKER/PLAYER | msg
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        for i in range(6, 13):
            if call.data == str(i):
                gpi.player = int(i)

        send_doc(message=call.message)
        b.mainFunction()
        text = f'{b.disaster}\n\n{b.about_bunker}'
        bot.send_message(chat_id=call.message.chat.id, text=text)


# SEND PLAYER FILES | func
@bot.message_handler(content_types='[text]')
def send_doc(message):

    # remove old txt files
    try:
        remove('prm/info.txt')
        for file in range(1, 13):
            remove('prm/' + str(file) + '.txt')
    except Exception:
        pass

    # send new txt files
    n = 1
    gpi.mainFunction()
    while n <= gpi.player:
        file = open('prm/' + str(n) + '.txt', "rb")
        bot.send_document(message.chat.id, file)
        sleep(0.2)

        if n == gpi.player:
            break
        else:
            n += 1


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
