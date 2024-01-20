import asyncio
import logging
import sys
from aiogram import F
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from config import TOKEN
from markups import choose_language_markup, open_web_markup


dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Reaction on command '/start'
    """
    await message.answer(f"Здравствуйте, {hbold(message.from_user.full_name)}!")
    await message.answer(f"Выберите язык бота:", reply_markup=choose_language_markup())

@dp.message(Command('about'))
async def command_about_handler(message: Message) -> None:
    """
    Reaction on command '/about'
    """
    await message.answer(f"Этот бот создан для кафешки...")

@dp.message(CommandStart('help'))
async def command_start_handler(message: Message) -> None:
    """
    Reaction on command '/help'
    """
    await message.answer(f"Остались вопросы? звоните или пишите к ...")

@dp.message(lambda message: 'Русский' or "O'zbek tili" in message.text)
async def command_start_handler(message: Message) -> None:
    """
    Reaction on button choose language
    """
    await message.delete()
    await message.answer(
        'Нажмите на кнопку!',
        reply_markup=open_web_markup()
    )

@dp.message()
async def echo_handler(message: types.Message) -> None:
    ...

async def main() -> None:
    """
    Main 
    """
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    """
    Start bot
    """
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
