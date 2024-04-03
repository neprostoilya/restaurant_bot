from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext

from utils.basic_utils import get_text, get_lang
from api_requests.requests import get_events_api
from keyboards.basic_kb import back_to_main_menu_kb


router_events = Router()


EVENTS = ['🎉 Акции', '🎉 Yordam']


@router_events.message(F.text.in_(EVENTS))
async def events_handler(message: Message, state: FSMContext) -> None:
    """
    Get events of restourant
    """
    chat_id: int = message.chat.id
    
    lang: str = await get_lang(chat_id=chat_id, state=state)
    
    events: dict = get_events_api()
    
    await message.answer(
        text=get_text(lang, 'events'),
        reply_markup=back_to_main_menu_kb(lang)
    )
    
    for event in events:
        await message.answer_photo(
            photo=FSInputFile(f'api{event.get('image')}'),
            caption=event.get('description_ru'),
            parse_mode='Markdown'
        )
    
 