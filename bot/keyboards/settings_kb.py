from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils.basic_utils import get_text


def settings_kb(language: str):
    """ 
    Settings button
    """
    builder = ReplyKeyboardBuilder()
    
    builder.button(
        text=get_text(language, 'change_language_btn'),
    )
    
    builder.button(
        text=get_text(language, 'change_phone'),
    )
    
    builder.button(
        text=get_text(language, 'back_to_main_btn'),
    )
    builder.adjust(2, 1)
    
    return builder.as_markup(
        resize_keyboard=True
    )
    