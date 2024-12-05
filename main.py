import telebot
from telebot import types
# from src.test import taims
from api.parcer import parcer
import src.tranzactions as tr
import datetime
# import json


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
            change_group_flag = 0

            today = datetime.datetime.now()
            #today = today.replace(day=6, hour=12, minute=50) # DEBUG
            days_ago = 0

            user_info = tr.read_users(message.chat.id)

            if user_info == -1:
                bot.send_message(message.chat.id, messages[0], reply_markup=menu)
                return

            group = user_info["group"]
            pgroup = user_info["pgroup"]
            dist_skip = user_info["dist_skip"]

            

            for i in range(5): # check the last 5 days
                if getter.get_info(group, today) == 0:
                    data = tr.json_read(f'cache/{group}.json') # read the json

                    date_call = "%s, %s %s" % (days_list[today.weekday()], today.day, month_list[today.month - 1]) # date to format: Суббота, 7 декабря

                    para_time = today # write to para_time date

                    for i in range(len(data)):
                        dist = bool(dist_skip == '1' and data[i]['room'] == "дист")
                        if dist:
                            continue
                        
                        if_consist_pg = data[i]['subject'][len(data[i]['subject']) - 5]
                        if if_consist_pg != pgroup and (if_consist_pg == '1' or if_consist_pg == '2'):
                            continue

                        flag = False
                        para_time = para_time.replace(hour=int(data[i]['time-start'].split(':')[0]), minute=int(data[i]['time-start'].split(':')[1])) # write to para_time starts   time
                        #print(para_time - today)
                        if str(para_time - today)[:2] == '-1' or str(para_time - today).split(':')[1] == '00': # calculate delta
                            delta = today - para_time
                            flag = True
                        else:
                            delta = para_time - today

                        para_time_30 = para_time

                        minute_buff = para_time_30.minute + 30 # calculate +30 minutes from start

                        if minute_buff <= 59: # manual convert into hours
                            para_time_30 = para_time_30.replace(minute=minute_buff)
                        else:
                            para_time_30 = para_time_30.replace(minute=(minute_buff - 60), hour=(para_time_30.hour + 1))

                        if para_time_30 > today: # check if nearest para
                            
                            if days_ago > 0: # check todsy is para
                                bot.send_message(message.chat.id, (messages[8] % (str(days_ago), str(date_call), str(data[i]['number']), str(data[i]['subject']), str(data[i]['time-start']), str(data[i]['time-end']), str(data[i]['teacher']), str(data[i]['room']))), reply_markup=menu)
                            else:
                                if flag == False:
                                    bot.send_message(message.chat.id, (messages[9]) % (str(str(delta)[:5].split(':')[0]), str(str(delta)[:5].split(':')[1]), str(date_call), str    (data[i]['number']), str(data[i]['subject']), str(data[i]['time-start']), str(data[i]['time-end']), str(data[i]['teacher']), str(data[i]    ['room'])), reply_markup=menu)
                                else:
                                    bot.send_message(message.chat.id, (messages[10]) % (str(str(delta)[:5].split(':')[0]), str(str(delta)[:5].split(':')[1]), str(date_call), str    (data[i]['number']), str(data[i]['subject']), str(data[i]['time-start']), str(data[i]['time-end']), str(data[i]['teacher']), str(data[i]    ['room'])), reply_markup=menu)
                            return
                    
                    days_ago = days_ago + 1
                    today += datetime.timedelta(days=1)
                    today = today.replace(hour=0, minute=0)



                else: # if today is no para

                    days_ago = days_ago + 1
                    today += datetime.timedelta(days=1)
                    today = today.replace(hour=0, minute=0)


            bot.send_message(message.chat.id, messages[1], reply_markup=menu) # if no para in nearest 5 days

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
