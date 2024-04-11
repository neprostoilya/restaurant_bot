from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold

from keyboards.tables_manager_kb import tables_manager_kb, back_btn_kb
from api_requests.requests import update_table_status_api
from keyboards.menu_manager_kb import main_menu_manager_kb

router_tables = Router()


@router_tables.message(F.text == '🍽️ Столы')
async def tables_handler(message: Message) -> None:
    """
    Tables handler
    """
    await message.answer(
        text=hbold('Столы'),
        reply_markup=back_btn_kb() 
    )
    
    await message.answer_photo(
        caption='Выберите стол:',
        photo=FSInputFile('bot/images/map.png'),
        reply_markup=tables_manager_kb()
    )
    

@router_tables.callback_query(F.data.startswith('free_table_manager'))
async def update_free_status_table_handler(call: CallbackQuery) -> None:
    """
    Update free status table handler
    """
    table: int = int(call.data.split("_")[-1])

    update_table_status_api(
        table_id=table, 
        status='Занят'
    )

    await call.message.edit_reply_markup(
        reply_markup=tables_manager_kb()
    )
    

@router_tables.callback_query(F.data.startswith('busy_table_manager'))
async def update_busy_status_table_handler(call: CallbackQuery) -> None:
    """
    Update busy status table handler
    """
    table: int = int(call.data.split("_")[-1])

    update_table_status_api(
        table_id=table, 
        status='Свободен'
    )

    await call.message.edit_reply_markup(
        reply_markup=tables_manager_kb()
    )


@router_tables.message(F.text == '⬅️ Назад')
async def back_btn_handler(message: Message) -> None:
    """
    Back Button handler
    """
    await message.answer(
        text='Выберите направление:',
        reply_markup=main_menu_manager_kb()
    )