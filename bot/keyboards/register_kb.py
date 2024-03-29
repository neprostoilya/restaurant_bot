from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils.basic_utils import get_text


def choose_language_kb():
    """
    Choose language keyboard
    """
    builder = ReplyKeyboardBuilder()

    builder.button(text='🇷🇺 Русский')
    builder.button(text="🇺🇿 O'zbek tili")

    builder.adjust(2)

    return builder.as_markup(
        resize_keyboard=True
    )


def send_contact_kb(lang: str):
    """
    Send Contact to s keyboard
    """
    builder = ReplyKeyboardBuilder()

    builder.button(
        text=get_text(lang, 'send_contact_btn'), 
        request_contact=True
    )

    return builder.as_markup(
        resize_keyboard=True
    )


