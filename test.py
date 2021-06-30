from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client, filters
from db import Mango
from csv_read import read_csv
from time_parse import addMsgToDB
import time, os
import asyncio
os.environ['TZ'] = os.environ.get('time_zone','Asia/Kolkata')
time.tzset()
botToken = os.environ.get('bot_token','1778181152:AAE4ZhYQtCE2KsW26Z6-LXUPb6wHZQz0rJY')

app = Client("my_account", api_hash="d5febb517d4bfdc89115e5fb4def57db",
api_id=1737146,
bot_token=botToken
)
LOG_CHAT = int(os.environ.get('log_chat','-1001196505905'))
CHECK = dict()

async def job():
    DY = time.strftime('%d/%m/%y')
    HM = time.strftime('%H:%M')
    DB = Mango()
    data = DB.get_all_data(
      {
        "date":DY,
        "time":HM
      }
    )
    print(DY, HM)
  
    for msg in data:
      print(msg)
      chat_id = msg['chat_id']
      msg_id = msg['msg_id']
      chats = msg['chats']
      try:
        getMSG = await app.get_messages(chat_id, msg_id)
      except Exception as err:
        await app.send_message(LOG_CHAT,f"Unable to Get Message from chat {chat_id}, msg_id {msg_id} - Error {str(err)}") 
      for chat in chats:
        try:
          await asyncio.sleep(2)
          CH = chat if '@' in chat else int(chat)
          await app.copy_message(CH, chat_id, msg_id, reply_markup=getMSG.reply_markup)
        except Exception as err:
          await app.send_message(LOG_CHAT,f"Falied to Forward Message in {CH} - Er - {str(err)}")
      DB.delete_all_data(
        {
          'chat_id':chat_id,
          'msg_id':msg_id,
          'date':DY,
          'time':HM

        }
      )
        



@app.on_message(filters.command(["add"]))
async def add(client, message):
    if message.message_id in CHECK:
        await message.reply("Already Added This CSV File in DB)
        return

    try:
      dl=await client.download_media(message.reply_to_message)
    except Exception as err:
      await message.reply("Please Reply to CSV file ",str(err))
      return

    try:
      data = read_csv(dl)
      await message.reply('Adding to db')
      for msg in data:
        addMsgToDB(msg)
      await message.reply("Added To DB")
      CHECK[message.message_id] = "True"
      return
    except Exception as errr:
      await message.reply("Something is wrong with CSV data Format \nCheck Again ",str(errr))
      return
    


@app.on_message(filters.command(["sc"]))
async def sc(client, message):
  getText = message.text.replace("/sc","").strip()
  addMsgToDB(getText)
  await message.reply("Done added")
  return

      


@app.on_message(filters.command(["start", "help"]))
async def my_handler(client, message):
    print(message)
    await message.reply("<b>Powered By Telegram Marketing Services.</b>\n<a href='http://wa.me/919472355218?text=Hi,%20I%20got%20your%20contact%20from%20telegram%20bot'>Telegram Marketing Services</a>")


scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=25)

scheduler.start()
app.run()
