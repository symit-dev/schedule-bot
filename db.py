import pymongo
import db
from time import time
import os, csv

class Mango:
  def __init__(self):
    self.db_url = "mongodb+srv://test:sumit12345@cluster0.7hauv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    self.client = pymongo.MongoClient(self.db_url)
    self.db = self.client.schedule
    self.collection = self.db.col

  def insert(self, json_data):
    return self.collection.insert_one(json_data)
    
  def get_all_data(self, json_data):
    return self.collection.find(json_data)
  

  def get_single_data(self, json_data):
    self.return_json = self.collection.find_one(json_data)
    return self.return_json

  def delete_single_data(self, json_data):
    self.check = self.collection.delete_one(json_data)
    return self.check.deleted_count

  def delete_all_data(self, json_data):
    return self.collection.delete_many(json_data)


# db = Mango()
# user = {
#   'chat_id': -1001196505905, 
#   'msg_id': 37204,
#   'time':'13:44',
#   'date':'27/06/2021',
#   'chats':['-1001196505905','-1001196505905']
#   }

def write_csv_dt(items):
    print(items)
    today = int(time())
    filename = f"schedule-{today}.csv"
    if not os.path.exists(filename):
      write_row = True
    else:
      write_row  = False
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile: 
    # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        if write_row:
          csvwriter.writerow(["msg_link","time","date","chats"])   
        csvwriter.writerows(items)
    return filename

def get_csv_schedule_file():
  datas = list()
  db = Mango()
  for data in db.get_all_data(None):
    chat_id = data['chat_id']
    if isinstance(chat_id, int):
      chat_id = int(str(chat_id).replace('-100',''))
    # https://t.me/c/1196505905/37204,16:03,27/06/21,/-1001196505905/-1001196505905
    msg_link = f"https://t.me/c/{chat_id}/{data['msg_id']}"
    time_ = data['time']
    date_ = data['date']
    chats = '/'+'/'.join(data['chats'])
    datas.append([msg_link, time_, date_, chats])
  file_ = write_csv_dt(datas)
  return file_

# print(get_csv_schedule_file())
