from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

router_order = Router()


class CreateOrder(StatesGroup):
    time = State()
    table = State()


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
        text='Для брони столика отправьте время в виде "##:##"',
    )