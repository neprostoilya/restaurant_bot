from aiogram.utils.markdown import hbold, hitalic


def get_text_for_dish_in_cart(cart: dict):
    """
    Get text for dish in cart user
    """
    text: str = f"{hbold('Название')}: {hbold(cart.get('get_dish_title'))}\n\n{hbold('Цена')}: " \
        f"{hitalic(cart.get('get_total_price'))} сум" 
    return text


def get_text_for_total_price(total_quantity: int, total_price: int):
    """
    Get text for total price and total quantity
    """
    text: str = f"{hbold('Общее колл-во')}: {total_quantity}\n{hbold('Общая цена')}: {total_price} сум"
        
    return text
