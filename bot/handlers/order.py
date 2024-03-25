import re
from datetime import datetime, timedelta

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile, LabeledPrice, PreCheckoutQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ContentType

from keyboards.basic_kb import back_to_main_menu_kb
from api_requests.requests import check_user_api, create_order_api, \
    get_orders_by_user_api, update_order_status_api, get_order_by_order_id_api
from keyboards.basic_kb import main_menu_kb
from keyboards.order_kb import select_time_kb, select_table_kb, select_payment_type_kb, \
    order_approval_kb, review_order_kb, back_btn_kb, pay_order_kb
from config.configuration import CLICK, PAYME, GROUP_ID
from utils.order_utils import get_text_for_order, get_text_for_accepted_order, \
    get_text_for_view_orders, get_text_for_rejected_order

router_order = Router()

class CreateOrder(StatesGroup):
    type_select_time = State()
    time = State()
    table = State()
    quantity_people = State()


class PayOrder(StatesGroup):
    finish_order = State()

@router_order.callback_query(F.data.startswith("create_order"))
async def create_order_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Create order handler
    """
    chat_id: int = call.from_user.id
    
    data: dict = await state.get_data()

    messages_id_list: list = data.get('messages_id_list')    
    
    await call.bot.delete_messages(
        chat_id=chat_id,
        message_ids=messages_id_list,
    )
    
    await call.message.answer(
        text='Укажите удобное для вас время для брони столика:',
        reply_markup=select_time_kb()
    )
    
    await state.set_state(CreateOrder.type_select_time)


@router_order.message(CreateOrder.type_select_time, F.text == '✅ Ближайшее время')
async def selected_nearest_time_handler(message: Message, state: FSMContext) -> None:
    """
    Selected nearest time for order handler
    """
    time = datetime.now() + timedelta(minutes=30)
    
    await message.answer(
        text='Хорошо, теперь выберите столик на миникарте.',
    )
    await state.update_data(
        time_order=f'{time.hour}:{time.minute}'
    )
    
    await message.answer_photo(
        caption='Хорошо, теперь выберите столик на миникарте.',
        photo=FSInputFile('bot/images/map.png'),
        reply_markup=select_table_kb(6) # TODO Change it quantity
    )
    
    await state.set_state(CreateOrder.table)


@router_order.message(CreateOrder.type_select_time, F.text == '🕛 Указать время')
async def selected_type_time_handler(message: Message, state: FSMContext) -> None:
    """
    Selected time for order handler
    """
    await message.answer(
        text='Для брони столика отправьте время в виде "##:##"'
    )
    
    await state.set_state(CreateOrder.time)
    
    
@router_order.message(CreateOrder.time)
async def selected_time_handler(message: Message, state: FSMContext) -> None:
    """
    Selected time for order handler
    """
    text: str = message.text
    
    time_pattern = r"([01]?[0-9]|2[0-3]):([0-5]?[0-9])"

    if re.match(time_pattern, text):
        hours, minutes = map(int, text.split(':'))
        if hours <= 23 and minutes <= 59:
            await message.answer_photo(
                caption='Хорошо, теперь выберите столик на миникарте.',
                photo=FSInputFile('bot/images/map.png'),
                reply_markup=select_table_kb(6) # TODO Change it quantity
            )
            
            await state.update_data(
                time_order=f'{hours}:{minutes}'
            )
            
            await state.set_state(CreateOrder.table)
        else:
            await message.answer(
                text='Формат допустимый, но время не правильное! Повторите еще раз.'
            )
    else:
        await message.answer(
            text='Ошибка при написании времени! Повторите еще раз.'
        )
        
        
@router_order.callback_query(CreateOrder.table, F.data.startswith("table_"))
async def selected_table_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Selected table for order handler
    """
    table: int = int(call.data.split("_")[-1])
    
    await state.update_data(
        table_order=table
    )
    
    await call.message.answer(
        'Отлично, теперь введите колл-во людей:'
    )
    
    await state.set_state(CreateOrder.quantity_people)


@router_order.message(CreateOrder.quantity_people)
async def selected_quantity_people_handler(message: Message, state: FSMContext) -> None:
    """
    Selected quantity people for order handler
    """
    quantity: str = message.text
    
    quantity_pattern = r"\d"
    
    if re.match(quantity_pattern, quantity):
        if 0 < int(quantity) < 50:
            await message.answer(
                text='Отлично, заявка создана, ждите одобрение от мененджера.',
            )
            
            await message.answer(
                text='Выберите направление:',
                reply_markup=main_menu_kb()
            )
            
            chat_id: int = message.chat.id
            
            username: int = message.from_user.username
            
            user: dict = check_user_api(chat_id=chat_id)[0]
            
            data: dict = await state.get_data()
            
            carts: list = data.get('carts')
                            
            total_price: int = data.get('total_price')

            total_quantity: int = data.get('total_quantity')
            
            time_order: str = data.get('time_order')
            
            table_order: int = data.get('table_order')
            
            dishes: list = []
            
            for dish_id, _ in carts:
                dishes.append(dish_id)
            
            print(time_order)
            
            order: dict = create_order_api(
                carts=dishes,
                status='Ожидание',
                user=user.get('pk'),
                total_price=total_price,
                total_quantity=total_quantity,
                time_order=time_order,
                table_order=table_order
            )

            await message.bot.send_message(
                chat_id=GROUP_ID,
                text=get_text_for_order(
                    phone=user.get('phone'),
                    carts=carts,
                    username=username,
                    total_price=total_price,
                    total_quantity=total_quantity,
                    time_order=time_order,
                    table_order=table_order
                ),
                reply_markup=order_approval_kb(
                    order_id=order.get('id'), 
                    chat_id=chat_id,
                )
            )
        else:
            await message.answer(
                text='Ошибка указано неправильное колл-во! Повторите еще раз.'
            )
    else:
        await message.answer(
            text='Ошибка указано было не колл-во! Повторите еще раз.'
        )


@router_order.callback_query(F.data.startswith("accept_order"))
async def accept_order_handler(call: CallbackQuery) -> None:
    """
    Accept order 
    """
    chat_id_user: int = int(call.data.split("_")[-1])
    
    order_id: int = int(call.data.split("_")[-2])
    
    order: dict = update_order_status_api(
        order_id=order_id,
        status='Принят'
    )
    
    await call.bot.send_message(
        chat_id=chat_id_user,
        text=get_text_for_accepted_order(
            order=order
        ),
        reply_markup=pay_order_kb(order.get('id'))
    )
    

@router_order.callback_query(F.data.startswith("reject_order"))
async def reject_order_handler(call: CallbackQuery) -> None:
    """
    Reject order 
    """
    chat_id_user: int = int(call.data.split("_")[-1])
    
    order_id: int = int(call.data.split("_")[-2])
    
    order: dict = update_order_status_api(
        order_id=order_id,
        status='Отклонен'
    )
    
    await call.bot.send_message(
        chat_id=chat_id_user,
        text=get_text_for_rejected_order(
            order=order
        )
    )


@router_order.callback_query(F.data.startswith("pay_order"))
async def select_payment_type_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Select payment type 
    """
    order_id: int = int(call.data.split("_")[-1])

    await state.update_data(
        order_id=order_id
    )

    await call.message.answer(
        text='Отлично, теперь выберите тип оплаты:',
        reply_markup=select_payment_type_kb()
    )

    await state.set_state(PayOrder.finish_order)


@router_order.callback_query(PayOrder.finish_order, F.data.startswith("type_click"))
async def payment_with_click_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Payment with click handler
    """
    data: dict = await state.get_data()
    
    order_id: int = data.get('order_id')
    
    order: dict = get_order_by_order_id_api(
        order_id=order_id
    )[0]
    
    total_price: int = order.get('total_price')
    
    await call.message.answer_invoice(
        title=f"Ваш заказ",
        description='Вы заказали блюда в боте',
        payload="bot-defined invoice payload",
        provider_token=CLICK,
        currency='UZS',
        prices=[
            LabeledPrice(
                label="Общая стоимость",
                amount=total_price * 100
            ),
        ]
    )


@router_order.callback_query(PayOrder.finish_order, F.data.startswith("type_payme"))
async def payment_with_payme_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Payment with payme handler
    """
    data: dict = await state.get_data()
    
    order_id: int = data.get('order_id')
    
    order: dict = get_order_by_order_id_api(
        order_id=order_id
    )[0]
    
    total_price: int = order.get('total_price')
    
    await call.message.answer_invoice(
        title=f"Ваш заказ",
        description='Вы заказали блюда в боте',
        payload="bot-defined invoice payload",
        provider_token=PAYME,
        currency='UZS',
        prices=[
            LabeledPrice(
                label="Общая стоимость",
                amount=total_price * 100
            ),
        ]
    )
    
    await call.message.answer(
        
    )

    
@router_order.pre_checkout_query(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    print('order_info')
    print(pre_checkout_query.order_info)
    await pre_checkout_query.answer(True)


@router_order.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment_handler(message: Message):
    print('successful_payment:')
    pmnt = message.successful_payment.to_python()
    for key, val in pmnt.items():
        print(f'{key} = {val}')
        
        
@router_order.message(F.text == '📖 Мои заказы')
async def get_all_orders_handler(message: Message) -> None:
    """
    Get all orders
    """
    chat_id: int = message.from_user.id 
    
    user: dict = check_user_api(chat_id=chat_id)[0].get('pk')
    
    orders: dict = get_orders_by_user_api(user=user)
    
    if orders:
        await message.answer(
            text='Ваши последние 3 заказа:',
            reply_markup=back_to_main_menu_kb()
        )
        
        for order in orders[::4]:
            await message.answer(
                text=get_text_for_view_orders(order=order),
                reply_markup=review_order_kb(order_id=order.get('id'))
            )
    else:
        await message.answer(
            text='У вас нету ни одного заказа. 😅'
        )


@router_order.message(F.web_app_data)
async def create_order_with_web_app_handler(message: Message, state: FSMContext) -> None:
    """
    Create order with web app handler
    """
    await message.answer(
        text='22'
    )