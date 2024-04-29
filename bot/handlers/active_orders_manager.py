from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold

from api_requests.requests import get_active_orders_api,  \
    get_user_by_pk_api
from utils.order_utils import get_dishes_order_api, \
    get_text_for_active_order


router_active_orders = Router()


@router_active_orders.message(F.text == '📖 Активные Заказы')
async def active_orders_handler(message: Message, state: FSMContext) -> None:
    """
    Active orders handler
    """
    await message.answer(
        text=hbold('Активные заказы')
    )
    
    active_orders: dict = get_active_orders_api()
    
    for order in active_orders:
        user_id: int = order.get('user')
        
        user: dict = get_user_by_pk_api(
            user_id=user_id
        )[0]

        username: str = user.get('username')
        
        phone: str = user.get('phone')
        
        total_price_all_dishes: int = order.get('total_price_all_dishes')    
        
        total_quantity_all_dishes: int = order.get('total_quantity_all_dishes')  
    
        datetime_created: int = order.get('datetime_created')
        
        datetime_selected: int = order.get('datetime_selected')
        
        people_quantity: int = order.get('people_quantity')
        
        place: int = order.get('place')
        
        order_id: int = order.get('pk')
        
        people_quantity: int = order.get('people_quantity')
        
        status: str = order.get('status')
        
        dishes: dict = get_dishes_order_api(
            order_id=order_id
        )
        
        await message.answer(
            text=get_text_for_active_order(
                username=username,
                phone=phone,
                dishes=dishes,
                total_price_all_dishes=total_price_all_dishes,
                total_quantity_all_dishes=total_quantity_all_dishes,
                datetime_created=datetime_created,
                datetime_selected=datetime_selected,
                people_quantity=people_quantity,
                place=place,
                order_id=order_id,
                status=status
            )
        )