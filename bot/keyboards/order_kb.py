from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from utils.basic_utils import get_text, get_lang
from api_requests.requests import get_tables_api


def create_order_btn_kb(language: str):
    """ 
    Create order button
    """
    builder = InlineKeyboardBuilder()
    
    builder.button(
        text=get_text(language, 'create_order_btn'),
        callback_data=f"create_order"
    )
    
    return builder.as_markup(
        resize_keyboard=True
    )
    
    
def select_time_kb(language: str):
    """ 
    Create order button
    """
    builder = ReplyKeyboardBuilder()
    
    builder.button(
        text=get_text(language, 'near_soon_btn'),
    )
    
    builder.button(
        text=get_text(language, 'set_time_btn'),
    )
    
    builder.button(
        text=get_text(language, 'back_btn'),
    )
    builder.adjust(2, 1)
    
    return builder.as_markup(
        resize_keyboard=True
    )
    
    
def select_table_kb():
    """ 
    Create order button
    """
    builder = InlineKeyboardBuilder()
    
    tables: dict = get_tables_api()
    
    for table in tables:
        if table.get('status') == 'Свободен':
            builder.button(
                text=f"№ {table.get('number')}",
                callback_data=f"table_{table.get('id')}"
            )
        else:
            builder.button(
                text=f"№ {table.get('number')} Занят",
                callback_data='ignore'
            )
            
    builder.adjust(3)
    
    return builder.as_markup(
        resize_keyboard=True
    )
    

def select_payment_type_kb(language: str):
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
        text=get_text(language, 'back_btn'),
        callback_data=f"back_to_select_table"
    )
    
    builder.adjust(2, 1)
    
    return builder.as_markup(
        resize_keyboard=True
    )


def order_approval_kb(order_id: int, chat_id: int):
    """ 
    Order approval keyboard
    """
    builder = InlineKeyboardBuilder()
    print(order_id, chat_id)
    builder.button(
        text=f"✔️ Принять",
        callback_data=f"accept_order_{order_id}_{chat_id}"
    )
    
    builder.button(
        text=f"✖️ Отклонить",
        callback_data=f"reject_order_{order_id}_{chat_id}"
    )
    
    builder.adjust(2)
    
    return builder.as_markup(
        resize_keyboard=True
    )
    
    
def review_order_kb(language: str, order_id: int):
    """ 
    Review order keyboard
    """
    builder = InlineKeyboardBuilder()

    builder.button(
        text=get_text(language, 'to_review_btn'),
        callback_data=f"to_review_order_{order_id}"
    )
    
    builder.adjust(1)
    
    return builder.as_markup(
        resize_keyboard=True
    )


def back_btn_kb(language: str):
    """ 
    Back btn button
    """
    builder = ReplyKeyboardBuilder()
    
    builder.button(
        text=get_text(language, 'back_btn'),
    )
    builder.adjust(2, 1)
    
    return builder.as_markup(
        resize_keyboard=True
    )
    

def pay_order_kb(language: str, order_id: int):
    """ 
    Pay order keyboard
    """
    builder = InlineKeyboardBuilder()

    builder.button(
        text=get_text(language, 'pay_order'),
        callback_data=f"pay_order_{order_id}"
    )
     
    builder.adjust(1)
    
    return builder.as_markup(
        resize_keyboard=True
    )