from api_requests.requests import get_user_language_api
from localization.localization import localization

async def get_lang(chat_id: int, state: object) -> str:
    """
    Get language
    """
    data: dict = await state.get_data()
    
    if data.get('language_user'):
        return data.get('language_user')
    else:
        language: dict = get_user_language_api(chat_id=chat_id)
        if language:
            await state.update_data(
                language_user=language.get('language')
            )
            return language.get('language')
        else:
            return 'ru'
    

def get_text(lang: str, key: str) -> str:
    """
    Get translated text
    """
    text: str = localization.get(lang).get(key)
   
    return text