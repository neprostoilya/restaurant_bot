from aiogram.utils.keyboard import ReplyKeyboardBuilder


def settings_kb():
    """ 
    Settings button
    """
    builder = ReplyKeyboardBuilder()
    
    builder.button(
        text="🇺🇿 Сменить язык",
    )
    
    builder.button(
        text="📞 Сменить номер",
    )
    
    builder.button(
        text="⬅️ Главное меню",
    )
    builder.adjust(2, 1)
    
    return builder.as_markup(
        resize_keyboard=True
    )
    