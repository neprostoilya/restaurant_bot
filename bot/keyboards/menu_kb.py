from aiogram.utils.keyboard import InlineKeyboardBuilder, \
    ReplyKeyboardBuilder

from api_requests.requests import get_categories_api, \
    get_dishes_by_category_api
from utils.basic_utils import get_text


def choose_type_order_kb(lang: str):
    """
    Choose type order keyboard
    """
    builder = ReplyKeyboardBuilder()
    builder.button(text=get_text(lang, 'delivery_btn'))
    builder.button(text=get_text(lang, 'booking_btn'))
    builder.button(text=get_text(lang, 'pickup_btn'))
    builder.button(text=get_text(lang, 'back_btn'))

    builder.adjust(1, 2, 1)

    return builder.as_markup(
        resize_keyboard=True
    )


def categories_menu_kb(lang: str, total_sum_cart: int):
    """
    Categories menu keyboard
    """
    categories = get_categories_api()

    builder = InlineKeyboardBuilder()

    builder.button(
        text=get_text(lang, 'cart_btn_in_menu') + f' ({total_sum_cart} сум)',
        callback_data='cart'
    )
    if lang == 'ru':
        for category in categories:
            builder.button(
                text=category['title_ru'],
                callback_data=f'category_{category['id']}'
            )
    else:
        for category in categories:
            builder.button(
                text=category['title_uz'],
                callback_data=f'category_{category['id']}'
            )
            
    builder.adjust(1, 2)

    return builder.as_markup(
        resize_keyboard=True
    )


def dishes_menu_kb(lang: str, category: int):
    """
    Dishes menu keyboard
    """
    carts: dict = get_dishes_by_category_api(category)

    builder = InlineKeyboardBuilder()
    
    if lang == 'ru':
        for cart in carts:
            builder.button(
                text=cart['title_ru'],
                callback_data=f'dish_{cart['pk']}'
            )
    else:
      for cart in carts:
        builder.button(
            text=cart['title_uz'],
            callback_data=f'dish_{cart['pk']}'
        )
            
    builder.button(
        text=get_text(lang, 'back_btn'),
        callback_data='bact_to_categories'
    )
    
    builder.adjust(3, 1)

    return builder.as_markup(
        resize_keyboard=True
    )


def in_dish_kb(lang: str, quantity: int, category: int):
    """
    Dish keyboard
    """
    builder = InlineKeyboardBuilder()

    builder.button(
        text="➖",
        callback_data=f"minus_in_dish"
    )
    
    builder.button(
        text=str(quantity),
        callback_data=f"ignore"
    )
    
    builder.button(
        text="➕",
        callback_data=f"plus_in_dish"
    )

    builder.button(
        text=get_text(lang, 'into_cart_btn'),
        callback_data=f"put_into_cart"
    )
    
    builder.button(
        text=get_text(lang, 'back_btn'),
        callback_data=f'bact_to_dishes_{category}'
    )

    builder.adjust(3, 1, 1)

    return builder.as_markup(
        resize_keyboard=True
    )


