import asyncio
import logging
import sys

from aiogram import Dispatcher
from aiogram.types import MenuButtonWebApp, WebAppInfo
from aiogram import Bot

from config.configuration import URL
from handlers import commands, register, menu, cart, order, \
    information, events, settings, commands_manager, \
    accept_or_reject_order_manager, active_orders_manager, tables_manager
from config.instance import bot_1, bot_2


async def on_startup(bot: Bot):
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text="Меню", web_app=WebAppInfo(url=URL + '/frontend/'))
    )


async def main():
    """ 
    Main 
    """
    dp_1 = Dispatcher()
    
    dp_2 = Dispatcher()
    
    dp_1.startup.register(on_startup)

    dp_1.include_routers(commands.router_commands)
    dp_1.include_routers(register.router_register)
    dp_1.include_routers(menu.router_menu)
    dp_1.include_routers(cart.router_cart)
    dp_1.include_routers(order.router_order)
    dp_1.include_routers(information.router_info)
    dp_1.include_routers(events.router_events)
    dp_1.include_routers(settings.router_settings)

    dp_2.include_routers(commands_manager.router_commands)
    dp_2.include_routers(active_orders_manager.router_active_orders)
    dp_2.include_routers(accept_or_reject_order_manager.router_accept_or_reject_order)
    dp_2.include_routers(tables_manager.router_tables)

    await bot_1.delete_webhook(drop_pending_updates=True)
    await bot_2.delete_webhook(drop_pending_updates=True)
    await asyncio.gather(dp_1.start_polling(bot_1), dp_2.start_polling(bot_2))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())