from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_callback_btns(
    *,
    btns: dict[str, str],
    sizes: tuple[int] = (2,)):
    
    keyboard = InlineKeyboardBuilder()
    
    for text, data in btns.items():
        # Добавляем экземпляр класса для создания кнопки
        keyboard.add(InlineKeyboardButton(text=text, callback_data=data))
        
    return keyboard.adjust(*sizes).as_markup()

#Для потравки ссылки - при нажатии открывается сайт - внешний источник по url
def get_url_btns(
    *,
    btns: dict[str, str],
    sizes: tuple[int] = (2,)):
    
    keyboard = InlineKeyboardBuilder()
    
    for text, url in btns.items():
        # Добавляем экземпляр класса для создания кнопки
        keyboard.add(InlineKeyboardButton(text=text, url=url))
        
    return keyboard.adjust(*sizes).as_markup()


#Создание микса из Callback и URL Кнопок
def get_inlineMix_btns(
    *, # Автоматический запрет на передачу неименнованных аргументов, то есть обязательно нужно указывать text, url and etc
    btns: dict[str, str],
    sizes: tuple[int] = (2,)):
    
    keyboard = InlineKeyboardBuilder()
    
    for text, value in btns.items():
        if '://' in value:
            keyboard.add(InlineKeyboardButton(text=text, url=value))
        else:
            keyboard.add(InlineKeyboardButton(text=text, callback_data=value))
        
    return keyboard.adjust(*sizes).as_markup()





















def get_keyboard(
    *btns: str,
    placeholder: str = None,
    request_contact: int = None,
    request_location: int = None,
    sizes: tuple[int] = (2,),
):
    '''
    Parameters request_contact and request_location must be as indexes of btns args for buttons you need.
    Example:
    get_keyboard(
            "Меню",
            "О магазине",
            "Варианты оплаты",
            "Варианты доставки",
            "Отправить номер телефона"
            placeholder="Что вас интересует?",
            request_contact=4,
            sizes=(2, 2, 1)
        )
    '''
    keyboard = ReplyKeyboardBuilder()

    for index, text in enumerate(btns, start=0):
        
        if request_contact and request_contact == index:
            keyboard.add(KeyboardButton(text=text, request_contact=True))

        elif request_location and request_location == index:
            keyboard.add(KeyboardButton(text=text, request_location=True))
        else:

            keyboard.add(KeyboardButton(text=text))

    return keyboard.adjust(*sizes).as_markup(
            resize_keyboard=True, input_field_placeholder=placeholder)

