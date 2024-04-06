from datetime import datetime

from aiogram.utils.markdown import hbold, hitalic

from api_requests.requests import get_dish_by_id_api


def get_text_for_order(phone: str, dishes: dict, username: str, total_price: int, total_quantity: int, status: str,
                       datetime_created: str, datetime_selected: str, table: int, order_id: int, people_quantity: int):
    """ 
    Get text for order
    """ 
    text_dishes: str = ''
    
    for dish_id in enumerate(dishes):
        dish: dict = get_dish_by_id_api(dish_id[1])
        
        title: str = dish.get('title')
        
        total_quantity_dish: int = 1
        
        total_price_dish: int = 100
        
        text_dishes += f'<b>Блюдо</b> <code>#{dish_id[0]}</code>\n<b>Название:</b> <code>{title}</code>\n<b>Колл-во:</b>', \
        f'<code>{total_quantity_dish}</code>\n<b>Цена:</b> <code>{total_price_dish}</code> <b>сум.</b>\n\n'
    
    text = f"""
<b>Заказ</b> <code>#${order_id}</code>

<b>От Пользователя:</b> <code>@${username}</code>

<b>Номер:</b> <code>${phone}</code>

<b>Дата и время создания:</b>   
<code>${datetime_created}</code>

<b>Забронированное время:</b> <code>${datetime_selected}</code>


${text_dishes}
<b>Номер столика:</b> <code>${table}</code>

<b>Колл-во людей:</b> <code>${people_quantity}</code>

<b>Общая цена:</b> <code>${total_price}</code> <b>сум</b> 

<b>Общее колл-во:</b> <code>${total_quantity}</code>`;

<b>Статус:</b> <code>{status}</code>
    """
    return text


def get_text_for_view_orders(order: dict):
    """ 
    Get text for view orders
    """        
    text: str = f'Заказ №{hbold(order.get('id'))}\n\n' 
    
    for cart in enumerate(order.get('dishes')):
        dish: dict = get_dish_by_id_api(dish_id=cart[1])
        
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
