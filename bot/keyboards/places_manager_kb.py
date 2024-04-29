from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from api_requests.requests import get_places_api


def update_status_place_kb():
    """ 
    Update Status Place
    """
    builder = InlineKeyboardBuilder()
    
    places: dict = get_places_api()
    
    for place in places:
        if place.get('is_view'):
            builder.button(
                text=f"{place.get('title_ru')} ✔️",
                callback_data=f"free_table_manager_{place.get('id')}"
            )
        else:
            builder.button(
                text=f"{place.get('title_ru')} ❌",
                callback_data=f"busy_table_manager_{place.get('id')}"
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
    