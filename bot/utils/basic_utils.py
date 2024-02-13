from aiogram.utils.markdown import hbold, hitalic

from api_requests.requests import get_dish_by_id_api


def get_text_for_dish(dish_id):
    """ 
    Get text for dish 
    """
    dish: dict = get_dish_by_id_api(dish_id)[0]
    
    text: str = f"{hbold(dish.get('title'))}\n\n{hbold('Описание')}:\n{hitalic(dish.get('description'))}" \
        f"\n\n{hbold('Цена')}: {hitalic(dish.get('price'))}"
    
    image: str = dish.get('image')
    
    return text, image