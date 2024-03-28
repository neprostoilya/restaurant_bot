from api_requests.requests import get_user_language_api
from localization.localization import localization

def get_lang(chat_id: int) -> str:
    """
    Get language
    """
    language: dict = get_user_language_api(chat_id=chat_id)
    
    return language.get('language')


def get_text(lang: str, key: str) -> str:
    """
    Get translated text
    """
    text: str = localization.get(lang).get(key)
    
    return text