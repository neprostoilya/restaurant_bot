from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery

from config import TOKEN
from markups import web_app_markup

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    """
    Reaction on command /start
    """
    chat_id = message.chat.id

    await bot.send_message(
        chat_id=chat_id,
        text='Кликни',
        reply_markup=web_app_markup()
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)