import re
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold
from aiogram.fsm.state import StatesGroup, State

from utils.basic_utils import get_text, get_lang
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
    
SETTINGS = ['⚙️ Настройки', '⚙️ Sozlamalar']

@router_settings.message(F.text.in_(SETTINGS))
async def settings_handler(message: Message, state: FSMContext) -> None:
    """
    Change settings user
    """
    chat_id: int = message.chat.id
    
    lang: str = await get_lang(chat_id=chat_id, state=state)
    
    await message.answer(
        text=get_text(lang, 'choose_action'),
        reply_markup=settings_kb(lang)
    )


CHANGE_LANGUAGE = ["🇺🇿 Сменить язык", "🇺🇿 Tilni o'zgartiring"]
        

@router_settings.message(F.text.in_(CHANGE_LANGUAGE))
async def change_language_handler(message: Message, state: FSMContext) -> None:
    """
    Change language
    """
    chat_id: int = message.chat.id
    
    lang: str = await get_lang(chat_id=chat_id, state=state)
    
    await message.answer(
        text=get_text(lang, 'choose_language_settings'),
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

    await state.update_data(
        language_user=language
    )
    
    await message.answer(
        text=get_text(language, 'succes_changed_language')
    )
    
    await message.answer(
        text=get_text(language, 'choose_direction'),
        reply_markup=main_menu_kb(language)
    )
    
    await state.set_state(None)


CHANGE_PHONE = ['📞 Сменить номер', "📞 Raqamni o'zgartiring"]


@router_settings.message(F.text.in_(CHANGE_PHONE))
async def change_phone_handler(message: Message, state: FSMContext) -> None:
    """
    Change phone
    """
    chat_id: int = message.chat.id
    
    lang: str = await get_lang(chat_id=chat_id, state=state)
    
    await message.answer(
        text=get_text(lang, 'change_phone_text'),
        reply_markup=ReplyKeyboardRemove()
    )
    
    await state.set_state(ChangePhone.phone)
    

@router_settings.message(ChangePhone.phone)
async def change_phone_handler(message: Message, state: FSMContext) -> None:
    """
    Change phone
    """
    text: str = message.text
    
    if re.match(r"\d{12}", text):
        chat_id: int = message.from_user.id
        
        lang: str = await get_lang(chat_id=chat_id, state=state)
        
        phone: str = message.text 

        update_user_phone_api(
            chat_id=chat_id,
            phone=phone
        )

        await message.answer(
            text=get_text(lang, 'succes_changed_phone')
        )
        
        await message.answer(
            text=get_text(lang, 'choose_direction'),
            reply_markup=main_menu_kb(lang)
        )
        
        await state.set_state(None)
    else:
        await message.answer(
            text=get_text(lang, 'error_form_phone'),
        )
        
        await state.set_state(ChangePhone.phone)
        