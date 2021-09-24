""" Данный скрипт в зависимости от текущего времени открывает нужную лекцию
    по расписанию, определенному в скрипте.
    Created by Gleb Nemetskiy 2021
"""
from os import environ, mkdir, path, system
from datetime import datetime as date
from urllib.parse import quote
from datetime import timedelta
from time import sleep
from json import load
from requests import get
from tzdifference import tz_difference
from threading import Thread as th
def open_lecture(schedule : dict, lecture_time : str, current_day : str):
    if schedule[current_day][lecture_time][0].find("zoom") != -1:
        print(f"Open {schedule[current_day][lecture_time][1]}...")
        cmd = "%APPDATA%/Zoom/bin/Zoom.exe " + "\"" + schedule[current_day][lecture_time][0] + "\""
        system(cmd)
        sleep(5)
        exit()
    else:
        print(f"Open {schedule[current_day][lecture_time][1]}...")
        cmd = "cmd /c %APPDATA%/Adobe/Connect/connect.exe " + "\""\
            + schedule[current_day][lecture_time][0] + "\""
        # process = subprocess.Popen(cmd, shell=True)
        system(cmd)
        exit()


if __name__ == "__main__": 
    schedule_url = 'https://drive.google.com/uc?export=download&id=1wmPa2wt1jI7aYuGdapLuZ3MvrAYZVIlp'
    # loading schedule from link and import or create user config
    if not path.isdir(environ['appdata'] + '/openlecture'):
        mkdir(environ['appdata'] + '/openlecture')
    try:
        r = get(schedule_url, allow_redirects=True)
        if (r.status_code == 404):
            exit()
        f = open(environ['appdata'] + "/openlecture/schedule.json", 'wb+').write(r.content)
    except:
        print("Connection error or not valid link.")
    if not path.isfile(environ['appdata'] + '/openlecture/user_config.json'):
        name = str(input("Enter your name for meeting: "))
        cfg_content = "{\n\t\"username\" : \"" + name + "\"\n}"
        f = open(environ['appdata'] + '/openlecture/user_config.json', 'wb+').write(str.encode(cfg_content))
    f_cfg = open(environ['appdata'] + "/openlecture/user_config.json", "rb")
    name = quote(load(f_cfg)["username"])
    f = open(environ['appdata'] + "/openlecture/schedule.json", "rb")
    schedule = load(f)
    # replacing name in schedule
    for day in schedule.keys():
        for lecture_time in schedule[day]:
            schedule[day][lecture_time][0] = schedule[day][lecture_time][0].replace("username", name)
    
    current_time = date.today().strftime("%H:%M") # Current time in string format
    current_day = date.today().strftime("%A")     # Current day name in string
    date_format_str = '%H:%M'
    current_timestamp = date.strptime(date.today().strftime("%H:%M"), date_format_str) + tz_difference()
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