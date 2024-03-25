from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold
from aiogram.fsm.state import StatesGroup, State

from api_requests.requests import update_user_language_api, \
    update_user_phone_api
from keyboards.settings_kb import settings_kb
from keyboards.register_kb import choose_language_kb
from keyboards.basic_kb import main_menu_kb

router_settings = Router()


class ChangeLanguage(StatesGroup):
    language = State()


class ChangePhone(StatesGroup):
    phone = State()
    

@router_settings.message(F.text == "⚙️ Настройки")
async def settings_handler(message: Message) -> None:
    """
    Change settings user
    """
    await message.answer(
        text=hbold('Выберите действие:'),
        reply_markup=settings_kb()
    )
        
        
@router_settings.message(F.text == "🇺🇿 Сменить язык")
async def change_language_handler(message: Message, state: FSMContext) -> None:
    """
    Change language
    """
    await message.answer(
        text=hbold('Выберите язык:'),
        reply_markup=choose_language_kb()
    )
    
    await state.set_state(ChangeLanguage.language)


languages: dict = {
    '🇷🇺 Русский': 'ru',
    "🇺🇿 O'zbek tili": 'uz'
}


@router_settings.message(ChangeLanguage.language, F.text.in_(languages.keys()))
async def change_language_handler(message: Message, state: FSMContext) -> None:
    """
    Change language
    """
    chat_id: int = message.from_user.id
    
    language: str = languages.get(message.text)  # RU or UZ

    update_user_language_api(
        chat_id=chat_id,
        language=language
    )

    await message.answer(
        text='Язык успешно изменен!😀'
    )
    
    await message.answer(
        text='Выберите направление:',
        reply_markup=main_menu_kb()
    )
    
    await state.set_state(None)


@router_settings.message(F.text == "📞 Сменить номер")
async def change_phone_handler(message: Message, state: FSMContext) -> None:
    """
    Change phone
    """
    await message.answer(
        text=hbold('Введите номер в виде +998##########:'),
        reply_markup=settings_kb()
    )
    
    await state.set_state(ChangePhone.phone)
    

@router_settings.message(ChangePhone.phone, F.text.regexp(r"\W\d{12}"))
async def change_phone_handler(message: Message, state: FSMContext) -> None:
    """
    Change phone
    """
    chat_id: int = message.from_user.id
    
    phone: str = message.text 

    update_user_phone_api(
        chat_id=chat_id,
        phone=phone
    )

    await message.answer(
        text='Номер успешно изменен!😉'
    )
    
    await message.answer(
        text='Выберите направление:',
        reply_markup=main_menu_kb()
    )
    
    await state.set_state(None)