from datetime import datetime

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
        
        text += f'Блюдо №{hbold(int(cart[0])+1)}.\nНазвание: {dish.get('title_ru')},\n'

        text += f'Колл-во: {hbold(cart[1][1])},\nЦена: {hbold(price)} сум\n\n'
        
    text += f'Забронированное время: {hbold(time_order)}\n\nНомер столика: {hbold(table_order)}\n\n'
    
    text += f'Общая цена: {hbold(total_price)}\n\nОбщее колл-во: {hbold(total_quantity)}'
    
    return text


def get_text_for_view_orders(order: dict):
    """ 
    Get text for view orders
    """        
    text: str = f'Заказ №{hbold(order.get('id'))}\n\n' 
    
    for cart in enumerate(order.get('dishes')):
        dish: dict = get_dish_by_id_api(dish_id=cart[1])[0]
        
        price: int = dish.get('price') * cart[1]
        
        text += f'Блюдо №{hbold(int(cart[0])+1)}.\nНазвание: {dish.get('title_ru')},\n'
        
        text += f'Колл-во: {hbold(cart[1])},\nЦена: {hbold(price)} сум\n\n'
    
    text += f'Забронированное время: {hbold(order.get('datetime_selected'))}'
    
    text += f'\n\nНомер столика: {hbold(order.get('table'))}\n\n'
    
    text += f'Общая цена: {hbold(order.get('total_price'))}\n'
    
    text += f'\nОбщее колл-во: {hbold(order.get('total_quantity'))}\n\n'
    
    text += f'Статус: {hbold(order.get('status'))}'
    
    return text


def get_text_for_accepted_order(language: str, order: dict):
    """ 
    Get text for accepted order
    """
    if language == 'ru':
        text: str = f'Ваш заказ №{hbold(order.get('id'))} был принят! 😀' 
    else:
        text: str = f'Sizning buyurtmangiz №{hbold(order.get('id'))} qabul qilindi! 😀' 
        
    return text


def get_text_for_rejected_order(language: str, order: dict):
    """ 
    Get text for rejected order
    """
    if language == 'ru':    
        text: str = f'Ваш заказ №{hbold(order.get('id'))} был отклонен! 😥' 
    else:
        text: str = f'Sizning buyurtmangiz №{hbold(order.get('id'))} rad etildi! 😥'
        
    return text
