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
        [types.InlineKeyboardButton(text="Open Web", web_app=types.WebAppInfo(url='https://b9bf-95-46-66-119.ngrok-free.app/dishes/dishes/'))],
    ]
    
    markup = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return markup