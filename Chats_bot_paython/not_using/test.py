def taims():
    from datetime import datetime
    #p1 = первая пара p2 = вторая p1_1 = начало 1 пары p1_2 = конец пары
    now = datetime.now() # сегоднешняя пара
    #значения конечные = 0 для работы логики
    x_start_hours = 0
    x_start_minutes = 0
    x_ends_hours = 0
    x_ends_minutes = 0
    #рассписание пар

    p1_1 = datetime(now.year, now.month, now.day, 8, 30)
    p1_2 = datetime(now.year, now.month, now.day, 10, 5)

    p2_1 = datetime(now.year, now.month, now.day, 10, 15)
    p2_2 = datetime(now.year, now.month, now.day, 11, 50)

    p3_1 = datetime(now.year, now.month, now.day, 12, 20)
    p3_2 = datetime(now.year, now.month, now.day, 13, 55)

    p4_1 = datetime(now.year, now.month, now.day, 14, 25)
    p4_2 = datetime(now.year, now.month, now.day, 16, 00)

    p5_1 = datetime(now.year, now.month, now.day, 16, 10)
    p5_2 = datetime(now.year, now.month, now.day, 17, 45)

    p6_1 = datetime(now.year, now.month, now.day, 17, 55)
    p6_2 = datetime(now.year, now.month, now.day, 19, 30)

    now = datetime.now()
    # вычесления для времения начало пары 1 пара
    if now < p1_1:
        time_difference = p1_1 - now
        x_start_hours = time_difference.seconds // 3600
        x_start_minutes = (time_difference.seconds % 3600) // 60
    # вычесления для конца пары по расписанию
    if now > p1_1:
        if now < p1_2:
            time_difference = now - p1_2
            time_difference = p1_2 - now
            x_ends_hours = time_difference.seconds // 3600
            x_ends_minutes = (time_difference.seconds % 3600) // 60
    # проверка чтоб не перезаписал данные
    if x_start_hours == 0:
        if x_start_minutes == 0:  
            # вычесления для времения начало пары 2 пара
            if now < p2_1:
                time_difference = p2_1 - now
                x_start_hours = time_difference.seconds // 3600
                x_start_minutes = (time_difference.seconds % 3600) // 60
    #проверка тоб не перезаписал данные
    if x_ends_hours == 0:
        if x_ends_minutes == 0:
            # вычесления для конца пары по расписанию
            if now > p2_1:
                if now < p2_2:
                    time_difference = now - p2_2
                    time_difference = p2_2 - now
                    x_ends_hours = time_difference.seconds // 3600
                    x_ends_minutes = (time_difference.seconds % 3600) // 60
    # проверка чтоб не перезаписал данные
    if x_start_hours == 0:
        if x_start_minutes == 0:  
            # вычесления для времения начало пары 3 пара
            if now < p3_1:
                time_difference = p3_1 - now
                x_start_hours = time_difference.seconds // 3600
                x_start_minutes = (time_difference.seconds % 3600) // 60
    #проверка тоб не перезаписал данные
    if x_ends_hours == 0:
        if x_ends_minutes == 0:
            # вычесления для конца пары по расписанию
            if now > p3_1:
                if now < p3_2:
                    time_difference = now - p3_2
                    time_difference = p3_2 - now
                    x_ends_hours = time_difference.seconds // 3600
                    x_ends_minutes = (time_difference.seconds % 3600) // 60
    # проверка чтоб не перезаписал данные
    if x_start_hours == 0:
        if x_start_minutes == 0:  
            # вычесления для времения начало пары 4 пара
            if now < p4_1:
                time_difference = p4_1 - now
                x_start_hours = time_difference.seconds // 3600
                x_start_minutes = (time_difference.seconds % 3600) // 60
    #проверка тоб не перезаписал данные
    if x_ends_hours == 0:
        if x_ends_minutes == 0:
            # вычесления для конца пары по расписанию
            if now > p4_1:
                if now < p4_2:
                    time_difference = now - p4_2
                    time_difference = p4_2 - now
                    x_ends_hours = time_difference.seconds // 3600
                    x_ends_minutes = (time_difference.seconds % 3600) // 60
    # проверка чтоб не перезаписал данные
    if x_start_hours == 0:
        if x_start_minutes == 0:  
            # вычесления для времения начало пары 5 пара
            if now < p5_1:
                time_difference = p5_1 - now
                x_start_hours = time_difference.seconds // 3600
                x_start_minutes = (time_difference.seconds % 3600) // 60
    #проверка тоб не перезаписал данные
    if x_ends_hours == 0:
        if x_ends_minutes == 0:
            # вычесления для конца пары по расписанию
            if now > p5_1:
                if now < p5_2:
                    time_difference = now - p5_2
                    time_difference = p5_2 - now
                    x_ends_hours = time_difference.seconds // 3600
                    x_ends_minutes = (time_difference.seconds % 3600) // 60
    # проверка чтоб не перезаписал данные
    if x_start_hours == 0:
        if x_start_minutes == 0:  
            # вычесления для времения начало пары 6 пара
            if now < p6_1:
                time_difference = p6_1 - now
                x_start_hours = time_difference.seconds // 3600
                x_start_minutes = (time_difference.seconds % 3600) // 60
    #проверка тоб не перезаписал данные
    if x_ends_hours == 0:
        if x_ends_minutes == 0:
            # вычесления для конца пары по расписанию
            if now > p6_1:
                if now < p6_2:
                    time_difference = now - p6_2
                    time_difference = p6_2 - now
                    x_ends_hours = time_difference.seconds // 3600
                    x_ends_minutes = (time_difference.seconds % 3600) // 60
    return x_start_hours,x_start_minutes,x_ends_hours,x_ends_minutes
