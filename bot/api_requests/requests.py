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
    return get(f'/users/users/{chat_id}')


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
    return get(f'/dishes/get_dish/{dish_id}/')


def create_order_api(carts: dict, user: int, total_price: int,
                    total_quantity: int, time_order: str, table_order: int):
    """
    Create order 
    """
    data: dict = {'dishes': carts, 'user': user, 'total_price': total_price,  
                  'total_quantity': total_quantity, 'datetime_selected': time_order, 'table': table_order}
        
    return post('/orders/create_order/', data=data)


def get_orders_by_user_api(user: int):
    """
    Get orders by user
    """
    return get(f'/orders/get_orders_by_user/{user}/')