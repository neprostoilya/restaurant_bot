import re
from datetime import datetime, timedelta

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.basic_kb import back_to_main_menu_kb
    
from utils.basic_utils import get_text, get_lang
from api_requests.requests import check_user_api, get_orders_by_user_api
from keyboards.order_kb import review_order_kb
from utils.order_utils import get_text_for_view_orders

router_my_orders = Router()
    

MY_ORDERS = ['📖 Мои заказы', '📖 Mening buyurtmalarim']


@router_my_orders.message(F.text.in_(MY_ORDERS))
async def get_my_orders_handler(message: Message, state: FSMContext) -> None:
    """
    Get my orders
    """
    chat_id: int = message.from_user.id 

    lang: str = await get_lang(chat_id=chat_id, state=state)

    user: dict = check_user_api(chat_id=chat_id)[0].get('pk')
    
    orders: dict = get_orders_by_user_api(user=user)
    
    if orders:
        await message.answer(
            text=get_text(lang, 'my_last_three_orders'),
            reply_markup=back_to_main_menu_kb(lang)
        )
        
        for order in orders[:3]:
            order_id: int = order.get('pk')
            
            type_order: str = order.get('type_order')
            
            total_price_all_dishes: int = order.get('total_price_all_dishes')    
            
            total_quantity_all_dishes: int = order.get('total_quantity_all_dishes')  
                       
            datetime_selected: str = order.get('datetime_selected')    
            
            datetime_selected: str = order.get('datetime_selected')    
                    
            datetime_created: str = order.get('datetime_created')            
                        
            people_quantity: int = order.get('people_quantity')        
            
            status: str = order.get('status')
            
            place: int = order.get('place')
            
            await message.answer(
                text=get_text_for_view_orders(
                    type_order=type_order,
                    lang=lang,
                    order=order, 
                    total_price_all_dishes=total_price_all_dishes,
                    total_quantity_all_dishes=total_quantity_all_dishes,
                    order_id=order_id,
                    datetime_selected=datetime_selected,
                    datetime_created=datetime_created,
                    people_quantity=people_quantity,
                    status=status,
                    place=place
                ),
                reply_markup=review_order_kb(lang, order_id=order_id)
            )
    else:
        await message.answer(
            text=get_text(lang, 'empty_orders'),
        )