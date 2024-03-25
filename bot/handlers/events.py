from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.utils.markdown import hbold

from api_requests.requests import get_events_api
from keyboards.basic_kb import back_to_main_menu_kb


router_events = Router()


@router_events.message(F.text == "🎉 Акции")
async def events_handler(message: Message) -> None:
    """
    Get events of restourant
    """
    events: dict = get_events_api()
    
    await message.answer(
        text=hbold('Акции'),
        reply_markup=back_to_main_menu_kb()
    )
    
    for event in events:
        await message.answer_photo(
            photo=FSInputFile(f'api{event.get('image')}'),
            caption=event.get('description'),
            parse_mode='Markdown'
        )
    
 