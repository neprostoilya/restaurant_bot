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
        data = response.json()
        return data


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
    Check User
    """
    return get(f'/users/users/{chat_id}')


def get_categories_api():
    """
    Get categories menu
    """
    return get(f'/categories/get_categories/')


def get_dishes_by_category_api(category):
    """
    Get dishes by category menu
    """
    return get(f'/dishes/get_dishes/{category}/')


def get_dish_by_id_api(dish_id):
    """
    Get dish by id menu
    """
    return get(f'/dishes/get_dish/{dish_id}/')


def put_into_to_cart_api(user, dish_id, amount):
    """
    Put into to cart
    """
    data = {'user': user, 'dish': dish_id, 'amount': amount}
    return post(f'/carts/create_cart/', data=data)
