from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from api_requests.requests import get_tables_api
    

def tables_manager_kb():
    """
    Tables manager keyboard
    """
    builder = InlineKeyboardBuilder()
    
    tables: dict = get_tables_api()
    
    for table in tables:
        if table.get('status') == 'Свободен':
            builder.button(
                text=f"№ {table.get('number')} ✔️",
                callback_data=f"free_table_manager_{table.get('id')}"
            )
        else:
            builder.button(
                text=f"№ {table.get('number')} ❌",
                callback_data=f"busy_table_manager_{table.get('id')}"
            )

    builder.adjust(3)

    return builder.as_markup(
        resize_keyboard=True
    )
    

def back_btn_kb():
    """ 
    Back button
    """
    builder = ReplyKeyboardBuilder()
    
    builder.button(
        text='⬅️ Назад',
    )
    builder.adjust(1)
    
    return builder.as_markup(
        resize_keyboard=True
    )
    