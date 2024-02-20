from aiogram.utils.keyboard import InlineKeyboardBuilder

from api_requests.requests import get_categories_api, get_dish_by_id_api, get_dishes_by_category_api


def categories_menu_kb(total_sum_cart):
    """
    Categories menu keyboard
    """
    categories = get_categories_api()

    builder = InlineKeyboardBuilder()

    builder.button(
        text=f'🛒 Корзина ({total_sum_cart} сум)',
        callback_data='cart'
    )

    for category in categories:
        builder.button(
            text=category['title'],
            callback_data=f'category_{category['id']}'
        )

    builder.adjust(1, 2, 1)

    return builder.as_markup(
        resize_keyboard=True
    )


def dishes_menu_kb(category):
    """
    Dishes menu keyboard
    """
    carts: dict = get_dishes_by_category_api(category)

    builder = InlineKeyboardBuilder()

    for cart in carts:
        builder.button(
            text=cart['title'],
            callback_data=f'dish_{cart['pk']}'
        )
        
    builder.button(
        text='⬅️ Назад',
        callback_data='bact_to_categories'
    )
    
    builder.adjust(3, 1)

    return builder.as_markup(
        resize_keyboard=True
    )


def in_dish_kb(quantity: int):
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
        text="🛒 В корзину",
        callback_data=f"put_into_cart"
    )
    
    builder.button(
        text='⬅️ Назад',
        callback_data='bact_to_dishes'
    )

    builder.adjust(3, 1, 1)

    return builder.as_markup(
        resize_keyboard=True
    )


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