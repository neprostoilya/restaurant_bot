from aiogram import Router, F
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from keyboards.basic_kb import back_to_main_menu_kb


router_info = Router()


@router_info.message(F.text == "ℹ️ Информация")
async def information_handler(message: Message) -> None:
    """
    Get information about restourant
    """
    await message.answer(
        text=f'{hbold('Кафе 7я')}\n\n{hbold('Режим работы')}:\nПн-Вс: 10:00 - 21:30\n\nМененджер: +998 706 14 09 59\nНаш адрес: г. Алмалык ул.Наследова Парк Маяковского'
    )
    
    await message.answer_location(
        latitude=40.835763,
        longitude=69.616893,
        reply_markup=back_to_main_menu_kb()
    )
