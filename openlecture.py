""" Данный скрипт в зависимости от текущего времени открывает нужную лекцию
    по расписанию, определенному в скрипте.
    Created by Gleb Nemetskiy 2021
"""
import os
import subprocess
from datetime import datetime as date
from urllib.parse import quote
from datetime import timedelta
from time import sleep

def open_lecture(schedule : dict, lecture_time : str, current_day : str):
    if schedule[current_day][lecture_time][0].find("zoom") != -1:
        print(f"Open {schedule[current_day][lecture_time][1]}...")
        cmd = "%APPDATA%/Zoom/bin/Zoom.exe " + "\"" + schedule[current_day][lecture_time][0] + "\""
        os.system(cmd)
        sleep(5)
        exit()
    else:
        print(f"Open {schedule[current_day][lecture_time][1]}...")
        cmd = "cmd /c %APPDATA%/Adobe/Connect/connect.exe " + "\""\
            + schedule[current_day][lecture_time][0] + "\""
        # process = subprocess.Popen(cmd, shell=True)
        os.system(cmd)
        exit()


if __name__ == "__main__": 
    name = quote("Немецкий Глeб") # Student name
    schedule = { # lectures
        "Monday"  : {
            "07:45" :  ("--url=zoommtg://zoom.us/join?action=join&confno=3020685716&pwd=8kYH9a",
                "Математические модели и методы логистики лекция"),
            "09:35" :  ("https://class.tsu.ru/m-course-31478/?guestName=" + name + "&proto=true",
                "Теория игр и исследование операций практика"),
            "11:25" :  ("https://class.tsu.ru/m-course-8927?guestName=" + name + "&proto=true",
                "Математические модели маркетинга лекция"), 
            "13:45" :  ("https://class.tsu.ru/m-course-31478?guestName=" + name + "&proto=true",
                "Теория игр и исследование операций лекция")      
        },
        "Tuesday" : {
            "13:35" : ("https://class.tsu.ru/m-course-13131?guestName=" + name + "&proto=true",
                "Управление в экономических системах лекция"),                    
            "15:35" : ("https://class.tsu.ru/m-course-13942?guestName=" + name + "&proto=true",
                "Эконометрическое моделирование и стохастические процессы лекция"),
            "17:25" : ("https://class.tsu.ru/m-course-441?guestName=" + name + "&proto=true",
                "Эконометрика лекция")
        },
        "Wednesday" : {
            "09:35" :  ("https://class.tsu.ru/m-course-9455?guestName=" + name + "&proto=true",
                "Теория массового обслуживания практика"),
            "11:25" :  ("https://class.tsu.ru/m-course-5218?guestName=" + name + "&proto=true",
               "Математические модели менеджмента практика"),
            "13:45" :  ("https://class.tsu.ru/m-course-7323?guestName=" + name + "&proto=true",
               "Интеллектуальные информационные системы лекция"),
            "15:35" :  ("https://class.tsu.ru/m-course-441?guestName=" + name + "&proto=true",
                "Эконометрика практика")
        },
        "Thursday" : {
             "16:00" :  ("--url=zoommtg://zoom.us/join?action=join&confno=3020685716&pwd=8kYH9a",
                "ВКР консультация"),
        },
        "Friday" : {
            "07:45" : ("--url=zoommtg://zoom.us/join?action=join&confno=8967702999&pwd=12345",
                "Уравнения в конечных разностях лекция"),
            "09:35" : ("https://class.tsu.ru/m-course-9455?guestName=" + name + "&proto=true",
                "Теория массового обслуживания лекция"),
            "11:25" : ("https://class.tsu.ru/m-course-14049?guestName=" + name + "&proto=true",
                "Экономико-математическое моделирование II"),
            "13:45" : ("https://class.tsu.ru/m-course-8930?guestName=" + name + "&proto=true",
                "Математические модели теории рисков практика"),
        },
        "Saturday" : {
            "07:45" : ("https://class.tsu.ru/m-course-8930?guestName=" + name + "&proto=true",
                "Математические модели теории рисков лекция"),
            "09:35" : ("https://class.tsu.ru/m-course-14049?guestName=" + name + "&proto=true",
                "Экономико-математическое моделирование II"),
            "13:45" : ("https://class.tsu.ru/m-course-5218?guestName=" + name + "&proto=true",
                "Математические модели менеджмента лекция")
        },
        "Sunday" : ""
    }
    current_time = date.today().strftime("%H:%M") # Current time in string format
    current_day = date.today().strftime("%A")     # Current day name in string
    date_format_str = '%H:%M'
    current_timestamp = date.strptime(date.today().strftime("%H:%M"), date_format_str) 
    if not schedule[current_day]:
        print("Today no lectures")
        sleep(5)
        exit()
    if date.strptime(list(schedule[current_day])[-1], date_format_str) + timedelta(minutes=90)  < current_timestamp:
        # Case when lectures end
        next_day = (date.today() + timedelta(days=1)).strftime("%A")
        if not (schedule[next_day]):
            print("Next day no lectures")
            sleep(5)
            exit()
        waiting_time = (date.strptime("23:59", date_format_str) + timedelta(minutes=1) - current_timestamp) + date.strptime(list(schedule[next_day])[0], date_format_str)
        print("Lectures will be on the next day. Time left: {0} hours and {1} minutes".format(waiting_time.strftime("%H%M")[:2], waiting_time.strftime("%H%M")[2:]))
        sleep(5)
        exit()
    if current_timestamp < date.strptime(list(schedule[current_day])[0], date_format_str) - timedelta(minutes=10):
        # Case when lectures not begin
        print(f"It's too early. Lectures will begin after {date.strptime(list(schedule[current_day])[0], date_format_str) - current_timestamp}")
        sleep(5)
        exit()
    else:
        for lecture_time in schedule[current_day]:
            if date.strptime(lecture_time, date_format_str) - timedelta(minutes=10) <= current_timestamp\
                    <= date.strptime(lecture_time, date_format_str) + timedelta(minutes=90):
                open_lecture(schedule, lecture_time, current_day)
## print how mucgh time to next lecture
## time between lectures
## moodle courses
## update schedule