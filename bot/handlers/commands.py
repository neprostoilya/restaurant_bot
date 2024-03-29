from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from utils.basic_utils import get_text, get_lang
from handlers.register import Registration
from api_requests.requests import check_user_api
from keyboards.register_kb import choose_language_kb
from keyboards.basic_kb import main_menu_kb

router_commands = Router()


@router_commands.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    """
    Reaction on command '/start'
    """
    chat_id: int = message.from_user.id
    
    nickname: str = message.from_user.full_name
    
    lang: str = await get_lang(chat_id=chat_id, state=state)
    
    await message.answer(
        text=get_text(lang, 'welcome_bot') + hbold(nickname)
    )

    if check_user_api(chat_id):
        await message.answer(
            text=get_text(lang, 'choose_direction'),
            reply_markup=main_menu_kb(lang)
        )
    else:
        await message.answer(
            text=get_text(lang, 'choose_lang'),
            reply_markup=choose_language_kb()
        )
        await state.set_state(Registration.language)


@router_commands.message(Command('about'))
async def command_about_handler(message: Message) -> None:
    """
    Reaction on command '/about'
    """
    await message.answer(
        text=f'Этот бот создан для ресторана...'
    )


@router_commands.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    """
    Reaction on command '/help'
    """
    await message.answer(
        text=f"Остались вопросы? звоните или пишите к ..."
    )
