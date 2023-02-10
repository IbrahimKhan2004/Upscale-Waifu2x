from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import logging 

# Enable logging 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO) 
logger = logging.getLogger(__name__) 
  
# Define a few command handlers. These usually take the two arguments bot and 
# update. Error handlers also receive the raised TelegramError object in error. 
def start(bot, update): 
    update.message.reply_text('Hi!') 

   # Kick new members when they join the group or channel    
def kick_new_members(bot, update): 

    # Get the list of users in the chat    
    chat_members = bot.getChatMembersCount(update.message.chat_id)

    # Get the list of new members who joined recently    
    new_members = [member for member in chat_members if member not in old_members]

    # Kick out all new members    
    for member in new_members: 

        # Kick out the member from the chat                             bot.kickChatMember(update.message.chat_id, member)  

        # Log that a user has been kicked out     logger.info("Kicked out user %s", member)  

        # Update old members list with current members list     old_members = chat_members  

   # on different commands - answer in Telegram def unknown(bot, update):      update.message.reply_text('Sorry, I didn\'t understand that command.')  

def main():     

    # Create the EventHandler and pass it your bot's token      updater = Updater("YOUR BOT TOKEN")      dp = updater.dispatcher      

    # Add command handler to respond to '/start'      dp.addHandler(CommandHandler("start", start))      

    # Add command handler to kick new members when they join      dp
