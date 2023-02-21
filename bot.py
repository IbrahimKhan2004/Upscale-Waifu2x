import os 
from telethon import TelegramClient, events 
from io import BytesIO 
from PIL import Image 
import requests 
from ratelimit import limits, sleep_and_retry 

# Replace the values below with your own Telegram API credentials and bot token 
api_id = os.environ['TELEGRAM_API_ID'] 
api_hash = os.environ['TELEGRAM_API_HASH'] 
bot_token = os.environ['TELEGRAM_BOT_TOKEN'] 

# Create a Telethon client instance 
bot = TelegramClient('image_upscale_bot', api_id, api_hash).start(bot_token=bot_token) 

# Define a rate limit of 1 request per second 
@sleep_and_retry 
@limits(calls=1, period=1) 
def upscale_image_waifu2x(image_url): 
 # Upscale the image using Waifu2x 
 url = 'https://api.waifu2x.booru.pics/convert' 
 data = { 
  'scale': 2, 
  'noise': 0, 
  'url': image_url, 
 } 
 response = requests.post(url, data=data) 
 if response.ok: 
  image_data = BytesIO(response.content) 
  image = Image.open(image_data) 
  return image 

# Define a message handler that will upscale the image sent by the user and send it back 
@bot.on(events.NewMessage(pattern='/upscale')) 
async def upscale_image(event): 
 # Download the image sent by the user 
 image_message = await event.get_reply_message() 
 if image_message and hasattr(image_message, 'photo'): 
  # also checks if user has actually sent a photo 
  image_media = image_message.photo 
  image_url = image_media.sizes[-1].location # selects best quality image (last in array) 
  # Upscale the image using Waifu2x 
  image = upscale_image_waifu2x(image_url) 
  # Send the upscaled image back to the user 
  await bot.send_file(event.chat_id, image) 

# Start the bot 
bot.run_until_disconnected()
