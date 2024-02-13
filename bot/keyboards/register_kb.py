from aiogram.utils.keyboard import ReplyKeyboardBuilder


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


def send_contact_kb():
    """
    Send Contact to s keyboard
    """
    builder = ReplyKeyboardBuilder()

    builder.button(text='📞 Отправить контакт', request_contact=True)

    return builder.as_markup(
        resize_keyboard=True
    )


