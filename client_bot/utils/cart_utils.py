from aiogram.utils.markdown import hbold, hitalic


def get_text_for_dish_in_cart(language: str, dish: dict, total_price: int):
    """
    Get text for dish in cart user
    """
    if language == 'ru':
        text: str = f"{hbold('Название')}: {hbold(dish.get('title_ru'))}\n\n{hbold('Цена')}: " \
            f"{hitalic(total_price)} сум" 
    else:
        text: str = f"{hbold('Nomi')}: {hbold(dish.get('title_ru'))}\n\n{hbold('Narxi')}: " \
            f"{hitalic(total_price)} so'm" 
            
    return text


def get_text_for_total_price(language: str, total_quantity_all_cart: int, total_price_all_cart: int):
    """
    Get text for total price and total quantity
    """
    if language == 'ru':
        text: str = f"{hbold('Общее колл-во')}: {total_quantity_all_cart}\n" \
            f"{hbold('Общая цена')}: {total_price_all_cart} сум"
    else:
        text: str = f"{hbold('Umumiy soni')}: {total_quantity_all_cart}\n" \
            f"{hbold('Umumiy narx')}: {total_price_all_cart} so'm"
            
    return text
