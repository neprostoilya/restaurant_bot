from aiogram.utils.markdown import hbold, hitalic

from api_requests.requests import get_dish_by_id_api


def get_text_for_dish(dish_id: int):
    """ 
    Get text for dish 
    """
    dish: dict = get_dish_by_id_api(dish_id)[0]
    
    text: str = f"{hbold('Название')}: {hbold(dish.get('title'))}\n\n{hbold('Описание')}:" \
        f"\n{hitalic(dish.get('description'))}\n\n{hbold('Цена')}: {hitalic(dish.get('price'))} сум"
    
    image: str = dish.get('image')
    
    return text, image


def get_text_for_dish_in_cart(cart: dict):
    """
    Get text for dish in cart user
    """
    text: str = f"{hbold('Название')}: {hbold(cart.get('get_dish_title'))}\n\n{hbold('Цена')}: " \
        f"{hitalic(cart.get('get_dish_price'))} сум" 
    return text