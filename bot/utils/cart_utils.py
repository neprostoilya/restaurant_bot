from aiogram.utils.markdown import hbold, hitalic


def get_text_for_dish_in_cart(dish: dict, total_price: int):
    """
    Get text for dish in cart user
    """
    text: str = f"{hbold('Название')}: {hbold(dish.get('title'))}\n\n{hbold('Цена')}: " \
        f"{hitalic(total_price)} сум" 
    return text


def get_text_for_total_price(total_quantity_all_cart: int, total_price_all_cart: int):
    """
    Get text for total price and total quantity
    """
    text: str = f"{hbold('Общее колл-во')}: {total_quantity_all_cart}\n" \
        f"{hbold('Общая цена')}: {total_price_all_cart} сум"
        
    return text
