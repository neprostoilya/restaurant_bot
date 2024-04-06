from aiogram.utils.keyboard import ReplyKeyboardBuilder


def send_contact_kb():
    """
    Send Contact to bot keyboard
    """
    builder = ReplyKeyboardBuilder()

    builder.button(
        text='📞 Отправить контакт', 
        request_contact=True
    )

    return builder.as_markup(
        resize_keyboard=True
    )

