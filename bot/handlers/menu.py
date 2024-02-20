from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.markdown import hbold

from keyboards.menu_kb import categories_menu_kb, dishes_menu_kb, in_dish_kb, cart_kb
from utils.menu_utils import get_text_for_dish, get_text_for_dish_in_cart
from api_requests.requests import put_into_to_cart_api, check_user_api, get_total_sum_cart_api, \
                                    get_cart_by_user_api
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
      
    total_sum_cart: int = get_total_sum_cart_api(
        user=check_user_api(chat_id=chat_id)[0].get('pk')
    )
    
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
    
    await state.clear()
    
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
    
    chat_id: int = call.from_user.id
    
    dish_id: int = data.get('dish_id')
    
    put_into_to_cart_api(
        user=check_user_api(chat_id=chat_id)[0].get('pk'),
        dish_id=dish_id,
        quantity=quantity
    )    
    
    await call.message.delete()
      
    total_sum_cart: int = get_total_sum_cart_api(
        user=check_user_api(chat_id=chat_id)[0].get('pk')
    )
    
    await call.message.answer(
        text='Выберите категорию:',
        reply_markup=categories_menu_kb(total_sum_cart)
    )

    await state.clear()


@router_menu.callback_query(F.data.startswith("cart"))
async def cart_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Get dishes in cart
    """
    chat_id: int = call.from_user.id
    
    await call.message.delete()
    
    carts: dict = get_cart_by_user_api(
        user=check_user_api(chat_id=chat_id)[0].get('pk')
    )
    
    messages_id_list: list = [] 
    
    for cart in carts:
        messages_id_list.append(call.message.message_id)
        await call.message.answer(
            text=get_text_for_dish_in_cart(cart=cart),
            reply_markup=cart_kb(
                quantity=cart.get('quantity'),
                dish_id=cart.get('dish')
            )
        )
    
    await state.update_data(
        messages_id_list=messages_id_list
    )

@router_menu.callback_query(F.data.startswith("plus_in_cart_"))
async def plus_quantity_in_cart_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Reaction on click plus in cart
    """
    chat_id: int = call.from_user.id
    
    quantity: int = int(call.data.split("_")[-1]) + 1
    
    dish_id: int = int(call.data.split("_")[-2])
    
    await call.message.edit_reply_markup(
        reply_markup=cart_kb(
            quantity=quantity,
            dish_id=dish_id
        ),
    )

    await call.answer(
        text='Колличество увеличено!'
    )

    put_into_to_cart_api(
        user=check_user_api(chat_id=chat_id)[0].get('pk'),
        dish_id=dish_id,
        quantity=1
    )
    

@router_menu.callback_query(F.data.startswith("minus_in_cart_"))
async def minus_quantity_in_cart_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Reaction on click minus in cart
    """
    chat_id: int = call.from_user.id
    
    quantity: int = int(call.data.split("_")[-1]) - 1
    
    dish_id: int = int(call.data.split("_")[-2])
    
    await call.message.edit_reply_markup(
        reply_markup=cart_kb(
            quantity=quantity,
            dish_id=dish_id
        ),
    )
    
    await call.answer(
        text='Колличество уменьшено'
    )
    
    put_into_to_cart_api(
        user=check_user_api(chat_id=chat_id)[0].get('pk'),
        dish_id=dish_id,
        quantity=-1
    )
    
@router_menu.callback_query(F.data.startswith("delete_in_cart_"))
async def delete_in_cart_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Reaction on click minus in cart
    """
    chat_id: int = call.from_user.id
    
    cart_id: int = int(call.data.split("_")[-2])
    
    await call.message.delete()
    
    await call.answer(
        text='Блюдо было удалено.'
    )
    
