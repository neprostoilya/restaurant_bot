import re
from datetime import datetime, timedelta


from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from keyboards.order_kb import select_time_btn_kb

router_order = Router()


class CreateOrder(StatesGroup):
    type_select_time = State()
    time = State()
    table = State()
    quantity_people = State()


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
        reply_markup=select_time_btn_kb()
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
        time_order=f'{time.hour} - {time.minute}'
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
            await message.answer(
                text='Хорошо, теперь выберите столик на миникарте.'
            )
            await state.update_data(
                time_order=f'{hours} {minutes}'
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
        
        
@router_order.message(CreateOrder.table)
async def selected_table_handler(message: Message, state: FSMContext) -> None:
    """
    Selected table for order handler
    """
    
    await state.set_state(CreateOrder.quantity_people)


