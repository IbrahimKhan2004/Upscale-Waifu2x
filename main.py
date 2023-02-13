from pyrogram import filters
from pyrogram import Client
import logging
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

#initialize bot
app = Client(name="okk", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, in_memory=True)

#handle new members on join
@app.on_message(pyrogram.Filters.group & pyrogram.Filters.new_chat_members)
def kick_new_users(client, message):
  for user in message.new_chat_members:
    msg = client.kick_chat_member(chat_id=message.chat.id, user_id=user.id)
    print(msg)

#start bot
app.run()
