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
    data: dict = await state.get_data()
    
    carts: dict = data.get('carts')
    
    messages_id_list: list = [] 
    
    total_price: int = 0
    
    total_quantity: int = 0
    
    await call.message.delete()
    
    print(carts,)
    
        # total_price += cart.get('get_total_price')
        # total_quantity += cart.get('quantity')
        
        # message_cart = await call.message.answer(
            # text=get_text_for_dish_in_cart(cart=cart),
            # reply_markup=cart_kb(
            #     quantity=cart.get('quantity'),
            #     dish_id=cart.get('dish')
            # )
    #     )
    #     messages_id_list.append(message_cart.message_id)
    
    # message_order = await call.message.answer(
    #     text=get_text_for_total_price(
    #         total_price=total_price, 
    #         total_quantity=total_quantity
    #     ),
    #     reply_markup=create_order_btn_kb()
    # )
    
    # messages_id_list.append(message_order.message_id)
    
        
    # await state.update_data(
    #     messages_id_list=messages_id_list
    # )

@router_cart.callback_query(F.data.startswith("plus_in_cart_"))
async def plus_quantity_in_cart_handler(call: CallbackQuery) -> None:
    """
    Reaction on click plus in cart
    """
    chat_id: int = call.from_user.id
    
    quantity: int = int(call.data.split("_")[-1]) + 1
    
    dish_id: int = int(call.data.split("_")[-2])
    
    user: int = check_user_api(chat_id=chat_id)[0].get('pk')
    
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
        user=user,
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
    
    user: int = check_user_api(chat_id=chat_id)[0].get('pk')
    
    await call.message.edit_reply_markup(
        reply_markup=cart_kb(
            quantity=quantity,
            dish_id=dish_id
        ),
    )
   
    if quantity <= 0:
        await call.answer(
            text='Блюдо удалено из корзины'
        )
        
        await call.message.delete()
        
        delete_cart(
            id=dish_id,
            user=user
        )
    else:
        await call.answer(
            text='Колличество уменьшено'
        )
    
    put_into_to_cart_api(
        user=user,
        dish_id=dish_id,
        quantity=-1
    )
    
