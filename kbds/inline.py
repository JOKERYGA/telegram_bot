from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

#Начальный маркер для callbacks ---> prefix = "menu"
class MenuCallBack(CallbackData, prefix="menu"):
    level: int
    menu_name: str
    category: int | None = None
    page: int = 1
    product_id: int | None = None



def get_user_main_btns(*, level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Товары 🍕": "catalog",
        "Корзина 🛒": "cart",
        "О нас 📌": "about",
        "Оплата 💰": "payment",
        "Доставка 🏎️": "shipping",
    }
    for text, menu_name in btns.items():
        if menu_name == 'catalog':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level+1, menu_name=menu_name).pack())) # pack - формирует строку из полученных данных
        elif menu_name == 'cart':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=3, menu_name=menu_name).pack()))
        else:
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()))
        
    return keyboard.adjust(*sizes).as_markup()


def get_user_catalog_btns(*, level: int, categories: list, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    
    keyboard.add(InlineKeyboardButton(text="Назад",
                                      callback_data=MenuCallBack(level=level-1, menu_name="main").pack()))
    keyboard.add(InlineKeyboardButton(text="Корзина 🛒",
                                      callback_data=MenuCallBack(level=3, menu_name='cart').pack()))
    
    for c in categories:
        keyboard.add(InlineKeyboardButton(text=c.name,
                                          callback_data=MenuCallBack(level=level+1, menu_name=c.name, category=c.id).pack()))
        
    return keyboard.adjust(*sizes).as_markup()


def get_products_btns(
    *,
    level: int,
    category: int,
    page: int, # Акутальная страница
    paginator_btns: dict, # кнопки назад/вперед
    product_id: int, # для размещения кнопки куптиь на конкретном товаре
    sizes: tuple[int] = (2, 1)
):
    keyboard = InlineKeyboardBuilder()
    
    keyboard.add(InlineKeyboardButton(text="Назад",
                                      callback_data=MenuCallBack(level=level-1, menu_name="catalog").pack()))
    keyboard.add(InlineKeyboardButton(text="Корзина 🛒",
                                      callback_data=MenuCallBack(level=3, menu_name='cart').pack()))
    keyboard.add(InlineKeyboardButton(text="Купить 💳",
                                      callback_data=MenuCallBack(level=level, menu_name="add_to_cart", product_id=product_id).pack()))
    #Кнопка не будет менять уровень, будет выводить сообщение, что товар добавлен в корзину

    keyboard.adjust(*sizes)
    
    row = []
    for text, menu_name in paginator_btns.items():
        if menu_name == "next":
            row.append(InlineKeyboardButton(text=text,
                                            callback_data=MenuCallBack(
                                                level=level,
                                                menu_name=menu_name,
                                                category=category,
                                                page=page + 1).pack()))
        elif menu_name == "previous":
            row.append(InlineKeyboardButton(text=text,
                                            callback_data=MenuCallBack(
                                                level=level,
                                                menu_name=menu_name,
                                                category=category,
                                                page=page - 1).pack()))
    
    return keyboard.row(*row).as_markup()
        




# Генерирует кнопки по словарю 
def get_callback_btns(*, btns: dict[str, str], sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    
    for text, data in btns.items():
        # Добавляем экземпляр класса для создания кнопки
        keyboard.add(InlineKeyboardButton(text=text, callback_data=data))
        
    return keyboard.adjust(*sizes).as_markup()












# #Для отправки ссылки - при нажатии открывается сайт - внешний источник по url
# def get_url_btns(
#     *,
#     btns: dict[str, str],
#     sizes: tuple[int] = (2,)):
    
#     keyboard = InlineKeyboardBuilder()
    
#     for text, url in btns.items():
#         # Добавляем экземпляр класса для создания кнопки
#         keyboard.add(InlineKeyboardButton(text=text, url=url))
        
#     return keyboard.adjust(*sizes).as_markup()


# #Создание микса из Callback и URL Кнопок
# def get_inlineMix_btns(
#     *, # Автоматический запрет на передачу неименнованных аргументов, то есть обязательно нужно указывать text, url and etc
#     btns: dict[str, str],
#     sizes: tuple[int] = (2,)):
    
#     keyboard = InlineKeyboardBuilder()
    
#     for text, value in btns.items():
#         if '://' in value:
#             keyboard.add(InlineKeyboardButton(text=text, url=value))
#         else:
#             keyboard.add(InlineKeyboardButton(text=text, callback_data=value))
        
#     return keyboard.adjust(*sizes).as_markup()


# def get_keyboard(
#     *btns: str,
#     placeholder: str = None,
#     request_contact: int = None,
#     request_location: int = None,
#     sizes: tuple[int] = (2,),
# ):
#     '''
#     Parameters request_contact and request_location must be as indexes of btns args for buttons you need.
#     Example:
#     get_keyboard(
#             "Меню",
#             "О магазине",
#             "Варианты оплаты",
#             "Варианты доставки",
#             "Отправить номер телефона"
#             placeholder="Что вас интересует?",
#             request_contact=4,
#             sizes=(2, 2, 1)
#         )
#     '''
#     keyboard = ReplyKeyboardBuilder()

#     for index, text in enumerate(btns, start=0):
        
#         if request_contact and request_contact == index:
#             keyboard.add(KeyboardButton(text=text, request_contact=True))

#         elif request_location and request_location == index:
#             keyboard.add(KeyboardButton(text=text, request_location=True))
#         else:

#             keyboard.add(KeyboardButton(text=text))

#     return keyboard.adjust(*sizes).as_markup(
#             resize_keyboard=True, input_field_placeholder=placeholder)

