# Initialize list
Lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Display list
print(Lst[1:9])

getMSG = await userge.bot.get_messages(-1001196505905, 37176)
print(getMSG)

await userge.bot.copy_message(message.chat.id, -1001196505905, 37176, reply_markup=getMSG.reply_markup)

await message.copy(message.chat.id)


z = "-100" + "1196505905"
print(int(z))
# ----

dl=await userge.bot.download_media(message.reply_to_message)
print(dl)

print(message)

chat = "234234"
CH = chat if '@' in chat else int(chat)
print(CH)