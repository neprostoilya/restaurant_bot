from aiogram.utils.keyboard import InlineKeyboardBuilder

from api_requests.requests import get_categories_api, get_dish_by_id_api, get_dishes_by_category_api


def categories_menu_kb():
    """
    Categories menu keyboard
    """
    categories = get_categories_api()

    builder = InlineKeyboardBuilder()

    for category in categories:
        builder.button(
            text=category['title'],
            callback_data=f'category_{category['id']}'
        )

    builder.adjust(2)

    return builder.as_markup(
        resize_keyboard=True
    )


def dishes_menu_kb(category):
    """
    Dishes menu keyboard
    """
    dishes = get_dishes_by_category_api(category)

    builder = InlineKeyboardBuilder()

    for dish in dishes:
        builder.button(
            text=dish['title'],
            callback_data=f'dish_{dish['pk']}'
        )

    builder.adjust(3)

    return builder.as_markup(
        resize_keyboard=True
    )


def in_dish_kb(quantity: int, dish_id: int):
    """
    Dish keyboard
    """
    builder = InlineKeyboardBuilder()

    builder.button(
        text="➖",
        callback_data=f"minus"
    )
    
    builder.button(
        text=str(quantity),
        callback_data=f"ignore"
    )
    
    builder.button(
        text="➕",
        callback_data=f"plus"
    )

    builder.button(
        text="🛒 В корзину",
        callback_data=f"put_into_cart_{dish_id}"
    )
     

    builder.adjust(3, 1)

    return builder.as_markup(
        resize_keyboard=True
    )

