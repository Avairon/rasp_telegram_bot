import datetime
import src.tranzactions as tr
import psycopg2


import sys
sys.path.insert(1, '../')

from api.parcer import parcer

month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
days_list = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']


def par_output(id):
    try:
        getter = parcer()

        messages = tr.read_messages()

        change_group_flag = 0
        today = datetime.datetime.now()
        days_ago = 0
        #today = today.replace(day=6, hour=12, minute=50) # DEBUG
        user_info = tr.read_users(id)

        if user_info == -1:
            ###
            return str(messages[0])
        


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
                            return str((messages[8] % (str(days_ago), str(date_call), str(data[i]['number']), str(data[i]['subject']), str(data[i]['time-start']), str(data[i]['time-end']), str(data[i]['teacher']), str(data[i]['room']))))
                        else:
                            if flag == False:
                                return str((messages[9]) % (str(str(delta)[:5].split(':')[0]), str(str(delta)[:5].split(':')[1]), str(date_call), str    (data[i]['number']), str(data[i]['subject']), str(data[i]['time-start']), str(data[i]['time-end']), str(data[i]['teacher']), str(data[i]['room'])))
                            else:
                                return str((messages[10]) % (str(str(delta)[:5].split(':')[0]), str(str(delta)[:5].split(':')[1]), str(date_call), str    (data[i]['number']), str(data[i]['subject']), str(data[i]['time-start']), str(data[i]['time-end']), str(data[i]['teacher']), str(data[i]['room'])))
                
                days_ago = days_ago + 1
                today += datetime.timedelta(days=1)
                today = today.replace(hour=0, minute=0)
            else: # if today is no para
                days_ago = days_ago + 1
                today += datetime.timedelta(days=1)
                today = today.replace(hour=0, minute=0)
        
        

        return str(messages[1]) # if no para in nearest 5 days
    except Exception as e:
        conn.close()
        tr.log_write('logs/errors.log', ("core.py/para_output: " + str(e)))
        