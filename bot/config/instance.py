from aiogram import Bot
from aiogram.enums import ParseMode
from config.configuration import TOKEN_BOT_1, TOKEN_BOT_2


bot_1 = Bot(token=TOKEN_BOT_1, parse_mode=ParseMode.HTML)

bot_2 = Bot(token=TOKEN_BOT_2, parse_mode=ParseMode.HTML)


