from aiogram.utils.markdown import hbold, hitalic

from api_requests.requests import get_dish_by_id_api


def get_text_for_order(phone: str, carts: dict, username: str, total_price: int,
                       total_quantity: int, time_order: str, table_order: int):
    """ 
    Get text for order
    """ 
    
    text: str = f'Заказ от @{username}\nНомер: {hbold(phone)}\n\n'
    
    for cart in enumerate(carts):
        dish: dict = get_dish_by_id_api(dish_id=cart[1][0])[0]
        
        price: int = dish.get('price') * cart[1][1]
        
        text += f'{hbold(f'Блюдо №{cart[0]+1}')}\nКолл-во: {hbold(cart[1][1])}\nЦена: {hbold(price)}\n\n'
        
    text += f'Забронированное время: {hbold(time_order)}\n\nНомер столика: {hbold(table_order)}\n\n'
    
    text += f'Общая цена: {hbold(total_price)}\n\nОбщее колл-во: {hbold(total_quantity)}'
    
    return text


def get_text_for_view_orders(dish_id: int):
    """ 
    Get text for view orders
    """        
    text: str = f'Заказ №{hbold(dish_id)}\n\n' 
    
    return text

