from aiogram.utils.markdown import hbold, hitalic


def get_text_for_dish(title: str, description: str, price: int) -> str:
    """ 
    Get text for dish 
    """ 
    text: str = f"{hbold('Название')}: {hbold(title)}\n\n{hbold('Описание')}:" \
        f"\n{hitalic(description)}\n\n{hbold('Цена')}: {hitalic(price)} сум"
    
    return text


