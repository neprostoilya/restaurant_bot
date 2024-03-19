from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold

from keyboards.menu_kb import categories_menu_kb, dishes_menu_kb, in_dish_kb
from utils.menu_utils import get_text_for_dish
from api_requests.requests import check_user_api, get_dish_by_id_api
from keyboards.basic_kb import back_to_main_menu_kb, open_web_menu_kb, main_menu_kb


router_menu = Router()


@router_menu.message(F.text == "🍽 Меню")
async def categories_menu_handler(message: Message, state: FSMContext) -> None:
    """
    Get categories menu handler
    """
    data: dict = await state.get_data()
    
    await message.answer(
        text=f'Вы выбрали {hbold("Меню")}',
        reply_markup=back_to_main_menu_kb()
    )
    
    web_menu = await message.answer(
        text='Попробуйте заказать в интерактивном меню 🤖',
        reply_markup=open_web_menu_kb()
    )  
    
    if data.get('total_price'):
        total_sum_cart: int = data.get('total_price') 
    else: 
        total_sum_cart: int = 0
    
    categories_menu = await message.answer(
        text='Выберите категорию:',
        reply_markup=categories_menu_kb(total_sum_cart)
    )
    
    menu_mesages_ids: list = []
    
    menu_mesages_ids.append(web_menu.message_id)
    
    menu_mesages_ids.append(categories_menu.message_id)
    
    await state.update_data(
        menu_mesages_ids=menu_mesages_ids
    )
    

@router_menu.message(F.text == "⬅️ Главное меню")
async def back_to_main_menu_handler(message: Message, state: FSMContext) -> None:
    """
    Back to main menu 
    """
    chat_id: int = message.from_user.id
    
    data: dict = await state.get_data()
    
    menu_mesages_ids: list = data.get('menu_mesages_ids')
    
    if menu_mesages_ids:
        await message.bot.delete_messages(
            chat_id=chat_id,
            message_ids=menu_mesages_ids
        )    

    await message.answer(
        text='Выберите направление:',
        reply_markup=main_menu_kb()
    )


@router_menu.callback_query(F.data.startswith("bact_to_categories"))
async def back_to_categories_menu_handler(call: CallbackQuery) -> None:
    """
    Back to categories menu 
    """
    total_sum_cart: int = 1000
    
    await call.message.edit_text(
        text='Выберите категорию:',
        reply_markup=categories_menu_kb(total_sum_cart)
    )

@router_menu.callback_query(F.data.startswith("category_"))
async def dishes_menu_handler(call: CallbackQuery) -> None:
    """
    Get dishes menu handler
    """
    category: int = int(call.data.split("_")[-1])

    await call.message.edit_text(
        text='Выберите блюдо:',
        reply_markup=dishes_menu_kb(category)
    )


@router_menu.callback_query(F.data.startswith("dish_"))
async def dish_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Inside Dish
    """
    dish_id: int = int(call.data.split("_")[-1])

    quantity: int = 0
    
    dish: dict = get_dish_by_id_api(dish_id)[0]
    
    text, image = get_text_for_dish(dish=dish)
    
    await state.update_data(
        dish_id=dish_id,
        quantity=quantity,
        price_dish=dish.get('price')
    )
    
    await call.message.delete()

    await call.message.answer_photo(
        photo=FSInputFile(f'api{image}'),
        caption=text,
        reply_markup=in_dish_kb(quantity=quantity, category=dish.get('category')),
    )


@router_menu.callback_query(F.data.startswith("bact_to_dishes"))
async def back_to_dishes_menu_handler(call: CallbackQuery) -> None:
    """
    Back to dishes menu 
    """
    category: int = int(call.data.split("_")[-1])

    await call.message.delete()

    await call.message.answer(
        text='Выберите блюдо:',
        reply_markup=dishes_menu_kb(category=category)
    )


@router_menu.callback_query(F.data.startswith("plus_in_dish"))
async def plus_quantity_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Reaction on click plus
    """
    data: dict = await state.get_data()
    
    quantity: int = data.get('quantity') + 1
    
    await state.update_data(
        quantity=quantity
    )
    
    await call.message.edit_reply_markup(
        reply_markup=in_dish_kb(quantity=quantity, category=data.get('category')),
    )

    await call.answer(
        text='Колличество увеличено'
    )


@router_menu.callback_query(F.data.startswith("minus_in_dish"))
async def plus_quantity_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Reaction on click minus
    """
    data: dict = await state.get_data()
    
    quantity: int = data.get('quantity') - 1
    
    await state.update_data(
        quantity=quantity,
    )
    
    await call.message.edit_reply_markup(
        reply_markup=in_dish_kb(quantity=quantity, category=data.get('category')),
    )
    
    await call.answer(
        text='Колличество уменьшено'
    )
    
    
@router_menu.callback_query(F.data.startswith("put_into_cart"))
async def put_into_cart_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Reaction on click put into cart
    """
    data: dict = await state.get_data()
    
    quantity: int = data.get('quantity') 
    
    dish_id: int = data.get('dish_id')
    
    carts: list = data.get('carts', [])
    
    carts.append([dish_id, quantity])
    
    total_price_all_cart: int = data.get('total_price', 0) + (data.get('price_dish') * quantity)
    
    total_quantity_all_cart: int = data.get('total_quantity', 0) + quantity
    
    await state.update_data(
        carts=carts,
        total_price=total_price_all_cart,
        total_quantity=total_quantity_all_cart
    )
    
    await call.message.delete()
      
    await call.message.answer(
        text='Выберите категорию:',
        reply_markup=categories_menu_kb(total_price_all_cart)
    )


