import requests

def test_product_list_returns_200():
    response = requests.get('https://fakestoreapi.com/products')
    assert response.status_code == 200

def test_product_list_response_size_is_greater_then_one():
    response = requests.get('https://fakestoreapi.com/products')
    assert len(response.json()) > 1

def test_product_list_response_item_has_id():
    response = requests.get('https://fakestoreapi.com/products')
    assert response.json()[0]["id"] is not None

def test_product_list_response_item_has_title():
    response = requests.get('https://fakestoreapi.com/products')
    assert response.json()[0]["title"] is not None