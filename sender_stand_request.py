import configuration
import requests
import data

# Создание заказа
def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)

# Получение заказа по его номеру
def get_order_by_number(track):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDERS + str(track))




