import re
from datetime import datetime, timedelta

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


from keyboards.basic_kb import main_menu_kb


from utils.basic_utils import get_text, get_lang
from api_requests.requests import check_user_api, create_delivery_order_api, \
    get_managers_api
from keyboards.order_kb import order_approval_kb
from config.instance import bot_2
from utils.order_utils import get_text_for_delivery_order


router_delivery_order = Router()


class CreateDeliveryOrder(StatesGroup): 
    get_location = State()


BACK_TO_MENU = ['⬅️ Orqaga', '⬅️ Назад']



@router_delivery_order.message(CreateDeliveryOrder.get_location, F.location)
async def get_location_handler(message: Message, state: FSMContext) -> None:
    """
    Get Location and create order handler
    """
    chat_id: int = message.chat.id
    
    lang: str = await get_lang(chat_id=chat_id, state=state)
    
    await message.answer(
        text=get_text(lang, 'succes_create_order'),
    )
    
    await message.answer(
        text=get_text(lang, 'choose_direction'),
        reply_markup=main_menu_kb(lang)
    )
    
    chat_id: int = message.from_user.id
    
    username: int = message.from_user.username
    
    user: dict = check_user_api(chat_id=chat_id)[0]
    
    data: dict = await state.get_data()
    
    carts: list = data.get('carts')
                    
    total_price: int = data.get('total_price')

    total_quantity: int = data.get('total_quantity')
    
    latitude: str = str(message.location.latitude)
    
    longitude: str = str(message.location.longitude)
    
    order: dict = create_delivery_order_api(
        status='Ожидание',
        user=user.get('pk'),
        total_price=total_price,
        total_quantity=total_quantity,
        latitude=latitude,
        longitude=longitude,
        type_order='Доставка'
    )
    
    managers: dict = get_managers_api()
    for manager in managers:
        try:
            await bot_2.send_location(
                chat_id=manager.get('telegram_pk'),
                latitude=latitude,  
                longitude=longitude
            )
            
            await bot_2.send_message(
                chat_id=manager.get('telegram_pk'),
                text=get_text_for_delivery_order(
                    phone=user.get('phone'),
                    carts=carts,
                    username=username,
                    total_price=total_price,
                    total_quantity=total_quantity,
                    datetime_created=order.get('datetime_created'),
                    order_id=order.get('pk'),
                    status=order.get('status'),
                ),
                reply_markup=order_approval_kb(
                    order_id=order.get('pk'), 
                    chat_id=chat_id,
                ),
                parse_mode='HTML'
            )
        except:
            pass
        
    await state.set_state(None)
    