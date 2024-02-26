from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold

from utils.cart_utils import get_text_for_dish_in_cart, get_text_for_total_price
from api_requests.requests import put_into_to_cart_api, check_user_api, \
                                    get_cart_by_user_api, delete_cart
from keyboards.cart_kb import cart_kb, create_order_btn_kb

router_cart = Router()

@router_cart.callback_query(F.data.startswith("cart"))
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
    
    total_price: int = 0
    
    total_quantity: int = 0
    
    for cart in carts:
        total_price += cart.get('get_total_price')
        total_quantity += cart.get('quantity')
        
        await call.message.answer(
            text=get_text_for_dish_in_cart(cart=cart),
            reply_markup=cart_kb(
                quantity=cart.get('quantity'),
                dish_id=cart.get('dish')
            )
        )
        messages_id_list.append(call.message.message_id)
    
    await state.update_data(
        messages_id_list=messages_id_list
    )
    
    await call.message.answer(
        text=get_text_for_total_price(
            total_price=total_price, 
            total_quantity=total_quantity
        ),
        reply_markup=create_order_btn_kb()
    )

@router_cart.callback_query(F.data.startswith("plus_in_cart_"))
async def plus_quantity_in_cart_handler(call: CallbackQuery) -> None:
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
    

@router_cart.callback_query(F.data.startswith("minus_in_cart_"))
async def minus_quantity_in_cart_handler(call: CallbackQuery) -> None:
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
    
@router_cart.callback_query(F.data.startswith("delete_in_cart_"))
async def delete_in_cart_handler(call: CallbackQuery) -> None:
    """
    Reaction on click minus in cart
    """
    cart_id: int = int(call.data.split("_")[-2])
    
    await call.message.delete()
    
    await call.answer(
        text='Блюдо было удалено.'
    )
    
    delete_cart(id=cart_id)
