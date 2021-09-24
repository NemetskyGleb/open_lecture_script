from datetime import datetime as date, timedelta
from datetime import timezone
from dateutil.relativedelta import * 
from pytz import timezone as pytztz

def tz_difference():
    """ Returs rdelta is difference between current timezone and Tomsk"""
    date_one = date.strptime(date.now(pytztz('Asia/Krasnoyarsk')).strftime('%d/%m/%Y %H:%M'),'%d/%m/%Y %H:%M')
    date_two = date.strptime(date.now(date.now(timezone.utc).astimezone().tzinfo).strftime('%d/%m/%Y %H:%M'), '%d/%m/%Y %H:%M')
    return relativedelta(date_one, date_two)