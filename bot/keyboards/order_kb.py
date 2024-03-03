from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


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
    
    
# def select_time_btn_kb():
#     """ 
#     Create order button
#     """
#     builder = ReplyKeyboardBuilder()
    
#     builder.button(
#         text="🕛 Ближайшее время",
#         callback_data=f"create_order"
#     )
    
#     builder.button(
#         text="⬅️ Назад",
#         callback_data=f"create_order"
#     )
    
#     return builder.as_markup(
#         resize_keyboard=True
#     )
    