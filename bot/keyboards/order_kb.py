from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_order_btn_kb():
    """ 
    Create order button
    """
    builder = InlineKeyboardBuilder()
    
    builder.button(
        text="✅ Заказать",
        callback_data=f"create_order"
    )
    
    return builder.as_markup(
        resize_keyboard=True
    )
    
def create_order_btn_kb():
    """ 
    Create order button
    """
    builder = InlineKeyboardBuilder()
    
    builder.button(
        text="✅ Заказать",
        callback_data=f"create_order"
    )
    
    return builder.as_markup(
        resize_keyboard=True
    )
    