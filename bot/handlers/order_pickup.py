import re
from datetime import datetime, timedelta

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


from keyboards.order_kb import select_place_kb, back_btn_kb
from keyboards.basic_kb import main_menu_kb


from utils.basic_utils import get_text, get_lang
from api_requests.requests import check_user_api, create_pickup_order_api, \
    get_managers_api
from keyboards.order_kb import select_place_kb, \
    order_approval_kb, back_btn_kb, select_time_kb
from config.instance import bot_2
from utils.order_utils import get_text_for_pickup_order


router_pickup_order = Router()


class CreatePickupOrder(StatesGroup):
    type_select_time = State()
    time = State()


BACK_TO_MENU = ['⬅️ Orqaga', '⬅️ Назад']


NEAR_TIME = ['✅ Ближайшее время', '✅ Tez orada']


@router_pickup_order.message(CreatePickupOrder.type_select_time, F.text.in_(NEAR_TIME))
async def selected_nearest_time_handler(message: Message, state: FSMContext) -> None:
    """
    Selected nearest time for order handler
    """
    chat_id: int = message.chat.id
    
    lang: str = await get_lang(chat_id=chat_id, state=state)
    
    time: object = datetime.now() + timedelta(minutes=30)
    
    time_order: str = f'{time.hour}:{time.minute}'

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
    
    order: dict = create_pickup_order_api(
        status='Ожидание',
        user=user.get('pk'),
        total_price=total_price,
        total_quantity=total_quantity,
        time_order=time_order,
        type_order='Самовывоз'
    )
    
    managers: dict = get_managers_api()
    
    for manager in managers:
        try:
            await bot_2.send_message(
                chat_id=manager.get('telegram_pk'),
                text=get_text_for_pickup_order(
                    phone=user.get('phone'),
                    carts=carts,
                    username=username,
                    total_price=total_price,
                    total_quantity=total_quantity,
                    datetime_selected=time_order,
                    datetime_created=order.get('datetime_created'),
                    order_id=order.get('pk'),
                    status=order.get('status')
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

SET_TIME = ['🕛 Указать время', '🕛 Vaqtni belgilang']


@router_pickup_order.message(CreatePickupOrder.type_select_time, F.text.in_(SET_TIME))
async def selected_type_time_handler(message: Message, state: FSMContext) -> None:
    """
    Selected time for order handler
    """
    chat_id: int = message.chat.id
    
    lang: str = await get_lang(chat_id=chat_id, state=state)
    
    await message.answer(
        text=get_text(lang, 'set_time_text'),
        reply_markup=back_btn_kb(lang)
    )
    
    await state.set_state(CreatePickupOrder.time)


@router_pickup_order.message(CreatePickupOrder.time, F.text.in_(BACK_TO_MENU))
async def back_to_set_time_handler(message: Message, state: FSMContext) -> None:
    """
    Back to menu handler
    """
    chat_id: int = message.chat.id
    
    lang: str = await get_lang(chat_id=chat_id, state=state) 
    
    await message.answer(
        text=get_text(lang, 'select_time'),
        reply_markup=select_time_kb(lang)
    )

@router_pickup_order.message(CreatePickupOrder.time)
async def selected_time_handler(message: Message, state: FSMContext) -> None:
    """
    Selected time for order handler
    """
    chat_id: int = message.chat.id
    
    lang: str = await get_lang(chat_id=chat_id, state=state)
    
    text: str = message.text
    
    time_pattern = r"([01]?[0-9]|2[0-3]):([0-5]?[0-9])"

    if re.match(time_pattern, text):
        hours, minutes = map(int, text.split(':'))
        if hours <= 23 and minutes <= 59:
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
            
            time_order: str = f'{hours}:{minutes}'
            
            order: dict = create_pickup_order_api(
                status='Ожидание',
                user=user.get('pk'),
                total_price=total_price,
                total_quantity=total_quantity,
                time_order=time_order,
                type_order='Самовывоз'
            )
            
            managers: dict = get_managers_api()
            
            for manager in managers:
                try:
                    await bot_2.send_message(
                        chat_id=manager.get('telegram_pk'),
                        text=get_text_for_pickup_order(
                            phone=user.get('phone'),
                            carts=carts,
                            username=username,
                            total_price=total_price,
                            total_quantity=total_quantity,
                            datetime_selected=time_order,
                            datetime_created=order.get('datetime_created'),
                            order_id=order.get('pk'),
                            status=order.get('status')
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
        else:
            await message.answer(
                text=get_text(lang, 'error_format_time')
            )
    else:
        await message.answer(
            text=get_text(lang, 'error_text_time')
        )
        