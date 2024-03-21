from aiogram.utils.markdown import hbold, hitalic


def get_text_for_info() -> str:
    """ 
    Get text for info 
    """ 
    text: str = f'{hbold('Кафе 7я')}\n\n{hbold('Режим работы')}:\nПн-Вс: 10:00 - 21:30\n\n' \
        'Мененджер: +998 706 14 09 59\nНаш адрес: г. Алмалык ул.Наследова Парк Маяковского'
    return text

