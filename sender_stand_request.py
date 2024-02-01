import configuration
import requests
import data


# создание заказа
def post_create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.POST_CREATE_ORDER,
                         json=order_body)


# получение заказа по треку
def get_order_track_number(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK+"?t="+track_number)

