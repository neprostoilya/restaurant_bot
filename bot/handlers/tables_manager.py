from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold

from api_requests.requests import get_tables_api

router_tables_orders = Router()


@router_tables_orders.message(F.text == '📖 Активные Заказы')
async def active_orders_handler(message: Message, state: FSMContext) -> None:
    """
    Active orders handler
    """
