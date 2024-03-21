from aiogram import Router, F
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from keyboards.basic_kb import back_to_main_menu_kb
from utils.information_utils import get_text_for_info

router_info = Router()


@router_info.message(F.text == "ℹ️ Информация")
async def information_handler(message: Message) -> None:
    """
    Get information about restourant
    """
    await message.answer(
        text=get_text_for_info()
    )
        
    await message.answer_location(
        latitude=40.835763,
        longitude=69.616893,
        reply_markup=back_to_main_menu_kb()
    )
