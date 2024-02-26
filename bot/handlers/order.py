from aiogram import Router, F
from aiogram.types import CallbackQuery


router_order = Router()

@router_order.callback_query(F.data.startswith("create_order"))
async def create_order_handler(call: CallbackQuery) -> None:
    """
    Create order handler
    """
    