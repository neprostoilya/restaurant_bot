from aiogram.utils.markdown import hbold, hitalic


def get_text_for_dish(dish: dict):
    """ 
    Get text for dish 
    """ 
    text: str = f"{hbold('Название')}: {hbold(dish.get('title'))}\n\n{hbold('Описание')}:" \
        f"\n{hitalic(dish.get('description'))}\n\n{hbold('Цена')}: {hitalic(dish.get('price'))} сум"
    
    image: str = dish.get('image')
    
    return text, image


