import os, time
import datetime

print("\n\n\n\n")
os.environ['TZ'] = 'Asia/Kolkata'
time.tzset()
"""
datetime is declared and assigned datetime.datetime(2020, 2, 11, 10, 20).
Here 2020 is the year, 2 is the month, 11 is the day, 10 is the hour and 20 is the minute
"""
# datetime = datetime.datetime(2021, 6, 23, 20, 44)
# unix = time.mktime(datetime.timetuple())
# print(unix)

sc = "https://t.me/c/@1397784007/689373 13:22 23/6/2021 1224234343,@hello,098455".split(' ')  
msg = sc[0].split('/')
chat_id = msg[-2] 
if not '@' in chat_id:
  chat_id = int(chat_id)
msg_id = int(msg[-1])

time_  = sc[1].split(':')
hours = int(time_[0])
mins =  (time_[1])
# print(time_, hours, mins)

date_  =  sc[2].split('/')
_date = int(date_[0])
month =  int(date_[1])
year = int(date_[2])
# print(date_, _date, month, year)

chats = sc[3]

HM = time.strftime('%H:%M')
DY = time.strftime('%d/%m/%y')

print(HM,DY)