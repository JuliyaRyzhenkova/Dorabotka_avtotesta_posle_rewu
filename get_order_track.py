import data
import sender_stand_request

# Рыженкова Юлия, 12 кагорта, дипломная работа
# Тест


def test_get_order_track():
    new_order = sender_stand_request.post_create_order(data.order_boby)
    track_number = str(new_order.json()["track"])
    response_order_track_status = sender_stand_request.get_order_track_number(track_number).status_code
    assert response_order_track_status == 200
