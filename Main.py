import logging
import pyrogram

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

app = pyrogram.Client("YOUR_APP_NAME")

# Define a few command handlers. These usually take the two arguments bot and 
# update. Error handlers also receive the raised TelegramError object in error.
@app.on_message(pyrogram.Filters.command("start"))
def start(client, message):
    message.reply_text("Hi!")

# Kick new members when they join the group or channel
@app.on_message(pyrogram.Filters.group)
def kick_new_members(client, message):
    # Get the list of users in the chat
    chat_members = client.get_chat_members_count(message.chat.id)

    # Get the list of new members who joined recently
    new_members = [member for member in chat_members if member not in old_members]

    # Kick out all new members
    for member in new_members:
        # Kick out the member from the chat
        client.kick_chat_member(message.chat.id, member)

        # Log that a user has been kicked out
        logger.info("Kicked out user %s", member)

        # Update old members list with current members list
        old_members = chat_members

# on different commands - answer in Telegram
@app.on_message(pyrogram.Filters.command)
def unknown(client, message):
    message.reply_text("Sorry, I didn't understand that command.")

app.run()
