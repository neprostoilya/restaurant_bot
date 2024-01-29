from aiogram import types
from config import URL

def choose_language_markup():
    """
    Choose language markup
    """
    kb = [
        [types.KeyboardButton(text='🇷🇺 Русский'),
        types.KeyboardButton(text="🇺🇿 O'zbek tili")]
    ]
    
    markup = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return markup

def open_web_markup():
    """
    Open web markup
    """
    kb = [
        [types.InlineKeyboardButton(text="Open Web", web_app=types.WebAppInfo(url='https://496e-92-63-204-73.ngrok-free.app/frontend/'))],
    ]
    
    markup = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return markup