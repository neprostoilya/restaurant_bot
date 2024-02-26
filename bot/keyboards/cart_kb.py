from aiogram.utils.keyboard import InlineKeyboardBuilder


def cart_kb(quantity: int, dish_id: int):
    """ 
    Cart keyboard
    """
    builder = InlineKeyboardBuilder()

    builder.button(
        text="➖",
        callback_data=f"minus_in_cart_{dish_id}_{quantity}"
    )
    
    builder.button(
        text=str(quantity),
        callback_data=f"ignore"
    )
    
    builder.button(
        text="➕",
        callback_data=f"plus_in_cart_{dish_id}_{quantity}"
    )
    
    builder.button(
        text="❌ Удалить",
        callback_data=f"delete_in_cart_{dish_id}_{quantity}"
    )
    
    builder.adjust(3, 1)

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
    