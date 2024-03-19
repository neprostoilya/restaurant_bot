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
    
    
def select_time_kb():
    """ 
    Create order button
    """
    builder = ReplyKeyboardBuilder()
    
    builder.button(
        text="✅ Ближайшее время",
        callback_data=f"create_order"
    )
    
    builder.button(
        text="🕛 Указать время",
        callback_data=f"create_order"
    )
    
    builder.button(
        text="⬅️ Назад",
        callback_data=f"create_order"
    )
    builder.adjust(2, 1)
    
    return builder.as_markup(
        resize_keyboard=True
    )
    
    
def select_table_kb(quantity_tables: int):
    """ 
    Create order button
    """
    builder = InlineKeyboardBuilder()
    
    for table in range(quantity_tables):
        builder.button(
            text=f"№ {table+1}",
            callback_data=f"table_{table+1}"
        )
    
    builder.adjust(2)
    
    return builder.as_markup(
        resize_keyboard=True
    )
    

def select_payment_type_kb():
    """ 
    Select payment type
    """
    builder = InlineKeyboardBuilder()

    builder.button(
        text=f"💳 Click",
        callback_data=f"type_click"
    )
    
    builder.button(
        text=f"💳 Payme",
        callback_data=f"type_payme"
    )
    
    builder.button(
        text=f"⬅️ Назад",
        callback_data=f"back_to_select_table"
    )
    
    builder.adjust(1, 1)
    
    return builder.as_markup(
        resize_keyboard=True
    )


def order_approval_kb(order_id: int):
    """ 
    Order approval keyboard
    """
    builder = InlineKeyboardBuilder()

    builder.button(
        text=f"✔️ Принять",
        callback_data=f"accept_order_{order_id}"
    )
    
    builder.button(
        text=f"✖️ Отклонить",
        callback_data=f"reject_order_{order_id}"
    )
    
    builder.adjust(2)
    
    return builder.as_markup(
        resize_keyboard=True
    )
    