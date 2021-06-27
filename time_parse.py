import os, time
import datetime
from db import Mango
from csv_read  import read_csv
import asyncio
os.environ['TZ'] = os.environ.get('time_zone','Asia/Kolkata')
time.tzset()
"""
datetime is declared and assigned datetime.datetime(2020, 2, 11, 10, 20).
Here 2020 is the year, 2 is the month, 11 is the day, 10 is the hour and 20 is the minute
"""
# datetime = datetime.datetime(2021, 6, 23, 20, 44)
# unix = time.mktime(datetime.timetuple())
# print(unix)

def addMsgToDB(msg):
  sc = msg.strip().split(' ')
  msg = sc[0].split('/')
  chat_id = msg[-2] 
  if not '@' in chat_id:
    chat_id = '-100' + chat_id
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

  chats = sc[3].split('/')[1:]
  # print(chats)
  json_ = {
    "chat_id":chat_id,
    "msg_id":msg_id,
    "time":sc[1],
    "date":sc[2],
    "chats":chats
  }
  db = Mango()
  db.insert(json_)
  return json_

# dl = read_csv('schedule.csv')
# for msg in dl:
#   addMsgToDB(msg)


db = Mango()
# # # user = {'name': 'sHalil', 'lang': 'Python'}
# # print(db.insert(json_))  get_single_data get_all_data

# check  = {"date":'29/06/2021'}
# getData = db.get_all_data(check)
# # print(list(getData))

# # if len(list(getData)) == 0:
# #   print('empty')

# for data in getData:
#   print(data['date'])







