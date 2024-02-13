from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State

from api_requests.requests import register_user_api
from keyboards.register_kb import send_contact_kb
from keyboards.basic_kb import main_menu_kb

router_register = Router()


class Registration(StatesGroup):
    language = State()
    contact = State()


languages: dict = {
    '🇷🇺 Русский': 'ru',
    "🇺🇿 O'zbek tili": 'uz'
}


@router_register.message(Registration.language, F.text.in_(languages.keys()))
async def set_language_handler(message: Message, state: FSMContext) -> None:
    """
    Reaction on change language
    """
    language: str = languages.get(message.text)  # RU or UZ

    await state.update_data(language=language)

    await message.delete()

    await message.answer(
        text='Отлично, теперь отправьте нам контакт.',
        reply_markup=send_contact_kb()
    )

    await state.set_state(Registration.contact)


@router_register.message(Registration.contact, F.contact)
async def finish_register_handler(message: Message, state: FSMContext) -> None:
    """
    Finish register user
    """
    data = await state.get_data()

    chat_id: int = message.from_user.id
    nickname: str = message.from_user.full_name
    language: str = data.get('language')
    contact: str = message.contact.phone_number

    register_user_api(
        username=nickname,
        phone=contact,
        chat_id=chat_id,
        language=language
    )

    await message.delete()

    await message.answer(
        text='Выберите направление:',
        reply_markup=main_menu_kb()
    )

    await state.clear()
