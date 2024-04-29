from datetime import datetime

from aiogram.utils.markdown import hbold, hitalic

from api_requests.requests import get_dish_by_id_api, create_dish_order_api, \
    get_dishes_order_api


def get_text_for_order(phone: str, carts: dict, username: str, total_price: int, total_quantity: int, status: str,
                       datetime_created: str, datetime_selected: str, place: int, order_id: int, people_quantity: int):
    """ 
    Get text for order
    """ 
    dt = datetime.fromisoformat(datetime_created)

    formatted_datetime = dt.strftime('%Y-%m-%d %H:%M')
    
    text_dishes: str = ''
    
    for cart in enumerate(carts):        
        dish_id: int = cart[1][0]
        
        dish: dict = get_dish_by_id_api(dish_id=dish_id)
        
        title: str = dish.get('title_ru')
        
        price: int = (dish.get('price') * cart[1][1])
        
        quantity: int = cart[1][1]
        
        create_dish_order_api(
            order=order_id,
            dish=dish_id,
            total_price=price,
            total_quantity=quantity
        )
        
        text_dishes += f'<b>Блюдо</b> <code>#{cart[0]+1}</code>\n<b>Название:</b> <code>{title}</code>\n<b>Колл-во:</b> '
        text_dishes += f'<code>{quantity}</code>\n<b>Цена:</b> <code>{price}</code> <b>сум.</b>\n\n'
    
    text = f"""
<b>Заказ</b> <code>#{order_id}</code>

<b>От Пользователя:</b> <code>@{username}</code>

<b>Номер:</b> <code>{phone}</code>

<b>Дата и время создания:</b>   
<code>{formatted_datetime}</code>

<b>Забронированное время:</b> <code>{datetime_selected}</code>


{text_dishes}
<b>Место:</b> <code>{place}</code>

<b>Колл-во людей:</b> <code>{people_quantity}</code>

<b>Общая цена:</b> <code>{total_price}</code> <b>сум</b> 

<b>Общее колл-во:</b> <code>{total_quantity}</code>

<b>Статус:</b> <code>{status}</code>
    """
    return text


def get_text_for_view_orders(order: dict, total_price_all_dishes: int, total_quantity_all_dishes: int,
                             order_id: int, datetime_selected: str, datetime_created: str, people_quantity: int, status: str, place: int, lang: str):
    """ 
    Get text for view orders
    """           
    dishes_orders: dict = get_dishes_order_api(
        order_id=order.get('pk')
    )
    
    text_dishes: str = ''
    for dish_order in enumerate(dishes_orders):
        dish_id: int = dish_order[1].get('dish')
        
        dish_quantity: int = dish_order[1].get('total_quantity')
        
        dish_price: int = dish_order[1].get('total_price')
        
        dish: dict = get_dish_by_id_api(dish_id=dish_id)
        
        title: str = dish.get('title_ru') if lang == 'ru' else dish.get('title_uz')
        
        if lang == 'ru':
            text_dishes += f'<b>Блюдо</b> <code>#{dish_order[0]+1}</code>\n<b>Название:</b> <code>{title}</code>\n<b>Колл-во:</b> '
            text_dishes += f'<code>{dish_quantity}</code>\n<b>Цена:</b> <code>{dish_price}</code> <b>сум.</b>\n\n'
        else:
            text_dishes += f'<b>Buyurtma</b> <code>#{dish_order[0]+1}</code>\n<b>Nomi:</b> <code>{title}</code>\n<b>Miqdor:</b> '
            text_dishes += f'<code>{dish_quantity}</code>\n<b>Narx:</b> <code>{dish_price}</code> <b>sum.</b>\n\n'
    
    formatted_datetime_created = datetime.fromisoformat(datetime_created).strftime('%Y-%m-%d %H:%M')
    
    if lang == 'ru':
        text = f"""
<b>Заказ</b> <code>#{order_id}</code>

<b>Дата и время создания:</b>   
<code>{formatted_datetime_created}</code>

<b>Забронированное время:</b> <code>{datetime_selected}</code>


{text_dishes}
<b>Место:</b> <code>{place}</code>

<b>Колл-во людей:</b> <code>{people_quantity}</code>

<b>Общая цена:</b> <code>{total_price_all_dishes}</code> <b>сум</b> 

<b>Общее колл-во:</b> <code>{total_quantity_all_dishes}</code>

<b>Статус:</b> <code>{status}</code>
        """
    else: 
        text = f"""
<b>Buyurtma</b> <code>#{order_id}</code>

<b>Yaratilgan vaqt:</b>   
<code>{formatted_datetime_created}</code>

<b>Axborot vaqt:</b> <code>{datetime_selected}</code>


{text_dishes}
<b>Joy:</b> <code>{place}</code>

<b>A'zolar soni:</b> <code>{people_quantity}</code>

<b>Umumiy narx:</b> <code>{total_price_all_dishes}</code> <b>sum</b> 

<b>Umumiy miqdor:</b> <code>{total_quantity_all_dishes}</code>

<b>Holat:</b> <code>{status}</code>
        """
    
    return text


def get_text_for_accepted_order(language: str, order: dict):
    """ 
    Get text for accepted order
    """
    if language == 'ru':
        text: str = f'Ваш заказ №{hbold(order.get('pk'))} был принят! 😀' 
    else:
        text: str = f'Sizning buyurtmangiz №{hbold(order.get('pk'))} qabul qilindi! 😀' 
        
    return text


def get_text_for_rejected_order(language: str, order: dict):
    """ 
    Get text for rejected order
    """
    if language == 'ru':    
        text: str = f'Ваш заказ №{hbold(order.get('pk'))} был отклонен! 😥' 
    else:
        text: str = f'Sizning buyurtmangiz №{hbold(order.get('pk'))} rad etildi! 😥'
        
    return text


def get_text_for_active_order(phone: str, dishes: dict, username: str, total_price_all_dishes: int, total_quantity_all_dishes: int, status: str,
                       datetime_created: str, datetime_selected: str, place: int, order_id: int, people_quantity: int):
    """ 
    Get text for order
    """ 
    dt = datetime.fromisoformat(datetime_created)

    formatted_datetime = dt.strftime('%Y-%m-%d %H:%M')
    
    text_dishes: str = ''
    
    for dish_order in enumerate(dishes):        
        dish_id: int = dish_order[1].get('dish')
        
        dish_quantity: int = dish_order[1].get('total_quantity')
        
        dish_price: int = dish_order[1].get('total_price')
        
        dish: dict = get_dish_by_id_api(dish_id=dish_id)
        
        title: str = dish.get('title_ru') 
        
        text_dishes += f'<b>Блюдо</b> <code>#{dish_order[0]+1}</code>\n<b>Название:</b> <code>{title}</code>\n<b>Колл-во:</b> '
        text_dishes += f'<code>{dish_quantity}</code>\n<b>Цена:</b> <code>{dish_price}</code> <b>сум.</b>\n\n'
    
    text = f"""
<b>Заказ</b> <code>#{order_id}</code>

<b>От Пользователя:</b> <code>@{username}</code>

<b>Номер:</b> <code>{phone}</code>

<b>Дата и время создания:</b>   
<code>{formatted_datetime}</code>

<b>Забронированное время:</b> <code>{datetime_selected}</code>


{text_dishes}
<b>Место:</b> <code>{place}</code>

<b>Колл-во людей:</b> <code>{people_quantity}</code>

<b>Общая цена:</b> <code>{total_price_all_dishes}</code> <b>сум</b> 

<b>Общее колл-во:</b> <code>{total_quantity_all_dishes}</code>

<b>Статус:</b> <code>{status}</code>
    """
    
    return text
