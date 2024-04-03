from aiogram.utils.markdown import hbold, hitalic


def get_text_for_info(language: str) -> str:
    """ 
    Get text for info 
    """
    if language == 'ru':
        text: str = f'{hbold('Кафе 7я')}\n\n{hbold('Режим работы')}:\nПн-Вс: 10:00 - 21:30\n\n' \
            'Мененджер: +998 706 14 09 59\nНаш адрес: г. Алмалык ул.Наследова Парк Маяковского'
    else:
        text: str = f'{hbold('Kafe 7ya')}\n\n{hbold('Ish tartibi')}:\nDushanba-yakshanba soat 10:00 dan 21:30 gacha\n\n' \
            "Menenger: +998 706 14 09 59\nSizning manzilingiz: Olmalik shahri, Nasledova Mayakovski Park ko'chasi"
    return text

