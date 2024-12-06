import telebot
from telebot import types

from api.parcer import parcer

import src.core as core
import src.tranzactions as tr

import datetime



month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
days_list = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

bot = telebot.TeleBot('8130108661:AAES_8zx0x-fWAucFfUQ7GHTmFqV_WES5k4')

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(types.KeyboardButton("Пара"), types.KeyboardButton("Настройка")) # add 2 buttons

messages = tr.read_messages()

getter = parcer()
#start bot codding commands /start

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "привет!", reply_markup = menu)
    
#stop bot codding commands /stop (verigud is not deleted)

@bot.message_handler(commands=['stop'])
def message(message):
    bot.send_message(message.chat.id, "крашем бота...")
    bot.stop_polling()

@bot.message_handler(content_types=['text'])
def text_messages(message):
    
    global group, pgroup, dist_skip
    global change_group_flag 

    try:
        if message.text[:4].lower() == 'пара': # check for command para
            
            bot.send_message(message.chat.id, core.par_output(message.chat.id), reply_markup=menu)
        elif message.text[:9].lower() == 'настройка': # options command
            bot.send_message(message.chat.id, messages[2], reply_markup=menu)

            change_group_flag = 1
            
            user_info = tr.read_users(message.chat.id)

            group = user_info["group"]
            pgroup = user_info["pgroup"]
            dist_skip = user_info["dist_skip"]


        elif change_group_flag == 1: # change group command
            group = message.text
            
            bot.send_message(message.chat.id, messages[3], reply_markup=menu)
            change_group_flag = 2

        elif change_group_flag == 2:
            pgroup = message.text
            bot.send_message(message.chat.id, messages[4], reply_markup=menu)
            change_group_flag = 3
        
        elif change_group_flag == 3:
            dist_skip = message.text

            if tr.write_users(message.chat.id, group, pgroup, dist_skip) == -1: # try to write and check if all good
                bot.send_message(message.chat.id, messages[5], reply_markup=menu)
                change_group_flag = 0
                return

            change_group_flag = 0
            bot.send_message(message.chat.id, messages[6], reply_markup=menu)

        else: # if uncorrect command
            bot.send_message(message.chat.id, messages[7], reply_markup=menu)
    except Exception as e:
        tr.log_write('logs/errors.log', ("main.py: " + str(e)))

bot.infinity_polling()
