from pyrogram import filters
from pyrogram import Client, new_chat_members
import logging
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

#initialize bot
app = Client(name="okk", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, in_memory=True)

#Add Start Handler
@app.on_message(filters.command(["start"]))
async def start(client, message):
    await message.reply("Hi! Thanks for adding me.")

#Add New Member Handler
@app.on_message(filters..new_chat_members)
async def new_member(client, message):
    await message.reply("Welcome mate, unfortunately you've been kicked!")
    await app.kick_chat_member(message.chat.id, message.from_user.id)

# Run the bot
app.run()
