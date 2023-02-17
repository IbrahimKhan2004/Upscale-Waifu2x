# Telegram Bot to Upscale Images using Waifu2x

A Telegram bot that upscales images using Waifu2x when sent with the `/upscale` command.

## Prerequisites

To run this bot, you need the following:

- A Telegram Bot Token obtained from [@BotFather](https://t.me/BotFather).
- Telegram API authentication information, which can be obtained from https://my.telegram.org.

## Required Fields

Before running the code, you need to fill in the following fields:

- `TELEGRAM_API_ID`: The API ID for your Telegram app. (Type: `int`)
- `TELEGRAM_API_HASH`: The API hash for your Telegram app. (Type: `str`)
- `TELEGRAM_BOT_TOKEN`: The Telegram Bot Token obtained from [@BotFather](https://t.me/BotFather). (Type: `str`)

## Running the Bot

Once you have filled in the required fields, simply run the code to activate the bot. To use the bot, send an image to the bot and reply to the image with the `/upscale` command. The bot will then upscale the image using Waifu2x and send it back to you.

Note: Please make sure to read and follow the [Telegram Bot API terms of service](https://core.telegram.org/bots/faq#my-bot-keeps-crashing-what-should-i-do) to avoid any issues.
