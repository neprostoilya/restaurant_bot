from aiogram.utils.keyboard import ReplyKeyboardBuilder, WebAppInfo, InlineKeyboardBuilder
from config.configuration import URL

from utils.basic_utils import get_text


def main_menu_kb(lang: str):
    """
    Main menu keyboard
    """
    builder = ReplyKeyboardBuilder()

    builder.button(text=get_text(lang, 'start_order_btn'))
    builder.button(text=get_text(lang, 'events_btn'))
    builder.button(text=get_text(lang, 'info_btn'))
    builder.button(text=get_text(lang, 'my_orders_btn'))
    builder.button(text=get_text(lang, 'settings_btn'))

    builder.adjust(1, 2, 2)

    return builder.as_markup(
        resize_keyboard=True
    )


def back_to_main_menu_kb(lang: str):
    """
    Back to Main menu keyboard
    """
    builder = ReplyKeyboardBuilder()

    builder.button(text=get_text(lang, 'back_to_main_btn'))

    return builder.as_markup(
        resize_keyboard=True
    )

