from aiogram.utils.markdown import hbold, hitalic


def get_text_for_dish(language: str, title: str, description: str, price: int) -> str:
    """ 
    Get text for dish 
    """ 
    if language == 'ru':
        text: str = f"{hbold('Название')}: {hbold(title)}\n\n{hbold('Описание')}:" \
            f"\n{hitalic(description)}\n\n{hbold('Цена')}: {hitalic(price)} сум"
    else:        
        text: str = f"{hbold('Nomi')}: {hbold(title)}\n\n{hbold('Tavsif')}:" \
            f"\n{hitalic(description)}\n\n{hbold('Narxi')}: {hitalic(price)} so'm"
            
    return text

