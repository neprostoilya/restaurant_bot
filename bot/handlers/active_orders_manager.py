from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold, hitalic

from api_requests.requests import get_active_orders_api,  \
    get_user_by_pk_api
from utils.order_utils import get_text_for_order


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
        )   

        username: str = user.get('username')
        
        phone: str = user.get('phone')
        
        dishes: list = order.get('dishes')
        
        total_price: int = order.get('total_price')
        
        total_quantity: int = order.get('total_quantity')
        
        datetime_created: int = order.get('datetime_created')
        
        datetime_selected: int = order.get('datetime_selected')
        
        people_quantity: int = order.get('people_quantity')
        
        table: int = order.get('table')
        
        order_id: int = order.get('pk')
        
        people_quantity: int = order.get('people_quantity')
        
        await message.answer(
            text=get_text_for_order(
                username=username,
                phone=phone,
                dishes=dishes,
                total_price=total_price,
                total_quantity=total_quantity,
                datetime_created=datetime_created,
                datetime_selected=datetime_selected,
                people_quantity=people_quantity,
                table=table,
                order_id=order_id
            )
        )