import json
import os
import re

def log_write(log_name, text):
    file = open(log_name, 'a')
    file.write(text + '\n')
    file.close()

def write_users(chat_id, group, pgroup, dist_skip):
    try:
        with open('data/users.json', 'r') as file: # read the json
            data = json.load(file)

        group = group.strip()

        # print(group) # проверка
        # pattern = r'^d{2}.d{2}.d{2}[п]?d?$'
        # #print(group)
        # # Проверяем соответствие
        # if re.search(pattern, group):
        #     pass
        # else:
        #     log_write('logs/user_changes.log', f"uncorrect transaction occured! user: {chat_id}, group: {group}")
        #     return -1
        
        for i in range(len(data)):
            #print(data[i])
            if data[i]['chat_id'] == chat_id:
                if (data[i]['group'] != group or data[i]['pgroup'] != pgroup or data[i]['dist_skip'] != dist_skip):
                    data[i] = ({"chat_id": chat_id, "group": group, "pgroup": pgroup, "dist_skip": dist_skip})
                    log_write('logs/user_changes.log', f"user: {chat_id} change options on group: {group}, pgroup: {pgroup}, dist_skip: {dist_skip}")
                    break

            if i == len(data) - 1 and data[i]['chat_id'] != chat_id:
                data.append({"chat_id": chat_id, "group": group, "pgroup": pgroup, "dist_skip": dist_skip})
                log_write('logs/user_changes.log', f"user: {chat_id} create profile, group: {group}, pgroup: {pgroup}, dist_skip: {dist_skip}")
                break
                    
        file = open('data/users.json', 'w')
        content = json.dumps(data)
        file.write(content)
        file.close()
    except Exception as e:
        log_write("logs/errors.log", str(e))
    

def json_read(json_name):
    try:
        with open(json_name, 'r') as file: # read the json
            data = json.load(file)
        os.remove(json_name)
        return data
    except Exception as e:
        log_write("logs/errors.log", str(e))

def read_users(chat_id):
    try:
        with open('data/users.json', 'r') as file: # read the json
            data = json.load(file)
        for i in range(len(data)):
            #print(data[i])
            if data[i]['chat_id'] == chat_id:
                return data[i]
        return -1
    except Exception as e:
        log_write("logs/errors.log", str(e))

def read_messages():
    with open("src/messages.txt", "r", encoding="utf-8") as file:
        txt = file.read()

    out = txt.split('////')
    return out