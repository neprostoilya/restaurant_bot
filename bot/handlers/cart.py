from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold

from utils.cart_utils import get_text_for_dish_in_cart, get_text_for_total_price
from api_requests.requests import check_user_api, get_dish_by_id_api
from keyboards.cart_kb import cart_kb, create_order_btn_kb


router_cart = Router()


@router_cart.callback_query(F.data.startswith("cart"))
async def cart_callback_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Get dishes in cart
    """
    data: dict = await state.get_data()
    
    carts: tuple = data.get('carts')
    
    if carts:
        messages_id_list: list = [] # messages ids list for delete
        
        await call.message.delete()
        
        for cart in carts:  
            dish: dict = get_dish_by_id_api(dish_id=cart[0])[0]
            
            total_price: int = dish.get('price') * cart[1]
            
            message_cart = await call.message.answer(
                text=get_text_for_dish_in_cart(dish=dish, total_price=total_price),
                reply_markup=cart_kb(
                    quantity=cart[1],
                    dish_id=dish.get('pk')
                )
            )
            messages_id_list.append(message_cart.message_id)
        
        message_order = await call.message.answer(
            text=get_text_for_total_price(
                total_price_all_cart=data.get('total_price'), 
                total_quantity_all_cart=data.get('total_quantity')
            ),
            reply_markup=create_order_btn_kb()
        )
        
        messages_id_list.append(message_order.message_id)
            
        await state.update_data(
            messages_id_list=messages_id_list,
            message_order_id=message_order.message_id
        )
    else:
        await call.message.answer(
            text='Извините, но ваша корзинка пуста 😅'
        )


@router_cart.message(F.text == '🛒 Корзина')
async def cart_message_handler(message: Message, state: FSMContext) -> None:
    """
    Get dishes in cart
    """
    data: dict = await state.get_data()
    
    carts: tuple = data.get('carts')
    
    if carts:
        messages_id_list: list = [] # messages ids list for delete
        
        for cart in carts:  
            dish: dict = get_dish_by_id_api(dish_id=cart[0])[0]
            
            total_price: int = dish.get('price') * cart[1]
            
            message_cart = await message.answer(
                text=get_text_for_dish_in_cart(dish=dish, total_price=total_price),
                reply_markup=cart_kb(
                    quantity=cart[1],
                    dish_id=dish.get('pk')
                )
            )
            messages_id_list.append(message_cart.message_id)
        
        message_order = await message.answer(
            text=get_text_for_total_price(
                total_price_all_cart=data.get('total_price'), 
                total_quantity_all_cart=data.get('total_quantity')
            ),
            reply_markup=create_order_btn_kb()
        )
        
        messages_id_list.append(message_order.message_id)
            
        await state.update_data(
            messages_id_list=messages_id_list,
            message_order_id=message_order.message_id
        )
    else:
        await message.answer(
            text='Извините, но ваша корзинка пуста 😅'
        )


@router_cart.callback_query(F.data.startswith("plus_in_cart_"))
async def plus_quantity_in_cart_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Reaction on click plus in cart 
    """
    chat_id: int = call.message.chat.id 
    
    quantity: int = int(call.data.split("_")[-1]) + 1
    
    dish_id: int = int(call.data.split("_")[-2])
    
    dish: dict = get_dish_by_id_api(dish_id=dish_id)[0]
    
    total_price: int = dish.get('price') * quantity
    
    data: dict = await state.get_data()
    
    total_price_all_cart: int = data.get('total_price') + dish.get('price')
    
    total_quantity_all_cart: int = data.get('total_quantity') + 1
    
    message_order_id: int = data.get('message_order_id')
    
    await state.update_data(
        total_price=total_price_all_cart,
        total_quantity=total_quantity_all_cart
    )
    
    await call.message.edit_text(
        text=get_text_for_dish_in_cart(dish=dish, total_price=total_price),
        reply_markup=cart_kb(
            quantity=quantity,
            dish_id=dish_id
        )
    )
    
    await call.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_order_id,
        text=get_text_for_total_price(
            total_price_all_cart=total_price_all_cart, 
            total_quantity_all_cart=total_quantity_all_cart
        ),
        reply_markup=create_order_btn_kb()
    )
    
    await call.answer(
        text='Колличество увеличено!'
    )


@router_cart.callback_query(F.data.startswith("minus_in_cart_"))
async def minus_quantity_in_cart_handler(call: CallbackQuery, state: FSMContext) -> None:
    """
    Reaction on click minus in cart
    """
    chat_id: int = call.message.chat.id
    
    quantity: int = int(call.data.split("_")[-1]) - 1
    
    dish_id: int = int(call.data.split("_")[-2])
    
    dish: dict = get_dish_by_id_api(dish_id=dish_id)[0]
    
    total_price: int = dish.get('price') * quantity
    
    data: dict = await state.get_data()
    
    total_price_all_cart: int = data.get('total_price') - dish.get('price')
    
    total_quantity_all_cart: int = data.get('total_quantity') - 1
    
    message_order_id: int = data.get('message_order_id')
    
    await state.update_data(
        total_price=total_price_all_cart,
        total_quantity=total_quantity_all_cart
    )
    
    await call.message.edit_text(
        text=get_text_for_dish_in_cart(dish=dish, total_price=total_price),
        reply_markup=cart_kb(
            quantity=quantity,
            dish_id=dish_id
        )
    )
    
    await call.bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_order_id,
        text=get_text_for_total_price(
            total_price_all_cart=total_price_all_cart, 
            total_quantity_all_cart=total_quantity_all_cart
        ),
        reply_markup=create_order_btn_kb()
    )
    
    await call.answer(
        text='Колличество уменьшено'
    )

