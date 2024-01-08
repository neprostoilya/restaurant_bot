from config import TOKEN

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=TOKEN)

dp = Dispatcher(bot, storage=storage)

# ... code next tomorow


if __name__ == '__main__':
    executor.start_polling(dp)