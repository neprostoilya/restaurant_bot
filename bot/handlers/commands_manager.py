import re

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from api_requests.requests import check_manager_api
from keyboards.menu_manager_kb import main_menu_manager_kb

router_commands = Router()


@router_commands.message(CommandStart())
async def command_start_manager_bot_handler(message: Message, state: FSMContext) -> None:
    """
    Reaction on command '/start' in manager bot
    """    
    
    chat_id: int = message.from_user.id
    
    await message.answer(
        text='Здравствуйте, ' + hbold(message.from_user.full_name)
    )
    
    manager_user: bool = check_manager_api(
        chat_id=chat_id
    )
    
    if manager_user:
        await message.answer(
            text='Проверка прошла успешно! 😉'
        )
        await message.answer(
            text='Выберите направление:',
            reply_markup=main_menu_manager_kb()
        )
    else:
        await message.answer(
            text='Проверка не прошла! Вы не мененджер. 😥'
        )
        await state.clear()


@router_commands.message(Command('about'))
async def command_about_handler(message: Message) -> None:
    """
    Reaction on command '/about'
    """
    await message.answer(
        text=f'Этот бот для мененджеров'
    )


@router_commands.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    """
    Reaction on command '/help'
    """
    await message.answer(
        text=f"Остались вопросы? звоните или пишите к ..."
    )
