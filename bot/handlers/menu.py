from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMedia
from aiogram.fsm.context import FSMContext

from keyboards.menu_kb import categories_menu_kb, dishes_menu_kb, in_dish_kb
from keyboards.basic_kb import open_web_menu_kb
from utils.basic_utils import get_text_for_dish
from api_requests.requests import put_into_to_cart_api

router_menu = Router()


@router_menu.message(F.text == "🍽 Меню")
async def categories_menu_handler(message: Message) -> None:
    """
    Get categories menu handler
    """
    await message.answer(
        text='Попробуйте заказать в интерактивном меню 🤖',
        reply_markup=open_web_menu_kb()     
    )    
    
    await message.answer(
        text='Выберите категорию:',
        reply_markup=categories_menu_kb()
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
    
    text, image = get_text_for_dish(dish_id)
    
    await state.clear()
    
    await state.update_data(
        dish_id=dish_id,
        quantity=quantity
    )
    
    await call.message.delete()

    await call.message.answer_photo(
        photo=FSInputFile(f'api{image}'),
        caption=text,
        reply_markup=in_dish_kb(quantity=quantity, dish_id=dish_id),
    )


@router_menu.callback_query(F.data.startswith("plus"))
async def plus_quantity_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Reaction on click plus
    """
    data: dict = await state.get_data()
    
    dish_id: int = data.get('dish_id')
    
    quantity: int = data.get('quantity') + 1
    
    await state.update_data(
        quantity=quantity
    )
    
    await call.message.edit_reply_markup(
        reply_markup=in_dish_kb(quantity=quantity, dish_id=dish_id),
    )

@router_menu.callback_query(F.data.startswith("minus"))
async def plus_quantity_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Reaction on click minus
    """
    data: dict = await state.get_data()
    
    dish_id: int = data.get('dish_id')
    
    quantity: int = data.get('quantity') - 1
    
    await state.update_data(
        quantity=quantity,
    )
    
    await call.message.edit_reply_markup(
        reply_markup=in_dish_kb(quantity=quantity, dish_id=dish_id),
    )
    
    
@router_menu.callback_query(F.data.startswith("put_into_cart_"))
async def put_into_cart_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Reaction on click put into cart
    """
    dish_id: int = int(call.data.split("_")[-1])
    
    put_into_to_cart_api(user=)    
