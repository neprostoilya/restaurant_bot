from aiogram import Bot
from aiogram.enums import ParseMode
from config.configuration import TOKEN


bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
