from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils.basic_utils import get_lang
from keyboards.basic_kb import back_to_main_menu_kb
from utils.information_utils import get_text_for_info

router_info = Router()


INFORMATION = ['ℹ️ Информация', "ℹ️ Ma'lumot"]


@router_info.message(F.text.in_(INFORMATION))
async def information_handler(message: Message, state: FSMContext) -> None:
    """
    Get information about restourant
    """
    chat_id: int = message.chat.id
    
    lang: str = await get_lang(chat_id=chat_id, state=state)
    
    await message.answer(
        text=get_text_for_info(lang)
    )
        
    await message.answer_location(
        latitude=40.835763,
        longitude=69.616893,
        reply_markup=back_to_main_menu_kb(lang)
    )
