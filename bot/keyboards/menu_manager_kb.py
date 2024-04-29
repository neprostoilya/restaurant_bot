from aiogram.utils.keyboard import ReplyKeyboardBuilder
    

def main_menu_manager_kb():
    """
    Choose type order keyboard
    """
    builder = ReplyKeyboardBuilder()

    builder.button(text='📖 Активные Заказы')
    builder.button(text='🍽️ Места Ресторана')
    builder.button(text='💬 Рассылка')

    builder.adjust(2, 1)

    return builder.as_markup(
        resize_keyboard=True
    )