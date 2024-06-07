# Светлана Абрамова, 17 когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_create_order_response():
    create_order_response = sender_stand_request.post_new_orders(data.orders_body)
    track_number = create_order_response.json()["track"]
    get_order_response = sender_stand_request.get_order_by_number(track_number)
    assert get_order_response.status_code == 200














