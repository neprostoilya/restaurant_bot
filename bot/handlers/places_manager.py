from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold

from keyboards.places_manager_kb import update_status_place_kb, back_btn_kb
from api_requests.requests import update_place_status_api
from keyboards.menu_manager_kb import main_menu_manager_kb

router_places = Router()


@router_places.message(F.text == '🍽️ Места Ресторана')
async def tables_handler(message: Message) -> None:
    """
    Tables handler
    """
    await message.answer(
        text=hbold('Места Ресторана'),
        reply_markup=back_btn_kb() 
    )
    
    await message.answer(
        text='Выберите место:',
        reply_markup=update_status_place_kb()
    )
    

@router_places.callback_query(F.data.startswith('free_table_manager'))
async def update_free_status_table_handler(call: CallbackQuery) -> None:
    """
    Update free status table handler
    """
    place: int = int(call.data.split("_")[-1])

    update_place_status_api(
        place_id=place, 
        is_view=False
    )

    await call.message.edit_reply_markup(
        reply_markup=update_status_place_kb()
    )
    

@router_places.callback_query(F.data.startswith('busy_table_manager'))
async def update_busy_status_table_handler(call: CallbackQuery) -> None:
    """
    Update busy status table handler
    """
    place: int = int(call.data.split("_")[-1])

    update_place_status_api(
        place_id=place, 
        is_view=True
    )

    await call.message.edit_reply_markup(
        reply_markup=update_status_place_kb()
    )


@router_places.message(F.text == '⬅️ Назад')
async def back_btn_handler(message: Message) -> None:
    """
    Back Button handler
    """
    await message.answer(
        text='Выберите направление:',
        reply_markup=main_menu_manager_kb()
    )