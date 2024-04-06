from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from api_requests.requests import update_order_status_api
from utils.basic_utils import get_lang
from utils.order_utils import get_text_for_accepted_order, get_text_for_rejected_order
from keyboards.order_kb import pay_order_kb
from config.instance import bot_1


router_accept_or_reject_order = Router()


@router_accept_or_reject_order.callback_query(F.data.startswith("accept_order"))
async def accept_order_handler(call: CallbackQuery) -> None:
    """
    Accept order 
    """
    chat_id_user: int = int(call.data.split("_")[-1])

    lang: str = await get_lang(chat_id=chat_id_user, state=None)
    
    order_id: int = int(call.data.split("_")[-2])
    
    order: dict = update_order_status_api(
        order_id=order_id,
        status='Принят'
    )
    
    await bot_1.send_message(
        chat_id=chat_id_user,
        text=get_text_for_accepted_order(
            language=lang,
            order=order
        ),
        reply_markup=pay_order_kb(lang, order.get('id'))
    )
    

@router_accept_or_reject_order.callback_query(F.data.startswith("reject_order"))
async def reject_order_handler(call: CallbackQuery) -> None:
    """
    Reject order 
    """
    chat_id_user: int = int(call.data.split("_")[-1])
    
    lang: str = await get_lang(chat_id=chat_id_user, state=None)
    
    order_id: int = int(call.data.split("_")[-2])
    
    order: dict = update_order_status_api(
        order_id=order_id,
        status='Отклонен'
    )
    
    await bot_1.send_message(
        chat_id=chat_id_user,
        text=get_text_for_rejected_order(
            language=lang,
            order=order
        )
    )