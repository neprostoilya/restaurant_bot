from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold

from keyboards.menu_kb import categories_menu_kb, dishes_menu_kb, in_dish_kb
from utils.menu_utils import get_text_for_dish
from api_requests.requests import put_into_to_cart_api, check_user_api, get_total_sum_cart_api, get_dish_by_id_api
from keyboards.basic_kb import back_to_main_menu_kb, open_web_menu_kb

router_menu = Router()


@router_menu.message(F.text == "🍽 Меню")
async def categories_menu_handler(message: Message) -> None:
    """
    Get categories menu handler
    """
    chat_id: int = message.from_user.id
    
    await message.answer(
        text=f'Вы выбрали {hbold("Меню")}',
        reply_markup=back_to_main_menu_kb()
    )
    
    await message.answer(
        text='Попробуйте заказать в интерактивном меню 🤖',
        reply_markup=open_web_menu_kb(
            token=check_user_api(chat_id=chat_id)[0].get('token')
        )     
    )  
      
    total_sum_cart: int = 1000
    
    await message.answer(
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
    
    text, image = get_text_for_dish(dish_id=dish_id)
    
    await state.update_data(
        dish_id=dish_id,
        quantity=quantity
    )
    
    await call.message.delete()

    await call.message.answer_photo(
        photo=FSInputFile(f'api{image}'),
        caption=text,
        reply_markup=in_dish_kb(quantity=quantity),
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
        reply_markup=in_dish_kb(quantity=quantity),
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
        reply_markup=in_dish_kb(quantity=quantity),
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
    
    carts: list = data.get('carts')
    
    if carts is None:
        carts: list = []
         
    carts_new: list = carts.append([dish_id, quantity])
    
    await state.update_data(
        carts=carts_new
    )
    
    await call.message.delete()
      
    total_sum_cart: int = 1000
    
    await call.message.answer(
        text='Выберите категорию:',
        reply_markup=categories_menu_kb(total_sum_cart)
    )


