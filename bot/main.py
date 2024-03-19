import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from handlers import commands, register, menu, cart, order, information
from config.configuration import TOKEN


async def main():
    """ 
    Main 
    """
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.include_routers(commands.router_commands)
    dp.include_routers(register.router_register)
    dp.include_routers(menu.router_menu)
    dp.include_routers(cart.router_cart)
    dp.include_routers(order.router_order)
    dp.include_routers(information.router_info)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())