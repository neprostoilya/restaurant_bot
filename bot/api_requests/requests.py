import requests
import json

from config.configuration import URL


def get(point: str):
    """
    Get
    """
    url = URL + point

    response = requests.get(url)

    response.raise_for_status()

    if response.status_code != 204:
        data = response.json()
        return data


def post(point: str, data: json):
    """
    Post
    """
    url = URL + point

    response = requests.post(url, json=data)

    if response.status_code != 204:
        try:
            data = response.json()
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
    else:
        return None

def put(point: str, data: json):
    """
    PUT
    """
    url = URL + point

    response = requests.put(url, json=data)

    if response.status_code != 204:
        data = response.json()
        return data


def register_user_api(username: str, phone: str, chat_id: int, language: str) -> object:
    """
    Register User
    """
    data = {'username': f'{username}', 'phone': f'{phone}', 'telegram_pk': f'{chat_id}', 'language': f'{language}'}
    return post('/users/register/', data=data)


def login_user_api(chat_id: int):
    """
    Login User
    """
    data = {'telegram_pk': f'{chat_id}'}
    return post('/users/login/', data=data)


def check_user_api(chat_id: int):
    """
    Check Or Get User
    """
    try:
        return get(f'/users/users/{chat_id}/')
    except requests.exceptions.HTTPError:
        return None

def get_categories_api():
    """
    Get categories menu
    """
    return get(f'/categories/get_categories/')


def get_dishes_by_category_api(category: int):
    """
    Get dishes by category menu
    """
    return get(f'/dishes/get_dishes/{category}/')


def get_dish_by_id_api(dish_id: int):
    """
    Get dish by id menu
    """
    
    try:
        return get(f'/dishes/get_dish/{dish_id}/')[0]
    except:
        return get(f'/dishes/get_dish/{dish_id}/')


def create_order_api(user: int, total_price: int, status: str, type_order: str,
                    total_quantity: int, time_order: str, place_name: str, people_quantity: int):
    """
    Create order 
    """
    data: dict = {'user': user, 'total_price': total_price, 'status': status, 'people_quantity': people_quantity,
                  'total_quantity': total_quantity, 'datetime_selected': time_order, 'place': place_name, 'type_order': type_order}
        
    return post('/orders/create_order/', data=data)


def create_pickup_order_api(user: int, total_price: int, status: str, total_quantity: int, time_order: str,
                             type_order: str,):
    """
    Create Pickup Order 
    """
    data: dict = {'user': user, 'total_price': total_price, 'status': status,
                  'total_quantity': total_quantity, 'datetime_selected': time_order, 'type_order': type_order}
        
    return post('/orders/create_order/', data=data)


def create_delivery_order_api(user: int, total_price: int, status: str, total_quantity: int,
                               latitude: str, longitude: str, type_order: str):
    """
    Create Delivery Order 
    """
    data: dict = {'user': user, 'total_price': total_price, 'status': status, 'latitude': latitude,
                  'total_quantity': total_quantity, 'longitude': longitude,
                  'type_order': type_order}
        
    return post('/orders/create_order/', data=data)


def create_dish_order_api(order: int, dish: int, total_price: int, total_quantity: int):
    """
    Create Dish order 
    """
    data: dict = {'order': order, 'total_price': total_price, 'dish': dish, 'total_quantity': total_quantity}
        
    return post('/orders/create_dish_order/', data=data)


def get_orders_by_user_api(user: int):
    """
    Get orders by user
    """
    try:    
        return get(f'/orders/get_orders_by_user/{user}/')
    except:
        return None


def update_order_status_api(order_id: int, status: str):
    """
    Update status order 
    """
    data = {'status': status}
    return put(f'/orders/update_order_status/{order_id}/', data=data)


def get_order_by_order_id_api(order_id: int):
    """
    Get order by order id
    """
    return get(f'/orders/get_order_by_order_id/{order_id}/')


def get_events_api() -> dict:
    """
    Get events of restourant
    """
    return get(f'/events/get_events/')


def update_user_phone_api(chat_id: id, phone: str) -> dict:
    """
    Update user phone
    """
    data = {'phone': phone}
    
    return put(f'/users/update/{chat_id}/', data=data)


def update_user_language_api(chat_id: id, language: str) -> dict:
    """
    Update user language
    """
    data = {'language': language}
    
    return put(f'/users/update/{chat_id}/', data=data)


def get_user_language_api(chat_id: int) -> dict:
    """
    Get user language
    """
    try:
        return get(f'/users/get_user_language/{chat_id}/').get('language')
    except:
        return 'ru'


def check_manager_api(chat_id: int) -> bool:
    """
    Check manager 
    """
    if get(f'/users/check_manager/{chat_id}/'):
        return True
    else:
        return False


def get_reserved_places_api() -> dict:
    """
    Get Reserved Places 
    """
    return get(f'/places/get_reserved_places/')


def get_places_api() -> dict:
    """
    Get All Places 
    """
    return get(f'/places/get_places/')


def update_place_status_api(place_id: int, is_view: str) -> dict:
    """
    Update place status 
    """
    data = {'is_view': is_view}
    
    return put(f'/places/update_place_status/{place_id}/', data=data)


def get_active_orders_api() -> dict:
    """
    Get active orders 
    """
    return get(f'/orders/get_active_orders/')


def get_user_by_pk_api(user_id: int) -> dict:
    """
    Get user pk(id)
    """
    return get(f'/users/get_user_by_pk/{user_id}/')


def get_dishes_order_api(order_id: int) -> dict:
    """
    Get dishes order
    """
    return get(f'/orders/get_dishes_order/{order_id}/')


def get_managers_api() -> dict:
    """
    Get Managers 
    """
    return get('/users/get_managers/')
    