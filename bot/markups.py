from aiogram.types import WebAppInfo
from aiogram import types

def web_app_markup():
    """
    Web App markup
    """
    return types.ReplyKeyboardMarkup(
        [
            [types.KeyboardButton(text='CLick me', web_app=WebAppInfo(url='https://3947-95-46-65-64.ngrok-free.app/static/index.html'))]
        ], resize_keyboard=True
    )